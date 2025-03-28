import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc


class AIRPAZ(unittest.TestCase):
    def setUp(self):
        self.browser = uc.Chrome()

    def test_LoginPositive(self):
        driver = self.browser
        driver.get('https://www.airpaz.com/en')
        driver.maximize_window()
        Login = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//div[@class="w-40 h-40 flex items-center justify-center"]'))
        )
        Login.click()
        ClosePopUp = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//div[@class="absolute -top-5 -right-5 w-15 h-15 cursor-pointer"]'))
        )
        ClosePopUp.click()
        SignIn2 = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//a[@class="flex items-center text-base font-bold px-10 py-5 cursor-pointer rounded text-white hover:bg-primary-light"]//span[text()="Sign in"]'))
        )
        SignIn2.click()
        Email = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//input[@class="bg-transparent border-0 border-b focus:outline-none focus:ring-0 focus:border-gray-darkest border-gray-lightest hover:border-gray-dark disabled:opacity-50 disabled:cursor-not-allowed disabled:pointer-events-none disabled:placeholder-gray-dark peer block w-full h-35 text-base font-bold placeholder-gray-light p-0"][@id="email"]'))
        )
        Email.send_keys("kecih94053@evluence.com")
        Password = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//input[@class="bg-transparent border-0 border-b focus:outline-none focus:ring-0 focus:border-gray-darkest border-gray-lightest hover:border-gray-dark disabled:opacity-50 disabled:cursor-not-allowed disabled:pointer-events-none disabled:placeholder-gray-dark peer block w-full h-35 text-base font-bold placeholder-gray-light p-0"][@id="password"]'))
        )
        Password.send_keys("QAtest123")
        btn_Signin = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//button[@data-testid="signIn-button"]'))
        )
        btn_Signin.click()
        time.sleep(3)
        try:
            wait = WebDriverWait(driver, 5)
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//div[@class="flex items-center text-base font-bold px-10 py-5 cursor-pointer rounded text-white hover:bg-primary-light"]//span[text()="Hi,  QA Test"]'))
            )
            print('Login berhasil dan masuk kehalaman utama')
        except:
            print('Login gagal, captcha salah')

    def test_LoginNegative(self):
        driver = self.browser
        driver.get('https://www.airpaz.com/en')
        driver.maximize_window()
        Login = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//div[@class="w-40 h-40 flex items-center justify-center"]'))
        )
        Login.click()
        ClosePopUp = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//div[@class="absolute -top-5 -right-5 w-15 h-15 cursor-pointer"]'))
        )
        ClosePopUp.click()
        SignIn2 = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//a[@class="flex items-center text-base font-bold px-10 py-5 cursor-pointer rounded text-white hover:bg-primary-light"]//span[text()="Sign in"]'))
        )
        SignIn2.click()
        Email = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//input[@class="bg-transparent border-0 border-b focus:outline-none focus:ring-0 focus:border-gray-darkest border-gray-lightest hover:border-gray-dark disabled:opacity-50 disabled:cursor-not-allowed disabled:pointer-events-none disabled:placeholder-gray-dark peer block w-full h-35 text-base font-bold placeholder-gray-light p-0"][@id="email"]'))
        )
        Email.send_keys("kecih94053@evluence.com")
        Password = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//input[@class="bg-transparent border-0 border-b focus:outline-none focus:ring-0 focus:border-gray-darkest border-gray-lightest hover:border-gray-dark disabled:opacity-50 disabled:cursor-not-allowed disabled:pointer-events-none disabled:placeholder-gray-dark peer block w-full h-35 text-base font-bold placeholder-gray-light p-0"][@id="password"]'))
        )
        Password.send_keys("Password123*")
        btn_Signin = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//button[@data-testid="signIn-button"]'))
        )
        btn_Signin.click()
        try:
            wait = WebDriverWait(driver, 5)
            error_message = wait.until(EC.presence_of_element_located(
                (By.XPATH,
                 '//p[@class="text-small mt-10 text-danger" and text()="Your email address or password is incorrect."]')
            ))
            error_message.text
            print("Login gagal: Akun tidak sesuai")
        except Exception as e:
            print("Data sesuai: Berhasil Login")
        time.sleep(3)

    def test_SignOutPositive(self):
        driver = self.browser
        driver.maximize_window()
        driver.get('https://www.airpaz.com/en')
        Login = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//div[@class="w-40 h-40 flex items-center justify-center"]'))
        )
        Login.click()
        ClosePopUp = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//div[@class="absolute -top-5 -right-5 w-15 h-15 cursor-pointer"]'))
        )
        ClosePopUp.click()
        SignIn2 = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//a[@class="flex items-center text-base font-bold px-10 py-5 cursor-pointer rounded text-white hover:bg-primary-light"]//span[text()="Sign in"]'))
        )
        SignIn2.click()
        Email = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//input[@class="bg-transparent border-0 border-b focus:outline-none focus:ring-0 focus:border-gray-darkest border-gray-lightest hover:border-gray-dark disabled:opacity-50 disabled:cursor-not-allowed disabled:pointer-events-none disabled:placeholder-gray-dark peer block w-full h-35 text-base font-bold placeholder-gray-light p-0"][@id="email"]'))
        )
        Email.send_keys("kecih94053@evluence.com")
        Password = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//input[@class="bg-transparent border-0 border-b focus:outline-none focus:ring-0 focus:border-gray-darkest border-gray-lightest hover:border-gray-dark disabled:opacity-50 disabled:cursor-not-allowed disabled:pointer-events-none disabled:placeholder-gray-dark peer block w-full h-35 text-base font-bold placeholder-gray-light p-0"][@id="password"]'))
        )
        Password.send_keys("QAtest123")
        btn_Signin = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//button[@data-testid="signIn-button"]'))
        )
        btn_Signin.click()
        time.sleep(3)
        try:
            wait = WebDriverWait(driver, 5)
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//div[@class="flex items-center text-base font-bold px-10 py-5 cursor-pointer rounded text-white hover:bg-primary-light"]//span[text()="Hi,  QA Test"]'))
            )
            print('Login berhasil dan masuk kehalaman utama')
        except:
            print('Login gagal, captcha salah')
        time.sleep(5)
        btn_Signout = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//div[@class="flex items-center text-base font-bold px-10 py-5 cursor-pointer rounded text-white hover:bg-primary-light"]'))
        )
        btn_Signout.click()
        try:
            sign_out = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
                (By.XPATH, '//button[@class="flex items-center justify-center px-15 rounded font-bold focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-opacity-50 bg-whiter hover:bg-gray-lightest active:bg-gray-lightest focus:ring-gray-lightest h-[49px] text-base !bg-transparent hover:!bg-whiter flex gap-x-10 items-center !justify-start p-10 rounded hover:bg-gray-dark hover:bg-opacity-20 text-primary"]')))
            sign_out.click()
            print('Sign Out berhasil dilakukan')
        except:
            print('Gagal melakukan Sign Out')
        time.sleep(3)

    def test_SignOutNegative(self):
        driver = self.browser
        driver.maximize_window()
        driver.get('https://www.airpaz.com/en')
        Login = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//div[@class="w-40 h-40 flex items-center justify-center"]'))
        )
        Login.click()
        ClosePopUp = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//div[@class="absolute -top-5 -right-5 w-15 h-15 cursor-pointer"]'))
        )
        ClosePopUp.click()
        SignIn2 = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//a[@class="flex items-center text-base font-bold px-10 py-5 cursor-pointer rounded text-white hover:bg-primary-light"]//span[text()="Sign in"]'))
        )
        SignIn2.click()
        Email = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//input[@class="bg-transparent border-0 border-b focus:outline-none focus:ring-0 focus:border-gray-darkest border-gray-lightest hover:border-gray-dark disabled:opacity-50 disabled:cursor-not-allowed disabled:pointer-events-none disabled:placeholder-gray-dark peer block w-full h-35 text-base font-bold placeholder-gray-light p-0"][@id="email"]'))
        )
        Email.send_keys("kecih94053@evluence.com")
        Password = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//input[@class="bg-transparent border-0 border-b focus:outline-none focus:ring-0 focus:border-gray-darkest border-gray-lightest hover:border-gray-dark disabled:opacity-50 disabled:cursor-not-allowed disabled:pointer-events-none disabled:placeholder-gray-dark peer block w-full h-35 text-base font-bold placeholder-gray-light p-0"][@id="password"]'))
        )
        Password.send_keys("QAtest123")
        btn_Signin = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//button[@data-testid="signIn-button"]'))
        )
        btn_Signin.click()
        time.sleep(3)
        try:
            wait = WebDriverWait(driver, 5)
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//div[@class="flex items-center text-base font-bold px-10 py-5 cursor-pointer rounded text-white hover:bg-primary-light"]//span[text()="Hi,  QA Test"]'))
            )
            print('Login berhasil dan masuk kehalaman utama')
        except:
            print('Login gagal, captcha salah')
        time.sleep(5)
        try:
            btn_Signout = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH,
                                            '//div[@class="flex items-center text-base font-bold px-10 py-5 cursor-pointer rounded text-white hover:bg-primary-light"]'))
            )
            btn_Signout.click()
            print('Gagal melakukan Sign Out')
        except:
            print('Sign Out berhasil dilakukan')
        time.sleep(3)

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
