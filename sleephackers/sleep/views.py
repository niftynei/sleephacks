from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.html import escape

import upconnect
import os
import logging
import sys

logger = logging.getLogger('django')   # Django's catch-all logger
hdlr = logging.StreamHandler()   # Logs to stderr by default
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.DEBUG)

# tools for encryption

app_name = "Sleep Hacker"

app_config = {
    'UP_API_CLIENT_ID': os.environ['UP_API_CLIENT_ID'],
    'UP_API_SECRET': os.environ['UP_API_SECRET']
}

redirect_url = 'http://127.0.0.1:8000/authorize'

def _up_provider():
    return upconnect.UPProvider(app_config['UP_API_CLIENT_ID'], app_config['UP_API_SECRET'])

def _token(request):
    token = request.COOKIES.get('token', None)
    return token

def index(request):
    token = _token(request)
    
    if not token:
        return redirect('/signup') 

    up = _up_provider()
    user = up.read(token, 'users/@me')
    response = HttpResponse('<html><b>Hello %s!</b></html>' % user['data']['first'], mimetype='text/html')

    return response

def signup(request):
    up = _up_provider()
    url = up.get_connect_url(redirect_url, 'basic_read move_read move_write')

    response = redirect(url)
    return response

def authorize(request):
    up = _up_provider()
    code = escape(request.GET.get('code', ''))
    token = up.get_user_token(code)
    ct = str(token['access_token'])

    response = redirect('/')
    response.set_cookie('token', ct, max_age=2592000)

    return response
