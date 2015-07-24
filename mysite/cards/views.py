from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Card

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'cards/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Card.objects.order_by('-created_at')[:5]


class DetailView(generic.DetailView):
    model = Card
    template_name = 'cards/detail.html'


class ResultsView(generic.DetailView):
    model = Card
    template_name = 'cards/results.html'
    

