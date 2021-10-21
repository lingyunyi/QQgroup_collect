from .tools import seleniums,manager_sql
from django.http import request
from django.shortcuts import redirect,render,HttpResponse,Http404
import threading,requests
import uuid,time,os
from .settings import *
import logging,hashlib

'''
    print(BASE_DIR) 打开什么文件的时候千万别忘记+from .settings import *的BASE_DIR

'''

manager_sqlx = manager_sql.SqlManger()

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s  - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def download(request):
    '''
        获取指定下载文件
    :param request:
    :return:
    '''
    '''
        得从请求中获取到文件路径
    '''
    # 获取远程访问IP
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    # 输出日志
    logger.warning("%s - function download" % (ip))
    try:
        # -----------------执行验证------------------
        # -----------------执行验证------------------
        try:
            uuid4_str = request.COOKIES.get("username_id")
            user_name = str(request.session.get(uuid4_str))
            logger.warning("function download - %s - user_name = %s" % (ip, user_name))
        except BaseException as e:
            logger.exception("function download - %s - requestx.COOKIES.get is false - %s" % (ip, e),exc_info=True)
            return redirect("/users/login/")
        # -----------------执行验证------------------
        # -----------------执行验证------------------
        filename = request.GET["file"]
        # 在执行一次是否输入用户文件的认证
        try:
            sql = '''select * from users_network_dick where qqclass_number = %s'''
            search_users_network_dick_result = manager_sqlx.search(sql,[filename])
            user_from_name = search_users_network_dick_result[0][3]
            if str(user_from_name) != str(user_name):
                logger.warning("function download - %s - str(%s) != str(%s)" % (ip, user_from_name,user_name))
                return redirect("/users/users_network_dick/")
        except BaseException as e :
            logging.exception('function download  - %s - requests method post - except' % (e), exc_info=True)
            return redirect("/users/users_network_dick/")
        file = open(r'%s\%s.cvs'%(qqclass_Path,filename), 'rb')
        response = HttpResponse(file)
        file.close()
        response['Content-Type'] = 'application/octet-stream'  # 设置头信息，告诉浏览器这是个文件
        response['Content-Disposition'] = 'attachment;filename="qqqun-%s.csv"'%(filename)
        return response
    except BaseException as e:
        logging.exception('function download  - %s - requests method post - except' % (e), exc_info=True)
        return redirect("/users/users_network_dick/")


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

