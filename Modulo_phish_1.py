from selenium import webdriver
from selenium.webdriver.common.by import By


tb_ele = '//*[@id="shorturl"]'
ans_ele = '//*[@id="r"]/tbody/tr/td[2]/a[1]'
b_ele = '//*[@id="w"]/input'
url = 'https://urlex.org'

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
# inp = 'bit.ly/ShunyaJackpot'
def answer(driver,inp,element):
    answer = [inp]
    que = driver.find_elements(By.XPATH,element)
    for a,q in zip(answer,que):
        q.send_keys(a)
    return driver
def submit(driver,element):
    driver.find_element(By.XPATH,element).click()
    return driver
def expander(inp):
    global driver
    driver.get(url)
    # driver.maximize_window()
    driver = answer(driver,inp,tb_ele)
    driver = submit(driver,b_ele)

    var = driver.find_element(By.XPATH,ans_ele)
    var2 = var.get_attribute('href')

    driver.close()
    return var2
