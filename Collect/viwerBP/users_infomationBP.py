from django.http import request
from django.shortcuts import redirect,render,HttpResponse,Http404
import threading,requests
import uuid,time,os
import logging,hashlib,json
from Collect.tools import manager_sql


manager_sqlx = manager_sql.SqlManger()

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s  - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def user_infomation(request):
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
                        # 首先先判断有没有信息，查询一下，如果没有直接进行更新
                        sql = '''select is_who from users_infomation_list limit 1'''
                        select_result = manager_sqlx.search(sql,[])
                        logger.warning(select_result)
                        if select_result == ():
                            sql = '''insert into users_infomation_list values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
                            insert_result = manager_sqlx.excute(sql,[
                                "","None","None","None","None",
                                "None","None","None","None",user_name
                            ])
                        sql = "select * from users_infomation_list where is_who = %s limit 1"
                        select_result = manager_sqlx.search(sql,[user_name])
                        if select_result != ():
                            return render(request, "users/users_infomation.html",{'user_info_list':select_result[0]})
                        return redirect("/users/center/")
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

def user_infomation_changer(request):
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

                        sql = '''select is_who from users_infomation_list limit 1'''
                        select_result = manager_sqlx.search(sql,[])
                        logger.warning(select_result)
                        if select_result == ():
                            sql = '''insert into users_infomation_list values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
                            insert_result = manager_sqlx.excute(sql,[
                                "","None","None","None","None",
                                "None","None","None","None",user_name
                            ])
                        sql = "select * from users_infomation_list where is_who = %s limit 1"
                        select_result = manager_sqlx.search(sql,[user_name])
                        if select_result != ():
                            return render(request, "users/users_infomation_change.html",{'user_info_list':select_result[0]})
                        return redirect("/users/center/")

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
            my_name = request.POST.get('my_name',"None")
            my_school = request.POST.get('my_school', "None")
            my_grade = request.POST.get('my_grade', "None")
            my_depart = request.POST.get('my_depart', "None")
            my_trade = request.POST.get('my_trade', "None")
            sql = '''UPDATE users_infomation_list SET name = %s,
             school = %s,
             grade = %s,
             depart = %s,
             trade = %s
            WHERE is_who = %s '''
            updata_result = manager_sqlx.excute(sql,[my_name,my_school,my_grade,my_depart,my_trade,user_name])
            if updata_result == True:
                return HttpResponse("200")
            else:
                return HttpResponse("404")
            # ----------------------POST请求可以返回内容的开始---------------------------
            # ----------------------POST请求可以返回内容的开始---------------------------
        except BaseException as e :
            logging.exception('function activity_details  - %s - requests method post - except'%(e), exc_info=True)
            return HttpResponse("404")