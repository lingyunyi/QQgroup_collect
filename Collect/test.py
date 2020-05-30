from .tools import seleniums,manager_sql
from django.http import request
from django.shortcuts import redirect,render,HttpResponse,Http404
import threading,requests
import uuid,time,os
from .settings import *
import logging

'''
    print(BASE_DIR) 打开什么文件的时候千万别忘记+from .settings import *的BASE_DIR

'''

manager_sqlx = manager_sql.SqlManger()

def read_img(request):
    print("\n-----------------------views-----------------------")
    print("\n-----------------------read_img-----------------------")
    """
    : 读取图片
    :param request:
    :return:
    """
    try:
        if  request.GET["img"] != "":
            data = request.GET
            # file_name = data.get("file_name")
            # imagepath = os.path.join(settings.BASE_DIR, "static/resume/images/{}".format(file_name))  # 图片路径
            file_name = request.GET["img"]
            path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            print(path,BASE_DIR)
            print(file_name)
            imagepath2 = "%s%s"%(BASE_DIR,file_name)
            print(imagepath2)
            with open(imagepath2, 'rb') as f:
                image_data = f.read()
            return HttpResponse(image_data, content_type="image/png")
    except Exception as e:
        print("\n-----def read_img----- except BaseException as e",e)
        return HttpResponse(str(e))
def read_file(request):
    print("\n-----------------------views-----------------------")
    print("\n-----------------------read_file-----------------------")
    '''
        获取指定下载文件
    :param request:
    :return:
    '''
    '''
        得从请求中获取到文件路径
    '''
    try:
        file_path = request.GET["file"]
        filex = str(file_path).split("\\")[-1]
        print(filex)
        file = open('%s'%(file_path), 'rb')
        response = HttpResponse(file)
        file.close()
        response['Content-Type'] = 'application/octet-stream'  # 设置头信息，告诉浏览器这是个文件
        response['Content-Disposition'] = 'attachment;filename="qqqun-%s"'%(filex)
        return response
    except BaseException as e:
        print("-----def read_file----- except BaseException as e")
        raise Http404("Question does not exist")
def updata_dict(dict,user_name):
    '''
        更新一下数据
    :return:
    '''
    print("\n-----------------------views-----------------------")
    print("\n-----------------------read_file-----------------------")
    try:
        ''''''
        ''''''
        sql = '''UPDATE user_session SET session_data = "%s" where user_name = "%s"    ''' % (
            dict, user_name)
        true_or_false = manager_sqlx.insert(sql)
        print("\n-----def updata_dict----- try",true_or_false)
        ''''''
        ''''''
        return true_or_false
    except BaseException as e:
        print("\n-----def updata_dict----- except BaseException as e",e)
        return False
def check(requestx):
    '''

    :return:
    '''
    print("\n-----------------------views-----------------------")
    print("\n-----------------------check-----------------------")
    try:
        uuid4_str = requestx.COOKIES.get("username_id")
        user_name = str(requestx.session.get(uuid4_str))
        '''
            其他页面判断就不需要创建文件了
        '''
        # # 判断是否有所属的文件夹目录，没有则创建
        # user_name_dir = "\Collect\QQclass\%s"%(user_name)
        # if os.path.exists(user_name_dir)  == False:
        #     os.makedirs(user_name_dir)
    except BaseException as e:
        print("\n-----def check-----except BaseException as e-----cookies get username_id false-----", e)
        '''如果未设置cookies就代表未登入，直接返回登入界面'''
        response = redirect("/index/")
        return response
        # 这里成功获取到用户名,数据格式为。得去数据库去。
        #  {"is_login": "true", "is_scan": "true", "img_path": "wait", "scan_status": "wait"}
    try:
        sql = '''   SELECT session_data FROM user_session where user_name = '{}'    '''.format(user_name)
        user_session = manager_sqlx.search(sql)
        print("\n-----def check-----try-----from mysql get user_session-----", user_session)
        if user_session[0][0] != "":
            print("\n-----def check-----try-----user_session have value-----",user_session[0][0])
            # 不等于空就代表有值，将字典获取
            get_user_session_dict = eval(user_session[0][0])
        elif user_session[0][0] == "":
            print("\n-----def check-----try-----user_session none value-----",user_session[0][0])
            # 等于空就代表，并未初始化，得跳转到登入界面
            response = redirect("/index/")
            return response
        print("\n-----def check-----try-----finaly-----")
    except BaseException as e:
        print("\n-----def check-----except BaseException as e-----from mysql get false-----",e)
        # 一样返回到登入界面
        response = redirect("/index/")
        return response
    content_tuple = [get_user_session_dict,user_name]
    return content_tuple
