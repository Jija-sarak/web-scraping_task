from bs4 import BeautifulSoup
import requests , random , time
from csv import writer
import csv
from datetime import datetime
user = int(input("enter a page number :"))
if user <=14 and user !=0 :
    list1 = ["URL" , "Image Link" , "Title" , "Author" , "Date" , "Location" , "Description"]
    list3 = []
    U = 1
    while U <= user :
        random_sleep = random.randint(1,3)
        time.sleep(random_sleep)
        api = "https://www.ndtv.com/india/page-"+str(U)
        page = requests.get(api)
        soup = BeautifulSoup(page.text,'html.parser')
        main_div = soup.find('div',class_="sp-cn ins_storybody lstng_Pg")
        sub_div = main_div.find_all('div',class_ = "news_Itm")
        for div in sub_div :
            list2 = ["URL" , "Image Link" , "Title" , "Author" , "Date" , "Location" , "Description"]
            img = div.find('div',class_ = "news_Itm-img")
            if img != None:
                image = img.find('a').img["src"]
                list2[1] = image
            Title = div.find('div',class_ = "news_Itm-cont")
            if Title != None:
                A = Title.h2.get_text()
                list2[2] = A
                url = Title.h2.a["href"]
                list2[0] = url
                content = Title.p.get_text()
                list2[6]= content
                author = Title.span.a
                if author != None :
                    list2[3]= author.get_text()
                date = Title.span.get_text().strip()
                presentime = datetime.now()
                sum = ""
                sum1 = ""
                for i in date :
                    if i == '|':
                        sum = ""
                        sum1 = ""
                    else:
                        sum+=i
                        sum1+=i
                    if str(presentime.year) in sum :
                        list2[4] = sum
                        sum = ""
                L = len(list2[4])+1
                list2[5] = sum1[L:] 
                list3.append(list2)
        U+=1
with open('all_story_details.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            i = 0
            while i < len(list3):
                if list3[i][0]==row[0]:
                    del list3[i]
                    break
                i+=1  
if len(list3) != 0 :                    
    with open('all_story_details.csv', 'a', newline='') as f_object:  
        writer_object = writer(f_object)
        writer_object.writerows(list3)  
        f_object.close()

