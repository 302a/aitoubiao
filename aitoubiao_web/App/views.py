import hashlib

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from App.models import industry_information
from App.models import Announcement
from App.models import User

# Create your views here.

def home(request):
    # 获取session判断用户是否登录
    userid = request.session.get('userid')
    data = {}

    user = User.object.filter(userid=userid)
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
    user = User.object.filter(userid=userid)

    if user.exists():
        data['status'] = '401'
        data['msg'] = '用户已存在'

    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_icon = request.FILES['user_icon']

        user = User()
        user.userid = userid
        user.username = username
        # 密码加密
        user.password = secret_pwd(password)
        user.user_icon = user_icon

        user.save()

        data['status'] = '200'
        data['msg'] = '注册成功'

    return JsonResponse(data)

def login(request):
    userid = request.POST.get('userid')
    data = {}

    user = User.object.filter(userid=userid)

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

    info = industry_information.object.all()
    data['news_info'] = info[0:12]
    return JsonResponse(data)
















