def qqscan(request):

    '''
        启动识别
    :param request:
    :return:
    '''
    print("\n-----------------------views-----------------------")
    print("\n-----------------------qqscan-----------------------")
    try:
        uuid4_str = request.COOKIES.get("username_id")
        user_name = str(request.session.get(uuid4_str))
        # 判断是否有所属的文件夹目录，没有则创建
        user_name_dir = r"\Collect\QQclass\%s\ "%(user_name)
        path = "%s%s" % (BASE_DIR, user_name_dir)
        try:
            if os.path.exists(path) == False:
                os.makedirs(path)
        except BaseException as e:
            print("\n-----def qqscan-----except BaseException as e-----crate dir false-----",e)
    except BaseException as e:
        print("\n-----def qqscan-----except BaseException as e-----from mysql get false-----",e)
        '''如果未设置cookies就代表未登入，直接返回登入界面'''
        return redirect("/index/")
    # 这里成功获取到用户名,数据格式为。得去数据库去。
    #  {"is_login": "true", "is_scan": "true", "img_path": "wait", "scan_status": "wait"}
    try:
        sql = '''   SELECT session_data FROM user_session where user_name = '{}'    '''.format(user_name)
        user_session = manager_sqlx.search(sql)
        print("\n-----def qqscan-----try-----from mysql get user_session-----", user_session)
        if user_session[0][0] != "":
            print("\n-----def qqscan-----try-----user_session have value-----",user_session[0][0])
            # 不等于空就代表有值，将字典获取
            get_user_session_dict = eval(user_session[0][0])
        elif user_session[0][0] == "":
            print("\n----def qqscan-----try-----user_session none value-----",user_session[0][0])
            # 等于空就代表，并未初始化，得跳转到登入界面
            return redirect("/index/")
        print("\n-----def qqscan-----try-----finaly-----")
    except BaseException as e :
        print("\n-----def qqscan-----except BaseException as e-----from mysql get false-----", e)

        # 一样返回到登入界面
        return redirect("/index/")

    # 如果到这里就代表已经获取到用户的字典信息，可以开始判断

    # {"is_login": "true", "is_scan": "true", "img_path": "wait", "scan_status": "wait"}
    '''
    来到进程登入判断状态
    '''
    if get_user_session_dict["is_login"] == "false":
        # 未登入跳转登入界面
        print("\n-----def qqscan-----get_user_session_dict-----[is_login] == false-----")
        return redirect("/index/")
    # 将个人字典传入

    # 初始化启动qq扫描文件
    selenium = seleniums.Seleniums(get_user_session_dict,user_name)
    scan_stauts = get_user_session_dict["scan_status"]
    print("\n-----def qqscan-----seleniums.Seleniums(get_user_session_dict,user_name)-----begin-----")


    # 如果扫描状态为   等待状态   或者  失败状态   可以进行再次扫描
    if scan_stauts == "wait" or scan_stauts == "false":
        print("\n-----def qqscan-----if or -----scan_stauts-----",scan_stauts == "wait" or scan_stauts == "false")
        t = threading.Thread(target=selenium.main)
        print("\n-----def qqscan-----target=selenium.main-----scan_stauts-----")
        get_user_session_dict["scan_status"] = "scan"
        # 子进程启动
        get_user_session_dict["img_path"] = "wait"
        true_or_false = updata_dict(get_user_session_dict, user_name)
        print("\n-----def qqscan-----updata_dict-----true_or_false-----")
        t.start()
        while True:
            '''
            # 是否登入 0未登入，1已登入
            "is_login": "true",
            # 是否扫描 0未扫描，1已扫描
            "is_scan": "true",
            # 获取的img路径 wait success有值状态
            "img_path": "wait",
            wait>value
            # 扫描状态 wait等待中 false失败 final完成 scan扫描中防止多次扫描
            wait>scan>success>flase>final
            未扫描>开始扫描>扫描中>扫描失败>扫描成功
            "scan_status": "wait",
        '''
            if get_user_session_dict["scan_status"] == "scan":
                if get_user_session_dict["img_path"] != "wait":
                    '''
                    更新一下数据
                    true_or_false
                    '''
                    true_or_false = updata_dict(get_user_session_dict,user_name)
                    if true_or_false == False:
                        return redirect("/index/")
                    '''
                    如果失败得重新登入
                    更新一下数据
                    true_or_false
                    '''
                    return render(request, "qqscan.html", {"img":get_user_session_dict["img_path"]})
            time.sleep(3)
    elif scan_stauts == "final" or scan_stauts == "scan" or "success" in scan_stauts:
        return redirect("/scan_status/")
