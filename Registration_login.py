import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
driver.maximize_window()

but1=driver.find_element_by_xpath('//*[@id="menu-item-50"]/a')
but1.click()

but2=driver.find_element_by_xpath('//*[@id="reg_email"]')
but2.send_keys('zhenya22.98@mail.ru')

but3=driver.find_element_by_xpath('//*[@id="reg_password"]')
but3.send_keys('evgesha22')

but4=driver.find_element_by_xpath('//*[@id="customer_login"]/div[2]/form/p[3]/input[3]')
but4.click()
driver.quit()


import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
driver.maximize_window()

but1=driver.find_element_by_xpath('//*[@id="menu-item-50"]/a')
but1.click()

but2=driver.find_element_by_xpath('//*[@id="username"]')
but2.send_keys('zhenya22.98@mail.ru')

but3=driver.find_element_by_xpath('//*[@id="password"]')
but3.send_keys('evgesha22')

but4=driver.find_element_by_xpath('//*[@id="customer_login"]/div[1]/form/p[3]/input[3]')
but4.click()
time.sleep(5)

assert driver.find_element_by_xpath('//*[@id="page-36"]/div/div[1]/nav/ul/li[6]/a').text =='Logout'
driver.quit()
