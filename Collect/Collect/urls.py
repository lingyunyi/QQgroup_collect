"""Collect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import admins_views
from . import users_views
from . import users_2_views
urlpatterns = [
    # path('admins/', admins.site.urls),
    # path(r"index/",index),
    # path(r"qqscan/", qqscan),
    # path(r"scan_status/",scan_status),
    # path(r"show/", show),
    # path(r"temp/",read_img),
    # path(r"download/",read_file)

# --------------------------------用户系统--------------------------------
    # 用户登入界面
    path(r"users/login/",users_views.login),
    # 用户个人中心页面
    path(r"users/center/",users_views.users_center),
    # 活动展示页面
    path(r"users/join_activity/",users_views.join_activity),
    path(r"users/activity_details/",users_views.activity_details),
    # 启动扫描页面
    path(r"users/qqscan/",users_views.qqscan),
    # 查看图片页面
    path(r"users/readimg/",users_views.read_img),
    path(r"users/download/",users_views.download),
    # 用户控制台
    path(r"users/control/",users_views.users_control),
    # 网盘管理
    path(r"users/users_network_dick/",users_views.users_network_dick),

# --------------------------------用户系统2--------------------------------
    # 我的团队
    path(r"users/users_my_team/",users_2_views.users_my_team),
    # 公示
    path(r"users/users_announce/",users_2_views.users_announce),
    # 注册
    path(r"users/users_register/",users_2_views.users_register),
    # 注册
    path(r"users/users_register_API/",users_2_views.users_register_API),






# --------------------------------超管系统---------------------------------
    # 登入界面,登出界面
    path(r"admins/login/",admins_views.login),
    path(r"admins/logout/",admins_views.logout),
    # 下载文件页面
    path(r"admins/download/",admins_views.download),
    # users_manager 用户管理界面
    path(r"admins/users_manager/",admins_views.users_manager),
    # users_disk_manager 用户网盘管理
    path(r"admins/users_disk_manager/",admins_views.users_disk_manager),
    # activity_manager 活动与公告管理界面
    path(r"admins/activity_manager/", admins_views.activity_manager),
]