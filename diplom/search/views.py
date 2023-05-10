from django.shortcuts import render
from django.http import HttpResponse
from .forms import QuestionsForm
from .forms import UploadFileForm
from .models import Questions, Keywords
from .utils import *
import csv


# Create your views here.

def add_in_database(number_work, question, answer):
    question_after_processing = text_processing(question.lower().strip())
    keywords = search_keywords(question_after_processing, True)

    if answer == '':
        instance = Questions.objects.create(question=question, number_work=number_work)
        for i in range(len(keywords)):
            instance.keywords.add(keywords[i])
    else:
        Questions.objects.create(question=question, number_work=number_work, answer=answer,
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


def send(request):
    if request.method == "POST":
        form = QuestionsForm(request.POST)
        if form.is_valid():
            question_from_form = form.cleaned_data['question'].lower().strip()
            print(question_from_form)
            number_work = form.cleaned_data['number_work']
            print(number_work)
            add_in_database(number_work, question_from_form, '')

    return render(request, 'search/send.html')


def search(request):
    if request.method == "POST":
        form = QuestionsForm(request.POST)
        if form.is_valid():

            question_from_form = form.cleaned_data['question'].lower().strip()
            number_work = form.cleaned_data['number_work']

            question_after_processing = text_processing(question_from_form)

            keywords = search_keywords(question_after_processing)

            filtered_posts_id = []
            if keywords != '':
                posts = Questions.objects.filter(number_work=number_work, is_answered=True)

                for i in range(len(posts)):
                    for j in range(len(keywords)):
                        keywords_for_questions = []
                        for k in range(len(posts[i].keywords.all())):
                            keywords_for_questions.append(
                                text_processing(posts[i].keywords.all()[k].word.lower().strip()))
                        if keywords[j] in keywords_for_questions:
                            filtered_posts_id.append(posts[i].id)
                            print(filtered_posts_id)

                if len(filtered_posts_id) == 0:
                    posts = Questions.objects.filter(is_answered=True)
                    for i in range(len(posts)):
                        for j in range(len(keywords)):
                            keywords_for_questions = []
                            for k in range(len(posts[i].keywords.all())):
                                keywords_for_questions.append(
                                    text_processing(posts[i].keywords.all()[k].word.lower().strip()))
                            if keywords[j] in keywords_for_questions:
                                filtered_posts_id.append(posts[i].id)

                if len(filtered_posts_id) == 0:
                    add_in_database(number_work, question_from_form, '')

            else:
                add_in_database(number_work, question_from_form, '')

            filtered_posts_id = sorted(set(filtered_posts_id), key=lambda x: (-filtered_posts_id.count(x),
                                                                              filtered_posts_id.index(x)))

            filtered_posts = []
            for i in range(len(filtered_posts_id)):
                filtered_posts.append(Questions.objects.get(pk=filtered_posts_id[i]))

            lenght = len(filtered_posts)
    else:
        form = QuestionsForm()

    return render(request, 'search/items.html', {"posts": filtered_posts, "lenght": lenght})


def detail(request, pk):
    post = Questions.objects.get(pk=pk)
    form = QuestionsForm()
    return render(request, 'search/detail.html', {"post": post, 'form': form})
