from .tools import seleniums,manager_sql
from django.http import request
from django.shortcuts import redirect,render,HttpResponse,Http404
import threading,requests
import uuid,time,os
from .settings import *
import logging,hashlib,json

manager_sqlx = manager_sql.SqlManger()

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s  - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def logout(request):
    '''

    :param request:
    :return:
    '''
    # 获取远程访问IP
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    try:
        uuid4_str = request.COOKIES.get("adminsname_id")
        user_name = str(request.session.get(uuid4_str))
        logger.warning("function logout - %s - user_name = %s" % (ip, user_name))
        # 如果查询用户session数据库不等于空就代表，已经有数据，这时候进行数据刷新就可以了。
        initDB = {
            # 存活时间以秒为单位，超过这个时间则死亡需要重新登入
            "alive_time_s": int(time.time()) - (60 * 60 * 60),
        }
        sql = '''UPDATE admins_Session SET admins_session = %s WHERE admins_account = %s'''
        # 进行数据更新
        updata_result_session = manager_sqlx.excute(sql, ["%s" % (initDB), user_name])
        return redirect("/admins/login")
    except BaseException as e:
        logger.exception("function logout - %s - requestx.COOKIES.get is false - %s" % (ip, e),exc_info=True)
        return redirect("/admins/login/")

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
    logger.warning("%s - function read_file" % (ip))
    try:
        # -----------------执行验证------------------
        # -----------------执行验证------------------
        try:
            uuid4_str = request.COOKIES.get("adminsname_id")
            user_name = str(request.session.get(uuid4_str))
            logger.warning("function users_disk_manager - %s - user_name = %s" % (ip, user_name))
        except BaseException as e:
            logger.exception("function users_disk_manager - %s - requestx.COOKIES.get is false - %s" % (ip, e),exc_info=True)
            return redirect("/admins/login/")
        # -----------------执行验证------------------
        # -----------------执行验证------------------
        filename = request.GET["file"]
        file = open(r'C:\PythonProject\Collect\Collect\QQclass\%s.cvs'%(filename), 'rb')
        response = HttpResponse(file)
        file.close()
        response['Content-Type'] = 'application/octet-stream'  # 设置头信息，告诉浏览器这是个文件
        response['Content-Disposition'] = 'attachment;filename="qqqun-%s.csv"'%(filename)
        return response
    except BaseException as e:
        logging.exception('function users_disk_manager  - %s - requests method post - except' % (e), exc_info=True)
        return redirect("/admins/users_disk_manager/")

