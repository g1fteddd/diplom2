from django.contrib import admin
from .models import Questions, Keywords


# Register your models here.

class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'created_at', 'updated_at', 'is_answered')
    list_display_links = ('id', 'question')
    search_fields = ('question',)
    list_filter = ('is_answered',)
    filter_horizontal = ['keywords']


admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Keywords)
