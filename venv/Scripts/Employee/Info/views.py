from django.shortcuts import render
from .models import Empdet
from .forms import EmpdetForms

# Create your views here.

def EmpInsert(request):
    #breakpoint()
    myform = EmpdetForms()
    if request.method == "POST":
        obj = EmpdetForms(request.POST)
        obj.save()
        myform = EmpdetForms()

    template_name = "Info/employ_form.html"
    context_name = {"obj": myform}
    return render(request,template_name,context_name)

