from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from bs4 import BeautifulSoup

driver = webdriver.Edge(executable_path='msedgedriver.exe')
driver.implicitly_wait(10)

driver.get("https://10fastfingers.com/login")
sleep(5)

email = input("Enter email address: ")
password = input("Enter password: ")

# manage Cookies
sleep(2)
driver.find_element(By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]').click()

# login
email_box = driver.find_element(By.ID, "UserEmail")
password_box = driver.find_element(By.ID, "UserPassword")
login_btn = driver.find_element(By.ID, "login-form-submit")
email_box.send_keys(email)
password_box.send_keys(password)
print("logged in\n")
login_btn.click()

sleep(3)
soup = BeautifulSoup(driver.page_source, features="html.parser")
i = 0
count = 0
while True:
    try:
        letter = soup.find('span', {"wordnr":i})

        count += 1
        if count == 8:
            count = 0
            print()
        print(letter.text, end=" ")

        input_box = driver.find_element(By.ID, "inputfield")
        input_box.send_keys(f"{letter.text} ")

        i += 1
        # sleep(.2)
    except:
        print("\n\nfinished")
        sleep(65)
        driver.close()
        break

