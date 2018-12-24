import hashlib
import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from App.models import industry_information
from App.models import Announcement
from App.models import User
from App.models import analyse_of_market
from App.models import web_list

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def home(request):
    # 获取session判断用户是否登录
    userid = request.session.get('userid')
    data = {}

    user = User.objects.filter(userid=userid)
    if user.exists():
        data['status'] = '203'
        data['msg'] = '用户已登录'
        data['person'] = user

    else:
        data['status'] = '300'
        data['msg'] = '用户未登录'

    return JsonResponse(data)


def secret_pwd(password):
    password = hashlib.md5(password.decode('utf-8')).hexdigest()
    return password


def register(request):
    userid = request.POST.get('userid')
    data = {}

    # 从数据库获取对应账号数据,如果有就说明用户已存在
    user = User.objects.filter(userid=userid)

    if user.exists():
        data['status'] = '401'
        data['msg'] = '用户已存在'

    else:
        user = User()
        user.userid = userid

        user.save()

        data['status'] = '200'
        data['msg'] = '注册成功'

    return JsonResponse(data)

def login(request):
    userid = request.POST.get('userid')
    data = {}

    user = User.objects.filter(userid=userid)

    if not user.exists():
        data['status'] = '402'
        data['msg'] = '用户不存在'

    else:
        user = user.first()

        password = request.POST.get('password')
        # 判断密码是否正确
        if password == secret_pwd(user.password):
            data['status'] = '201'
            data['msg'] = '登录成功'

            # 设置session
            request.session['userid'] = user.userid

        else:
            data['status'] = '403'
            data['msg'] = '密码错误'

    return JsonResponse(data)


def unlogin(request):
    request.session.flush()

    data = {
        'status': '202',
        'msg': '用户已注销'
    }

    return JsonResponse(data)


def home_model(request):
    data = {
        'status': '200',
        'msg': 'ok'
    }
    info = industry_information.objects.all()
    # data['news_info'] = info[0:12]
    data['info'] = list(info.values())[0:12]
    # print(list(info.values))

    return JsonResponse(data)

# 编辑用户信息
def compile_userinfo(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user_icon = request.FILES['user_icon']

    data = {}

    # 获取当前用户
    userid = request.session.get('userid')

    user = User.objects.filter(userid=userid)
    if user.exists():
        user = user.first()
        user.username = username
        # 密码加密
        user.password = secret_pwd(password)
        user.user_icon = user_icon

        user.save()

    return JsonResponse(data)

def test(request):
    if request.method == 'GET':
        print('*************')
        print(request.GET.get('id'))
        print('这是GET请求',request.body)
        print(request.method)
    elif request.method == 'POST':
        print('*************')
        username = request.POST.get('username')
        users_vue = request.body
        user_dict = users_vue.decode()
        user_dict = json.loads(user_dict)
        username = user_dict['username']
        password = user_dict['password']
        print('post数据',username)
        print(password)

    data = {
        'status': '200',
        'msg': 'ok',
    }

    return JsonResponse(data)

















































