from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from rsvp.models import Guest, Question

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
    message = forms.CharField(label="Vragen? Nog iets dat we moeten weten?", required=False, widget=forms.Textarea())
 
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'form'
        self.helper.form_method = 'post'

        self.helper.add_input(Submit('submit', 'Opslaan'))
        super(ReplyForm, self).__init__(*args, **kwargs)
 
    class Meta:
        model = Guest
        fields = ('reply', 'message')
    
    