from flask import Flask
import requests
import time
from plyer import notification
app = Flask(__name__)

@app.route('/')
def route_main():
    res = requests.get('https://sports-api.named.com/v1.0/sports/soccer/games/11229398/broadcasts')
    print(res.text)
    
    notification.notify(
        title = 'test test',
        message = '메시지 내용',
        app_name = '테스트앱',
        timeout = 10,
    )
    return '<h1>Hello World!</h1>'

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port="8081")