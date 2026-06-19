import threading
import requests
import bs4

from bs4 import BeautifulSoup

urls={
    'https://docs.langchain.com/oss/python/build-overview',
    'https://docs.langchain.com/langsmith/test-overview',
    'https://smith.langchain.com/settings'
}

def fetch_content(url):
    response = requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f"fetched { len(soup.text)} characters from {url}")

threads=[]

for url in urls:
    thread=threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()      
    
for thread in threads:
    thread.join()

print("finished fetching all urls" )