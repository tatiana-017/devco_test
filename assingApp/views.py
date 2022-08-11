from django.shortcuts import render
from .forms import assingForm
from .models import assing


# Create your views here.

url  = ''
def assing(request):
    assing_form=assingForm()
    if request.POST:
        assing_form=assingForm(request.POST, request.FILES)
        if assing_form.is_valid():
            assing_form.save()
        return render(request, "assingApp/assing.html", {'myAssingForm':assing_form})
    return render(request, "assingApp/assing.html", {'myAssingForm':assing_form})