def login(request):
    '''
        用户登入页面
    :param request:
    :return:
    '''
    # 获取远程访问IP
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    # 输出日志
    logger.warning("%s - function login"%(ip))
    if request.method == "GET":
        logger.warning("function login - %s - requests method get" %(ip))
        # 首先判断是否已经登入
        return render(request, "users/users_login.html", {})

    elif request.method == "POST":
        logger.warning("function login - %s - requests method post" % (ip))
        # 在这里进行账号认证
        logger.warning("function login - %s - begin ajax post data" % (ip))
        try:
            users_account = request.POST.get("users_account")
            users_passwd = request.POST.get("users_passwd")
            if users_account != None and users_passwd != None:
                logger.warning("function login - %s - post account not is null - %s - %s" % (ip,users_account,users_passwd))
                # 如果账号不为空
                sql = '''select * from users_Account where users_account = %s'''
                search_result_account = manager_sqlx.search(sql,[users_account])
                logger.warning("function login - %s - login begin - %s - %s" % (ip, users_account, users_passwd))
                if search_result_account != ():
                    # 能进来这里就代表，使用表单数据查询数据库有数据，所以不等于空
                    logger.warning("function login - %s - login begin - search_result_account != ()"%(ip))
                    if search_result_account[0][1] == users_account and search_result_account[0][2] == hashlib.md5(users_passwd.encode(encoding='UTF-8')).hexdigest():
                        # 303 账号或秘密错误,404密码不存在
                        logger.warning("function login - %s - login success - %s - %s" % (ip, users_account, users_passwd))
                        # 首先判断有没有进行初始化，就是有没有进行session数据初始化
                        sql = '''select * from users_Session where users_account = %s'''
                        search_result_session = manager_sqlx.search(sql, [users_account])
                        # 未进行初始化，进行初始化
                        # 初始化用户
                        initDB = {
                            # 存活时间以秒为单位，超过这个时间则死亡需要重新登入
                            "alive_time_s": int(time.time()) + (60 * 60 * 24),
                            # 获取的img路径 wait success有值状态
                            "img_path": "wait",
                            # 扫描状态 wait等待中 success成功 false失败 final完成 scan扫描中防止多次扫描
                            "scan_status": "wait",
                            "scan_numbers":"0-0"
                        }
                        if search_result_session == ():
                            # 如果等于空就代表没有进行初始化，就代表没有进行session初始化
                            logger.warning("function login - %s - login success init start - %s - %s" % (ip, users_account, users_passwd))
                            sql = '''insert into users_Session (users_account,users_session) values (%s,%s)'''
                            insert_result_session = manager_sqlx.excute(sql, [users_account,"%s"%(initDB)])
                            # 如果执行成功，就代表数据更新成功
                            if insert_result_session == True:
                                # 进行首页跳转，200，数据执行成功
                                logger.warning("function login - %s - insert_result_session susscess - %s - %s" % (ip, users_account, users_passwd))
                                uuid4_str = str(uuid.uuid4())
                                request.session[uuid4_str] = users_account
                                obj = HttpResponse("200")
                                obj.set_cookie("username_id", uuid4_str, 60*60*24)
                                logger.warning("function login - %s - updata_result_session susscess - %s - %s" % (ip, uuid4_str, users_account))
                                return obj
                            if insert_result_session == False:
                                logger.warning("function login - %s - insert_result_session false - %s - %s" % (ip, users_account, users_passwd))
                                # 如果失败，返回重试，505请重试
                                return HttpResponse("505")
                        elif search_result_session != ():
                            # 如果查询用户session数据库不等于空就代表，已经有数据，这时候进行数据刷新就可以了。
                            having_search_result_session = eval(search_result_session[0][2])
                            if int(having_search_result_session.get("alive_time_s")) > int(time.time()):
                                uuid4_str = str(uuid.uuid4())
                                request.session[uuid4_str] = users_account
                                logger.warning("function login - %s - (alive_time_s)) > int(time.time()) - %s - %s" % (ip, users_account, users_passwd))
                                obj = HttpResponse("200")
                                obj.set_cookie("username_id", uuid4_str, 60 * 60 * 24)
                                return obj
                            elif int(having_search_result_session.get("alive_time_s")) <= int(time.time()):
                                logger.warning("function login - %s - (alive_time_s)) <= int(time.time()) - %s - %s" % (ip, users_account, users_passwd))
                                sql = '''UPDATE users_Session SET users_session = %s WHERE users_account = %s'''
                                # 进行数据更新
                                having_search_result_session["alive_time_s"] = "%s"%(int(time.time()) + (60 * 60 * 24))
                                having_search_result_session["scan_status"] = "wait"
                                updata_result_session = manager_sqlx.excute(sql,["%s"%(having_search_result_session),users_account])
                                if updata_result_session == True:
                                    # 进行首页跳转，200数据执行成功
                                    logger.warning("function login - %s - updata_result_session susscess - %s - %s" % (ip,users_account,users_passwd))
                                    uuid4_str = str(uuid.uuid4())
                                    request.session[uuid4_str] = users_account
                                    obj = HttpResponse("200")
                                    obj.set_cookie("username_id", uuid4_str, 60 * 60 * 24)
                                    logger.warning("function login - %s - updata_result_session susscess - %s - %s" % (ip, uuid4_str, users_account))
                                    return obj
                                if updata_result_session == False:
                                    logger.warning("function login - %s - updata_result_session false - %s - %s" % (ip,users_account,users_passwd))
                                    # 如果失败，返回重试，505请重试
                                    return HttpResponse("505")
                    else:
                        # 来到这里代表账号密码不匹配
                        logger.warning("function login - %s - login false - %s - %s" % (ip,users_account,users_passwd))
                        # 303 账号或秘密错误,404密码不存在
                        return HttpResponse("303")
                elif search_result_account == ():
                    # 账号不存在
                    logger.warning("function login - %s - login account is null - %s - %s" % (ip,users_account,users_passwd))
                    # 303 账号或秘密错误,404密码不存在
                    return HttpResponse("303")
            elif users_account == None or users_passwd == None:
                # 303 账号或秘密错误,404账号和密码不存在
                # 如果到这里就代表，前端传入的界面的值，为空。
                logger.warning("function login - %s - post account is null - %s - %s" % (ip,users_account,users_passwd))
                return HttpResponse("404")
        except BaseException as e:
            logging.exception('function login - %s - requests method post - except'%(e), exc_info=True)
            return HttpResponse("505")
    # 结尾,505请重试
    return HttpResponse("505")




