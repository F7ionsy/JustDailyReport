import requests
import json
import time

#提交日期 tbrq
tbrq = time.strftime("%Y-%m-%d", time.localtime())
print(tbrq)
#提交时间 tjsj
tjsj = time.strftime("%Y-%m-%d %H:%M", time.localtime())
print(tjsj)
# 登陆并返回session
def getSession():
    params = {
        'login_url': 'http://ehall.just.edu.cn/default/work/jkd/jkxxtb/jkxxcj.jsp',
        'username': '',
        'password': ''
    }

    cookies = {}
    # 借助上一个项目开放出来的登陆API，模拟登陆
    res = requests.post('http://www.zimo.wiki:8080/wisedu-unified-login-api-v1.0/api/login', params, verify=False)
    # print(res.text)
    # cookieStr = 'acw_tc=2f624a1e16087946934723466e2c6d88780f6a06bd3945819decfb20280209; MOD_AUTH_CAS=95faece2-d030-4cd5-84d1-c66a5e6587c4'
    cookieStr = str(res.json()['cookies'])
    print(cookieStr)
    if cookieStr == 'None':
        print(res.json())
        return None

    # 解析cookie
    for line in cookieStr.split(';'):
        name, value = line.strip().split('=', 1)
        cookies[name] = value
    session = requests.session()
    session.cookies = requests.utils.cookiejar_from_dict(cookies)
    return session
#提交信息
def PostDaily():
    url='http://ehall.just.edu.cn/default/work/jkd/jkxxtb/com.sudytech.portalone.base.db.saveOrUpdate.biz.ext'
    #在data等号后填写你抓包来的字段。
    data=
    headers={
        'Referer': 'http://ehall.just.edu.cn/default/work/jkd/jkxxtb/jkxxcj.jsp',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75'
    }
    content = session.post(url, json=data, headers=headers)
    return content.text

def Json():
    json_str = json.dumps(PostDaily())
    # 将 JSON 对象转换为 Python 字典
    data2 = json.loads(json.loads(json_str))
    return data2

def Server():
    api = "https://sc.ftqq.com/你的key.send"
    title = "江苏科技大学" + " " + tbrq + " " + "打卡任务简报"
    content = "提交状态：  " + Json()["result"] + '   (1表示提交成功，其他表示失败)' \
              + '\n' + '\n' + "姓名：  " + Json()["resultEntity"]["sqrmc"] \
              + '\n' + '\n' + "性别：  " + Json()["resultEntity"]["xb"] + '   (1表示男，2表示女)' \
              + '\n' + '\n' + "学号：  " + Json()["resultEntity"]["gh"] \
              + '\n' + '\n' + "身份证号：  " + Json()["resultEntity"]["sfzh"] \
              + '\n' + '\n' + "联系电话：  " + Json()["resultEntity"]["lxdh"] \
              + '\n' + '\n' + "今晨体温：  " + Json()["resultEntity"]["tw"] + "℃" \
              + '\n' + '\n' + "昨晚体温：  " + Json()["resultEntity"]["zwtw"] + "℃" \
              + '\n' + '\n' + "籍贯省：  " + Json()["resultEntity"]["jgshen"] \
              + '\n' + '\n' + "籍贯市：  " + Json()["resultEntity"]["jgshi"] \
              + '\n' + '\n' + "今日居住地详细地址：  " + Json()["resultEntity"]["jrjzdxxdz"] \
              + '\n' + '\n' + '提交时间:    ' + tjsj
    data = {
        "text": title,
        "desp": content
    }
    req = requests.post(api, data=data)


session = getSession()
res = session.get('http://ehall.just.edu.cn/default/work/jkd/jkxxtb/jkxxcj.jsp')
PostDaily()
Json()
Server()



