from warnings import warn
import re
import pandas as pd

from bs4 import BeautifulSoup
from datetime import date, datetime
from IPython.core.display import clear_output
import random
from requests import get
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from time import time
start_time = time()

url = "https://www.creditkarma.com/reviews/personal-loan/single/id/SoFi_Personal_Loans?pg=1"

# this will open up new window with the url provided above
chromerdriver = '/Users/rmorales/Desktop/chromedriver'
driver = webdriver.Chrome(chromerdriver)
driver.get(url)
sleep(5)
# action = ActionChains(driver)

# setting up list for job information
rating = []
review_date = []
review_text = []
review_title = []
is_helpful = []
not_helpful = []

pageCounter = 1
maxPageCount = 36

# Each scroll = 25 results
# ScrollNumber = 1
# for i in range(1, ScrollNumber):
#     # if driver.find_element_by_xpath('/html/body/main/div/section/button').is_displayed():
#     #     driver.find_element_by_xpath(
#     #         '/html/body/main/div/section/button').click()
#     driver.execute_script("window.scrollTo(1,document.body.scrollHeight)")
#     sleep(random.uniform(2.5, 4.9))
while (pageCounter < maxPageCount):
    next_page = 'https://www.creditkarma.com/reviews/personal-loan/single/id/SoFi_Personal_Loans?pg={}'.format(pageCounter + 1)
   
    sleep(5)
    # parsing the visible webpage
    pageSource = driver.page_source
    lxml_soup = BeautifulSoup(pageSource, 'html.parser')
    
    # searching for all job containers
    review_container = lxml_soup.find('div', class_='center pa3')
    
    # no results on page
    no_results_xpath = '/html/body/main/div/div/div/div/div[2]/div[1]/section[2]/div/div/div/div/span'


    if review_container:
        # check for no results, if so, go to next page

        try:
            driver.find_element_by_xpath(no_results_xpath)
            driver.get(next_page) 
            pageCounter += 1
        except NoSuchElementException:
        
            # check if no results in review container
            print('You are scraping information about {} reviews.'.format(len(review_container)))


            # for loop for job title, company, id, location and date posted
            for review in review_container:
                
                # RATING
                svg_container = review.find("div", class_="dib mr2")
                star_count = 0
                for svg in svg_container:
                    classes = svg.attrs['class']
                    if 'ck-primary-50' in classes: 
                        star_count += 1
                rating.append(star_count)
            
                # DATE
                date_value = review.find('span', class_='dib f5 lh-copy').text
                review_date.append(date_value)

                #REVIEW TITLE
                title_value = review.find('h5', class_='f4 lh-title ck-black-90 mb2 mt3').text
                review_title.append(title_value)

                # REVIEW TEXT
                review_value = review.find('p', class_='f4 lh-copy ma0').text
                review_text.append(review_value)

                # IS HELPFUL
                upvotes = review.find('div', title='Helpful').text
                is_helpful.append(upvotes)

                # NOT HELPFUL
                downvotes = review.find('div', title='Not Helpful').text
                not_helpful.append(downvotes)

            # next_page = '//div[@data-testid="reviews__pagination-next-page"]'
            # # /html/body/main/div/div/div/div/div[2]/div[1]/div[7]/div[3]'
            # driver.find_element_by_xpath(next_page).click()
            driver.get(next_page) 

            pageCounter += 1
    else: 
        driver.get(next_page) 
        pageCounter += 1

        # # posting date
        # post_dates = job.select_one('time')['datetime']
        # post_date.append(post_dates)


# to check if we have all information
print(len(rating))
print(len(review_date))
print(len(review_text))
print(len(review_title))
print(len(is_helpful))
print(len(not_helpful))


# creating a dataframe
review_data = pd.DataFrame({'Rating': rating,
                         'Date': review_date,
                         'Review Text': review_text,
                         'Review Title': review_title,
                         'Is Helpful': is_helpful,
                         'Not Helpful': not_helpful
                         })

# cleaning description column
review_data['Review Text'] = review_data['Review Text'].str.replace('\n', ' ')
review_data.drop_duplicates(subset=None, inplace=True)

print(review_data.info())
review_data.head()

review_data.to_csv('CK_Reviews_SoFi_9-7-2021.csv', index=0)
