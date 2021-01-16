from bs4 import BeautifulSoup
import requests
from pprint import pprint

res = requests.get("https://localhackday.mlh.io/build#ChallengesD").text
soup = BeautifulSoup(res, 'html.parser')


challenges = soup.select('div.event-title-bg > h3.hero-sub-head')
challenges_desc = soup.select(' div > div > div.event-description.w-richtext > p')



for i in range(len(challenges)):
   pprint({"Title":challenges[i].get_text(),"description":challenges_desc[i].get_text()})
