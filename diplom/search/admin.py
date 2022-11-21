from django.contrib import admin
from .models import Questions


# Register your models here.

class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'keywords', 'created_at', 'updated_at', 'is_answered')
    list_display_links = ('id', 'question')
    search_fields = ('question',)
    list_filter = ('is_answered',)


admin.site.register(Questions, QuestionsAdmin)
