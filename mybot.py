import requests
from slack_sdk import WebClient
from datetime import datetime


# slack 챗 봇
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
                             headers={"Authorization": "Bearer " + token},
                             data={"channel": channel, "text": text})
    print(response.text)


# slack 토큰
myToken = "xoxb-2841907287282-2868284211216-fEZY3L2l2jt5rRebcfNXjogK"


# message로 받은 인자를 파이썬 쉘과 슬랙 #채널이름 에 동시에 출력한다
def dbgout(message):
    print(datetime.now().strftime('[%m/%d %H:%M:%S]'), message)
    strbuf = datetime.now().strftime('[%m/%d %H:%M:%S] ') + message
    post_message(myToken, "#일반", strbuf)


def bot_test(message):
    slack_token = myToken
    client = WebClient(token=slack_token)

    response = client.chat_postMessage(
        channel="#일반",
        text="Hello silently from your app! :tada:")

if __name__ == '__main__':
    dbgout("Hello World by bot python testing...")
    #bot_test("hello world")
