from django.shortcuts import render
from django.contrib.auth import authenticate, login
# Create your views here.
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from .models import UserProfile, EmailVerfyRecord
from .forms import LoginForm, RegisterForm, ForgetPwdForm, ModifyPwdForm
from django.contrib.auth.hashers import make_password
from apps.utils.email_send import send_register_email


class CustomBackend(ModelBackend):
    """重写authenticate，默认为用户名方式登录，增加通过email方式登录"""
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class RegisterView(View):
    """当为前端为get的时候执行"""
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html", {'register_form': register_form})

    def post(self, request):
        """保存注册信息"""
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('email', '')
            if UserProfile.objects.filter(email=user_name):
                return render(request, "register.html", {'register_form': register_form, "msg": "用户已经存在"})
            pass_word = request.POST.get('password', '')
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.is_active = False
            user_profile.password = make_password(pass_word)
            user_profile.save()
            send_register_email(user_name, 'Register')
            return render(request, "login.html")
        else:
            return render(request, "register.html", {'register_form': register_form})


class LoginView(View):
    """登录视图类,系统自动判断前端的方法"""
    def get(self, request):
        """当为前端为get的时候执行"""
        login_form = LoginForm()
        return render(request, "login.html", {"login_form": login_form})

    def post(self, request):
        """当为前端为post的时候执行"""
        login_form = LoginForm(request.POST)
        if login_form.is_valid():  # 表单验证前端输入数据
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:  # 检查用户是否激活
                    login(request, user)
                    return render(request, "index.html")
                else:
                    return render(request, "login.html",
                                  {"msg": "用户未激活！", "login_form": login_form})
            else:
                return render(request, "login.html",
                              {"msg": "用户名或密码错误！", "login_form": login_form})
        else:
            return render(request, "login.html",
                          {"login_form": login_form})


class AciveUserView(View):
    """邮箱激活"""
    def get(self, request, active_code):
        active_codes = EmailVerfyRecord.objects.filter(code=active_code)
        if active_codes:
            for code in active_codes:
                email = code.email
                user = UserProfile.objects.get(email=email)
                # if user.is_active:
                #     return render(request, "index.html")
                user.is_active = True
                user.save()
        else:
            return render(request, "active_fail.html")
        return render(request, "index.html")


class ForgetPwdView(View):
    """找回密码"""
    def get(self, request):
        forget_form = ForgetPwdForm()
        return render(request, "forgetpwd.html", {'forget_form': forget_form})

    def post(self, request):
        forget_form = ForgetPwdForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get('email', "")
            try:
                user_emails = UserProfile.objects.filter(email=email)
            except Exception as e:
                print(e.__str__())
                if user_emails:
                   send_register_email(email, 'Forget')
                   return render(request, "send_sucess.html")

        else:
            return render(request, "forgetpwd.html", {'forget_form': forget_form})


class ResetView(View):
    """重置密码"""
    def get(self, request, active_code):
        active_codes = EmailVerfyRecord.objects.filter(code=active_code)
        if active_codes:
            for code in active_codes:
                email = code.email
                return render(request, "password_reset.html", {'email': email})
        return render(request, "index.html")


class ModifyPwdView(View):
    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get('password1', "")
            pwd2 = request.POST.get('password2', "")
            email = request.POST.get('email', "")
            if pwd1 != pwd2:
                return render(request, "password_reset.html", {'email': email, "msg": "密码不一致！"})
            user = UserProfile.objects.get(email=email)
            user.password = make_password(pwd2)
            user.save()
            return render(request, "login.html")
        else:
            email = request.POST.get('email', "")
            return render(request, "password_reset.html", {'email': email, "modify_form": modify_form})


def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username', '')
        pass_word = request.POST.get('password', '')
        user = authenticate(username=user_name, password=pass_word)
        if user is not None:
            login(request, user)
            return render(request, "index.html")
        else:
            return render(request, "login.html", {"msg": "用户名或密码错误！"})
    elif request.method == 'GET':
        return render(request, "login.html", {})
