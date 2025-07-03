import json
from django import http
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.views.generic.base import View

from accounts.forms import LoginForm
from accounts.serializers import UserProfileSerializer, UserSerializer
from utils.response import BadRequestJsonResponse, MethodNotAllowedJsonResponse, UnauthenticatedJsonResponse


def user_login(request):
    """ 用户登录 """
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            print('表单验证通过')
        else:
            print(form.errors)
    else:
        form = LoginForm()
    return render(request, 'user_login.html', {
        'form': form
    })

def user_logout(request):
    """ 用户退出登录 """
    logout(request)
    return redirect('/accounts/user/info/')

@login_required
def user_info(request):
    """ 用户信息 """
    print(request.user)
    return render(request, 'user_info.html')


def user_api_login(request):
    """ 用户登录接口-POST """
    # 获取输入的内容
    if request.method == 'POST':
        # 表单验证
        form = LoginForm(request.POST)
        if form.is_valid():
            # 如果通过验证，执行登录
            user = form.do_login(request)
            profile = user.profile
            # 返回的内容：用户的信息（基本信息、详细信息）
            data = {
                'user': UserSerializer(user).to_dict(),
                "profile": UserProfileSerializer(profile).to_dict()
            }
            return http.JsonResponse(data)
        else:
            # 如果没有通过表单验证，返回表单错误信息
            err = json.loads(form.errors.as_json())
            return BadRequestJsonResponse(err)
    else:
        #  请求不被允许
        return MethodNotAllowedJsonResponse()



def user_api_logout(request):
    """ 用户退出接口 """
    logout(request)
    return http.HttpResponse(status=201)

class UserDetailView(View):
    """ 用户详细信息接口 """
    def get(self, request):
        user = request.user
        # 用户：是游客吗？
        if user.is_authenticated:
            # 返回401状态码
            return UnauthenticatedJsonResponse()
        else:
            # 返回详细信息
            profile = user.profile
            # 返回的内容：用户的信息（基本信息、详细信息）
            data = {
                'user': UserSerializer(user).to_dict(),
                "profile": UserProfileSerializer(profile).to_dict()
            }
            return http.JsonResponse(data)

def user_api_register(request):
    """ 用户注册 """
    #  1. 表单，验证用户输入的信息（用户名、昵称、验证码）
    #  2. 创建用户基础信息表、用户详细信息表
    #  3. 执行登录
    #  4. 保留登录的日志


class UserRegisterView(FormView):
    """ 用户注册的接口 """
    form_class = RecursionForm
    http_method_names = ['post']

    def form_valid(self, form):
        """ 表单通过验证 """
        reslut = form.do_register(requset=self.request)
        if reslut is not None:
            user, profile=
            data = {
                'user': UserSerializer(user).to_dict(),
                "profile": UserProfileSerializer(profile).to_dict()
            }
            return http.JsonResponse(data, status=201)
        return ServerErrorJsonResponse()

    def form_invalid(self, form):
        """  表单未通过验证 """
        err_list = json.load(form.errors.as_json())
        return BadRequestJsonResponse(err_list)



