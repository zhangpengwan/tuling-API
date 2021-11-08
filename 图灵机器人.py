import requests
import json
userid = str('Eliza')
apikey = str('ec3')

def robot(content):
    api = r'http://openapi.tuling123.com/openapi/api/v2'

    data = {
        "perception": {
            "inputText": {
                "text": content
            }
        },
        "userInfo": {
            "apiKey": '4670f9d766704929b7983312808cdfa7',
            "userId": userid,
        }
    }

    jsondata = json.dumps(data)

    response = requests.post(api, data=jsondata)

    robot_res = json.loads(response.content)

    print(robot_res["results"][0]['values']['text'])


for x in range(100):
    content = input("talk:")

    robot(content)
    if x == 100:
        break

while True:
    content = input("talk:")

    robot(content)
    if content == 'bye':

        break






#网课https://tiku.gjzhan.cn/gongzhonghao/wangke.php
#123456