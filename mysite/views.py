from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    #redirect user to the polls index
    return HttpResponseRedirect(reverse('poll:index'))