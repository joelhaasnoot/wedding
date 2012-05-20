from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from utils.showonly import ShowOnly
from rsvp.models import Guest, Question, Answer, Response
from django.forms.widgets import TextInput, HiddenInput, Select

class StringWidget(forms.widgets.Input):
    def render(self, name, value, attrs=None):
        # Create a hidden field first
        hidden_field = forms.widgets.HiddenField(attrs) 
        return mark_safe(u'<p>%s</p>%s' % (value, hidden_field.render(value, attrs)))

class SearchForm(forms.Form):
    last_name = forms.CharField()
    postcode = forms.CharField(max_length=8)
    
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'form'
        self.helper.form_method = 'post'

        self.helper.add_input(Submit('submit', 'Opzoeken'))
        super(SearchForm, self).__init__(*args, **kwargs)
        
class ReplyForm(forms.ModelForm):    
    reply = forms.IntegerField(label="Kom je ook?", widget=forms.Select(choices=Guest.RSVP_CHOICES))
    people = forms.IntegerField(label="Met hoeveel mensen kom je?")
    message = forms.CharField(label="Vragen? Nog iets dat we moeten weten?", required=False, widget=forms.Textarea())
    
    def __init__(self, *args, **kwargs):
        super(ReplyForm,self ).__init__(*args,**kwargs) # populates the post
        self.helper = FormHelper()
        self.helper.form_tag = False
        
    class Meta:
        model = Guest
        fields = ('reply', 'people', 'message')
    
class ResponseForm(forms.ModelForm):
    question = forms.CharField(required=False, label=None, widget=HiddenInput())
    response = forms.ModelChoiceField(Answer.objects.filter(), label='', required=False)
    
    class Meta:
        model = Response    
        
    def clean_question(self): # Prevent editing
        return self.instance.question

    def __init__(self,*args,**kwargs):
        super(ResponseForm,self ).__init__(*args,**kwargs) # populates the post
        if self.instance:
            self.fields["response"].queryset = Answer.objects.filter(question=self.instance.question)
        self.helper = FormHelper()
        self.helper.form_tag = False