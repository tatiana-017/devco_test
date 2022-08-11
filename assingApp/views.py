from django.shortcuts import render, redirect
from .forms import assingForm
from .models import assing
import urllib.request 
import json
import requests


# Create your views here.

def assing(request):
    url = 'https://mockend.com/tatiana-017/devco_test/posts'
    responseApi = requests.get(url)
    dataApi = responseApi.text
    json_dataApi = json.loads(dataApi)
    serialApi = []

    for entry in json_dataApi:
        serialApi.append(entry['id'])

    serialIn = 0
    assing_form=assingForm()
    if request.POST:
        assing_form=assingForm(request.POST, request.FILES)
        assingData = dict(assing_form.data)
        serialIn = assingData.get('serial')
        final = int(serialIn[0])

        if final in serialApi:
            return redirect("/assing/?invalid")

        if assing_form.is_valid():
            assing_form.save()
            return redirect("/assing/?valid")
        return render(request, "assingApp/assing.html", {'myAssingForm':assing_form})
    return render(request, "assingApp/assing.html", {'myAssingForm':assing_form})
