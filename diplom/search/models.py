from django.db import models


# Create your models here.


class Keywords(models.Model):
    word = models.CharField(max_length=200, verbose_name="Ключевое слово")

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = 'Ключевое слово'
        verbose_name_plural = 'Ключевые слова'


class Questions(models.Model):
    question = models.CharField(max_length=201, verbose_name='Вопрос')
    keywords = models.ManyToManyField(Keywords, verbose_name="Ключевые слова")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    answer = models.TextField(blank=True, verbose_name='Ответ')
    is_answered = models.BooleanField(default=False, verbose_name='Есть ответ?')
    number_work = models.IntegerField(verbose_name="Лабораторная работа")


    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Вопросы'
        verbose_name_plural = 'Вопросы'
        ordering = ['created_at']
