import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd


def extract(page):
 
#   headers ={'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56'}
  url=f'https://quera.org/magnet/jobs?page={page}'
  r=requests.get(url)
  
  # driver = webdriver.Chrome('C:\Users\ALI\OneDrive\Desktop\chromedriver.exe')
  # r=driver.get(url)
  soup=BeautifulSoup(r.content,'html.parser')
  return soup


print(extract(1))
def transform(soup):
      for item in soup:
        j=[]
        skills_divs=item.find_all('div', class_="chakra-stack css-5lzoxc e35d97a1")
      
        for skill in skills_divs:
            spans=skill.find_all('span', dir="ltr")
            
            for i in spans:
                
                j.append(i.text)
       
            
        title=item.find('a',class_="chakra-link css-spn4bz").text.strip()
        company_name=item.find('p', class_="chakra-text css-1m52y4d").text.strip()

        job={
            'title':title,
            'company':company_name,
            'skills':j
            
        }
        joblist.append(job)
      return
       


joblist=[]

for i in range(1,18):
    print (f'Getting Page,{i}')
    c= extract(i)
    transform(c)

df=pd.DataFrame(joblist)
print(df.head())
df.to_csv('jobs.csv')

