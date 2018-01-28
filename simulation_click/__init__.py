from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from pip._vendor.retrying import retry
import time


# //*[@id="scripteditor-container"]/div/div[1]/div/div[2]/button[2]/span[1]


@retry(wait_random_min=1000, wait_random_max=2000)
def find_element_with_retry(driver, type, content):
    option = {
        "id": driver.find_element_by_id,
        "name": driver.find_element_by_name,
        "xpath": driver.find_element_by_xpath
    }
    return option.get(type)(content)


driver = webdriver.Chrome('./chromedriver')
driver.get('https://10.29.42.18')

elem_user = driver.find_element_by_name("username")
elem_user.send_keys("qlik-loader\yidxue")
elem_pwd = driver.find_element_by_name("pwd")
elem_pwd.send_keys("Cisco@2017")
elem_pwd.send_keys(Keys.RETURN)
time.sleep(5)

login_form = driver.find_element_by_xpath(
    "//*[@id=\"q-route-area\"]/div/div[2]/div/div/div/div/ul/li[16]/div/div[3]/div[1]/div")
ActionChains(driver).context_click(login_form).perform()

login_form = driver.find_element_by_xpath(
    "//*[@id=\"show-service-popup-dialog\"]/div/div/div/div/ng-transclude/ul/li[1]")
login_form.click()

find_element_with_retry(driver,'id','confirmButton').click()

#
# login_form = driver.find_element_by_id("confirmButton")
# login_form.click()




# time.sleep(15)
# lf = driver.find_element_by_xpath("//*[@id=\"confirmButton\"]")
# lf.click()


# assert "baidu" in driver.title
# driver.close()
# driver.quit()
