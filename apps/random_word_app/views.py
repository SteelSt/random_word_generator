from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
# Create your views here.
def index(request):
    if 'count' not in request.session:
        request.session['count'] = 1
    request.session['word'] = get_random_string(length=14)
    request.session['count']+=1
    return render(request,'random_word_app/index.html')

def reset(request):
    request.session.clear()
    request.session['count'] = 1
    del request.session['count']
    return render(request,'random_word_app/index.html')

def generate(request, methods=['POST']):
    return redirect('/')