import os
import json
import requests
from bs4 import BeautifulSoup
import re


GOOGLE_IMAGE = \
    'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'
usr_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
}

SAVE_FOLDER='images'



def main():
    if not os.path.exists(SAVE_FOLDER):
        os.makedirs(SAVE_FOLDER)
    download_images()


lst = [
    "Road direction sign boards",
    "Banner/Advertisements Banners",
    "Government Identity Cards",
    "Aadhar Cards""Notices",
    "Articles",
    "Posters",
    "Book Cover"
]

def download_images():
    # data=input("What are you looking for ?  ")
    data="govt id card"
    data= data if len(data.split(" ")) == 1 else '_'.join(data.split(" "))
    # print(data)
    # n_images=int(input("How Many Images you want?  "))
    n_images=1000


    print('start searching...')
    searchUrl=GOOGLE_IMAGE+'q='+data
    # print(searchUrl)
    response=requests.get(searchUrl,headers=usr_agent)

    # print(response.status_code)
    html=response.text

    soup = BeautifulSoup(html, 'html.parser')
    # file = open("myfile.html",'w') 
    # print(soup)
    # file.write(html)
    # file.close()
    # print(soup)
    results = soup.find_all('img', {'class': 't0fcAb'}, limit=n_images)

    # print(results)

    # file = open("data.txt",'w') 
    # file.write((results))
    # file.close()

    
    # print(results)
   
    imageLinksList=[]
   

    for result in results:
        # print(result)
        imageLinks=(result.get('src'))
        imageLinksList.append(imageLinks)
       
    print(f'found  {len(imageLinks)} images')
    print('start downloading...')

    for i,imageLink in enumerate(imageLinksList):
        response=requests.get(imageLink)

        imageName=SAVE_FOLDER+"/"+data+str(i+1)+'.jpg'
        with open(imageName,'wb') as file:
            file.write(response.content)


    print('Done')

   
    

if __name__ =='__main__':
    main()