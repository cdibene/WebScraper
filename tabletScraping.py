#use your computer's native csv viewer (Excel, Numbers, etc) to view the csv
#look perfectly formatted not viewing the csv in VSCode
import requests
from bs4 import BeautifulSoup
#allows us to write to CSV files
from csv import writer

#get request for the url
#response variable 
response = requests.get('https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets')
#intialize the variable but this time passing in the response variable
#this will grab the webpage 
soup = BeautifulSoup(response.text,'html.parser')

#all listing cards
tablets = soup.findAll(class_='thumbnail')

#can be any csv name but the 'w' allows you to write to the csv file
with open('tablets.csv','w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Description', 'Reviews']
    #csv writer has a built in method to write to rows
    #passing in the headers
    csv_writer.writerow(headers)


    #for all of the tablets
    for tablet in tablets:
        #find a description and replaces the new lines with nothing
        description = tablet.find(class_='description').get_text().replace('\n','')
        #finding the ratings
        reviews = tablet.find(class_='ratings').get_text().replace('\n','')
        #printing to test before putting into csv
        #print(description, reviews)
        #writing a list with all the variables working with
        csv_writer.writerow([description, reviews])
    


