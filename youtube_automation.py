import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

mydriver = webdriver.Firefox()  #Opens Firefox browser 
mydriver.maximize_window() #Maximizes the window

#uBlockExtension= '/home/aravindv/.mozilla/firefox/39r924ap.default/extensions/{2b10c1c8-a11f-4bad-fe9c-1c11e82cac42}.xpi'
#identifier = mydriver.install_addon(uBlockExtension, temporary=True)
#mydriver.uninstall_addon(identifier) #to uninstall the addon
#First, uBlock should be installed in a regular Firefox browser.
#Path and .xpi file name may not be same for other devices, so it should be changed accordingly after previous step

#Function to go to YouTube Homepage
def YouTubeHomepage(driver):
    driver.get("https://www.youtube.com")  

YouTubeHomepage(mydriver)

#Function to Sign In to YouTube after opening youtube homepage
def YouTubeSignIn(driver):
    mydriver.implicitly_wait(15)  #To load all the elements
    time.sleep(1.5)
    sign_in = driver.find_element_by_link_text("SIGN IN")
    sign_in.click()
    time.sleep(1.5)
    gmail_id = mydriver.find_element_by_name('identifier')
    username = raw_input("Enter your Gmail ID: ")  #Enter gmail ID
    gmail_id.send_keys(str(username))
    time.sleep(0.5)
    gmail_id.send_keys(Keys.RETURN)
    time.sleep(1)
    pwd = WebDriverWait(mydriver, 10).until(expected_conditions.element_to_be_clickable((By.NAME, "password")))
    passwd = raw_input("Enter the corresponding password: ")  #Enter password
    pwd.send_keys(passwd + Keys.RETURN)
    time.sleep(1)

YouTubeSignIn(mydriver)

#Toggles Dark Mode after signing in
def toggleDarkMode(driver):
    time.sleep(1.5)
    avatar = driver.find_element_by_id("avatar-btn")
    avatar.click()
    accountName = str(driver.find_element_by_id('account-name').text)
    print "Signed In as: " + accountName
    time.sleep(1.5)
    darkModeOption = driver.find_element_by_class_name('style-scope ytd-toggle-theme-compact-link-renderer')
    darkModeOption.click()
    time.sleep(1.5)
    enable = driver.find_element_by_id("toggleButton")
    enable.click()
    print "Toggled Dark Mode"
    time.sleep(1.5)
    back = mydriver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[2]/ytd-simple-menu-header-renderer/ytd-button-renderer/a')
    back.click()
    time.sleep(0.5)
    avatar.click()
    #YThomepage(driver)
    time.sleep(1.5)

toggleDarkMode(mydriver)

#Two lists that store channel names to keep track of subscribed and unsubscibed channels
subbedChannels = []
unsubbedChannels = []

#Function to subscribe to a channel
def subscribeChannel(driver, link):
    driver.get(link)
    subscribeButton = driver.find_element_by_xpath("/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/div[2]/ytd-c4-tabbed-header-renderer/app-header-layout/div/app-header/div[2]/div[2]/div/div[1]/div[4]/ytd-subscribe-button-renderer/paper-button")
    name = str((driver.find_element_by_xpath('//*[@id="channel-title"]')).text)
    if name not in subbedChannels:
        subbedChannels.append(name)
    if name in unsubbedChannels:
        unsubbedChannels.remove(name)
    if(subscribeButton.get_attribute("subscribed") != ""):
        time.sleep(1.5)
        subscribeButton.click()
        print "Subscribed to " + name
        time.sleep(1.5)
    else:
        print "Already Subscribed to " + name
        time.sleep(1.5)
    
#Function to unsubscribe from a channel
def unsubscribeChannel(driver, link):
    driver.get(link)
    subscribeButton = driver.find_element_by_xpath("/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/div[2]/ytd-c4-tabbed-header-renderer/app-header-layout/div/app-header/div[2]/div[2]/div/div[1]/div[4]/ytd-subscribe-button-renderer/paper-button")
    name = str((driver.find_element_by_xpath('//*[@id="channel-title"]')).text)
    if name not in unsubbedChannels:
        unsubbedChannels.append(name)
    if name in subbedChannels:
        subbedChannels.remove(name)
    if(subscribeButton.get_attribute("subscribed") == ""):
        time.sleep(1.5)
        subscribeButton.click()
        time.sleep(1.5)
        confirm = driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/paper-dialog/yt-confirm-dialog-renderer/div[2]/div/yt-button-renderer[2]/a')
        confirm.click()
        print "Unsubscribed from " + name
        time.sleep(1.5)
    else:
        print "Already Unsubscribed from " + name
        time.sleep(1.5) 

