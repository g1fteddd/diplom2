from django.shortcuts import render
from django.http import HttpResponse
from .forms import QuestionsForm
from .forms import UploadFileForm
from .models import Questions
from .utils import *
import csv

# Create your views here.

def add_in_database(number_work, question, answer):
    question_after_processing = text_processing(question.lower().strip())
    print(question_after_processing)
    keywords = search_keywords(question_after_processing)
    print(keywords)
    if answer == '':
        Questions.objects.create(question=question, keywords=keywords, number_work=number_work)
    else:
        Questions.objects.create(question=question, keywords=keywords, number_work=number_work, answer=answer,
                                 is_answered=True)

def index(request):
    form = QuestionsForm()
    return render(request, 'search/index.html', {'form': form})


def upload_file(request):
    if request.method == "POST":
        form_csv = UploadFileForm(request.POST, request.FILES)
        file = request.FILES['file']
    else:
        form_csv = UploadFileForm()
    return render(request, 'search/add.html', {'form_csv': form_csv})

def item(request):
    if request.method == "POST":
        form = QuestionsForm(request.POST)
        if form.is_valid():

            # array = read_csv()
            # for item in array:
            #     add_in_database(int(item[0]), item[1], item[2])



            question_from_form = form.cleaned_data['question'].lower().strip() # Вопрос студента
            number_work = form.cleaned_data['number_work']  # Номер практической работы
            question_after_processing = text_processing(question_from_form)
            keywords = search_keywords(question_after_processing)
            keywords = keywords.split(';')
            print(keywords)

            filtered_posts_id = []
            if keywords[0] != '':
                print(len(keywords))
                # Поиск по статьям с определённым номером лабы
                posts = Questions.objects.filter(number_work=number_work)

                for i in range(len(posts)):
                    for j in range(len(keywords)):
                        if keywords[j] in posts[i].keywords.split(';'):
                            filtered_posts_id.append(posts[i].id)

                # Поиск по всем статьям
                if len(filtered_posts_id) == 0:
                    posts = Questions.objects.all()
                    for i in range(len(posts)):
                        for j in range(len(keywords)):
                            if keywords[j] in posts[i].keywords.split(';'):
                                filtered_posts_id.append(posts[i].id)

                print(len(filtered_posts_id))
                # Если вообще ничего не нашлось
                if len(filtered_posts_id) == 0:
                    add_in_database(number_work, question_from_form, '')

            else:
                add_in_database(number_work, question_from_form, '')

            filtered_posts = []
            for i in range(len(filtered_posts_id)):
                filtered_posts.append(Questions.objects.get(pk=filtered_posts_id[i]))

            filtered_posts = set(filtered_posts)
            lenght = len(filtered_posts)
            # add_in_database(number_work, question_from_form, '')

    else:
        form = QuestionsForm()


    return render(request, 'search/item.html', {"posts": filtered_posts, "lenght": lenght})

def detail(request, pk):
    post = Questions.objects.get(pk=pk)

    return render(request, 'search/detail.html', {"post": post})