# Google-Map-City-Extractor
I have created a web scrapper which takes in the longitude and latitude of a city from an excel sheet. It then extracts then name from the google map. It cleans out the whole string and only takes the name.
I had a csv file with city names but they were all gibberish to solve that problem I created this code.

Task:
1. To fetch the cities' names using their coordinates

Process:
1. Opening the Google Map link with static coordinates using selenium.
2. Trying to capture the details of the page using beautiful soup 4.
3. Capture Details using bs4 which are enclosed within a span tag.
4. Once the details are fetched the next process is to split the whole information and discard the unnecessary information.
5. From the line which contains plus coordinates and city name (after splitting), cut the code and only take the city name.
6. Make a dynamic variable which stores these city name(s).
7. Input path and name of the file from which the coordinates will be taken.
8. Store them within the respective variables. (coordinates, filename, & city_list)
9. Make the map link static so the coordinates can be attached as they are fetched from the file using pandas. Once each coordinate goes through this process
   then the next coordinate should be fetched.
10. With each sprint, store the fetched data within a dataframe built using pandas library.
11. Once all the process is done then the dataframe which holds all the fetched information should be outputted to a csv file, new_city.csv.
THIS CONCLUDES THE PROGRAM.

Technology Used:
1. Selenium (to open the site that used javascript)
2. BeautifulSoup4 (To fetch the data from the source of the page(s))
3. Pandas (To read the coordinates from the excel file and write the newly fetched cities names in it)

Sources Used:
1. All Cities coordinates data (a .csv file downloaded online)
2. Visual Studio code
3. Python

NOTE: This my first repository on Github. kinda excited! 
please let me know if there are any errors as there is always room for improvement. ^_^
If you have any better suggestions I am open to those as well. 
