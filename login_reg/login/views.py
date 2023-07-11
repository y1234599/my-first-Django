from django.shortcuts import render

# Create your views here.
from .models import RegisterUser
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
import re


def main_page(request):
    login_msg = "恭喜！ 登录成功"
    return render(request, 'main_page.html', {'login_msg': login_msg})


'''用户登录'''
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    # 如果是post请求方法，获取用户输入的账号密码
    if request.method == 'POST':
        userEmail = request.POST.get('username')
        userPassword = request.POST.get('password')

        # 这里变量类型都是字符串，所以不能使用if .. == None，只能使用 if .. == ''或者if not
        if not userEmail or not userPassword:
            error_msg = '输入为空'
            return render(request, 'login.html', {'error_msg': error_msg})

        # 查询数据库中的账号密码
        try:
            user = RegisterUser.objects.get(reg_mail=userEmail)
            if userPassword == user.reg_pwd:
                return redirect('/main_page/')

            else:
                error_msg = '密码错误'
                return render(request, 'login.html', {'error_msg': error_msg})
        except:
            error_msg = "用户不存在"
            return render(request, 'login.html', {'error_msg': error_msg})


'''用户注册'''
def register(request):
    if request.method == 'POST':
        userEmail = request.POST.get('userEmail')
        userPassword = request.POST.get('userPassword')
        userRePassword = request.POST.get('userRePassword')


        # 防止用户输入为空
        # 这里变量类型都是字符串，所以不能使用if .. == None，只能使用 if .. == ''或者if not
        if not userEmail or not userPassword or not userRePassword:
            error_msg = '输入为空'
            return render(request, 'register.html', {'error_msg': error_msg})

        # 正则表达验证密码是否合规
        elif not check(userPassword):
            error_msg = '请输入8-16位密码，只可包含数字，字母'
            return render(request, 'register.html', {'error_msg': error_msg})

        # 判断用户名是否存在
        try:
            user = RegisterUser.objects.get(reg_mail=userEmail)
            if user:
                error_msg = '用户名已存在'
                return render(request, 'register.html', {'error_msg': error_msg})

        # 判断两次输入密码是否一至
        except:
            if userPassword != userRePassword:
                error_msg = '密码不一致'
                return render(request, 'register.html', {'error_msg': error_msg})

            # 将注册信息写入login_registeruser表中
            else:
                register = RegisterUser()
                register.reg_mail = userEmail
                register.reg_pwd = userPassword
                register.save()
                return redirect('/login/')

    else:
        return render(request, 'register.html')


def about(request):
    return render(request, 'about.html')


def cooperation(request):
    return render(request, 'cooperation.html')


def help(request):
    return render(request, 'help.html')


def join(request):
    return render(request, 'join.html')


def check(n):
    password = re.compile(r"^[a-zA-Z0-9]{8,16}$")
    if password.findall(n):
        return True
    else:
        return False