def users_center(request):
    '''
        users_center
    :param request:
    :return:
    '''
    # 获取远程访问IP
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    # 输出日志
    logger.warning("%s - function users_center" % (ip))
    if request.method == "GET":
        logger.warning("function users_center - %s - requests method get" % (ip))
        # 首先判断是否已经登入
        # -------------------
        try:
            uuid4_str = request.COOKIES.get("username_id")
            user_name = str(request.session.get(uuid4_str))
            logger.warning("function users_center - %s - user_name = %s" % (ip,user_name))
            # 执行数据库查询内容
            sql = '''select * from users_Account where users_account = %s'''
            search_users_account_result = manager_sqlx.search(sql,[user_name])
            if search_users_account_result != ():
                logger.warning("function users_center - %s - users_account is true" % (ip))
                logger.warning("function users_center - %s - search_users_account_result = %s" % (ip, search_users_account_result))
                # 获取他的数据库session，判断存活时间是否大于现在时间，如果小于这退出。
                sql = '''select * from users_Session where users_account = %s'''
                search_users_session_result = manager_sqlx.search(sql, [user_name])
                if search_users_session_result != ():
                    logger.warning("function users_center - %s - users_Session is true" % (ip))
                    logger.warning("function users_center - %s - search_users_Session_result = %s" % (ip, search_users_session_result))
                    # 返回正常页面
                    if int(eval(search_users_session_result[0][2]).get("alive_time_s")) <= int(time.time()):
                        #代表管理员账户已过期
                        logger.warning("function users_center - %s - search_users_Session_result[0][3]['alive_time_s'] is false" % (ip))
                        return redirect("/users/login/")
                    elif int(eval(search_users_session_result[0][2]).get("alive_time_s")) > int(time.time()):
                        logger.warning("function users_center - %s - search_users_Session_result[0][3]['alive_time_s'] is true" % (ip))
                        # ----------------------Get请求可以返回内容的开始---------------------------
                        # ----------------------Get请求可以返回内容的开始---------------------------
                        return render(request,"users/users_center.html",{"user_name":user_name})
                        # ----------------------Get请求可以返回内容的开始---------------------------
                        # ----------------------Get请求可以返回内容的开始---------------------------
                elif search_users_session_result == ():
                    logger.warning("function users_center - %s - users_Session is false" % (ip))
                    return redirect("/users/login/")
            elif search_users_account_result == ():
                logger.warning("function users_center - %s - users_Account is false" % (ip))
                return redirect("/users/login/")
        except BaseException as e:
            logger.exception("function users_center - %s - requestx.COOKIES.get is false - %s" % (ip,e),exc_info=True)
            return redirect("/users/login/")
        # -------------------
    elif request.method == "POST":
        logger.warning("function users_center  - %s - requests method post" % (ip))
        # 在这里进行账号认证
        logger.warning("function users_center  - %s - begin ajax post data" % (ip))
        try:
            # ------------------------------
            # ------------------------------
            # 这里应该还需要认证一次是否已经登入
            try:
                uuid4_str = request.COOKIES.get("username_id")
                user_name = str(request.session.get(uuid4_str))
                logger.warning("function users_center - %s - user_name = %s" % (ip, user_name))
            except BaseException as e :
                logger.exception("function users_center - %s - requestx.COOKIES.get is false - %s" % (ip, e),exc_info=True)
                return HttpResponse("404")
            # ----------------------POST请求可以返回内容的开始---------------------------
            # ----------------------POST请求可以返回内容的开始---------------------------

            # ----------------------POST请求可以返回内容的开始---------------------------
            # ----------------------POST请求可以返回内容的开始---------------------------
        except BaseException as e :
            logging.exception('function users_center  - %s - requests method post - except'%(e), exc_info=True)
            return HttpResponse("404")


