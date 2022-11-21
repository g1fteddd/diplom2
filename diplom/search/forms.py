from django import forms


class QuestionsForm(forms.Form):
    question = forms.CharField(max_length=200, label='Вопрос')
    number_work = forms.IntegerField(label="Номер практической работы")


class UploadFileForm(forms.Form):
    file = forms.FileField()
