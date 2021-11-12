import os
import sys
from django.http import HttpResponse
from django.conf.urls import url
from django.conf import settings
from django.core.wsgi import get_wsgi_application
from django.core.management import execute_from_command_line

#settingd
#url
#moodel
#debug, allowed hosts, secret key
DEBUG = os.environ.get('DEBUG', 'on') == 'on',
ALLOWED_HOST = os.environ.get('ALLOWED_HOSST', 'localhost').split(','),
SECRET_KEY = os.environ.get('SECRET_KEY', '{{ secret_key}}')

settings.configure(
    DEBUG = DEBUG,
    ALLOWED_HOST = ALLOWED_HOST,
    SECRET_KEY = SECRET_KEY,
    ROOT_URLCONF =__name__,
    MIDDLEWARE_CLASSES = (
        'django.middleware.common.commonMiddleware',
        'django.midlleware.csrf.csrfViewMiddleware',
        'django.middleware.clickjacking.XframeOptionMiddleware'
    ),


)

def index(request):
    return HttpResponse('i was here ')


urlpatterns =[
    url(r'^$', index),

]

application = get_wsgi_application()

if __name__ == '__main__':
    execute_from_command_line(sys.argv)