def join_activity(request):
    '''
        join_activity
    :param request:
    :return:
    '''
    # 获取远程访问IP
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    # 输出日志
    logger.warning("%s - function join_activity" % (ip))
    if request.method == "GET":
        logger.warning("function join_activity - %s - requests method get" % (ip))
        # 首先判断是否已经登入
        # -------------------
        try:
            uuid4_str = request.COOKIES.get("username_id")
            user_name = str(request.session.get(uuid4_str))
            logger.warning("function join_activity - %s - user_name = %s" % (ip,user_name))
            # 执行数据库查询内容
            sql = '''select * from users_Account where users_account = %s'''
            search_users_account_result = manager_sqlx.search(sql,[user_name])
            if search_users_account_result != ():
                logger.warning("function join_activity - %s - users_account is true" % (ip))
                logger.warning("function join_activity - %s - search_users_account_result = %s" % (ip, search_users_account_result))
                # 获取他的数据库session，判断存活时间是否大于现在时间，如果小于这退出。
                sql = '''select * from users_Session where users_account = %s'''
                search_users_session_result = manager_sqlx.search(sql, [user_name])
                if search_users_session_result != ():
                    logger.warning("function join_activity - %s - users_Session is true" % (ip))
                    logger.warning("function join_activity - %s - search_users_Session_result = %s" % (ip, search_users_session_result))
                    # 返回正常页面
                    if int(eval(search_users_session_result[0][2]).get("alive_time_s")) <= int(time.time()):
                        #代表管理员账户已过期
                        logger.warning("function join_activity - %s - search_users_Session_result[0][3]['alive_time_s'] is false" % (ip))
                        return redirect("/users/login/")
                    elif int(eval(search_users_session_result[0][2]).get("alive_time_s")) > int(time.time()):
                        logger.warning("function join_activity - %s - search_users_Session_result[0][3]['alive_time_s'] is true" % (ip))
                        # ----------------------Get请求可以返回内容的开始---------------------------
                        # ----------------------Get请求可以返回内容的开始---------------------------

                        sql = '''select id,notice_activity_name,notice_activity_type,notice_activity_create_time from alls_notice_activity_list order by id desc limit 8'''
                        search_alls_notice_activity_list_result = manager_sqlx.search(sql,[])
                        activity_list = []
                        for row in search_alls_notice_activity_list_result:
                            if row[2] == 1 or row[2] == "1":
                                activity_list.append(row)
                        return render(request,"users/join_activity.html",{"activity_list":activity_list})

                        # ----------------------Get请求可以返回内容的开始---------------------------
                        # ----------------------Get请求可以返回内容的开始---------------------------
                elif search_users_session_result == ():
                    logger.warning("function join_activity - %s - users_Session is false" % (ip))
                    return redirect("/users/login/")
            elif search_users_account_result == ():
                logger.warning("function join_activity - %s - users_Account is false" % (ip))
                return redirect("/users/login/")
        except BaseException as e:
            logger.exception("function join_activity - %s - requestx.COOKIES.get is false - %s" % (ip,e),exc_info=True)
            return redirect("/users/login/")
        # -------------------
    elif request.method == "POST":
        logger.warning("function join_activity  - %s - requests method post" % (ip))
        # 在这里进行账号认证
        logger.warning("function join_activity  - %s - begin ajax post data" % (ip))
        try:
            # ------------------------------
            # ------------------------------
            # 这里应该还需要认证一次是否已经登入
            try:
                uuid4_str = request.COOKIES.get("username_id")
                user_name = str(request.session.get(uuid4_str))
                logger.warning("function join_activity - %s - user_name = %s" % (ip, user_name))
            except BaseException as e :
                logger.exception("function join_activity - %s - requestx.COOKIES.get is false - %s" % (ip, e),exc_info=True)
                return HttpResponse("404")
            # ----------------------POST请求可以返回内容的开始---------------------------
            # ----------------------POST请求可以返回内容的开始---------------------------

            # ----------------------POST请求可以返回内容的开始---------------------------
            # ----------------------POST请求可以返回内容的开始---------------------------
        except BaseException as e :
            logging.exception('function join_activity  - %s - requests method post - except'%(e), exc_info=True)
            return HttpResponse("404")




def activity_details(request):
    '''
        activity_details
    :param request:
    :return:
    '''
    # 获取远程访问IP
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    # 输出日志
    logger.warning("%s - function activity_details" % (ip))
    if request.method == "GET":
        logger.warning("function activity_details - %s - requests method get" % (ip))
        # 首先判断是否已经登入
        # -------------------
        try:
            uuid4_str = request.COOKIES.get("username_id")
            user_name = str(request.session.get(uuid4_str))
            logger.warning("function activity_details - %s - user_name = %s" % (ip,user_name))
            # 执行数据库查询内容
            sql = '''select * from users_Account where users_account = %s'''
            search_users_account_result = manager_sqlx.search(sql,[user_name])
            if search_users_account_result != ():
                logger.warning("function activity_details - %s - users_account is true" % (ip))
                logger.warning("function activity_details - %s - search_users_account_result = %s" % (ip, search_users_account_result))
                # 获取他的数据库session，判断存活时间是否大于现在时间，如果小于这退出。
                sql = '''select * from users_Session where users_account = %s'''
                search_users_session_result = manager_sqlx.search(sql, [user_name])
                if search_users_session_result != ():
                    logger.warning("function activity_details - %s - users_Session is true" % (ip))
                    logger.warning("function activity_details - %s - search_users_Session_result = %s" % (ip, search_users_session_result))
                    # 返回正常页面
                    if int(eval(search_users_session_result[0][2]).get("alive_time_s")) <= int(time.time()):
                        #代表管理员账户已过期
                        logger.warning("function activity_details - %s - search_users_Session_result[0][3]['alive_time_s'] is false" % (ip))
                        return redirect("/users/login/")
                    elif int(eval(search_users_session_result[0][2]).get("alive_time_s")) > int(time.time()):
                        logger.warning("function activity_details - %s - search_users_Session_result[0][3]['alive_time_s'] is true" % (ip))
                        # ----------------------Get请求可以返回内容的开始---------------------------
                        # ----------------------Get请求可以返回内容的开始---------------------------

                        sql = '''select * from alls_notice_activity_list where id = %s'''
                        search_alls_notice_activity_list_result = manager_sqlx.search(sql,[request.GET.get("nid")])
                        return render(request,"users/activity_details.html",{"activity_list":search_alls_notice_activity_list_result[0]})

                        # ----------------------Get请求可以返回内容的开始---------------------------
                        # ----------------------Get请求可以返回内容的开始---------------------------
                elif search_users_session_result == ():
                    logger.warning("function activity_details - %s - users_Session is false" % (ip))
                    return redirect("/users/login/")
            elif search_users_account_result == ():
                logger.warning("function activity_details - %s - users_Account is false" % (ip))
                return redirect("/users/login/")
        except BaseException as e:
            logger.exception("function activity_details - %s - requestx.COOKIES.get is false - %s" % (ip,e),exc_info=True)
            return redirect("/users/login/")
        # -------------------
    elif request.method == "POST":
        logger.warning("function activity_details  - %s - requests method post" % (ip))
        # 在这里进行账号认证
        logger.warning("function activity_details  - %s - begin ajax post data" % (ip))
        try:
            # ------------------------------
            # ------------------------------
            # 这里应该还需要认证一次是否已经登入
            try:
                uuid4_str = request.COOKIES.get("username_id")
                user_name = str(request.session.get(uuid4_str))
                logger.warning("function activity_details - %s - user_name = %s" % (ip, user_name))
            except BaseException as e :
                logger.exception("function activity_details - %s - requestx.COOKIES.get is false - %s" % (ip, e),exc_info=True)
                return HttpResponse("404")
            # ----------------------POST请求可以返回内容的开始---------------------------
            # ----------------------POST请求可以返回内容的开始---------------------------

            # ----------------------POST请求可以返回内容的开始---------------------------
            # ----------------------POST请求可以返回内容的开始---------------------------
        except BaseException as e :
            logging.exception('function activity_details  - %s - requests method post - except'%(e), exc_info=True)
            return HttpResponse("404")


