import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
driver.execute_script("window.scrollTo(0,600)")

book=driver.find_element_by_xpath('//*[@id="text-22-sub_row_1-0-2-0-0"]/div/ul/li/a[1]/img')
book.click()

book1=driver.find_element_by_xpath('//*[@id="product-160"]/div[3]/ul/li[2]/a')
book1.click()

book2=driver.find_element_by_xpath('//*[@id="commentform"]/p[2]/p/span/a[5]')
book2.click()

book3=driver.find_element_by_xpath('//*[@id="author"]')
book3.send_keys('Evgeniy')
book4=driver.find_element_by_xpath('//*[@id="email"]')
book4.send_keys('zhenya22.98@mail.ru')
book5=driver.find_element_by_xpath('//*[@id="comment"]')
book5.send_keys('Nice book!')
book6=driver.find_element_by_xpath('//*[@id="submit"]')
book6.click()

driver.quit()