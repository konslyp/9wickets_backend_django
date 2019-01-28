from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from backend.models import User
# Create your views here.
def setMessage(context,request):
    error = ''
    if 'error' in request.session:
        error = request.session['error']
        request.session['error'] = ""
    context['error'] = error;

    message = ''
    if 'message' in request.session:
        message = request.session['message']
        request.session['message'] = ""
    context['message'] = message;
    return context
def isLogin(request):
    if 'role' in request.session:
        role = request.session['role']
        if role == '':
            return 0
        return 1
    return 0
def error (request,error):
    request.session['error'] = error
    return;

def login(request):
    context = {}
    context = setMessage(context,request)
    return render(
        request,
        'login.html',
        context,
    )
def index(request):
    if isLogin(request) == 1:
        return redirect('/panel/dashboard')
    return redirect('/panel/login')
def dashboard(request):
    if isLogin(request) == 0:
        return redirect('/panel/login')
    context = {}
    context = setMessage(context,request)
    context['pageName'] = 'Dashboard'
    return render(
        request,
        'main.html',
        context,
    )
def systemAdmin(request):
    if isLogin(request) == 0:
        return redirect('/panel/login')
    systemAdmins = User.objects.filter(type = 1).all()
    context = {}
    context = setMessage(context,request)
    context['pageName'] = 'SystemAdmin'
    context['users'] = systemAdmins
    return render(request,'main.html',context)

def actionLogin(request):
    userName = request.POST.get("user", "")
    userPw = request.POST.get("pw", "")
    userType = request.POST.get("type", "")
    if not userName:
        error(request,'Please fill username')
        return redirect('/panel/')
    if not userPw:
        error(request,'Please fill password')
        return redirect('/panel/')
    userInfo = User.objects.filter(name = userName,pw = userPw,type = int(userType)).get()
    if not userInfo:
        error(request,'User does not exist.')
        return redirect('/panel/')
    print ('id' + userInfo.name)
    request.session['role'] = userType
    request.session['userName'] = userInfo.name
    context = {}
    context = setMessage(context,request)
    return redirect('/panel/dashboard')

def actionLogout(request):
    request.session['role'] = ''
    request.session['userName'] = ''
    return redirect('/panel/')
def test(request):
    return HttpResponse("<h1>aaa</h1>")
