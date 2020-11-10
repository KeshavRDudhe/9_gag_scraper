import requests
import os
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

path_to_save_files = 'D:\scraper2'

name_of_website_url = 'https://9gag.com/'

storage_url = 'https://img-9gag-fun.9cache.com/photo/'


# import pdb
# pdb.set_trace()


def download_image(url,what_name_to_save,path_to_save_files):          #save image function
    file_extension = url[-10:].split(".")[1]    
    path_to_save_files = path_to_save_files + "\what_name_to_save."
    path_to_save_files = path_to_save_files.replace("what_name_to_save",what_name_to_save)
    f = open(path_to_save_files, 'wb')
    f.write(requests.get(url).content)
    f.close()




os.chdir(path_to_save_files)

saved_image_name_starts_from = ':{\\\\"name\\\\":\\\\"'

start_url_from = '\\'

req = Request(name_of_website_url , headers={'User-Agent': 'Mozilla/5.0'})

webpage = urlopen(req).read()

file_formates = [".webm",".pm4",".webp"] 

urls = []

os.chdir(path_to_save_files)

file_names = os.listdir()

loopThis = str(webpage).split(saved_image_name_starts_from)

for link in loopThis:
    link = link.split(start_url_from)[0]
    url = name_of_website_url+ link
    urls = urls + [url]

urls = list(set(urls))     

print('Total number of sub urls , extracted ',len(urls))

adding_some_extra_urls = ['https://9gag.com/hot','https://9gag.com/trending','https://9gag.com/fresh']

urls = urls + adding_some_extra_urls

remove_texts_from_file_name   = ['100','body']

start_file_name_from          = '\/'

remove_special_signs          = ['\\','/',' ']

image_thumbnails = False



for url in urls:
    
    try:
        
        req = Request(url , headers={'User-Agent': 'Mozilla/5.0'
                                    })
                
        webpage = urlopen(req).read()      
                        
        for file_format in file_formates:

            #print('file_format',file_format)

            loopData = str(webpage).split(file_format)

            loopData = loopData[:-1]#remove last one

            for file_name in loopData:
                

                for remove_text in remove_texts_from_file_name:
                    
                    if remove_text in file_name:
                        continue
                
                    file_name = file_name[-20:]
                    
                    try:
                        file_name = file_name.split(start_file_name_from)[1]
                    except:
                        continue
                        
                    
                    for remove_special_sign in remove_special_signs:
                        file_name = file_name.replace(remove_special_sign,'')
                                            
                    file_name = file_name+file_format
                    
                    url = storage_url+file_name
                        
                                                                
                    if file_name not in file_names:
                        print(file_name)                                                
                        download_image(url,file_name,path_to_save_files)
                        file_names = file_names + [file_name]
                                        
    except Exception as err:
        print(url, err)
        continue
                
        

