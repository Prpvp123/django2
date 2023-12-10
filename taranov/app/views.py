from django.shortcuts import render
from django.http import HttpResponse


def index(request, name='gbvgh', age=0):
    host = request.META['HTTP_HOST']
    user_agent = request.META['HTTP_USER_AGENT']
    path = request.path

    return HttpResponse(f"""
        <p>Host: {host}<p/>
        <p>User-agent: {user_agent}<p/>
        <p>Path: {path}<p/>
        
    """ + f'user: {name}, age {age}', headers={'SecretCode': '1234567890'})
