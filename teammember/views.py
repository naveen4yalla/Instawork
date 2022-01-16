from django.http import request
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .forms import PostForm
from .models import People

class TeamList(ListView):
    model = People
    context_object_name= 'peoplelist'
    #To get the total count of the members in the list 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['totalcount'] = People.objects.all().count
        return context
    """ def get_queryset(self):
        queryset = super(TeamList,self).get_queryset()
        for a in queryset:
            a.phone=a[:3]+"-"+a[4:7]+"-"+a[7:]
        return queryset """

class AddPeople(CreateView):
    model = People
    form_class = PostForm
    context_object_name = 'addpeople'
    template_name = 'teammember/addpeople.html'
    success_url = reverse_lazy('team')

    
class EditPeople(UpdateView):
    model=People
    context_object_name = 'editpeople'
    form_class = PostForm
    template_name = 'teammember/editpeople.html'
    success_url = reverse_lazy('team')
    
    
class DeletPeople(DeleteView):
    model=People
    context_objct_nmae = 'deletepeople'
    success_url = reverse_lazy('team')
    