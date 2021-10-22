# 导入需要的包
# 爬取qq群的成员信息
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import json
import csv
import uuid,os
from Collect.settings import *
from Collect.tools import manager_sql
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s  - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class Seleniums(object):


    def __init__(self,user_name):
        print("\n-----------------------seleniums-----------------------")
        print("\n-----------------------__init__-----------------------")
        '''
        获取初始文件
                # 获取的img路径 wait success有值状态 flase失败
                "img_path":"wait",
                # 扫描状态 wait等待中 success成功 false失败
                "scan_status":"wait",
        '''
        self.user_name = user_name
        self.manager_sqlx = manager_sql.SqlManger()
        sql = '''select * from users_Session where users_account = %s'''
        search_users_session_result = self.manager_sqlx.search(sql, [user_name])
        self.get_user_session_dict = eval(search_users_session_result[0][2])

        self.times = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.add_list = []

    def updata_dict(self):
        print("\n-----------------------seleniums-----------------------")
        print("\n-----------------------updata_dict-----------------------")
        '''
            更新一下数据
        :return:
        '''
        try:
            ''''''
            ''''''
            sql = '''UPDATE users_Session SET users_session = %s where users_account = %s   '''
            true_or_false = self.manager_sqlx.excute(sql,[str(self.get_user_session_dict),self.user_name])
            print("\n-----def updata_dict-----self.manager_sqlx.insert(sql)-----true_or_false-----",true_or_false)
            ''''''
            ''''''
        except BaseException as e :
            print("\n-----def updata_dict-----self.manager_sqlx.insert(sql)----- except BaseException as e :-----",e)



    # 开始登陆
    def login_spider(self):
        print("\n-----------------------seleniums-----------------------")

        print("\n-----------------------login_spider-----------------------")
        url = 'https://qun.qq.com/'
        # 构建谷歌驱动器
        #部署环境 需要放到自己的目录，不然没有权限访问
        browser = webdriver.Firefox(executable_path=selenuim_Exe)


        #browser = webdriver.Firefox()
        print("-----def updata_dict-----browser-----webdriver.Firefox()-----")
        # 请求url
        browser.get(url)
        # 模拟登陆，首先找到登陆的id，并点击
        browser.find_element_by_css_selector('#headerInfo p a').click()
        # 点击之后会弹出一个登陆框，这时候我们用显示等待来等待这个登陆框加载出来
        WebDriverWait(browser, 1000).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, '#loginWin iframe')
            )
        )
        print("\n-----def login_spider-----browser-----login flask is ok-----")

        iframe_url = browser.find_element_by_css_selector('#loginWin iframe').get_attribute('src')

        browser.get(iframe_url)


        flag = 2
        str = uuid.uuid4()
        while flag > 0:
            flag -= 1
            print("\n-----def login_spider-----while flag > 0:-----havs num is   {}   choose-----".format(flag))
            try:
                if browser.find_element_by_xpath("/html/body/div[1]/div[4]/div[8]/div/span/span[1]"):
                    path = r"\Collect\temp\{}.png".format(str)

                    '''截屏二维码'''
                    browser.find_element_by_xpath('//*[@id="qrlogin_img"]').screenshot("%s%s"%(BASE_DIR,path))
                    '''赋值'''
                    self.get_user_session_dict["img_path"] = path
                    self.updata_dict()
                if browser.find_element_by_xpath("/html/body/div[1]/div/div/div/p[1]/a[2]"):
                    pass
                    '''为了报错而存在冗余代码，下次优化'''
            except BaseException as e:
                print("\n-----def login_spider-----browser.find_element_by_xpath   no is login-----except BaseException as e:-----",e)
                time.sleep(22)
                continue
        try:
            if browser.find_element_by_xpath("/html/body/div[1]/div/div/div/p[1]/a[2]"):
                self.get_user_session_dict["scan_status"] = "success"
                '''
                更新一下数据
                '''
                self.updata_dict()
                '''
                更新一下数据
                '''
                return browser
        except BaseException as e:
            print("\n-----def login_spider-----browser.find_element_by_xpath  is login-----except BaseException as e:-----",e)
            browser.quit()

        self.get_user_session_dict["scan_status"] = "false"
        '''
        更新一下数据
        '''
        self.updata_dict()
        '''
        更新一下数据
        '''
        return False


    # 切换句柄操作
    def switch_spider(self,browser):
        print("\n-----------------------seleniums-----------------------")
        print("\n-----------------------switch_spider-----------------------")
        # 登陆成功之后，我们就找到群管理的标签并点击,首先等待这个元素加载完成
        WebDriverWait(browser, 1000).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, '/html/body/div[1]/div/div/ul/li[3]')
            )
        )
        print("\n-----def switch_spider-----WebDriverWait-----begin-----群管理(点击)")
        browser.find_element_by_xpath('/html/body/div[1]/div/div/ul/li[3]').click()
        # 点击之后，我们找到成员管理标签并点击
        WebDriverWait(browser, 1000).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, '/html/body/div[3]/ul/li[1]')
            )
        )
        print("\n-----def switch_spider-----(By.CLASS_NAME, '群成员点击')-----begin-----")
        browser.find_element_by_xpath('/html/body/div[3]/ul/li[1]').click()
        # 打印全部窗口句柄
        # print(browser.window_handles)
        # 打印当前窗口句柄
        # print(browser.current_window_handle)
        # 注意这里点击成员管理之后会自动跳转到一个新窗口打开这个页面
        # 所以我们需要将窗口句柄切换到这个新窗口
        browser.switch_to.window(browser.window_handles[1])
        # 解释一下browser.switch_to.window是获取当前一共有几个窗口
        # 这里是2个
        # browser.switch_to.window这个是指定当前游标切换到哪个窗口
        # 其实也可以这么写
        # all_window = browser.switch_to.window返回的是一个列表
        # browser.switch_to.window(all_window[1])
        # 效果是一样的

        return browser


    # 开始采集数据
    def start_spider(self,browser):
        print("\n-----------------------seleniums-----------------------")
        print("\n-----------------------start_spider-----------------------")

        # 声明一个列表存储字典
        data_list = []
        # 切换句柄之后，我们显示等待窗口出来
        WebDriverWait(browser, 1000).until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, 'my-all-group')
            )
        )
        print("\n-----def start_spider-----(By.CLASS_NAME, 'my-all-group')-----begin-----")
        lis = []
        try:
            mygroup = browser.find_elements_by_class_name("my-group-list")
            print(mygroup)
            for i in mygroup:
                li = i.find_elements_by_tag_name("li")
                for j in li:
                    lis.append(j)
            print(lis)

            for i in lis:
                print(i)
                name = i.get_attribute("title")
                print(name)


        except BaseException as error:
            print("\n-----def start_spider-----(lis = find_elements_by_xpath('li'))-----false-----")
            return False
        # 遍历
        num = 0
        while len(lis) != num:
            print("\n-----def start_spider-----( while len(lis) != num:)-----%s:%s-----"%(len(lis),num))
            data_list = []
            try:
                # 按顺序选择群并获取信息
                # 先点击该群获取成员信息

                # 先获取这个页面的内容再点击，否则找不到任何东西
                qun_id = lis[num].get_attribute("data-id")
                qun_name = lis[num].get_attribute("title")
                #
                lis[num].click()
                # 显示等待信息加载完成
                WebDriverWait(browser, 1000).until(
                    EC.presence_of_all_elements_located(
                        (By.CLASS_NAME, 'list')
                    )
                )
                print("\n-----def start_spider-----(By.CLASS_NAME, 'list')-----begin-----")
                # 获取该群当前有多少人，后面翻页需要
                groupMemberNum = eval(browser.find_element_by_id('groupMemberNum').text)
                # 每一次翻页都会刷新21条信息，所以写个循环
                # 这里加1是因为假如一个群有36人，那么count=1，如果循环的话就不会翻页了
                # 也就是只能抓到一页的数据，大家可以自己想想其中的流程就知道了
                count = groupMemberNum // 21 + 1
                # 这里我只爬取每个群的一部分，如果想爬取全部成员信息
                '''
                # 请注释下面的if语句
                if count > 5:
                    count = 5
                '''
                # 每次循环都进行翻页
                while count:
                    count -= 1
                    browser.execute_script('document.documentElement.scrollTop=100000')
                    time.sleep(2)
                time.sleep(3)
                # 开始获取成员信息
                trs = browser.find_elements_by_class_name('mb')
                writer_status = "true"
                if trs:
                    # 遍历
                    for tr in trs:
                        tds = tr.find_elements_by_tag_name('td')[2:]
                        if len(tds) == 8:
                            # qq网名
                            qq_name = tds[0].text
                            # 群名称
                            group_name = tds[1].text
                            # qq号
                            qq_number = tds[2].text
                            # 性别
                            gender = tds[3].text
                            # qq年龄
                            qq_year = tds[4].text
                            # 入群时间
                            join_time = tds[5].text
                            # 等级（积分）
                            level = None
                            # 最后发言时间
                            end_time = tds[6].text

                            # 声明一个字典存储数据
                            data_dict = {}
                            data_dict['qq_name'] = qq_name
                            data_dict['group_name'] = group_name
                            data_dict['qq_number'] = qq_number
                            data_dict['gender'] = gender
                            data_dict['qq_year'] = qq_year
                            data_dict['join_time'] = join_time
                            data_dict['level'] = level
                            data_dict['end_time'] = end_time

                            print(data_dict)
                        elif len(tds) == 9:
                            # qq网名
                            qq_name = tds[0].text
                            # 群名称
                            group_name = tds[1].text
                            # qq号
                            qq_number = tds[2].text
                            # 性别
                            gender = tds[3].text
                            # qq年龄
                            qq_year = tds[4].text
                            # 入群时间
                            join_time = tds[5].text
                            # 等级（积分）
                            level = tds[6].text
                            # 最后发言时间
                            end_time = tds[7].text

                            # 声明一个字典存储数据
                            data_dict = {}
                            data_dict['qq_name'] = qq_name
                            data_dict['group_name'] = group_name
                            data_dict['qq_number'] = qq_number
                            data_dict['gender'] = gender
                            data_dict['qq_year'] = qq_year
                            data_dict['join_time'] = join_time
                            data_dict['level'] = level
                            data_dict['end_time'] = end_time
                            print(data_dict)

                        data_list.append(data_dict)
                print("\n-----def start_spider-----(while count:)-----finaly success-----")
                browser.find_element_by_id('changeGroup').click()
                time.sleep(3)
                WebDriverWait(browser, 1000).until(
                    EC.presence_of_all_elements_located(
                        (By.CLASS_NAME, 'ui-dialog')
                    )
                )
                # try:
                #     lis = None
                #     print('**********************************.//div[@class="my-all-group"]/ul[2]/li')
                #     if browser.find_elements_by_xpath('.//div[@class="my-all-group"]/ul[2]/li'):
                #         lis = browser.find_elements_by_xpath('.//div[@class="my-all-group"]/ul[2]/li')
                # except BaseException as e:
                #     print(e)
                #     if lis == None:
                #         try:
                #             print('-------------------------------------.//div[@class="my-all-group"]/ul[2]/li')
                #             if browser.find_elements_by_xpath('.//div[@class="my-all-group"]/ul/li'):
                #                 lis = browser.find_elements_by_xpath('.//div[@class="my-all-group"]/ul/li')
                #         except BaseException as e:
                #             print(e)
                '''
                    页面跳转初始化一次
                '''
                num += 1
                lis = []
                try:
                    mygroup = browser.find_elements_by_class_name("my-group-list")
                    print(mygroup)
                    for i in mygroup:
                        li = i.find_elements_by_tag_name("li")
                        for j in li:
                            lis.append(j)
                    print(lis)
                except BaseException as error:
                    print("\n-----def start_spider-----(except BaseException as error)-----chose qqqun false-----")
                    writer_status = "false"
                if qun_id in self.add_list:
                    continue
                self.add_list.append(qun_id)
                print("\n-----def start_spider-----(open(%(BASE_DIR,path2))-----writer cvs is begin-----")
                print("\n-----def start_spider-----(open(%(BASE_DIR,path2))-----writer cvs is begin2-----")
                with open(r"%s/%s.cvs"%(qqclass_Path,qun_id), 'w', encoding='utf-8-sig', newline='') as f:
                    try:
                        # 表头
                        print("\n-----def start_spider-----(open(%(BASE_DIR,path2))-----writer cvs is error11-----")
                        title = data_list[0].keys()
                        # 声明writer
                        print("\n-----def start_spider-----(open(%(BASE_DIR,path2))-----writer cvs is error22-----", )
                        writer = csv.DictWriter(f, title)
                        # 写入表头
                        print("\n-----def start_spider-----(open(%(BASE_DIR,path2))-----writer cvs is error33-----", )
                        writer.writeheader()
                        # 批量写入数据
                        print("\n-----def start_spider-----(open(%(BASE_DIR,path2))-----writer cvs is error55-----", )
                        writer.writerows(data_list)
                        '''
                            list index out of range
                            批量写入数据这里出现了，写入错误。
                        '''
                    except BaseException as e:
                        print("\n-----def start_spider-----(open(%(BASE_DIR,path2))-----writer cvs is error-----",e)
                    f.close()
                print("\n-----def start_spider-----(open(%(BASE_DIR,path2))-----writer cvs is ok-----")
                print("\n-----def start_spider-----( while len(lis) != num:)-----%s:%s-----" % (len(lis), num))
                # 到这里已经循环了一个群号
                # '''这里可以告知数量
                # --------------------------------------------------------------------------------------------------------
                # ------------------------------------------------这里得更新数据库--------------------------------------------------------
                try:
                    sql = '''insert into users_network_dick values (%s,%s,%s,%s,%s,%s,%s,%s) '''
                    self.manager_sqlx.excute(sql,[None,qun_name,qun_id,self.user_name,0,groupMemberNum,0,time.strftime("%Y-%m-%d %H:%M", time.localtime())])
                except BaseException as e:
                    print("----------**************************--------------",e)
                # -----------------------------------------------------这里得更新数据库---------------------------------------------------
                # --------------------------------------------------------------------------------------------------------
                self.get_user_session_dict["scan_numbers"] = "%s-%s" %(num,len(lis))
                '''
                更新一下数据
                '''
                self.updata_dict()
                '''
                更新一下数据
                '''

            except Exception as e:
                print("\n-----def start_spider-----(except Exception as e)-----while true false-----",e)
                if "refreshed" in str(e):
                    print("\n，#############>>>   Web_loading_false_so_refresh_web_need_sleep_6s", e)
                    browser.refresh()
                    time.sleep(6)
                continue


        if writer_status == "true":
            self.get_user_session_dict["scan_status"] = "finaly-%s" %(self.times)
            '''
            更新一下数据
            '''
            self.updata_dict()
            '''
            更新一下数据
            '''
            browser.quit()
            return True
        else:
            self.get_user_session_dict["scan_status"] = "false"
            '''
            更新一下数据
            '''
            self.updata_dict()
            '''
            更新一下数据
            '''
            browser.quit()
            return False


    def main(self):
        print("\n-----------------------main-----------------------")
        try:
            browser = self.login_spider()
            if browser == False:
                self.get_user_session_dict["scan_status"] = "false"
                '''
                更新一下数据
                '''
                print("\n-----def main-----(if browser == False)-----yes is false-----")
                self.updata_dict()
                '''
                更新一下数据
                '''
                return
            browser = self.switch_spider(browser)
            data_list = self.start_spider(browser)
            if data_list == False:
                self.get_user_session_dict["scan_status"] = "false"
                '''
                更新一下数据
                '''
                print("\n-----def main-----(if browser == False)-----yes is false-----")
                self.updata_dict()
                '''
                更新一下数据
                '''
                return
            try:
                browser.quit()
            except BaseException as e:
                print("\n-----def main-----(except BaseException as e)-----browser.close()-----", e)
        except BaseException as e :
            print("\n-----def main-----(except BaseException as e)-----false-----",e)
            self.get_user_session_dict["scan_status"] = "false"
            '''
            更新一下数据
            '''
            self.updata_dict()
            '''
            更新一下数据
            '''
            try:
                browser.quit()
            except BaseException as e:
                print("\n-----def main-----(except BaseException as e)-----browser.close()-----", e)


if __name__ == '__main__':
    main()
