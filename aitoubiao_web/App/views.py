import hashlib
import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from App.models import industry_information, web_lists
from App.models import Announcement
from App.models import User
from App.models import analyse_of_market
from App.models import web_list
from App.models import test


# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from App.user_help import help_login


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
    username = request.POST.get('username')
    data = {}

    user = User.objects.filter(username=username)
    password = request.POST.get('password')

    if not user.exists():
        # 查总用户表
        code = help_login(username, password)
        if code == '没有此用户':
            data['status'] = '404'
            data['msg'] = '登录失败'
        elif code == '登录成功':
            data['status'] = '200'
            data['msg'] = '登录成功'

    else:
        user = user.first()
        data['status'] = '200'
        data['msg'] = '登录成功'

        request.session['id'] = user.id

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
    data['info'] = list(info.values())[0:12]

    # info = test.objects.all()
    # print(list(info.values()))
    # data['info'] = list(info.values())

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

# 保存web网站链接信息
def tests(request):
    if request.method == "GET":
        return render(request, "web_img_info.html")
    elif request.method == "POST":

        web_name = request.POST.get("web_name")
        web_url = request.POST.get("web_url")
        web_type = request.POST.get("web_type")
        icon = request.FILES.get("icon")
        web = web_lists()
        web.web_name = web_name
        web.web_url = web_url
        web.web_type = web_type
        web.web_icon = icon
        web.save()

        return render(request, "web_img_info.html")


def save_img(request):
    return render(request,'web_img_info.html')

def web_name(request):
    data = {
        'status': '200',
        'msg': 'ok'
    }

    info_list = web_list.objects.all()
    web_type_list = []
    for info in info_list:
        if info.web_type.strip(' ') not in web_type_list:
            web_type_list.append(info.web_type.strip(' '))

    for web_type in web_type_list:
        if web_type == '报送数据前十名':
            web_type = ' 报送数据前十名'
        web_object = web_list.objects.filter(web_type=web_type)
        data[web_type] = list(web_object.values())

    # data['info'] = list(info.values())

    return JsonResponse(data)

















