#Few channels to subscribe and unsubscribe. More can be added by passing the channel url to the function.
subscribeChannel(mydriver, "https://www.youtube.com/user/PewDiePie")
unsubscribeChannel(mydriver,"https://www.youtube.com/user/tseries" )
subscribeChannel(mydriver, "https://www.youtube.com/channel/UC6nSFpj9HTCZ5t-N3Rm3-HA")
subscribeChannel(mydriver, 'https://www.youtube.com/user/2CELLOSlive')
unsubscribeChannel(mydriver, "https://www.youtube.com/user/tseries")
subscribeChannel(mydriver, "https://www.youtube.com/channel/UCCq1xDJMBRF61kiOgU90_kw")
unsubscribeChannel(mydriver, "https://www.youtube.com/channel/UCfM3zsQsOnfWNUppiycmBuw")

#prints subscribed channels
print "Subscribed channels: "
for chn in subbedChannels:
    print chn
#prints unsubscribed channels
print "\nUnsubscribed channels: "
for chn in unsubbedChannels:
    print chn

#Function to search an item on youtube
def YouTubeSearch(driver, search_item):
    YouTubeHomepage(driver)
    query = WebDriverWait(mydriver, 10).until(expected_conditions.element_to_be_clickable((By.NAME, "search_query")))
    query.send_keys(str(search_item))
    time.sleep(1)
    query.send_keys(Keys.RETURN)

#Function that scrapes top 10 results for a given query and returns a tuple which has information about each result
def topResults(driver, search_item):
    YouTubeSearch(driver, search_item)
    top = []
    channel = []
    views = []
    uleddate = []
    vidsParent = WebDriverWait(mydriver, 15).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'html body ytd-app div#content.style-scope.ytd-app ytd-page-manager#page-manager.style-scope.ytd-app ytd-search.style-scope.ytd-page-manager div#container.style-scope.ytd-search ytd-two-column-search-results-renderer.style-scope.ytd-search div#primary.style-scope.ytd-two-column-search-results-renderer ytd-section-list-renderer.style-scope.ytd-two-column-search-results-renderer div#contents.style-scope.ytd-section-list-renderer ytd-item-section-renderer.style-scope.ytd-section-list-renderer div#contents.style-scope.ytd-item-section-renderer')))
    time.sleep(2) #To load all the video elements
    vids = vidsParent.find_elements_by_tag_name('ytd-video-renderer')
    for vid in vids[:10]:
        thumbnail = WebDriverWait(vid, 15).until(expected_conditions.element_to_be_clickable((By.TAG_NAME, 'h3')))
        link = WebDriverWait(thumbnail, 15).until(expected_conditions.element_to_be_clickable((By.TAG_NAME, 'a')))
        href = link.get_attribute('href')
        top.append(str(href))
        channelName = vid.find_element_by_id('byline')
        channel.append(str(channelName.get_attribute('title')))
        metadata = vid.find_element_by_id('metadata-line').find_elements_by_tag_name('span') #Extracts list of 2 elements, first one is number of views and second one is the time it was uploaded.
        views.append(str(metadata[0].text))
        uleddate.append(str(metadata[1].text))
    return zip(top, channel, views, uleddate)

#Function to like a youtube video
def Like(driver):
    try:
        like = driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[3]/div[1]/div/div[5]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[1]/a')#.click()
        #like.click()
        if (like.find_element_by_tag_name('yt-icon-button')).get_attribute('class') == 'style-scope ytd-toggle-button-renderer style-text':
            like.click()
            print "You liked the video"
    except NoSuchElementException as e:
        print "No video is playing"

#Function to dislike a youtube video
def Dislike(driver):
    try:
        dislike = driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[3]/div[1]/div/div[5]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[2]/a')
        if (dislike.find_element_by_tag_name('yt-icon-button')).get_attribute('aria-pressed') == "false":
            dislike.click()
            print "You disliked the video"
    except NoSuchElementException as e:
            print "No video is playing"

searchInfo = raw_input("Enter what you want to search on YouTube: ")  #Search something on youtube
topLinksInfo = topResults(mydriver, searchInfo)
print "\nTop ten results and their info: "
for linkInfo in topLinksInfo:
    print linkInfo  #Prints all the info regaring a video in topLinksInfo

#Select a video that you want to play
chooseResult = input("\nEnter(in number ranging 1-10) which result you want to open: ")
mydriver.get(topLinksInfo[chooseResult-1][0])

time.sleep(5)
#Enter if you like or dislike the video
likeOrDislike = raw_input("Do you like the video?\nType 'yes' if you like it\nOr 'no' if you disliked it\nOr just press enter to remain neutral\nYour Response: ")
time.sleep(2)
if(likeOrDislike == "yes"):
    Like(mydriver)
if(likeOrDislike == "no"):
    Dislike(mydriver)



