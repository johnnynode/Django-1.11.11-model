# 此文件是自己添加的，并非模板自带

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"), # 首页
    url(r'^users$', views.getUsers, name="users"), # 浏览信息
    url(r'^user/add$', views.addUser, name="adduser"), # 加载添加表单
    url(r'^user/insert$', views.insertUser, name="insertuser"), # 用户信息添加
    url(r'^user/del/(?P<uid>[0-9]+)$', views.delUser, name="deluser"), # 删除信息
    url(r'^user/edit/(?P<uid>[0-9]+)$', views.editUser, name="edituser"), # 用户信息修改
    url(r'^user/update$', views.updateUser, name="updateuser"), # 执行用户信息修改
]
