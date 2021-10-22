from .tools import seleniums,manager_sql
from django.http import request
from django.shortcuts import redirect,render,HttpResponse,Http404
import threading,requests
import uuid,time,os,random
from .settings import *
import logging,hashlib,json
from django.views.decorators.clickjacking import xframe_options_sameorigin      # iframe拒绝问题

'''
    print(BASE_DIR) 打开什么文件的时候千万别忘记+from .settings import *的BASE_DIR

'''

manager_sqlx = manager_sql.SqlManger()

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s  - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def users_my_team(request):
    return render(request,"users/users_announce.html",{})


def users_announce(request):
    return render(request,"users/users_my_team.html",{})



@xframe_options_sameorigin
def users_register(request):
    '''
         注册页面
     :param request:
     :return:
     '''
    # 获取远程访问IP
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    # 输出日志
    logger.warning("%s - function users_register" % (ip))
    if request.method == "GET":
        logger.warning("function users_register - %s - requests method get" % (ip))
        # 首先判断是否已经登入
        return render(request, "users/users_register.html", {})

    elif request.method == "POST":
        # 结尾,505请重试
        return HttpResponse("505")







def users_register_API(request):
    '''
         验证码接受页面
     :param request:
     :return:
     '''
    # 获取远程访问IP
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    # 输出日志
    logger.warning("%s - function users_register_API" % (ip))
    if request.method == "GET":
        logger.warning("function users_register_API - %s - requests method get" % (ip))
        # 首先判断是否已经登入
        return HttpResponse("200")
    elif request.method == "POST":
        typex = request.POST.get("type")
        if typex == "send":
            logger.warning("function users_register_API - %s - typex == send:" % (ip))
            users_phone = request.POST.get("users_phone")
            logger.warning("function users_register_API - %s - %s " % (ip,users_phone))
            # if users_phone != None:
            #     random_num = ""
            #     seeds = "1234567890"
            #     for i in range(0,4):
            #         random_num += str(random.choice(seeds))
            #     # 向验证码平台发送数据
            #     send_url = "http://jk.smstcby.com/smsUTF8.aspx"
            #     send_data = {
            #         "type": "send",
            #         "username": "18227365322",
            #         "password": hashlib.md5("123456".encode(encoding='UTF-8')).hexdigest(),
            #         "gwid": "7cfae11b",
            #         "mobile": users_phone,
            #         "message": "【隆康路科技】欢迎注册红遍中国自愿者,您的验证码是:%s"%(random_num),
            #         "dstime": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + int(2))),
            #         "rece": "json"
            #     }
            #     logger.warning("function users_register_API - %s - requests.post url=send_url" % (ip))
            #     try:
            #         responseX = requests.post(url=send_url, data=send_data, verify=False, allow_redirects=True, timeout=30).content
            #         jsonStr = json.loads(responseX)
            #         logger.warning("function users_register_API - %s - jsonStr = json.loads %s" % (ip, jsonStr))
            #         if jsonStr["returnstatus"] == "success":
            #             uuid4_str = str(uuid.uuid4()) + "_number"
            #             request.session[uuid4_str] = random_num
            #             obj = HttpResponse("200")
            #             obj.set_cookie("random_num", uuid4_str, 60 * 60 * 24)
            #             logger.warning("function users_register_API - %s - random_num = %s" % (ip,random_num))
            #             return obj
            #         else:
            #             return HttpResponse("505")
            #     except BaseException as e:
            #         logger.exception("function users_register_API - %s - except BaseException as e: - %s" % (ip, e),exc_info=True)
            #         HttpResponse("505")
        if typex == "register":
            logger.warning("function users_register_API - %s - typex == register:" % (ip))
            users_phone = request.POST.get("users_phone")
            users_passwd = request.POST.get("users_passwd")
            # 获取用户输入验证码与手机验证码是否对应
            users_random_num = request.POST.get("users_random_num")
            logger.warning("function users_register_API - %s - %s - %s - %s" % (ip,users_phone,users_passwd,users_random_num))
            if users_phone != None and users_passwd != None and users_random_num != None:
                try:
                    uuid4_str = request.COOKIES.get("random_num")
                    random_num = str(5678)
                    # random_num = str(request.session.get(uuid4_str))
                except BaseException as e:
                    logger.exception("function users_register_API - %s - users_register_API is false - %s" % (ip, e),exc_info=True)
                    return HttpResponse("404")
                # 判断用户输入的验证码是否正确
                if users_random_num != random_num:
                    logger.warning("function users_register_API - %s - %s != %s " % (ip,users_random_num,random_num))
                    # 505验证码错误，404请重试刷新页面
                    return HttpResponse("505")
                elif users_random_num == random_num:
                    # 这里得做判断，如果已经有账号就刷新，没有就插入，同时做忘记密码的修改。
                    sql = '''select * from users_Account where users_account = %s'''
                    search_result_session = manager_sqlx.search(sql, [users_phone])

                    if search_result_session == ():
                        logger.warning("function users_register_API - %s - search_result_session == () " % (ip))
                        users_passwd_md5 = hashlib.md5(users_passwd.encode(encoding='UTF-8')).hexdigest(),
                        sql = '''insert into users_Account (users_account,users_passwd,users_alives_time_s) values (%s,%s,%s)'''
                        insert_users_account_result = manager_sqlx.excute(sql,[users_phone,users_passwd_md5[0],int(time.time()+60*60*24)])

                        if insert_users_account_result == True:
                            logger.warning("function users_register_API - %s - insert_users_account_result == True" % (ip))
                            return HttpResponse("200")
                        elif insert_users_account_result == False:
                            logger.warning("function users_register_API - %s - insert_users_account_result == False" % (ip))
                            return HttpResponse("404")
                    elif search_result_session != ():
                        logger.warning("function users_register_API - %s - search_result_session != () " % (ip))
                        users_passwd_md5 = hashlib.md5(users_passwd.encode(encoding='UTF-8')).hexdigest(),
                        sql = '''UPDATE users_Account SET users_passwd = %s WHERE users_account = %s'''
                        updata_users_account_passwd = manager_sqlx.excute(sql, [users_passwd_md5[0],users_phone])

                        if updata_users_account_passwd == True:
                            logger.warning("function users_register_API - %s - updata_users_account_passwd == True" % (ip))
                            return HttpResponse("200")
                        elif updata_users_account_passwd == False:
                            logger.warning("function users_register_API - %s - updata_users_account_passwd == False" % (ip))
                            return HttpResponse("404")
        logger.warning("function users_register_API - %s - POST no type " % (ip))
        HttpResponse("404")




