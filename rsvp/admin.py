from django.contrib import admin
from rsvp.models import Level, Answer, Question, Guest, Response

class QuestionInlineAdmin(admin.StackedInline):
    model = Question
    fields = ('prompt',)

class LevelAdmin(admin.ModelAdmin):
    inlines = [QuestionInlineAdmin]
    
class AnswerAdmin(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]

class ResponseAdmin(admin.TabularInline):
    model = Response
    extra = 1

class GuestAdmin(admin.ModelAdmin):
    inlines = [ResponseAdmin]

admin.site.register(Level, LevelAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Guest, GuestAdmin)