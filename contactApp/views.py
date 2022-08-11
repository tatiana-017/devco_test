from django.shortcuts import render, redirect
from .forms import contactForm
from django.core.mail import EmailMessage

# Create your views here.

def contact(request):
    contact_Form = contactForm()

    if request.method=="POST":
        contact_Form = contactForm(data=request.POST)
        if contact_Form.is_valid():
            requestName = request.POST.get("requestName")
            requestEmail = request.POST.get("requestEmail")
            requestCont = request.POST.get("requestCont")

            requestEmail=EmailMessage("Soporte Devco Endowment Allocation", "El usuario {} con la dirección {} tiene el siguiente requerimiento: \n {}"
            .format(requestName,requestEmail,requestCont), "", ["tr2303100@gmail.com"],reply_to=[requestEmail])

            try:
                requestEmail.send()
                return redirect("/contact/?send")
            except:
                return redirect("/contact/?error")

    return render(request, "contactApp/contact.html", {'requestForm': contact_Form})