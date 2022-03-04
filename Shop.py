# import time
# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.get("http://practice.automationtesting.in/")
# driver.maximize_window()
#
# but1=driver.find_element_by_xpath('//*[@id="menu-item-50"]/a')
# but1.click()
#
# but2=driver.find_element_by_xpath('//*[@id="username"]')
# but2.send_keys('zhenya22.98@mail.ru')
#
# but3=driver.find_element_by_xpath('//*[@id="password"]')
# but3.send_keys('evgesha22')
#
# but4=driver.find_element_by_xpath('//*[@id="customer_login"]/div[1]/form/p[3]/input[3]')
# but4.click()
# time.sleep(3)
#
# but5=driver.find_element_by_xpath('//*[@id="menu-item-40"]/a')
# but5.click()
#
# but6=driver.find_element_by_xpath('//*[@id="content"]/ul/li[3]/a[1]/h3')
# but6.click()
#
# assert driver.find_element_by_xpath('//*[@id="product-181"]/div[2]/h1').text=='HTML5 Forms'
# driver.quit()


# import time
# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.get("http://practice.automationtesting.in/")
# driver.maximize_window()
#
# but1=driver.find_element_by_xpath('//*[@id="menu-item-50"]/a')
# but1.click()
#
# but2=driver.find_element_by_xpath('//*[@id="username"]')
# but2.send_keys('zhenya22.98@mail.ru')
#
# but3=driver.find_element_by_xpath('//*[@id="password"]')
# but3.send_keys('evgesha22')
#
# but4=driver.find_element_by_xpath('//*[@id="customer_login"]/div[1]/form/p[3]/input[3]')
# but4.click()
# time.sleep(3)
#
# but5=driver.find_element_by_xpath('//*[@id="menu-item-40"]/a')
# but5.click()
#
# but6=driver.find_element_by_xpath('//*[@id="woocommerce_product_categories-2"]/ul/li[2]/a')
# but6.click()
#
# assert len(driver.find_elements_by_css_selector(".products > li")) == 3
# driver.quit()

#
# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# driver=webdriver.Chrome()
# driver.get("http://practice.automationtesting.in/")
# driver.maximize_window()
# but1=driver.find_element_by_xpath('//*[@id="menu-item-50"]/a')
# but1.click()
#
# but2=driver.find_element_by_xpath('//*[@id="username"]')
# but2.send_keys('zhenya22.98@mail.ru')
#
# but3=driver.find_element_by_xpath('//*[@id="password"]')
# but3.send_keys('evgesha22')
#
# but4=driver.find_element_by_xpath('//*[@id="customer_login"]/div[1]/form/p[3]/input[3]')
# but4.click()
# time.sleep(3)
#
# shop=driver.find_element_by_xpath('//*[@id="menu-item-40"]/a')
# shop.click()
#
# sort_sel=driver.find_element_by_xpath('//*[@id="content"]/form/select/option[1]')
# sort_sel_znach=sort_sel.get_attribute('selected')
# if sort_sel_znach is not None: print('Выбрана сортировка по умолчанию')
# time.sleep(2)
#
# selector_=driver.find_element_by_xpath('//*[@id="content"]/form/select')
# selector=Select(selector_)
# selector.select_by_value('price-desc')
# time.sleep(2)
# sort_sel=driver.find_element_by_xpath('//*[@id="content"]/form/select/option[6]')
# sort_sel_znach=sort_sel.get_attribute('selected')
# if sort_sel_znach is not None: print('Выбрана сортировка цена: высокая--низкая')
# driver.quit()


# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.get("http://practice.automationtesting.in/")
# driver.maximize_window()
# but1=driver.find_element_by_xpath('//*[@id="menu-item-50"]/a')
# but1.click()
#
# but2=driver.find_element_by_xpath('//*[@id="username"]')
# but2.send_keys('zhenya22.98@mail.ru')
#
# but3=driver.find_element_by_xpath('//*[@id="password"]')
# but3.send_keys('evgesha22')
#
# but4=driver.find_element_by_xpath('//*[@id="customer_login"]/div[1]/form/p[3]/input[3]')
# but4.click()
# time.sleep(3)
#
# shop=driver.find_element_by_xpath('//*[@id="menu-item-40"]/a')
# shop.click()
#
# book=driver.find_element_by_xpath('//*[@id="content"]/ul/li[1]/a[1]/h3')
# book.click()
#
# cena1=driver.find_element_by_xpath('//*[@id="product-169"]/div[2]/div[1]/p/del/span')
# cena2=driver.find_element_by_xpath('//*[@id="product-169"]/div[2]/div[1]/p/ins/span')
# cena1_t=cena1.text
# cena2_t=cena2.text
# assert cena1_t == "₹600.00"
# assert cena2_t == "₹450.00"
#
# progress_bar = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#product-169 > div.images')))
# but1=driver.find_element_by_css_selector('#product-169 > div.images').click()
#
# close_b=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'body > div.pp_pic_holder.pp_woocommerce > div.pp_content_container > div > div > div > div.pp_fade > div.pp_details > a')))
# but2=driver.find_element_by_css_selector('body > div.pp_pic_holder.pp_woocommerce > div.pp_content_container > div > div > div > div.pp_fade > div.pp_details > a').click()
# driver.quit()


#
# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.get("http://practice.automationtesting.in/")
# driver.maximize_window()
# but1=driver.find_element_by_xpath('//*[@id="menu-item-50"]/a')
# but1.click()
#
# but2=driver.find_element_by_xpath('//*[@id="username"]')
# but2.send_keys('zhenya22.98@mail.ru')
#
# but3=driver.find_element_by_xpath('//*[@id="password"]')
# but3.send_keys('evgesha22')
#
# but4=driver.find_element_by_xpath('//*[@id="customer_login"]/div[1]/form/p[3]/input[3]')
# but4.click()
# time.sleep(3)
#
# shop=driver.find_element_by_xpath('//*[@id="menu-item-40"]/a')
# shop.click()
#
# add_book=driver.find_element_by_xpath('//*[@id="content"]/ul/li[4]/a[2]')
# add_book.click()
# time.sleep(2)
# text2=(driver.find_element_by_xpath('//*[@id="wpmenucartli"]/a/span[2]')).text
# assert text2=='₹180.00'
# text1=(driver.find_element_by_xpath('//*[@id="wpmenucartli"]/a/span[1]')).text
# assert text1=='1 Item'
#
# corzina=(driver.find_element_by_xpath('//*[@id="wpmenucartli"]')).click()
#
# total = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH,'//*[@id="page-34"]/div/div[1]/form/table/tbody/tr[1]/td[6]/span'),"₹180.00"))
#
# subtotal = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH,'//*[@id="page-34"]/div/div[1]/div/div/table/tbody/tr[1]/td/span'),"₹180.00"))
# driver.quit()


# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.get("http://practice.automationtesting.in/")
# driver.maximize_window()
#
# shop=driver.find_element_by_xpath('//*[@id="menu-item-40"]/a')
# shop.click()
#
# add_book1=driver.find_element_by_xpath('//*[@id="content"]/ul/li[4]/a[2]')
# add_book1.click()
# time.sleep(1)
# add_book2=driver.find_element_by_xpath('//*[@id="content"]/ul/li[5]/a[2]')
# add_book2.click()
# time.sleep(1)
#
# korzina=driver.find_element_by_xpath('//*[@id="wpmenucartli"]/a')
# korzina.click()
# time.sleep(1)
# del_item1=driver.find_element_by_xpath('//*[@id="page-34"]/div/div[1]/form/table/tbody/tr[1]/td[1]/a')
# del_item1.click()
# time.sleep(3)
# otmena_del=driver.find_element_by_xpath('//*[@id="page-34"]/div/div[1]/div[1]/a')
# otmena_del.click()
#
# vvod=driver.find_element_by_xpath('//*[@id="page-34"]/div/div[1]/form/table/tbody/tr[2]/td[5]/div/input')
# vvod_atr=vvod.get_attribute('value')
# vvod.set_attribute('value','3')



