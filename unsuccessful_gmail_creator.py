from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import random
#def ClickableWait(driver, time, finder, finder_value):
#    return WebDriverWait(mydriver, time).until(expected_conditions.element_to_be_clickable(By.finder), finder_value)
mydriver = webdriver.Firefox()
mydriver.maximize_window()
mydriver.get("https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=http%3A%2F%2Fmail.google.com%2Fmail%2F%3Fpc%3Dcarousel-about-en&flowName=GlifWebSignIn&flowEntry=SignUp")
#createAccount = mydriver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/content/span")
#createAccount.click()
firstName = mydriver.find_element_by_xpath('//*[@id="firstName"]')
firstName.send_keys("some")
lastName = mydriver.find_element_by_xpath('//*[@id="lastName"]')
x =random.randint(1000, 10000)
print "random = ", x
lastName.send_keys("one")
username = mydriver.find_element_by_xpath('//*[@id="username"]')
username.send_keys("someonesgmailaccount_" + str(x))
pwd = WebDriverWait(mydriver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div[2]/div/div[1]/div[3]/div[1]/div[1]/div/div/div[1]/div/div[1]/input')))
pwd.send_keys("somerandompassword@123")
password = "somerandompassword@123"
#pwd = mydriver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div[2]/div/div[1]/div[3]/div[1]/div[1]/div/div/div[1]')
#pwd.send_keys("hello12345")
confirmPwd = WebDriverWait(mydriver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div[2]/div/div[1]/div[3]/div[1]/div[3]/div/div/div[1]/div/div[1]/input')))
confirmPwd.send_keys("xX_420BlaZeIt_Xx"+Keys.RETURN)
phoneNumber = WebDriverWait(mydriver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="phoneNumberId"]')))
phoneNumber.send_keys("9381319341" + Keys.RETURN)
verificationCode = raw_input()
vCode = WebDriverWait(mydriver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="code"]')))
vCode.send_keys(verificationCode + Keys.RETURN)
inputDate = input("Enter your date of birth: ")
date = mydriver.find_element_by_xpath('//*[@id="day"]')
date.send_keys(inputDate)
inputMonth = raw_input("Enter one of the following months:\nJanuary\nFebruary\nMarch\nApril\nMay\nJune\nJuly\nAugust\nSeptember\nOctober\nNovember\nDecember\n ")
monthID = mydriver.find_element_by_id('month')
for monthOption in monthID.find_elements_by_tag_name('option'):
    if(monthOption.text == inputMonth):
        monthOption.click()
        break

inputYear = input("Enter year of birth(18+ only): ")
yearID = mydriver.find_element_by_id("year")
yearID.send_keys(inputYear)
inputGender = raw_input("Enter one of the following genders: \nFemale\nMale\nRather not say\nCustom\n ")
genderSelect = mydriver.find_element_by_id('gender')
for genderOption in genderSelect.find_elements_by_tag_name('option'):
    if(genderOption.text == inputGender):
        genderOption.click()
        break
mydriver.find_element_by_id("personalDetailsNext").click()
skip = mydriver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div[2]/button')
skip.click()
scroll = mydriver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div[2]/div/div/div/div[1]/div/div/content/span/svg')
scroll.click()
scroll.click()
try:
    scroll.click()
except:
    pass
Agree = mydriver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div[2]/div/div/div/div[2]/div/div[1]/div/content')
Agree.click()
pwdVerify = mydriver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/form/content/section/div/content/div[2]/div/div[1]/div/div[1]/input')
pwdVerify.send_keys(password)



#confirmPwd = mydriver.find_element_by_xpath('//*[@id="confirm-passwd"]')