from django.shortcuts import render
from django.views import generic

# Create your views here.


class HomeView(generic.TemplateView):
    template_name = "buildmaker/home.html"


class TodoView(generic.TemplateView):
    template_name: str = "buildmaker/todo.html"
