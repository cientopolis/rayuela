from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from alaapp.models.token import Token
from werkzeug.security import generate_password_hash,check_password_hash
from decouple import config

import hashlib
import random

class System(object):
    
    
    @staticmethod
    def is_logged(request):
        try:
            request.session['id']
        except KeyError:
            return False     
        else:
            return True


    @staticmethod
    def f_send_mail(user):
        token = System.generate_token()
        encript = generate_password_hash(str(user.get_id()), 'sha256', 5)
        t=Token(user_id=user,token=token)
        t.save()
        message_ = render_to_string(
            'alaapp/verificate/activate_account.html',
            { 'token': token+encript,'site': config('DEFAULT_DOMAIN') }
            )
        subject="Bienvenido/a a ALA"
        message=''
        email_from=settings.EMAIL_HOST_USER
        recipient_list=[user.get_email()]
        html_message=message_
        send_mail(
            subject=subject, 
            message=message, 
            recipient_list=recipient_list, 
            from_email=email_from, 
            fail_silently=False,
            html_message=html_message
            )

    @staticmethod
    def set_session(request,user):
        try:
            request.session['profile_image'] = user.get_profile_image().url   
        except ValueError:
            pass
        finally:
            request.session['id'] = user.get_id()
            request.session['username'] = user.get_username()
            request.session['email'] = user.get_email()
            request.session['complete_name'] = user.get_complete_name() 
            request.session['role'] = user.get_role().get_name()

    @staticmethod
    def logout(request):
        
        try:
            del request.session['id']
        except KeyError:
            return False  
    

    @staticmethod
    def generate_token(length=15):
        chars = list(
        'ABCDEFGHIJKLMNOPQRSTUVWYZabcdefghijklmnopqrstuvwyz01234567890'
        )
        random.shuffle(chars)
        chars = ''.join(chars)
        sha1 = hashlib.sha1(chars.encode('utf8'))
        token = sha1.hexdigest()
        return token[:length]   

    def decode_token(token):
        object_token=Token.objects.get(token__iexact=token[:15])  
        return object_token.user_equal(token)
        
    def is_admin(request):
        return (request.session['role']=='ADMIN')

    def is_root(request):
        return (request.session['role']=='ROOT')  

    def is_player(request):
        return (request.session['role']=='PLAYER')  


    @staticmethod
    def get_navbar_color():
        return settings.NAVBAR_COLOR
  
    @staticmethod
    def is_access_correct(var):
        try:
            var
        except KeyError:
            return False     
        else:
            return True