def qqscan(request):
    '''

    :param requets:
    :return:
    '''
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    if request.method == "GET":
        return HttpResponse("1234556978979")
    if request.method == "POST":
        logger.warning("function qqscan  - %s - requests method post" % (ip))
        # 在这里进行账号认证
        logger.warning("function qqscan  - %s - begin ajax post data" % (ip))
        try:
            # ------------------------------
            # ------------------------------
            # 这里应该还需要认证一次是否已经登入
            try:
                uuid4_str = request.COOKIES.get("username_id")
                user_name = str(request.session.get(uuid4_str))
                logger.warning("function qqscan - %s - user_name = %s" % (ip, user_name))
            except BaseException as e:
                logger.exception("function qqscan - %s - requestx.COOKIES.get is false - %s" % (ip, e),exc_info=True)
                return HttpResponse("404")
            # ----------------------POST请求可以返回内容的开始---------------------------
            # ----------------------POST请求可以返回内容的开始---------------------------
            '''
                业务逻辑
                首先判断是否具有参加活动权限，如果没有，则返回  no_have_power
                
                其次判断其扫描状态,如果是等待wait,则可以扫描，启用引擎返回二维码。倒计时十五秒。
                如果是成功success，则返回，scaning，扫描中，跳转到个人网盘。  200
                
                如果是false，,则可以扫描，启用引擎返回二维码。倒计时十五秒。
                
                404 重定向回到参加活动
                
                
                no_hava_power 提示：需要充值，200，跳转到个人网盘。404，跳转到参加活动。
            '''
            sql = '''select users_alives_time_s from users_account where users_account = %s'''
            search_users_alives_time_s_result = manager_sqlx.search(sql,[user_name])
            # 判断用户是否存在，如果用户不存在
            if search_users_alives_time_s_result == ():
                logger.warning("function qqscan - %s - search_users_alives_time_s_result == ()" % (ip))
                return HttpResponse("404")
            # 判断用户是否存在，如果用户存在
            elif search_users_alives_time_s_result != ():
                logger.warning("function qqscan - %s - search_users_alives_time_s_result != ()" % (ip))
                users_alives_time_s = search_users_alives_time_s_result[0][0]
                logger.warning("function qqscan - %s - %s" % (ip,search_users_alives_time_s_result[0][0]))
                # 判断用户时间余额是否足够，不足够
                if int(users_alives_time_s) <= int(time.time()):
                    # 代表用户没有多余时间了
                    logger.warning("function qqscan - %s - users_alives_time_s is false" % (ip))
                    return HttpResponse("no_have_power")
                # 判断用户时间余额是否足够，足够
                elif int(users_alives_time_s) > int(time.time()):
                    # 代表用户还有多余时间，可以启用引擎
                    logger.warning("function qqscan - %s - users_alives_time_s is true" % (ip))
                    # 这里还得判断扫描状态。
                    # 这里还得判断扫描状态。
                    # 查询用户字典，如果有值
                    sql = '''select * from users_Session where users_account = %s'''
                    search_users_session_result = manager_sqlx.search(sql, [user_name])
                    if search_users_session_result != ():
                        logger.warning("function qqscan - %s - users_Session is true" % (ip))
                        logger.warning("function qqscan - %s - search_users_Session_result = %s" % (ip, search_users_session_result))
                    # -------------------------------------------------------------------------------------------------------
                    # 这里还得判断扫描状态。
                        user_session = eval(search_users_session_result[0][2])
                        if user_session.get("scan_status") == "wait" or user_session.get("scan_status") == "false":
                            # 更新数据库
                            updataDB = {
                                # 存活时间以秒为单位，超过这个时间则死亡需要重新登入
                                "alive_time_s": int(time.time()) + (60 * 60 * 3),
                                # 获取的img路径 wait success有值状态
                                "img_path": "wait",
                                # 扫描状态 wait等待中 success成功 false失败 final完成 scan扫描中防止多次扫描
                                "scan_status": "wait",
                                "scan_numbers":"0-0"
                            }
                            sql = '''UPDATE users_Session SET users_session = %s WHERE users_account = %s'''
                            # 进行数据更新
                            updata_result_session = manager_sqlx.excute(sql, ["%s" % (updataDB), user_name])
                            logger.warning("function qqscan - %s - user_session.get(scan_status) == wait or user_session.get(scan_status) == false" % (ip))
                            # 启动引擎，直到img有值
                            selenium = seleniums.Seleniums(user_name=user_name)
                            t = threading.Thread(target=selenium.main)
                            # 启动引擎
                            t.start()
                            # 死守数据，再取一次数据
                            sql = '''select * from users_Session where users_account = %s'''
                            search_users_session_result = manager_sqlx.search(sql, [user_name])
                            user_session = eval(search_users_session_result[0][2])
                            while user_session.get("scan_status") != "false" and user_session.get("img_path") == "wait":
                                # 再次获取数据
                                sql = '''select * from users_Session where users_account = %s'''
                                search_users_session_result = manager_sqlx.search(sql, [user_name],show=False)
                                user_session = eval(search_users_session_result[0][2])
                                if user_session.get("scan_status") == "false":
                                    # 返回重新登入界面，这里代表已经失败了。不可能获取到img-path了
                                    logger.warning("function qqscan - %s - %s - %s ---------404-------------" % (ip,user_session.get("scan_status"),user_session.get("img_path")))
                                    return HttpResponse("404")
                                    break
                                if user_session.get("img_path") != "wait":
                                    logger.warning("function qqscan - %s - %s - %s ----------img------------" % (ip,user_session.get("scan_status"),user_session.get("img_path")))
                                    return HttpResponse(user_session.get("img_path"))
                                    break
                                time.sleep(0.5)
                        elif "finaly" in user_session.get("scan_status") or user_session.get("scan_status") == "success":
                            logger.warning("function qqscan - %s - success ! finaly ! - %s" % (ip, user_session.get("scan_status")))
                            return HttpResponse("200")
                    # -------------------------------------------------------------------------------------------------------
                    # 查询用户字典，如果不存在，则重定向，重新登入
                    elif search_users_session_result == ():
                        logger.warning("function qqscan - %s - users_Session is false" % (ip))
                        return HttpResponse("404")
            # ----------------------POST请求可以返回内容的开始---------------------------
            # ----------------------POST请求可以返回内容的开始---------------------------
        except BaseException as e:
            logging.exception('function qqscan  - %s - requests method post - except' % (e), exc_info=True)
            return HttpResponse("404")


