from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from rsvp.forms import SearchForm, ReplyForm
from rsvp.models import Guest 

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            guest = Guest.objects.get(last_name__iexact=form.cleaned_data['last_name'].lower())
            if guest:
                request.session['guest'] = guest.id
                return HttpResponseRedirect(reverse('questions'))
    else:
        form = SearchForm()
    return render(request, 'rsvp/search.html', {'form': form})
    
def questions(request):
    if 'guest' not in request.session or request.session['guest'] is None:
        return HttpResponseRedirect(reverse('search'))
    guest = Guest.objects.get(pk=request.session['guest'])
    if request.POST:
        reply_form = ReplyForm(request.POST, instance=guest)
        if reply_form.is_valid():
            reply_form.save()
            del request.session['guest']
            return HttpResponseRedirect(guest.level.redirect)
    else:
        reply_form = ReplyForm(instance=guest)
    return render(request, 'rsvp/answer.html', {'guest': guest, 'reply' : reply_form})