from django.contrib import admin

from .models import Question, Choice

# Register your models here.

admin.site.site_header = "Poll Maker"
admin.site.site_title = "Poll Maker Admin"
admin.site.index_title = "Welcome to the Poll Maker Admin"

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldset = [(None, {'fields': ['question_text']}), ('Date Info', {
        'fields': ['pub_date'], 'classes': ['collapse']}), ]
    
admin.site.register(Question, QuestionAdmin)