from django.shortcuts import redirect, render, HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings

def index(request):
    return render(request, 'index.html', {
        
    })

def tests(request):
    return render(request, 'tests.html', {

    })

def products(request):
    return render(request, 'products.html', {

    })

def services(request):
    return render(request, 'services.html', {
        
    })

def policy(request):
    return render(request, 'policy.html', {
        
    })

def send_email(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        city = request.POST['city']
        neighborhood = request.POST['neighborhood']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']

        context = {
            'name': name,
            'age': age,
            'city': city,
            'neighborhood': neighborhood,
            'phone': phone,
            'email': email,
            'message': message
        }

        template = get_template('email.html')

        content = template.render(context)

        email = EmailMultiAlternatives(
            'Nueva inquietud de {}'.format(name),
            'pruebasmasvidas.com',
            settings.EMAIL_HOST_USER, 
            [settings.EMAIL_HOST_USER]
        )

        email.attach_alternative(content, 'text/html')
        email.send()

        return redirect('index')
        
