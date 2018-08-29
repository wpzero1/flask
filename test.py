from bs4 import BeautifulSoup
import requests #크롤링 관련

name = "hide on bush" #request에 있는 arguments를 불러옴. 저쪽에서는 name을 q라는 변수로 받아왔기에 q로 get한다.
url = "http://www.op.gg/summoner/userName="    
res = requests.get(url+name)
bs = BeautifulSoup(res.content, 'html.parser')
win = bs.select('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins')[0].text
lose = bs.select('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses')[0].text
#구글 소스에서 copy-copy selector로 골라낸다.

print(win)
print(lose)