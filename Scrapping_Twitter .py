#!/usr/bin/env python
# coding: utf-8

# In[2]:


from selenium import webdriver       #Used for validation of websites
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException


#You can change the parameters you want to extract based on your requirements 
def twitter_data(element):
    username = element.find_element(By.XPATH , './/span').text
    id_username = element.find_element(By.XPATH , './/span[contains(text(),"@")]').text
    try:
        date = element.find_element(By.XPATH, './/time').get_attribute('datetime')
    except NoSuchElementException:
        return
    comment = element.find_element(By.XPATH , './/div[@data-testid = "tweetText"]').text
    num_reply = element.find_element(By.XPATH , './/div[@data-testid = "reply"]').text
    num_retweet = element.find_element(By.XPATH , './/div[@data-testid = "retweet"]').text
    num_like = element.find_element(By.XPATH , './/div[@data-testid = "like"]').text
    
    tweet_info = (username,id_username,date,comment,num_reply,num_retweet,num_like)
    return tweet_info


# Link for chrome driver (https://chromedriver.chromium.org/downloads)z
# Link for Firefox driver (https://github.com/mozilla/geckodriver/releases)
# Link for Internet explorer driver (https://github.com/SeleniumHQ/selenium/wiki/InternetExplorerDriver) 
#Link for Microsoft Edge driver (https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

#Replace webdriver.Chrome with respective web browser (webdriver.Firefox , webdriver.Edge etc.)

#Insert the path for the driver 
driver = webdriver.Chrome(executable_path = 'CHROME DRIVER PATH LOCALLY')

#Try to increase the sleep time if you are facing loading issues with the code 
driver.get('https://twitter.com/i/flow/login')

time.sleep(5)

# Enter your Twitter ID here

driver.find_element(By.XPATH , '//input[@name ="text"]').send_keys('twitter_Id') 
driver.find_element(By.XPATH , '//input[@name ="text"]').send_keys(Keys.RETURN)

time.sleep(3)


#Enter the password here
driver.find_element(By.XPATH , '//input[@name = "password"]').send_keys('password')
driver.find_element(By.XPATH , '//input[@name = "password"]').send_keys(Keys.RETURN)

time.sleep(5)

#Enter any hashtag
driver.find_element(By.XPATH , '//input[@data-testid = "SearchBox_Search_Input"]').send_keys('#hashtag') 
driver.find_element(By.XPATH , '//input[@data-testid = "SearchBox_Search_Input"]').send_keys(Keys.RETURN)

time.sleep(5)

driver.find_element(By.LINK_TEXT ,'Latest').click()

tweet_data = []
last_page = driver.execute_script("return window.pageYOffset;")
reach_last = True

while reach_last:
    all_elements = driver.find_elements(By.XPATH, '//div[@class = "css-1dbjc4n r-1iusvr4 r-16y2uox r-1777fci r-kzbkwu"]')
    for ele in all_elements:
        t_data = twitter_data(ele)
        if t_data:
            tweet_data.append(t_data)
   
    try_scrolling = 0
    while True:
        
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        time.sleep(3)
        current_page = driver.execute_script("return window.pageYOffset;")
        if last_page == current_page:
            try_scrolling = try_scrolling + 1
            
            if try_scrolling >= 3:
                reach_last = False
                break
            else:
                time.sleep(5)
        else:
            last_page = current_page
            break
            
            
# All the information will be stored in variable tweet_data


# In[3]:





# In[ ]:





# In[ ]:





# In[ ]:




