import os
import json
import requests
from bs4 import BeautifulSoup
import re



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
    "Book Cover",
    ""
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
    print(searchUrl)
    try:
        response=requests.get(searchUrl,headers=user_agent)
    except KeyError:
        print('error')
        return

    # print(response.status_code)


    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup)
    # file = open("myfile.txt",'w') 
    # # # print(soup)
    # file.write(str(soup))
    # file.close()
    # print(soup)
    # results = soup.find_all('img', {'class': 't0fcAb'}, limit=n_images)
    results = soup.findAll('img', {'class': 'rg_i Q4LuWd'}, limit=n_images)



    # print(results)

    # file = open("data.txt",'w') 
    # file.write((results))
    # file.close()

    
    # print(results)
   
    imageLinksList=[]
   

    for result in results:
        # print(result)
        try:

            imageLinks=result.get('data-src')
            imageLinksList.append(imageLinks)
        except KeyError:
            continue
       
    print(f'found  {len(imageLinksList)} images')
    print('start downloading...')

    for i,imageLink in enumerate(imageLinksList):
        # print(i)
        if (imageLink == None):
            continue
        else:
            # print(imageLink)
            response=requests.get(imageLink)
           

            imageName=SAVE_FOLDER+"/"+data+str(i+1)+'.jpg'
            with open(imageName,'wb') as file:
                file.write(response.content)


    print('Done')

   
    

if __name__ =='__main__':
    main()