from django.shortcuts import render
from django.http import HttpResponse


def second_index(request):
    host = request.META['HTTP_HOST']
    identificator = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']

    return HttpResponse(f'''
    host: {host}
    id: {identificator}
    user_agent: {user_agent}
    ''')


def error(request):
    return HttpResponse(f'''Извините, произошла ошибка''', status=400,
                        reason='ctyyu')


def user(request, login='aboba', directory='abobus', post='lool'):
    # return HttpResponse('hgfgfygfyhgyhg')
    return HttpResponse(f'''
    Name:{login}
    Directory: {directory}
    post: {post}
    ''')
