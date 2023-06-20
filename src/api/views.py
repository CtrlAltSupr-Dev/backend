from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from .forms import RegistrationForm
from .models import CustomUser

from .models import Teacher
from .serializers import *


@api_view(['GET'])
def api_greet(request):
    data = Teacher.objects.all()
    serializer = TeacherSerializer(data, context={'request': request}, many=True)
    return Response(serializer.data)

@api_view(["POST"])
@csrf_exempt
def register(request):
    print('IS VALID')
    if request.method == 'POST':
        form = RegistrationForm(request.data)
        print(f"request: {request.data}")
        print(form)
        if form.is_valid():
            print('VALID')
            user = form.save()
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            print(f"current_site: {current_site}")
            mail_subject = 'Activate your account'

            # Renderizar el contenido del correo electrónico en formato HTML
            html_content = render_to_string('registration/verification_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
                'google': 'google.com',
            })

            # Configurar el contenido del correo electrónico como HTML y texto plano
            text_content = strip_tags(html_content)
            msg = EmailMultiAlternatives(mail_subject, text_content, 'ctrlaltsuprsoftware@gmail.com', [user.email])
            msg.attach_alternative(html_content, "text/html")

            # Enviar el correo electrónico
            msg.send()

            return JsonResponse({'message': 'Registration successful. Please check your email for verification instructions.'})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'error': errors}, status=400)
    else:
        form = RegistrationForm()

    return JsonResponse({'error': 'Invalid request method'}, status=405)

def activate_account(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = CustomUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return JsonResponse({'message': 'Account activation successful.'})
    else:
        return JsonResponse({'error': 'Invalid activation link.'}, status=400)
    
def test_email_verification(request):
    subject = 'Correo de verificación'
    message = '¡Gracias por registrarte! Por favor, verifica tu correo electrónico.'
    from_email = 'ctrlaltsuprsoftware@example.com'
    recipient_list = ['santelicesvicente@gmail.com']

    send_mail(subject, message, from_email, recipient_list)
    return HttpResponse('Correo de prueba enviado')