def login(request):
    '''
        超管登入页面
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
        return render(request, "admins/admins_login.html", {})
    elif request.method == "POST":
        logger.warning("function login - %s - requests method post" % (ip))
        # 在这里进行账号认证
        logger.warning("function login - %s - begin ajax post data" % (ip))
        try:
            admins_account = request.POST.get("admins_account")
            admins_passwd = request.POST.get("admins_passwd")
            if admins_account != None and admins_passwd != None:
                logger.warning("function login - %s - post account not is null - %s - %s" % (ip,admins_account,admins_passwd))
                # 如果账号不为空
                sql = '''select * from admins_Account where admins_account = %s'''
                search_result_account = manager_sqlx.search(sql,[admins_account])
                logger.warning("function login - %s - login begin - %s - %s" % (ip, admins_account, admins_passwd))
                if search_result_account != ():
                    # 能进来这里就代表，使用表单数据查询数据库有数据，所以不等于空
                    if search_result_account[0][1] == admins_account and search_result_account[0][2] == hashlib.md5(admins_passwd.encode(encoding='UTF-8')).hexdigest():
                        # 303 账号或秘密错误,404密码不存在
                        logger.warning("function login - %s - login success - %s - %s" % (ip, admins_account, admins_passwd))
                        # 首先判断有没有进行初始化，就是有没有进行session数据初始化
                        sql = '''select * from admins_Session where admins_account = %s'''
                        search_result_session = manager_sqlx.search(sql, [admins_account])
                        # 未进行初始化，进行初始化
                        # 初始化用户
                        initDB = {
                            # 存活时间以秒为单位，超过这个时间则死亡需要重新登入
                            "alive_time_s": int(time.time()) + (60 * 60 * 3),
                        }
                        if search_result_session == ():
                            # 如果等于空就代表没有进行初始化，就代表没有进行session初始化
                            logger.warning("function login - %s - login success init start - %s - %s" % (ip, admins_account, admins_passwd))
                            sql = '''insert into admins_Session (admins_account,admins_session) values (%s,%s)'''
                            insert_result_session = manager_sqlx.excute(sql, [admins_account,"%s"%(initDB)])
                            # 如果执行成功，就代表数据更新成功
                            if insert_result_session == True:
                                # 进行首页跳转，200，数据执行成功
                                logger.warning("function login - %s - insert_result_session susscess - %s - %s" % (ip, admins_account, admins_passwd))
                                uuid4_str = str(uuid.uuid4())
                                request.session[uuid4_str] = admins_account
                                obj = HttpResponse("200")
                                obj.set_cookie("adminsname_id", uuid4_str, 60*60*5)
                                logger.warning("function login - %s - updata_result_session susscess - %s - %s" % (ip, uuid4_str, admins_account))
                                return obj
                            if insert_result_session == False:
                                logger.warning("function login - %s - insert_result_session false - %s - %s" % (ip, admins_account, admins_passwd))
                                # 如果失败，返回重试，505请重试
                                return HttpResponse("505")
                        elif search_result_session != ():
                            # 如果查询用户session数据库不等于空就代表，已经有数据，这时候进行数据刷新就可以了。
                            sql = '''UPDATE admins_Session SET admins_session = %s WHERE admins_account = %s'''
                            # 进行数据更新
                            updata_result_session = manager_sqlx.excute(sql,["%s"%(initDB),admins_account])
                            if updata_result_session == True:
                                # 进行首页跳转，200数据执行成功
                                logger.warning("function login - %s - updata_result_session susscess - %s - %s" % (ip, admins_account, admins_passwd))
                                uuid4_str = str(uuid.uuid4())
                                request.session[uuid4_str] = admins_account
                                obj = HttpResponse("200")
                                obj.set_cookie("adminsname_id", uuid4_str, 60*60*5)
                                logger.warning("function login - %s - updata_result_session susscess - %s - %s" % (ip, uuid4_str, admins_account))
                                return obj
                            if updata_result_session == False:
                                logger.warning("function login - %s - updata_result_session false - %s - %s" % (ip, admins_account, admins_passwd))
                                # 如果失败，返回重试，505请重试
                                return HttpResponse("505")
                    else:
                        # 来到这里代表账号密码不匹配
                        logger.warning("function login - %s - login false - %s - %s" % (ip, admins_account, admins_passwd))
                        # 303 账号或秘密错误,404密码不存在
                        return HttpResponse("303")
                elif search_result_account == ():
                    # 账号不存在
                    logger.warning("function login - %s - login account is null - %s - %s" % (ip, admins_account, admins_passwd))
                    # 303 账号或秘密错误,404密码不存在
                    return HttpResponse("303")
            elif admins_account == None or admins_passwd == None:
                # 303 账号或秘密错误,404账号和密码不存在
                # 如果到这里就代表，前端传入的界面的值，为空。
                logger.warning("function login - %s - post account is null - %s - %s" % (ip,admins_account,admins_passwd))
                return HttpResponse("404")
        except BaseException as e:
            logging.exception('function login - %s - requests method post - except'%(e), exc_info=True)
            return HttpResponse("505")
    # 结尾,505请重试
    return HttpResponse("505")


def users_manager(request):
    '''
         超管登入页面
     :param request:
     :return:
     '''
    # 获取远程访问IP
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    # 输出日志
    logger.warning("%s - function users_manager" % (ip))
    if request.method == "GET":
        logger.warning("function users_manager - %s - requests method get" % (ip))
        # 首先判断是否已经登入
        # -------------------
        try:
            uuid4_str = request.COOKIES.get("adminsname_id")
            user_name = str(request.session.get(uuid4_str))
            logger.warning("function users_manager - %s - user_name = %s" % (ip,user_name))
            # 执行数据库查询内容
            sql = '''select * from admins_Account where admins_account = %s'''
            search_admins_account_result = manager_sqlx.search(sql,[user_name])
            if search_admins_account_result != ():
                logger.warning("function users_manager - %s - admins_Account is true" % (ip))
                logger.warning("function users_manager - %s - search_admins_account_result = %s" % (ip, search_admins_account_result))
                # 获取他的数据库session，判断存活时间是否大于现在时间，如果小于这退出。
                sql = '''select * from admins_Session where admins_account = %s'''
                search_admins_session_result = manager_sqlx.search(sql, [user_name])
                if search_admins_session_result != ():
                    logger.warning("function users_manager - %s - admins_Session is true" % (ip))
                    logger.warning("function users_manager - %s - search_admins_Session_result = %s" % (ip, search_admins_session_result))
                    # 返回正常页面
                    if int(eval(search_admins_session_result[0][2]).get("alive_time_s")) <= int(time.time()):
                        #代表管理员账户已过期
                        logger.warning("function users_manager - %s - search_admins_Session_result[0][3]['alive_time_s'] is false" % (ip))
                        return redirect("/admins/login/")
                    elif int(eval(search_admins_session_result[0][2]).get("alive_time_s")) > int(time.time()):
                        # ----------------------GET请求可以返回内容的开始---------------------------
                        # ----------------------GET请求可以返回内容的开始---------------------------
                        logger.warning("function users_manager - %s - search_admins_Session_result[0][3]['alive_time_s'] is true" % (ip))
                        # 这里需要提取用户列表数据,可以根据存活时间的大小，进行排序，只要修改SQL语句即可。
                        sql = '''select * from users_account order by users_alives_time_s'''
                        search_users_account_result =manager_sqlx.search(sql,[])
                        users_data_list = []
                        logger.warning("function users_manager - %s - search_users_account_result is true" % (ip))
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

                            users_data_list.append([id,user_account,user_alive_time_h,user_alive_time_s])
                        # 这里需要提取用户列表数据
                        return render(request, "admins/users_manager.html", {"users_data_list":users_data_list,"user_name":user_name})
                    # ----------------------GET请求可以返回内容的开始---------------------------
                    # ----------------------GET请求可以返回内容的开始---------------------------
                elif search_admins_session_result == ():
                    logger.warning("function users_manager - %s - admins_Session is false" % (ip))
                    return redirect("/admins/login/")
            elif search_admins_account_result == ():
                logger.warning("function users_manager - %s - admins_Account is false" % (ip))
                return redirect("/admins/login/")
        except BaseException as e:
            logger.exception("function users_manager - %s - requestx.COOKIES.get is false - %s" % (ip,e),exc_info=True)
            return redirect("/admins/login/")
        # -------------------
    elif request.method == "POST":
        logger.warning("function users_manager  - %s - requests method post" % (ip))
        # 在这里进行账号认证
        logger.warning("function users_manager  - %s - begin ajax post data" % (ip))
        try:
            # ------------------------------
            # ------------------------------
            # 这里应该还需要认证一次是否已经登入
            try:
                uuid4_str = request.COOKIES.get("adminsname_id")
                user_name = str(request.session.get(uuid4_str))
                logger.warning("function users_manager - %s - user_name = %s" % (ip, user_name))
            except BaseException as e :
                logger.exception("function users_manager - %s - requestx.COOKIES.get is false - %s" % (ip, e),exc_info=True)
                return HttpResponse("404")
            # ----------------------POST请求可以返回内容的开始---------------------------
            # ----------------------POST请求可以返回内容的开始---------------------------
            user_id = request.POST.get("user_id")
            updata_time = request.POST.get("updata_time")
            users_alives_time_s = request.POST.get("users_alives_time_s")
            logger.warning("function users_manager  - %s - updata times %s - %s - %s" % (ip,user_id,updata_time,users_alives_time_s))
            # 如果不等于空，就可以进行更新数据库
            if user_id != None and updata_time != None and  users_alives_time_s != None:
                sql = '''UPDATE users_account SET users_alives_time_s = %s WHERE id = %s'''
                # 新时间等于原本时间+需要更新的时间
                if int(users_alives_time_s) <= int(time.time()):
                    users_alives_time_s_news = int(time.time()) + (int(updata_time)*24*60*60)
                # 如果存活时间大于现实时间
                elif int(users_alives_time_s) > int(time.time()):
                    users_alives_time_s_news = int(users_alives_time_s) + (int(updata_time)*24*60*60)
                updata_users_alives_time_s_news_result = manager_sqlx.excute(sql,[users_alives_time_s_news,user_id])
                if updata_users_alives_time_s_news_result == True:
                    logger.warning("function users_manager  - %s - updata times is ture ok" % (ip))
                    return HttpResponse("200")
                elif updata_users_alives_time_s_news_result == False:
                    logger.warning("function users_manager  - %s - updata times is false" % (ip))
                    return HttpResponse("404")
            elif user_id == None or updata_time == None or users_alives_time_s == None:
                logger.warning("function users_manager  - %s - user_id == None and updata_time == None and  users_alives_time_s == None" % (ip))
                return HttpResponse("404")
            # ----------------------POST请求可以返回内容的开始---------------------------
            # ----------------------POST请求可以返回内容的开始---------------------------
        except BaseException as e :
            logging.exception('function users_manager  - %s - requests method post - except'%(e), exc_info=True)
            return HttpResponse("404")




def users_disk_manager(request):
    '''
        users_disk_manager 用户网盘管理界面
    :param requets:
    :return:
    '''
    # 获取远程访问IP
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    # 输出日志
    logger.warning("%s - function login" % (ip))
    if request.method == "GET":
        logger.warning("function users_disk_manager - %s - requests method get" % (ip))
        # 首先判断是否已经登入
        # -------------------
        try:
            uuid4_str = request.COOKIES.get("adminsname_id")
            user_name = str(request.session.get(uuid4_str))
            logger.warning("function users_disk_manager - %s - user_name = %s" % (ip,user_name))
            # 执行数据库查询内容
            sql = '''select * from admins_Account where admins_account = %s'''
            search_admins_account_result = manager_sqlx.search(sql,[user_name])
            if search_admins_account_result != ():
                logger.warning("function users_disk_manager - %s - admins_Account is true" % (ip))
                logger.warning("function users_disk_manager - %s - search_admins_account_result = %s" % (ip, search_admins_account_result))
                # 获取他的数据库session，判断存活时间是否大于现在时间，如果小于这退出。
                sql = '''select * from admins_Session where admins_account = %s'''
                search_admins_session_result = manager_sqlx.search(sql, [user_name])
                if search_admins_session_result != ():
                    logger.warning("function users_disk_manager - %s - admins_Session is true" % (ip))
                    logger.warning("function users_disk_manager - %s - search_admins_Session_result = %s" % (ip, search_admins_session_result))
                    # 返回正常页面
                    if int(eval(search_admins_session_result[0][2]).get("alive_time_s")) <= int(time.time()):
                        #代表管理员账户已过期
                        logger.warning("function users_disk_manager - %s - search_admins_Session_result[0][3]['alive_time_s'] is false" % (ip))
                        return redirect("/admins/login/")
                    elif int(eval(search_admins_session_result[0][2]).get("alive_time_s")) > int(time.time()):
                        logger.warning("function users_disk_manager - %s - search_admins_Session_result[0][3]['alive_time_s'] is true" % (ip))
                        # ----------------------GET请求可以返回内容的开始---------------------------
                        # ----------------------GET请求可以返回内容的开始---------------------------


                        return render(request, "admins/users_disk_manager.html",{"user_name":user_name})
                        # ----------------------GET请求可以返回内容的开始---------------------------
                        # ----------------------GET请求可以返回内容的开始---------------------------
                elif search_admins_session_result == ():
                    logger.warning("function users_disk_manager - %s - admins_Session is false" % (ip))
                    return redirect("/admins/login/")
            elif search_admins_account_result == ():
                logger.warning("function users_disk_manager - %s - admins_Account is false" % (ip))
                return redirect("/admins/login/")
        except BaseException as e:
            logger.exception("function users_disk_manager - %s - requestx.COOKIES.get is false - %s" % (ip,e),exc_info=True)
            return redirect("/admins/login/")
        # -------------------
    elif request.method == "POST":
        logger.warning("function users_disk_manager  - %s - requests method post" % (ip))
        # 在这里进行账号认证
        logger.warning("function users_disk_manager  - %s - begin ajax post data" % (ip))
        try:
            # ------------------------------
            # 这里应该还需要认证一次是否已经登入
            # 这里应该还需要认证一次是否已经登入
            # 这里应该还需要认证一次是否已经登入
            try:
                uuid4_str = request.COOKIES.get("adminsname_id")
                user_name = str(request.session.get(uuid4_str))
                logger.warning("function users_disk_manager - %s - user_name = %s" % (ip, user_name))
            except BaseException as e:
                logger.exception("function users_disk_manager - %s - requestx.COOKIES.get is false - %s" % (ip, e),exc_info=True)
                return HttpResponse("404")
            # 这里应该还需要认证一次是否已经登入
            # 这里应该还需要认证一次是否已经登入
            # 这里应该还需要认证一次是否已经登入
            # ------------------------------
            # 到这里就可以做正常的返回数据，防止有心之人使用post请求直接修改数据。
            # ------------------------------
            # ----------------------POST请求可以返回内容的开始---------------------------
            # ----------------------POST请求可以返回内容的开始---------------------------
            search_content = request.POST.get("search_content")
            logger.warning("function users_disk_manager - %s - search_content = %s" % (ip,search_content))
            if search_content != "":
                logger.warning("function users_disk_manager - %s - earch_content != None" % (ip))
                sql = '''select * from users_network_dick'''
                return_uses_network_dict = {}
                search_uses_network_dick_result = manager_sqlx.search(sql, [])
                if search_uses_network_dick_result == ():
                    logger.warning("function users_disk_manager - %s - search_uses_network_dick_result == ()" % (ip))
                    return HttpResponse("303")
                elif search_uses_network_dick_result != ():
                    logger.warning("function users_disk_manager - %s - search_uses_network_dick_result != ()" % (ip))
                    for index,row in enumerate(search_uses_network_dick_result):
                        id = row[0]
                        qqclass_name = row[1]
                        qqclass_number = row[2]
                        qqclass_from_user_account = row[3]
                        if row[4] == 0:
                            user_is_like = "nolike"
                        elif row[4] == 1:
                            user_is_like = "like"
                        download_location = row[5]
                        if str(search_content) in (str(id)  + str(qqclass_name)  + str(qqclass_number)  + str(qqclass_from_user_account)) or str(search_content) == user_is_like:
                            return_uses_network_dict[index] = [id,qqclass_name,qqclass_number,qqclass_from_user_account,user_is_like,download_location]
                    return_jsonDB = json.dumps(return_uses_network_dict,ensure_ascii=False)
                    return HttpResponse(return_jsonDB)
            elif search_content == "":
                logger.warning("function users_disk_manager - %s - sarch_content == None" % (ip))
                sql = '''select * from users_network_dick'''
                return_uses_network_dict = {}
                search_uses_network_dick_result = manager_sqlx.search(sql,[])
                if search_uses_network_dick_result == ():
                    logger.warning("function users_disk_manager - %s - search_uses_network_dick_result == ()" % (ip))
                    return HttpResponse("303")
                elif search_uses_network_dick_result != ():
                    logger.warning("function users_disk_manager - %s - search_uses_network_dick_result != ()" % (ip))
                    for index,row in enumerate(search_uses_network_dick_result):
                        id = row[0]
                        qqclass_name = row[1]
                        qqclass_number = row[2]
                        qqclass_from_user_account = row[3]
                        if row[4] == 0:
                            user_is_like = "nolike"
                        elif row[4] == 1:
                            user_is_like = "like"
                        download_location = row[5]
                        return_uses_network_dict[index] = [id,qqclass_name,qqclass_number,qqclass_from_user_account,user_is_like,download_location]
                    return_jsonDB = json.dumps(return_uses_network_dict,ensure_ascii=False)
                    return HttpResponse(return_jsonDB)
                # ----------------------POST请求可以返回内容的开始---------------------------
                # ----------------------POST请求可以返回内容的开始---------------------------
        except BaseException as e:
            logging.exception('function users_disk_manager  - %s - requests method post - except'%(e), exc_info=True)
            return HttpResponse("404")
        
        
        
def activity_manager(request):
    '''

    :param request:
    :return:
    '''
    # 获取远程访问IP
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    # 输出日志
    logger.warning("%s - function activity_manager" % (ip))
    if request.method == "GET":
        logger.warning("function activity_manager - %s - requests method get" % (ip))
        # 首先判断是否已经登入
        # -------------------
        try:
            uuid4_str = request.COOKIES.get("adminsname_id")
            user_name = str(request.session.get(uuid4_str))
            logger.warning("function activity_manager - %s - user_name = %s" % (ip,user_name))
            # 执行数据库查询内容
            sql = '''select * from admins_Account where admins_account = %s'''
            search_admins_account_result = manager_sqlx.search(sql,[user_name])
            if search_admins_account_result != ():
                logger.warning("function activity_manager - %s - admins_Account is true" % (ip))
                logger.warning("function activity_manager - %s - search_admins_account_result = %s" % (ip, search_admins_account_result))
                # 获取他的数据库session，判断存活时间是否大于现在时间，如果小于这退出。
                sql = '''select * from admins_Session where admins_account = %s'''
                search_admins_session_result = manager_sqlx.search(sql, [user_name])
                if search_admins_session_result != ():
                    logger.warning("function activity_manager - %s - admins_Session is true" % (ip))
                    logger.warning("function activity_manager - %s - search_admins_Session_result = %s" % (ip, search_admins_session_result))
                    # 返回正常页面
                    if int(eval(search_admins_session_result[0][2]).get("alive_time_s")) <= int(time.time()):
                        #代表管理员账户已过期
                        logger.warning("function activity_manager - %s - search_admins_Session_result[0][3]['alive_time_s'] is false" % (ip))
                        return redirect("/admins/login/")
                    elif int(eval(search_admins_session_result[0][2]).get("alive_time_s")) > int(time.time()):
                        logger.warning("function activity_manager - %s - search_admins_Session_result[0][3]['alive_time_s'] is true" % (ip))
                        # ----------------------Get请求可以返回内容的开始---------------------------
                        # ----------------------Get请求可以返回内容的开始---------------------------
                        sql = "select * from alls_notice_activity_list where is_delete = 0 order by id desc;"
                        search_alls_notice_activity_list_result = manager_sqlx.search(sql,[])




                        return render(request,"admins/activity_manager.html",{"activity_list":search_alls_notice_activity_list_result,"user_name":user_name})
                        # ----------------------Get请求可以返回内容的开始---------------------------
                        # ----------------------Get请求可以返回内容的开始---------------------------
                elif search_admins_session_result == ():
                    logger.warning("function activity_manager - %s - admins_Session is false" % (ip))
                    return redirect("/admins/login/")
            elif search_admins_account_result == ():
                logger.warning("function activity_manager - %s - admins_Account is false" % (ip))
                return redirect("/admins/login/")
        except BaseException as e:
            logger.exception("function activity_manager - %s - requestx.COOKIES.get is false - %s" % (ip,e),exc_info=True)
            return redirect("/admins/login/")
        # -------------------
    elif request.method == "POST":
        logger.warning("function activity_manager  - %s - requests method post" % (ip))
        # 在这里进行账号认证
        logger.warning("function activity_manager  - %s - begin ajax post data" % (ip))
        try:
            # ------------------------------
            # ------------------------------
            # 这里应该还需要认证一次是否已经登入
            try:
                uuid4_str = request.COOKIES.get("adminsname_id")
                user_name = str(request.session.get(uuid4_str))
                logger.warning("function activity_manager - %s - user_name = %s" % (ip, user_name))
            except BaseException as e :
                logger.exception("function activity_manager - %s - requestx.COOKIES.get is false - %s" % (ip, e),exc_info=True)
                return HttpResponse("404")
            # ----------------------POST请求可以返回内容的开始---------------------------
            # ----------------------POST请求可以返回内容的开始---------------------------
            activity_id = request.POST.get("activity_id")
            sql = '''UPDATE alls_notice_activity_list SET is_delete = 1 WHERE id = %s'''
            updata_alls_notice_activity_list_result = manager_sqlx.excute(sql,[activity_id])
            if updata_alls_notice_activity_list_result == True:
                return HttpResponse("200")
            elif updata_alls_notice_activity_list_result == False:
                return HttpResponse("404")
            # ----------------------POST请求可以返回内容的开始---------------------------
            # ----------------------POST请求可以返回内容的开始---------------------------
        except BaseException as e :
            logging.exception('function activity_manager  - %s - requests method post - except'%(e), exc_info=True)
            return HttpResponse("404")
