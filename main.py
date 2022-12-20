import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# code to ignore browser notifications
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome('H:/chromedriver.exe', chrome_options=chrome_options)

# open the webpage
driver.get("https://wwww.facebook.com/")

# target username
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))

# enter username and password
username.clear()

username.send_keys("happyeunn@gmail.com")
password.clear()
# use your username and password
password.send_keys("Zeu)K\"78")

# target the login button and click it
time.sleep(5)
button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

# We are logged in!
print("Logged in")


# program to parse username who posted comment
# def Nameparse():
#     driver.get(url)
#     names = driver.find_elements(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[4]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div[4]/div/div/div[2]/ul/li[1]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/div/div/span/a/span/span')
#     for name in names:
#         name = name.text
#         if name == 'Eunice Teh':  # Omitting Narendra modi name from parsed list
#             continue
#         Name.append(name)


# program to parse comments
def Commentparse():
    driver.get(url)
    comments = driver.find_elements(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[4]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div[4]/div/div/div[2]/ul/li[1]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/div/div/div/span/div')
    # by=By.CSS_SELECTOR, value="[class='ee']") or driver.find_elements(by=By.CSS_SELECTOR, value="[class='eg']")
    for comment in comments:
        comment = comment.text
        Comment.append(comment)


# Program to scrap comments from each page
# Name = []
Comment = []
cnt = 0
# program to parse comments from 5 pages, if you want comments from all pages then use while loop
for i in range(6):
    # while True:
    url = "https://facebook.com/story.php?story_fbid=pfbid0cgVVNQUMrWAPwYUEQA9Pg2LHKZHJYzqd51ecdB4uckqsWBamAWr78NKyLvsBzLyRl&id=31373189944&eav=AfYfwmgU3xhp7R2Hhwwq6yyI72q3apf2e_Z1IvORudJ2O-aEGxZG3FTFR11dZJyU0Do&refid=17&ref=wizard&_ft_=encrypted_tracking_data.0AY-hMCFifVjrf81qhAF0kC2fcrkMe5UwxWjj2GM4IYkRK8BZ97PmsTPMtWYvrID8H4MGnmqUtZmHyFp3bfX0vCNRC1s_swmo82Ssg2oYFA_N-Y_1Iieuc2DjJXftfnJnx9AWQlZWPFenSLuN3nEHQVjJbviAtT7jCYfycmmNSrolRSGPdh95YkiO95GrmpTqsDY27BXGGIpWlr17_fNB-RhOyLECMM8A8U6gHe5kLOeIRqgBLziTdhUCxirF4KgxeXIvyQvduyKM6cNS9T-W3F8hwlRb8YOkEyHgIHpJ-IsH_yV79J3k_Mno9J8y9iaeYG5kK6cz2Cn4FiCFumrtMwXLBgfkSGpAdvV00P9JO4bT-3ZyFriGQcMIizLTFLSmAarp8K-PXS7rWbudrkizgqUYHYnN9dzfjsjeODJJ0m0aseFv2k2rVf8pnbpRbQB7851-J38AGtFKx8I6cZNkoUbH3-r-JIjvrtQoIhY27KZeC7R0horsohFYSna3oTIcPDnojzPofCdp_glSszQYg6weX21TLDdIcQKeC2EhgfDhoDFw4XPZbpHCNqkS15yPoKr3UxBKDpuC0LKiQUkf-0vaaAXGlSYwJw076r4Js1ZdfnVCkzOMGlCvf2TTLqruKNgdwOWbd7eV-qEvfWdF2VD5FoKagwsBXNVVj_3lmlstzA6CW4WcHf45eivRbyo2b551zkVFt47fSc3u6W2WUhc25BSxDDH42H3eDzt54gAgs4tmecmHFt8zm3i9gUTh9G_t0699_-PQisq_rnmc2bte-DQWuk7kTgz3DJj3Tyc-Nipv_dxzB527iflZldb6_gJJPBRiFqCfeS_b-XV2IDI7_xun2P2LrrWNYWjn3Do-cgqSdfo1mXkEAIEQlSrPt3EW_jP18TgTau_PzzU6dxnP5chu1g0gbgdOHgnnKQzGD7QJgBN0I6E6eig_XB0O9GJY2B-DOYOhAhJPnI9RH8H2RbiP9ScDqC4ZFQhse1a3_IpFmxdNXWKju7DZhMHg4jjEJcwudwg6YfK64jN4v9QSke-3Iw7x3WjEZw0-3FW21TJWW1ZHsHQXhhJAAS7jXm1soH9LRyA6GBytmJEUkb_VaAvD_XQfnGOIGWjIh-AlIlCEgv4SpOHwGEJH7uXST92A5aPt_WCARuoFDpVGWKRyHDBGvPYhKwvRc3PWCUw97t0D83_VAXyrU0cMhqyDbj5cXPmxQF2snZ1wCRH-sHo8uiq5drj1tQAUCrtyBK8YpdoGyv8F1pc1_H1T9W1uqeuxC4L3Yt8uvlEGvbJ_CY6rdt5FtCvJhDgcbaBrXzEzAdqfj1J5e6Pb5bSK3H1NwTXNcQ&__tn__=%2AW-R&paipv=0"
    url = url + str(cnt)
    # Nameparse()
    # print(Name)
    Commentparse()
    print(Comment)
    print(url)
    cnt = cnt + 10

# create a dataframe
data = pd.DataFrame({'Comment': Comment})
data.to_csv('Facebbok_comments.csv')
print('data saved')
