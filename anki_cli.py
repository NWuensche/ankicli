from selenium import webdriver

driver = webdriver.PhantomJS()

driver.maximize_window()
driver.get('https://ankiweb.net/account/login')
driver.find_element_by_id('email').send_keys(YOUR_EMAIL)
driver.find_element_by_id('password').send_keys(YOUR_PASSWORD)
driver.find_element_by_xpath("//input[@value='Log in']").click()

driver.get("https://ankiuser.net/edit/");

try:
    driver.find_element_by_id('deck').clear()
    driver.find_element_by_id('deck').send_keys(input("Deck: "))
except Exception: #Exception doesn't swallow KeyboardInterrupts
    pass

while (True):
    try:
        driver.find_element_by_id('f0').send_keys(input("Front: "))
    except Exception:
        pass

    try:
        driver.find_element_by_id('f1').send_keys(input("Back: "))
    except Exception:
        pass

    try:
        driver.find_element_by_xpath("//button[@class='btn btn-primary']").click()
    except Exception:
        pass

