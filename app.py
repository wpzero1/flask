from flask import Flask, render_template, request
#render_template : HTML관련 템플릿 리턴 형식 임포트 request : 사용자 요청 처리할수 있도록 함
import datetime
import random
from bs4 import BeautifulSoup
import requests #크롤링 관련

app = Flask(__name__)

#print(datetime.today())

@app.route("/")
def hello():
    return render_template("index.html")
    
@app.route("/tibidabo")
def helloys():
    return "Hello, YS."
    
#variable routing - 특정한 변수를 처리하는 방법
@app.route("/hello/<string:name>")
def hellotak(name): #윗줄에서 나온 변수를 넘겨줘야 쓸수 있다.
    return render_template("hello.html", n=name) #변수를 불러오고싶다면 여기서 지정


# https://ide.c9.io/cube/숫자
# 제곱한 결과를 출력
@app.route("/cube/<int:number>")
def cube(number):
    return render_template("cube.html", n=number*number) #여기서 계산을 시켜줘도 되고, html에서 해도 되고.

@app.route("/lunch")
def lunch():
    lunch_box = ["20층", "김밥카페", "양자강", "바스버거", "시골집"]
    #lunch = random.sample(lunch_box, 1) #이건 배열에서 두번째 인자 숫자만큼 뽑아주는 것
    lunch = random.choice(lunch_box) #이렇게 하면 하나만 뽑아준다.
    
    return render_template("lunch.html", lunch=lunch, box=lunch_box)

@app.route("/godtest")
def godtest():
    godtest_box = ["유머감각", "의리", "응큼함", "멍청함", "지능", "존재감"]
    godtest = random.sample(godtest_box, 3)
    
    return render_template("godtest.html", godtest=godtest, result=godtest_box)
    
    
@app.route("/christmas")
def christmas() :
    now = datetime.datetime.now()
    christmas = ""
    if now.day == 25 and now.month == 12:
        return "<h1>메리크리스마스!</h1>"
    else:
        return "아니야"
        return render_template("christmas.html", christmas=christmas)
        
@app.route("/htmlguide")
def html() :
    return render_template("htmlguide.html")

@app.route('/google')
def google():
    return render_template("google.html")
    
@app.route('/opgg')
def opgg():
    return render_template("opgg.html")
    
@app.route('/opggresult')
def opggresult():
    name = request.args.get('q') #request에 있는 arguments를 불러옴. 저쪽에서는 name을 q라는 변수로 받아왔기에 q로 get한다.
    url = "http://www.op.gg/summoner/userName="    
    res = requests.get(url+name)
    bs = BeautifulSoup(res.content, 'html.parser')
    win = bs.select('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins')[0].text
    lose = bs.select('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses')[0].text
    #구글 소스에서 copy-copy selector로 골라낸다.
    
    return render_template("opggresult.html", name=name, win=win, lose=lose) #위에서 받은 변수를 어떻게 넘겨줄 것인지.

        
if __name__ =="__main__":
    app.run(host='0.0.0.0',port=8080)
    