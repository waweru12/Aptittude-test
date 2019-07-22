from django.contrib import admin
from .models import Exam,Question

admin.site.register(Exam)
class QuestionAdmin(admin.ModelAdmin):
  
   change_list_template = 'exam.html'

admin.site.register(Question,QuestionAdmin)
