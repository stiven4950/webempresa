from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse

from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data = request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Se envía el correo de prueba
            email = EmailMessage(
                'La Caffettiera: Nuevo mensaje de contacto',
                'De {} <{}>\n\nEscribió: \n\n{}'.format(name, email, content),
                'no-response@inbox.mailtrap.io',
                ['omarrocha4950@gmail.com'], # Hacia donde se quieren enviar los mensajes
                reply_to=[email]
            )

            try:
                email.send()
                return redirect(reverse('contact') + '?ok')
            except:
                # Algo no ha ido bien
                return redirect(reverse('contact') + '?fail')

    return render(request, 'contact/contact.html', {'form':contact_form})