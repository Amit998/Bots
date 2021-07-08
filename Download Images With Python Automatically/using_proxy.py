import os
import json
import requests
from bs4 import BeautifulSoup
import re
from proxycrawl.proxycrawl_api import ProxyCrawlAPI
import api_key


GOOGLE_IMAGE = \
    'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'
user_agent = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
} #write: 'my user agent' in browser to get your browser user agent details


SAVE_FOLDER='google_images'


def download_images(SAVE_FOLDER,data):
    data= data if len(data.split(" ")) == 1 else '+'.join(data.split(" "))
    n_images=1000
    print('start searching...')
    # print(data)
    searchUrl=GOOGLE_IMAGE+'q='+data
    print(searchUrl)
    api = ProxyCrawlAPI({ 'token': api_key.API_KEY_JS})
    try:
        response = api.get(searchUrl, {'scroll': 'true', 'scroll_interval': '60', 'ajax_wait': 'true'})
    except KeyError:
        print("error")
    


    if(response['status_code']== 200):

        soup = BeautifulSoup(response['body'], 'html.parser')
       
        results = soup.findAll('img', {'class': 'rg_i Q4LuWd'}, limit=n_images)
        imageLinksList=[]
        for result in results:
           
            try:
                imageLinks=result.get('data-src')
                imageLinksList.append(imageLinks)
            except KeyError:
                continue
        
        print(f'found  {len(imageLinksList)} images')

        print('start downloading...')

        for i,imageLink in enumerate(imageLinksList):
            
            if (imageLink == None):
                continue
            else:
                response=requests.get(imageLink)
                print(response.status_code,"status code"+"id no "+ f'{(i+1)}'+" name  "+data)

                imageName=SAVE_FOLDER+"/"+data+"_"+str(i+1)+'.jpg'
                with open(imageName,'wb') as file:
                    file.write(response.content)


        print('Done')

def new_main(SAVE_FOLDER,data):
    if not os.path.exists(SAVE_FOLDER):
        os.makedirs(SAVE_FOLDER)
    download_images(SAVE_FOLDER,data)

lst = [
    # "notice",
    "notice sample",
    "school notice",
    "letter format notice",
    "personal reason resignation letter",
    # "Road direction sign boards",
    # "Advertisements Banners",
    # "Government Identity Cards",
    # "Aadhar Cards Notices",
    # "Posters",
    # "Book Cover",
 
]


for l in lst:
    SAVE_FOLDER='google_images/'+l
    new_main(SAVE_FOLDER,l)








   
    


