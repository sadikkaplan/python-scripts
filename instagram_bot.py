from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
class Instagram:
    def __init__(self,username,password):
        self.browser=webdriver.Chrome()
        self.username=username
        self.password=password
    def SignIn(self):
        self.browser.get("https://www.instagram.com/accounts/login")
        time.sleep(2)
        emailinput=self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')
        emailinput.send_keys(self.username)
        passinput=self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')
        passinput.send_keys(self.password)
        passinput.send_keys(Keys.ENTER)
        time.sleep(2)

    def followUser(self,username):
        self.browser.get(f"https://www.instagram.com/{username}/")
        time.sleep(2)
        fbtn=self.browser.find_element_by_tag_name("button")
        #fbtn = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[2]/div/span/span[1]/button')
        if fbtn.text=="Takiptesin":
            print("Zaten takip ediyorsun")
        else:
            fbtn.click()

    def getfollower(self,username=None):
        if username is None:
            self.browser.get(f"https://www.instagram.com/{self.username}/")
        else:
            self.browser.get(f"https://www.instagram.com/{username}/")
        time.sleep(2)
        btn=self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        btn.click()
        #self.browser.find_element_by_xpath('//*[@id="f27fbc0e037e7bc"]/div/div/a')
        followers=self.browser.find_element_by_css_selector("div[role=dialog] ul")
        takipciler=followers.find_elements_by_css_selector("li")
        for user in takipciler:
            link=user.find_element_by_css_selector("a").get_attribute("href")
            print(link)


bot=Instagram("Your Accountname","yourpassword")
bot.SignIn()
bot.followUser("user")
bot.getfollower("anotherUser")


