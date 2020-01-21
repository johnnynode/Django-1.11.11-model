from django.shortcuts import render
from django.http import HttpResponse
from app.models import Users

# 首页
def index(request):
    # return HttpResponse('Hello')
    return render(request, "app/index.html")

# 用户信息列表
def getUsers(request):
    list = Users.objects.all()
    context = {"userList": list}
    return render(request, 'app/user/index.html', context)

# 用户信息列表
def addUser(request):
    return render(request, 'app/user/add.html')

# 新增用户信息
def insertUser(request):
    try:
        user = Users()
        user.name = request.POST['name']
        user.age = request.POST['age']
        user.phone = request.POST['phone']
        user.save()
        context = {"info":"添加成功!"}
    except:
        context = {"info":"添加失败!"}
    return render(request, "app/user/info.html", context)

# 删除用户信息
def delUser(request, uid):
    # return HttpResponse(uid)
    try:
        ob = Users.objects.get(id=uid)
        ob.delete()
        context = {"info":"删除成功!"}
    except:
        context = {"info":"删除失败!"}
    return render(request, "app/user/info.html", context)


# 编辑用户
def editUser(request, uid):
    try:
        ob = Users.objects.get(id=uid)
        context = {"u": ob}
        return render(request, "app/user/edit.html", context)
    except Exception as e:
        # print(e)
        context = {"info", "没有找到要修改的信息!"}
        return render(request, "app/user/info.html", context)

# 更新用户信息
def updateUser(request):
    try:
        user = Users.objects.get(id=request.POST['id'])
        user.name = request.POST['name']
        user.age = request.POST['age']
        user.phone = request.POST['phone']
        user.save()
        context = {"info":"修改成功!"}
    except:
        context = {"info":"修改失败!"}
    return render(request, "app/user/info.html", context)
