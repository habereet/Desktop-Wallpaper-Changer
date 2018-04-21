from urllib.request import urlopen, urlretrieve
from os import path
import datetime
import random

from lib.set_wallpaper_permanent import set_wallpaper_permanent
from lib.debug import print_download_status
from lib.save_image import save_image
from lib.get_url import get_url

activate_search = True

search_terms=[]

date = datetime.date.today()

def picpath_unsplash(file_url, saveDir, SHOW_DEBUG):
    if SHOW_DEBUG:
        print ("Download from:%s" %file_url)

    #Get Current Date as fileName for the downloaded Picture
    picPath_unsplash = saveDir  + 'unsplash' + str(date) + str(random.randint(1,10000000)) + '.jpg'

    picPath_unsplash = get_url ( file_url, picPath_unsplash, SHOW_DEBUG )
    picPath_unsplash = save_image ( picPath_unsplash, SHOW_DEBUG )

    return picPath_unsplash

def change_wp(wp_unsplash, saveDir, SHOW_DEBUG):
    url = 'https://source.unsplash.com/featured/2732x1536'
    
    if activate_search == True:
        choice = int(input('Do you want to search for specific images? 0: No, 1: Yes : '))

        if (choice == 1):
            search_terms = input('Input the search terms (Space separated):').split()
            if len(search_terms) !=0:
                url = url + '?'
                for items in search_terms:
                    url = url + items + ','

    file_url = url
    picPath_unsplash = picpath_unsplash(file_url, saveDir, SHOW_DEBUG)
    set_wallpaper_permanent(picPath_unsplash, SHOW_DEBUG)