def index(request):
    '''
        首次登入获取 session 未获取的全部都跳转到这来
    :param request:
    :return:
    '''
    print("\n-----------------------views-----------------------")
    print("\n-----------------------index-----------------------")
    # if request.method == "GET":
    #     pass
    # if request.method == "POST":
    #     pass


    # 这里首先得做是否有账号密码的判断
    user_name = "lingyunyi"
    sql = '''   SELECT session_data FROM user_session where user_name = '{}'    '''.format(user_name)
    user_session = manager_sqlx.search(sql)
    print("\n-----def index-----try-----from mysql get user_session-----", user_session)
    if user_session[0][0] == "":
        # 这里代表 user_session没有值
        print("\n-----def index-----user_session is none-----init begin-----", user_session[0][0])
        # 如果没有值，未初始化
        init_data = {
            # 存活时间以秒为单位，超过这个时间则死亡需要重新登入
            "alive_time_s": int(time.time()) + (60*60*3),
        }
        true_or_false = updata_dict(init_data, user_name)
        if true_or_false == False:
            # 如果失败得重新登入
            return redirect("/index/")
        # user_session 是执行数据库后获取的数据，session_data是数据库字段名
    if user_session[0][0] != "":
        print("\n-----def index-----user_session is value-----request.session[strx] = user_name-----", user_session[0][0])
        get_session_data = eval(user_session[0][0]).items()
        strx = str(uuid.uuid4())
        request.session[strx] = user_name
        obj = HttpResponse(get_session_data)
        obj.set_cookie("username_id",strx)
        return obj
def scan_status(request):
    '''
        中间状态页面
    :param request:
    :return:
    '''
    print("\n-----------------------views-----------------------")
    print("\n-----------------------scan_status-----------------------")
    response = check(request)
    if type(response).__name__!='list':
        return response
    else:
        get_user_session_dict = response[0]
        user_name = response[1]
    '''
        如果能来到这里就代表已经获得数据库字典，数据。
        {"is_login": "true", "is_scan": "true", "img_path": "wait", "scan_status": "wait"}
    '''
    return render(request,"scan_status.html",{"user_dict":get_user_session_dict})
def show(request):
    '''

    :param request:
    :return:
    '''
    print("\n-----------------------views-----------------------")
    print("\n-----------------------show-----------------------")
    response = check(request)
    if type(response).__name__!='list':
        return response
    else:
        get_user_session_dict = response[0]
        user_name = response[1]

    '''
        这里得获取当前用户下的所有文件
    '''
    try:
        user_name_dir = "\Collect\QQclass\%s\\" % (user_name)
        '''
            老哥别老忘记+R
            r 不转义
        '''
        path = r"%s%s" % (BASE_DIR, user_name_dir)
        '''
        获取用户名下的所有目录
        '''
        allfile_cvs = os.listdir(path)
        allfile_cvs_list = []
        for i in allfile_cvs:
            file_path = "%s%s"%(path,i)
            file_name = i.split(".")[0]
            allfile_cvs_list.append([file_name,file_path])
    except BaseException as e :
        print("\n----show----",e)
        return redirect("/scan_status/")
    return render(request,"show.html",{"allfile_cvs_list":allfile_cvs_list})


