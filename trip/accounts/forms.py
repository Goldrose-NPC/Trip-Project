import re

from django import forms
from django.contrib.auth import authenticate, login
from django.core.cache import cache
from django.db import transaction
from django.utils.timezone import now

from accounts.models import User, Profile
from utils import constants


class LoginForm(forms.Form):
    """ 登录表单 """
    username = forms.CharField(label='用户名',
                               max_length=100,
                               required=False,
                               help_text='使用帮助',
                               initial='admin')
    password = forms.CharField(label='密码', max_length=200, min_length=6,
                               widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 当前登录的用户
        self.user = None

    def clean_username(self):
        """ 验证用户名 hook 钩子函数 """
        username = self.cleaned_data['username']
        pattern = r'^1[0-9]{10}$'
        if not re.search(pattern, username):
            raise forms.ValidationError('手机号%s输入不正确',
                                        code='invalid_phone',
                                        params=(username, ))
        return username

    def clean(self):
        data = super().clean()
        print(data)
        # 如果单个字段有错误，直接返回，不执行后面的验证
        if self.errors:
            return
        username = data.get('username', None)
        password = data.get('password', None)
        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError('用户名或者是密码不正确')
        else:
            if not user.is_active:
                raise forms.ValidationError('该用户已经被禁用')
        self.user = user
        return data

    def do_login(self, request):
        """ 执行用户登录 """
        user = self.user
        # 调用登录
        login(request, user)
        # 修改最后登录的时间
        user.last_login = now()
        user.save()
        # TODO 保存登录历史
        return user

class RegisterForm(forms.Form):
    """ 用户注册 """
    username = forms.CharField(label='手机号码', max_length=11, required=True, error_messages={
        'required': '请输入手机号码'
    })
    password = forms.CharField(label='密码', max_length=128, required=True, error_messages={
        'required': '请输入密码'
    })
    nickname = forms.CharField(label='昵称', max_length=128, required=True, error_messages={
        'required': '请输入昵称'
    })
    sms_code = forms.CharField(label='验证码', max_length=6, required=True, error_messages={
        'required': '请输入验证码'
    })

    def clean_username(self):
        """ 验证用户名 hook 钩子函数 """
        username = self.cleaned_data['username']
        pattern = r'^1[0-9]{10}$'
        if not re.search(pattern, username):
            raise forms.ValidationError('手机号%s输入不正确',
                                        code='invalid_phone',
                                        params=(username,))
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('手机号已经被使用了')
        return username

    def clean_nickname(self):
        """ 验证昵称 hook 钩子函数 """
        nickname = self.cleaned_data['nickname']
        if User.objects.filter(nickname=nickname).exists():
            raise forms.ValidationError('昵称已经被使用了')
        return nickname

    def clean(self):
        """ 验证码 hook 钩子函数 """
        data = super().clean()
        if self.errors:
            return
        phone_num = self.cleaned_data.get('username', None)
        sms_code = self.cleaned_data.get('sms_code', None)

        # redis中的验证码key
        key = '{}{}'.format(constants.REGISTER_MSM_CODE_KEY, phone_num)

        code = cache.get(key)
        # code已失效
        if code is None:
            raise forms.ValidationError('验证码已失效')

        if str(code) != sms_code:
            raise forms.ValidationError('验证码输入不正确')

        return data

    @transaction.atomic()
    def do_register(self, request):
        """ 执行注册 """
        data = self.cleaned_data
        version = request.headers.get('version', '')
        source = request.headers.get('source', '')
        try:
            # 1. 创建基础信息表
            user = User.objects.create_user(
                username=data.get('username', None),
                password=data.get('password', None),
                nickname=data.get('nickname', None),
            )
            # 2. 创建详细信息表
            profile = Profile.objects.create(
                user=user,
                username=user.username,
                version=version,
                source=source
            )
            # 3. 执行登录
            login(request, user)
            # 4. 记录登录日志
            user.last_login = now()
            user.save()
            ip = request.META.get('REMOTE_ADDR', '')
            user.add_login_record(username=user.username, ip=ip,
                                  version=version,
                                  source=source)
            return user, profile
        except Exception as e:
            print(e)
            return None