def users_control(request):
    '''
        users_control
    :param request:
    :return:
    '''
    # 获取远程访问IP
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    # 输出日志
    logger.warning("%s - function users_control" % (ip))
    if request.method == "GET":
        logger.warning("function users_control - %s - requests method get" % (ip))
        # 首先判断是否已经登入
        # -------------------
        try:
            uuid4_str = request.COOKIES.get("username_id")
            user_name = str(request.session.get(uuid4_str))
            logger.warning("function users_control - %s - user_name = %s" % (ip,user_name))
            # 执行数据库查询内容
            sql = '''select * from users_Account where users_account = %s'''
            search_users_account_result = manager_sqlx.search(sql,[user_name])
            if search_users_account_result != ():
                logger.warning("function users_control - %s - users_account is true" % (ip))
                logger.warning("function users_control - %s - search_users_account_result = %s" % (ip, search_users_account_result))
                # 获取他的数据库session，判断存活时间是否大于现在时间，如果小于这退出。
                sql = '''select * from users_Session where users_account = %s'''
                search_users_session_result = manager_sqlx.search(sql, [user_name])
                if search_users_session_result != ():
                    logger.warning("function users_control - %s - users_Session is true" % (ip))
                    logger.warning("function users_control - %s - search_users_Session_result = %s" % (ip, search_users_session_result))
                    # 返回正常页面
                    if int(eval(search_users_session_result[0][2]).get("alive_time_s")) <= int(time.time()):
                        #代表管理员账户已过期
                        logger.warning("function users_control - %s - search_users_Session_result[0][3]['alive_time_s'] is false" % (ip))
                        return redirect("/users/login/")
                    elif int(eval(search_users_session_result[0][2]).get("alive_time_s")) > int(time.time()):
                        logger.warning("function users_control - %s - search_users_Session_result[0][3]['alive_time_s'] is true" % (ip))
                        # ----------------------Get请求可以返回内容的开始---------------------------
                        # ----------------------Get请求可以返回内容的开始---------------------------

                        sql = '''select id,notice_activity_name,notice_activity_content,notice_activity_type,notice_activity_create_time from alls_notice_activity_list where is_delete = 0 order by id desc limit 5'''
                        search_alls_notice_activity_list_result = manager_sqlx.search(sql, [])
                        activity_list = []
                        logger.warning(search_alls_notice_activity_list_result)
                        for row in search_alls_notice_activity_list_result:
                            if row[3] == 0 or row[3] == "0":
                                activity_list.append(row)
                        logger.warning(activity_list)
                        return render(request,"users/users_control.html",{"activity_list":activity_list})
                        # ----------------------Get请求可以返回内容的开始---------------------------
                        # ----------------------Get请求可以返回内容的开始---------------------------
                elif search_users_session_result == ():
                    logger.warning("function users_control - %s - users_Session is false" % (ip))
                    return redirect("/users/login/")
            elif search_users_account_result == ():
                logger.warning("function users_control - %s - users_Account is false" % (ip))
                return redirect("/users/login/")
        except BaseException as e:
            logger.exception("function users_control - %s - requestx.COOKIES.get is false - %s" % (ip,e),exc_info=True)
            return redirect("/users/login/")
        # -------------------
    elif request.method == "POST":
        logger.warning("function users_control  - %s - requests method post" % (ip))
        # 在这里进行账号认证
        logger.warning("function users_control  - %s - begin ajax post data" % (ip))
        try:
            # ------------------------------
            # ------------------------------
            # 这里应该还需要认证一次是否已经登入
            try:
                uuid4_str = request.COOKIES.get("username_id")
                user_name = str(request.session.get(uuid4_str))
                logger.warning("function users_control - %s - user_name = %s" % (ip, user_name))
            except BaseException as e :
                logger.exception("function users_control - %s - requestx.COOKIES.get is false - %s" % (ip, e),exc_info=True)
                return HttpResponse("404")
            # ----------------------POST请求可以返回内容的开始---------------------------
            # ----------------------POST请求可以返回内容的开始---------------------------

            # ----------------------POST请求可以返回内容的开始---------------------------
            # ----------------------POST请求可以返回内容的开始---------------------------
        except BaseException as e :
            logging.exception('function users_control  - %s - requests method post - except'%(e), exc_info=True)
            return HttpResponse("404")




