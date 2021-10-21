from django.http import request
from django.shortcuts import redirect,render,HttpResponse,Http404
import threading,requests
import uuid,time,os
import logging,hashlib,json
from Collect.tools import manager_sql


manager_sqlx = manager_sql.SqlManger()

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s  - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def activity_manager_add(request):
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


                        return render(request,"admins/activity_manager_add.html",{"user_name":user_name})
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
            active_name = request.POST.get("active_name",None)
            active_content = request.POST.get("active_content", None)
            active_type = request.POST.get("active_type", None)
            active_end_time = request.POST.get("active_end_time", None)
            #如果为空直接，返回404
            if active_name == None or active_name =="" or active_content == None or active_content =="" or active_type == None or active_type == "":
                return HttpResponse("404")
            if active_end_time == None or active_end_time == "":
                return HttpResponse("404")
            # 这里输入的值都不为空，可以进行数据插入
            sql = '''insert into alls_notice_activity_list values (%s,%s,%s,%s,%s,%s,%s,%s)'''
            insert_result = manager_sqlx.excute(sql,[
                "",
                active_name,
                active_content,
                active_type,
                time.strftime('%Y-%m-%d',time.localtime(time.time())),
                active_end_time,
                user_name,
                0
            ])
            if insert_result == True:
                return HttpResponse("200")
            else:
                return HttpResponse("404")
            # ----------------------POST请求可以返回内容的开始---------------------------
            # ----------------------POST请求可以返回内容的开始---------------------------
        except BaseException as e :
            logging.exception('function activity_manager  - %s - requests method post - except'%(e), exc_info=True)
            return HttpResponse("404")