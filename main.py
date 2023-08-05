from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import threading


def randuser():
    rand = random.randint(1, 99)
    rand2 = random.randint(100, 114)
    user_agent = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.{rand} (KHTML, like Gecko) Chrome/{rand2}.0.0.0 Safari/537.36 OPR/100.0.0.0"
    return user_agent


def CitriaLove():
    while True:
        try:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--disable-notifications")
            chrome_options.add_argument("--window-position=-32000,-32000")
            chrome_options.add_argument(f"user-agent={randuser()}")
            driver = webdriver.Chrome(options=chrome_options)
            driver.get('https://support.hypixel.net/hc/en-us/requests/new')
            element_label = "Please select the topic you are contacting about below."
            panel_element = driver.find_element(By.XPATH, f"//a[@aria-label='{element_label}']")
            panel_location = panel_element.location
            panel_element.click()
            print("Successfully clicked on the element.")
            target_x = panel_location['x'] + 30
            target_y = panel_location['y'] + 50
            actions = ActionChains(driver)
            actions.move_by_offset(target_x, target_y).click().perform()
            print("Successfully clicked Support")
            email_input_element = driver.find_element(By.NAME, "request[anonymous_requester_email]")
            email_input_element.click()
            email_to_type = f"hub{random.randint(1, 999999)}@gmail.com"
            email_input_element.send_keys(email_to_type)
            print(f"Successfully typed email: {email_to_type}")
            subject_input_element = driver.find_element(By.NAME, "request[subject]")
            subject_input_element.click()
            list = ["I Love Citra", "FreeMoneyHub <3 Citria", "Help Big Bugs Need Fix", "Some Weird Glitch", "UI is not responsive", "Data is not loading correctly", "Application is crashing", "There are errors in the logs", "Users are reporting problems", "The website is down", "The server is not responding", "There is a security vulnerability", "The database is corrupted"]
            subject_to_type = f"{random.choice(list)}"
            subject_input_element.send_keys(subject_to_type)
            print(f"Successfully typed subject: {subject_to_type}")
            nesty_input_element = driver.find_elements(By.XPATH, "//a[@class='nesty-input' and @tabindex='0']")[1]
            nesty_input_location = nesty_input_element.location
            nesty_input_element.click()
            print("Successfully clicked on the element.")
            actions = ActionChains(driver)
            actions.move_to_element(nesty_input_element).move_by_offset(0, 20).click().perform()
            print("Successfully clicked 20 pixels below.")
            input_xpath = "//input[@type='text' and @aria-required='true']"
            input_elements = driver.find_elements(By.XPATH, input_xpath)
            if len(input_elements) >= 2:
                input_element = input_elements[2]
                input_element.click()
                text_to_type = f"citra_lover{random.randint(1, 999)}"
                input_element.send_keys(text_to_type)
                print(f"Successfully typed text: {text_to_type}")
                input_element2 = input_elements[3]
                input_element2.click()
                type2int = random.randint(1, 9999)
                text_to_type2 = f"freemoneyhub{type2int}"
                input_element2.send_keys(text_to_type2)
                print(f"Successfully typed text: {text_to_type2}")
            else:
                print("Couldn't find the required text element")
            time.sleep(.5)
            scroll_height = driver.execute_script("return document.body.scrollHeight")
            driver.execute_script(f"window.scrollTo(0, {scroll_height / 2})")
            time.sleep(.5)
            nesty_input_element2 = driver.find_elements(By.XPATH, "//a[@class='nesty-input' and @tabindex='0']")[2]
            nesty_input_location2 = nesty_input_element2.location
            nesty_input_element2.click()
            print("Successfully clicked on the element.")
            actions.move_to_element(nesty_input_element2).move_by_offset(0, 45).click().perform()
            actions.move_to_element(nesty_input_element2).move_by_offset(0, 200).click().perform()
            text_to_type = random.choice(["Weird Bug Around Citra From British Columbia Cannda Age 21 Glitch", "How I Prouce My Love To Citria", "Please Tell Citria How Amazing She Looks And To Add Me BAck @freemoneyhub on discord "])
            actions.send_keys(text_to_type).perform()
            print(f"Successfully typed text: {text_to_type}")
            submit_button = driver.find_element(By.XPATH, "//input[@type='submit' and @name='commit']")
            submit_button.click()
            print("Successfully clicked the Submit button.")
            time.sleep(1)
        except Exception as e:
            print(f"An error occurred: {e}")
        driver.quit()

threads = []
for i in range(5):
    thread = threading.Thread(target=CitriaLove)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
