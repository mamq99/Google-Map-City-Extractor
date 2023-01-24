
import bs4
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# File path with file name
filename = r"C:\downloads\cities2.csv"
file2 = r"C:\downloads\new_city.csv"

# An empty list which would hold the information fetched regarding cities
city_list = []
coordinates = []

# Reading the main dataframe with only four columns: City, lat, long, city_name
main_df = pd.read_csv(filename, encoding= 'unicode_escape', usecols=[0,1,2,3])
df2 = pd.read_csv(file2, usecols=[0,1,2]) #Practice

def read_long_lat():
    
    # created a list for long and lat
    # Taking each longitude & latitude values and saving them in respective variables 
    lat = []
    long = []

    # Setting the range of values that will be saved. "0:" meaning all the data till end
    lat = main_df.loc[0:, 'latitude']
    long = main_df.loc[0:, 'longitude']

    # Setting a total_count variable to set the total number of rows within either list (both lists are identicle)
    total_count=lat.count()
    print(total_count)
    i=0
    while i < total_count:
        coordinates.append("{}+{}".format(lat[i], long[i]))
        i += 1
        if i == total_count:
            break
    return coordinates

def selecting_city_name(i):
    # From multiple lists selected the second list and within it selected the first item that contained city name
    # After that read the string after the first 9 chars i.e., "QP3M+395 "

    city_name = (city_list[1][0][9:])
    main_df.loc[main_df.index[i], 'new_city_name'] = city_name
    main_df.to_csv(file2)
    print(city_name)
 

def parsing_using_browser():

    read_long_lat()

    # Using Selenium we have opened the link in the chrome browser. Options() set web driver options.
    # Web driver is the extension through which we are managing the functionalities(browsing, typing etc) 
    # of chrome from our code 
    options = webdriver.ChromeOptions() 
    options.add_experimental_option("excludeSwitches", ["enable-logging"]) #Ignores the bluetooth adapter error
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=Options()) 
    coord_data = read_long_lat()
    i=0
    for coord in coord_data:
        # Driver.get is Opening the given URL in the browser 
        driver.get('http://maps.google.com/maps?z=12&t=m&q=loc:'+coord)  #35.75264+139.73348
        # Waiting for 5 seconds after the webpage is opened so all the information is loaded.
        time.sleep(5)

        # We are using beautiful soup once the webpage is opened. 
        # Using bs4 we have searched the tag within which our required data is stored.
        soup = bs4.BeautifulSoup(driver.page_source, "html.parser")
        # As we have created a list for the variable city_list we are appending the fetched text into the list
        for city_element in soup.find_all("span", {"class": "DkEaL"}):
            for row in city_element:
                city_list.append((city_element.text).split(","))
                # print(city_list)

        selecting_city_name(i)
        i+=1
        city_list.clear() ##CLEANS THE DATA FOR NEXT CITY AFTER THE CURRENT CITY IS EXTRACTED
    driver.quit()    

parsing_using_browser()


##PROBLEM: Characters are being saved instead of complete strings
##SOLVED: Used Lists and appended the fetched string after spliting them on the delimiter ','

# QUESTION: Why use selenium and beautiful soup4 together?
# ANSWER:   There are certain restrictions within the bs4 like it can't access the elements that are fetched using JS.
#           To overcome that issue, we use selenium as it opens the browser and fetches the elements that are availible
#           only through JavaScript(browser)




