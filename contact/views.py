from django.shortcuts import render, redirect
from django.urls import  reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    contact_form = ContactForm()
    
    #asegurarse que halla ocurrido una peticion post
    if request.method == "POST":
        #procesare formulario, rellenar plantilla automaticamente
        contact_form = ContactForm(data=request.POST)
        
        #recuperando informacion
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            
            #Enviamos el correo y redireccionamos
            email = EmailMessage(
                "La cafetiera: nuevo mensaje de contacto", #asunto
                "De {} <{}>\n\nEscribio:\n\n{}".format(name, email, content),#cuerpo
                "no-contestar@inbox.mailtrap.io", #email_origen
                ["gr4ciany@gmail.com"], #email_destino,
                reply_to=[email]
            )
            try:
                email.send()
                #todo ha ido bien, redireccionamos a ok
                return redirect(reverse('contact')+"?ok")
            except:
                #Algo no ha ido bien, redireccionamos a FAIL
                return redirect(reverse('contact')+"?fail")
            
    
    return render(request, 'contact/contact.html',{'form': contact_form})