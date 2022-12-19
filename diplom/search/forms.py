from django import forms


class QuestionsForm(forms.Form):
    question = forms.CharField(max_length=200, label='Вопрос', widget=forms.TextInput(attrs={'placeholder': 'Начните '
                                                                                                         'вводить '
                                                                                                         'вопрос'}))
    number_work = forms.IntegerField(label="Номер")


class UploadFileForm(forms.Form):
    file = forms.FileField()
