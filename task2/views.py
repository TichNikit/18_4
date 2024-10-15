from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

def def_func_template(request):
    return render(request, 'func_template.html')

class Class_template(TemplateView):
    template_name = 'class_template.html'
