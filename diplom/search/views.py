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
    keywords = search_keywords(question_after_processing)
    if answer == '':
        Questions.objects.create(question=question, keywords=keywords, number_work=number_work)
    else:
        Questions.objects.create(question=question, keywords=keywords, number_work=number_work, answer=answer,
                                 is_answered=True)

def index(request):
    if request.method == "POST":
        form = QuestionsForm(request.POST)
        if form.is_valid():

            array = read_csv()
            for item in array:
                add_in_database(int(item[0]), item[1], item[2])



            # question_from_form = form.cleaned_data['question'].lower().strip() # Вопрос студента
            # number_work = form.cleaned_data['number_work'] # Номер практической работы
            # add_in_database(number_work, question_from_form, '')


            # Сделать парсинг файлов csv про определённому формату
    else:
        form = QuestionsForm()
    return render(request, 'search/index.html', {'form': form})


def upload_file(request):
    if request.method == "POST":
        form_csv = UploadFileForm(request.POST, request.FILES)
        file = request.FILES['file']
    else:
        form_csv = UploadFileForm()
    return render(request, 'search/add.html', {'form_csv': form_csv})