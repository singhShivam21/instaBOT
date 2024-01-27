from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
import credential
import pyautogui
import os

def get_jpg_files(folder_path):
    jpg_files = [os.path.splitext(f)[0] for f in os.listdir(folder_path) if f.lower().endswith('.jpg')]
    return jpg_files

#  folder path where post data is saved
folder_path =r"C:\Users\littlex\PycharmProjects\selenium01\PostData"
jpg_files = get_jpg_files(folder_path)

credentials=credential.credentials_()
chromedriver_path = r"C:\Users\littlex\PycharmProjects\selenium01\WebDriver\chromedriver.exe"
start_service = Service(chromedriver_path)
driver = webdriver.Chrome(service=start_service)
driver.get("https://www.instagram.com/")
driver.maximize_window()
time.sleep(2)
username_input = driver.find_element(By.NAME, "username")
username_input.send_keys(credentials['username'])
time.sleep(2)
password_input = driver.find_element(By.NAME, "password")
password_input.send_keys(credentials['password'])
time.sleep(2)
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(4)

for jpg_file in jpg_files:
    driver.find_element(By.XPATH, "(//*[@aria-label='New post'])").click()
    time.sleep(2)
    login_button = driver.find_element(By.XPATH, "(//*[@aria-label='Post'])").click()
    time.sleep(2)
    login_button = driver.find_element(By.XPATH, "//button[text()='Select from computer']").click()
    time.sleep(2)
    #import the windos file handling function here fileAccess.py.............

    path = rf"C:\Users\littlex\PycharmProjects\selenium01\PostData\{jpg_file}.jpg"
    pyautogui.click(500, 510, 1)
    pyautogui.typewrite(path)
    pyautogui.hotkey('enter')

    time.sleep(1)
    driver.find_element(By.XPATH, "//div[contains(text(),'Next')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//div[contains(text(),'Next')]").click()
    time.sleep(2)

    with open(rf"C:\Users\littlex\PycharmProjects\selenium01\PostData\{jpg_file}.txt",'r',encoding='utf-8')as caption_file:
        caption = caption_file.read()
        driver.find_element(By.XPATH, "//div[@aria-label='Write a caption...']").send_keys(caption)

    time.sleep(2)
    driver.find_element(By.XPATH, "//div[contains(text(),'Share')]").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "(//*[@aria-label='Close'])").click()
    time.sleep(2)
    driver.refresh()
    time.sleep(5)