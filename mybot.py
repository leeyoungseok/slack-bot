import requests
from slack_sdk import WebClient
from datetime import datetime
import cnu_crawl

# slack 토큰
myToken = ""

# slack 챗 봇
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
                             headers={"Authorization": "Bearer " + token},
                             data={"channel": channel, "text": text})
    print(response.text)

def slack_post(message):
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
    config = cnu_crawl.config_read()
    myToken = config['TOKEN']
    menu = cnu_crawl.web_crawl("취업지원회관")
    slack_post(menu)
    menu = cnu_crawl.web_crawl("제3학생회관")
    slack_post(menu)
