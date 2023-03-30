import re
import csv
from .models import Keywords, Questions

import pymorphy2 as pymorphy2

morph = pymorphy2.MorphAnalyzer()


def search_keywords(text, flag=False):
    # text = " ".join(text)
    if not flag:

        keywords = []
        keywords_for_db = Keywords.objects.all()
        for i in range(len(keywords_for_db)):
            word = text_processing(keywords_for_db[i].word.lower().strip())
            len_words = len(word)
            sum = 0
            for j in range(len_words):
                if word[j] in text:
                    sum += 1

            if sum == len_words:
                keywords.append(word)

        if len(keywords) == 0:
            return ''

        return keywords
    else:
        keywords = []
        keywords_for_db = Keywords.objects.all()
        for i in range(len(keywords_for_db)):
            word = text_processing(keywords_for_db[i].word.lower().strip())
            len_words = len(word)
            sum = 0
            for j in range(len_words):
                if word[j] in text:
                    sum += 1

            if sum == len_words:
                keywords.append(keywords_for_db[i])

        if len(keywords) == 0:
            return ''

        return keywords


def remove_exception_symbols(text):
    reg = re.compile('[^a-zA-Zа-яА-Я- ёЁ]')
    text = reg.sub('', text)
    return text


def lemmatization(text):
    return [morph.parse(word)[0].normal_form for word in text]


def text_processing(main_text):
    main_text = remove_exception_symbols(main_text)
    main_text = main_text.split(" ")
    main_text = lemmatization(main_text)
    return main_text


def read_csv():
    arr = []
    with open("a.csv", newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            arr.append([row['Number'], row['Question'], row['Answer']])
    return arr
