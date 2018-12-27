import hashlib
import json
import time

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

# 判断用户是否登录
def home(request):
    # 获取session判断用户是否登录
    id = request.session.get('id')
    data = {}

    user = User.objects.filter(pk=id)
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
    # 设置默认昵称

    return JsonResponse(data)

def login(request):
    username = request.POST.get('username')
    data = {}

    user = User.objects.filter(username=username)
    password = request.POST.get('password')
    password = secret_pwd(password)

    if not user.exists():
        # 查总用户表
        code = help_login(username, password)

        if code == '登录成功':
            user = User.objects.filter(username=username)

            if user.exists():
                user = user.first()
                data['status'] = '200'
                data['msg'] = '登录成功'
                request.session['id'] = user.id
            else:
                data['status'] = '404'
                data['msg'] = '账号或密码错误'

        else:
            data['status'] = '404'
            data['msg'] = '账号或密码错误'

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

# 首页新闻数据
def home_model(request):
    data = {
        'status': '200',
        'msg': 'ok'
    }
    info = industry_information.objects.all()
    data['info1'] = list(info.values())[0:3]
    data['info2'] = list(info.values())[3:6]
    data['info3'] = list(info.values())[6:9]
    data['info4'] = list(info.values())[9:12]

    # info = test.objects.all()
    # print(list(info.values()))
    # data['info'] = list(info.values())

    return JsonResponse(data)

# 编辑用户信息
def compile_userinfo(request):
    nickname = request.POST.get('nickname')
    password = request.POST.get('password')
    user_icon = request.FILES['user_icon']

    data = {}

    # 获取当前用户
    id = request.session.get('id')

    user = User.objects.filter(pk=id)
    if user.exists():
        user = user.first()
        user.nickname = nickname
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

# 对时间进行处理
def operate_date(data_list):
    data_set_return = {}
    data_list_return = []
    timeStamp_list = []
    count = 1

    # 根据时间进行排序
    for i in data_list:
        date = i['date']
        if len(date) < 12:
            date = date + ' 00:00:00'
        # print('获取的日期为',date)

        # 转为时间数组
        timeArray = time.strptime(date, "%Y-%m-%d %H:%M:%S")
        timeStamp = int(time.mktime(timeArray))

        if timeStamp in data_set_return:
            # print('时间戳重复',timeStamp)
            timeStamp += count
            count += 1

        # print('修改后的时间戳',timeStamp)
        data_set_return[timeStamp] = i
        # print('时间戳为:::',timeStamp)
        timeStamp_list.append(int(timeStamp))

    timeStamp_list.sort(reverse=True)

    # 将排好序的对象保存并返回
    # print('来到了这里')
    for j in timeStamp_list:
        data_list_return.append(data_set_return[j])

    return data_list_return

# 获取数据库信息
def get_data(data_list,count):
    if count == None:
        data_list_return = operate_date(data_list)
        return data_list_return

    else:
        # print('进入了这里')
        data_list_return = operate_date(data_list)
        # print('切片后的值为：：：',data_list_return,type(data_list_return),count)
        return data_list_return[0:int(count)]

# 行业公告
def send_announce(request):
    # print('进入此页面')
    count = request.GET.get('count')
    # print(count)
    data_list = Announcement.objects.all()
    data_list = list(data_list.values())
    data = {}

    announce = get_data(data_list, count)
    # print(industry)
    data['info'] = announce
    return JsonResponse(data)


# 行业资讯
def send_industry(request):
    count = request.GET.get('count')
    data_list = industry_information.objects.all()
    data_list = list(data_list.values())
    data = {}
    # if len(data_list[0]['date']) < 12:
    #     date = data_list[0]['date'] + ' 00:00:00'
    # print('日期信息为::::',date)

    industry = get_data(data_list,count)
    # print(industry)
    data['info'] = industry
    return JsonResponse(data)

# 行业分析
def send_analyse(request):
    count = request.GET.get('count')
    data_list = analyse_of_market.objects.all()
    data_list = list(data_list.values())
    data = {}

    analyse = get_data(data_list, count)
    # print(industry)
    data['info'] = analyse
    return JsonResponse(data)

def web_home(request):
    data = {
        'status': '200',
        'msg': 'ok'
    }

    info_list = web_lists.objects.all()
    web_type_list = []
    for info in info_list:
        if info.web_type.strip(' ') not in web_type_list:
            web_type_list.append(info.web_type.strip(' '))

    for web_type in web_type_list:
        web_object = web_lists.objects.filter(web_type=web_type)
        data[web_type] = list(web_object.values())

    return JsonResponse(data)

def save_icon(request):
    icon = request.FILES.get('icon')
    # a = str(icon)
    # print(icon,type(icon))
    a = User.objects.get(pk=8)
    print(str(a.user_icon),type(str(a.user_icon)))

    user = User()
    user.username = '11'
    user.password = '123456'
    user.user_icon = icon

    user.save()

    return HttpResponse('保存成功')

def test_img(request):
    return render(request,'img_test.html')

def home_each(request):
    data = {
        'status': '200',
        'msg': 'ok'
    }

    id  = request.GET.get('id')
    info = industry_information.objects.filter(pk=id)

    data['info'] = list(info.values())
    return JsonResponse(data)

# 热点头条详情页
def get_announce(request):
    data = {
        'status': '200',
        'msg': 'ok'
    }

    id = request.GET.get('id')

    info = Announcement.objects.filter(pk=id)

    data['info'] = list(info.values())
    return JsonResponse(data)

def get_industry(request):
    data = {
        'status': '200',
        'msg': 'ok'
    }

    id = request.GET.get('id')
    info = industry_information.objects.filter(pk=id)

    data['info'] = list(info.values())
    return JsonResponse(data)

def get_analyse(request):
    data = {
        'status': '200',
        'msg': 'ok'
    }

    id = request.GET.get('id')
    info = analyse_of_market.objects.filter(pk=id)

    data['info'] = list(info.values())
    return JsonResponse(data)

# 网址导航更多页面
def web_guide(request):
    data = {
        'status': '200',
        'msg': 'ok'
    }

    types = request.GET.get('type')

    info_list = web_list.objects.filter(web_type=types)
    data['info'] = list(info_list.values())

    return JsonResponse(data)


































