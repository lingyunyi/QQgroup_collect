# import logging
#
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)
#
# logger.info('This is a log info')
# logger.debug('Debugging')
# logger.warning('Warning exists')
# logger.info('Finish')
#
# try:
#     int("asdf")
# except BaseException as e :
#     logging.exception('%s'%(e), exc_info=True)
#
#
# print("ssss")
# print("ssss")
# print("ssss")
# print("ssss")

# import hashlib
# # m = hashlib.md5()
# # m.update(b'123')
# # m.hexdigest()
# data = "123456"
# a = hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()
# print(a)
import requests
import hashlib,time,json
send_url = "http://jk.smstcby.com/smsUTF8.aspx"
send_data = {
    "type": "send",
    "username": "18227365322",
    "password": hashlib.md5("123456".encode(encoding='UTF-8')).hexdigest(),
    "gwid": "7cfae11b",
    "mobile": 18172041272,
    "message": "【红遍中国自愿者】欢迎注册红遍中国自愿者，您的验证码是：666666" ,
    "dstime": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()+int(2))),
    "rece": "json"
}
jsonStr = json.loads(requests.post(url=send_url, data=send_data).content)
print(jsonStr)