from django.contrib import Admin

from .models import Choice, Question

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    ...
        # ...

    fieldsets = [

from .models import Question

# ...
admin.site.register(Choice)
class QuestionAdmin(admin.ModelAdmin):
       fieldsets = [
         (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
       ]
    fields = ["pub_date", "question_text"]

    admin.site.register(Question, QuestionAdmin)




# Register your models here.