def users_network_dick(request):
    '''
        users_network_dick
    :param request:
    :return:
    '''
    # 获取远程访问IP
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    # 输出日志
    logger.warning("%s - function users_control" % (ip))
    if request.method == "GET":
        logger.warning("function users_network_dick - %s - requests method get" % (ip))
        # 首先判断是否已经登入
        # -------------------
        try:
            uuid4_str = request.COOKIES.get("username_id")
            user_name = str(request.session.get(uuid4_str))
            logger.warning("function users_network_dick - %s - user_name = %s" % (ip,user_name))
            # 执行数据库查询内容
            sql = '''select * from users_Account where users_account = %s'''
            search_users_account_result = manager_sqlx.search(sql,[user_name])
            if search_users_account_result != ():
                logger.warning("function users_network_dick - %s - users_account is true" % (ip))
                logger.warning("function users_network_dick - %s - search_users_account_result = %s" % (ip, search_users_account_result))
                # 获取他的数据库session，判断存活时间是否大于现在时间，如果小于这退出。
                sql = '''select * from users_Session where users_account = %s'''
                search_users_session_result = manager_sqlx.search(sql, [user_name])
                if search_users_session_result != ():
                    logger.warning("function users_network_dick - %s - users_Session is true" % (ip))
                    logger.warning("function users_network_dick - %s - search_users_Session_result = %s" % (ip, search_users_session_result))
                    # 返回正常页面
                    if int(eval(search_users_session_result[0][2]).get("alive_time_s")) <= int(time.time()):
                        #代表管理员账户已过期
                        logger.warning("function users_network_dick - %s - search_users_Session_result[0][3]['alive_time_s'] is false" % (ip))
                        return redirect("/users/login/")
                    elif int(eval(search_users_session_result[0][2]).get("alive_time_s")) > int(time.time()):
                        logger.warning("function users_network_dick - %s - search_users_Session_result[0][3]['alive_time_s'] is true" % (ip))
                        # ----------------------Get请求可以返回内容的开始---------------------------
                        # ----------------------Get请求可以返回内容的开始---------------------------
                        success_half = eval(search_users_session_result[0][2]).get("scan_numbers")
                        scan_status = eval(search_users_session_result[0][2]).get("scan_status")
                        sql = '''select * from users_network_dick where qqclass_from_users_account = %s'''
                        like_uses_network_list = []
                        all_uses_network_list = []
                        search_uses_network_dick_result = manager_sqlx.search(sql, [user_name])
                        for row in search_uses_network_dick_result:
                            all_uses_network_list.append(row)
                            if row[4] == 1:
                                like_uses_network_list.append(row)
                        # ------------------------------------------------------------------------------------------

                        sql = '''select * from users_account where users_account = %s'''
                        search_users_account_result =manager_sqlx.search(sql,[user_name])
                        users_data_list = []
                        logger.warning("function users_network_dick - %s - search_users_account_result is true" % (ip))
                        for row in search_users_account_result:
                            id = row[0]
                            user_account = row[1]
                            user_alive_time_s = row[3]
                            # 如果存活时间小于现实时间
                            if int(user_alive_time_s) <= int(time.time()):
                                user_alive_time_h = 0
                            # 如果存活时间大于现实时间
                            elif int(user_alive_time_s) > int(time.time()):
                                user_alive_time_h = (int(user_alive_time_s) - int(time.time()))//3600

                        # ------------------------------------------------------------------------------------------
                        return render(request,"users/users_network_dick.html",{
                            "all_uses_network_list":all_uses_network_list,
                            "like_uses_network_list":like_uses_network_list,
                            "success_half":success_half,
                            "scan_status":scan_status,
                            "user_name":user_name,
                            "user_alive_time_h":user_alive_time_h,
                        })
                        # ----------------------Get请求可以返回内容的开始---------------------------
                        # ----------------------Get请求可以返回内容的开始---------------------------
                elif search_users_session_result == ():
                    logger.warning("function users_network_dick - %s - users_Session is false" % (ip))
                    return redirect("/users/login/")
            elif search_users_account_result == ():
                logger.warning("function users_network_dick - %s - users_Account is false" % (ip))
                return redirect("/users/login/")
        except BaseException as e:
            logger.exception("function users_network_dick - %s - requestx.COOKIES.get is false - %s" % (ip,e),exc_info=True)
            return redirect("/users/login/")
        # -------------------
    elif request.method == "POST":
        logger.warning("function users_network_dick  - %s - requests method post" % (ip))
        # 在这里进行账号认证
        logger.warning("function users_network_dick  - %s - begin ajax post data" % (ip))
        try:
            # ------------------------------
            # ------------------------------
            # 这里应该还需要认证一次是否已经登入
            try:
                uuid4_str = request.COOKIES.get("username_id")
                user_name = str(request.session.get(uuid4_str))
                logger.warning("function users_network_dick - %s - user_name = %s" % (ip, user_name))
            except BaseException as e :
                logger.exception("function users_network_dick - %s - requestx.COOKIES.get is false - %s" % (ip, e),exc_info=True)
                return HttpResponse("404")
            # ----------------------POST请求可以返回内容的开始---------------------------
            # ----------------------POST请求可以返回内容的开始---------------------------
            dick_id = request.POST.get("dick_id")
            action = request.POST.get("action")
            logger.warning("function users_network_dick - %s - %s - %s" % (ip, dick_id,action))
            if action == "add":
                sql = '''UPDATE users_network_dick SET users_is_like = %s WHERE id = %s'''
                updata_users_network_dick_result = manager_sqlx.excute(sql,[1,dick_id])
                if updata_users_network_dick_result == True:
                    return HttpResponse("200")
                else:
                    return HttpResponse("404")
            elif action == "pop":
                sql = '''UPDATE users_network_dick SET users_is_like = %s WHERE id = %s'''
                updata_users_network_dick_result = manager_sqlx.excute(sql, [0, dick_id])
                if updata_users_network_dick_result == True:
                    return HttpResponse("200")
                else:
                    return HttpResponse("404")
            # ----------------------POST请求可以返回内容的开始---------------------------
            # ----------------------POST请求可以返回内容的开始---------------------------
        except BaseException as e :
            logging.exception('function users_network_dick  - %s - requests method post - except'%(e), exc_info=True)
            return HttpResponse("404")
