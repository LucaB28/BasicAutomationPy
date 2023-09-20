from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
import time
import unittest
from  selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



#AL UTILIZAR UNNITEST SIEMPRE SE COMIENZA CON LA CLASE (UNITTEST.TESTCASE)
#LUEGO LA FUNCION SETUP , LUEGO LOS TEST Y LUEGO TEARDOWN Y PARA CERRAR LA CLASE EL MAIN
class BaseTest_Login(unittest.TestCase):

    def setUp(self):
        chromedriver_path = "C:/Users/Luca/OneDrive/Escritorio/LUCA/chromedriver.exe"
        service = ChromeService(executable_path=chromedriver_path)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.get("https://www.saucedemo.com/v1/")
        time.sleep(2)


    def test_login1(self):
        self.driver.get("https://www.saucedemo.com/v1/")

        Username = self.driver.find_element("xpath","//*[@id='user-name']")
        Password = self.driver.find_element("xpath","//*[@id='password']")
        Button_Loggin = self.driver.find_element("xpath","//*[@id='login-button']")

        Username.send_keys("Luca")
        Password.send_keys("adm123")
        Button_Loggin.click()

        time.sleep(2)

        error = self.driver.find_element("xpath" , "//*[@id='login_button_container']/div/form/h3")
        error = error.text
        #print(error)

        if(error == "Epic sadface: Username and password do not match any user in this service"):
            print("Los datos no son correctos")
            print("Prueba uno")

        time.sleep(2)

    def test_login2(self):
        self.driver.get("https://www.saucedemo.com/v1/")

        Username = self.driver.find_element("xpath","//*[@id='user-name']")
        Password = self.driver.find_element("xpath","//*[@id='password']")
        Button_Loggin = self.driver.find_element("xpath","//*[@id='login-button']")

        Username.send_keys("")
        Password.send_keys("adm123")
        Button_Loggin.click()

        time.sleep(2)

        error = self.driver.find_element("xpath" , "//*[@id='login_button_container']/div/form/h3")
        error = error.text
        #print(error)

        if(error == "Epic sadface: Username is required"):
            print("Username vacio")
            print("Prueba dos")

    def test_login3(self):
        self.driver.get("https://www.saucedemo.com/v1/")

        Username = self.driver.find_element("xpath","//*[@id='user-name']")
        Password = self.driver.find_element("xpath","//*[@id='password']")
        Button_Loggin = self.driver.find_element("xpath","//*[@id='login-button']")

        Username.send_keys("Luca")
        Password.send_keys("")
        Button_Loggin.click()

        time.sleep(2)

        error = self.driver.find_element("xpath" , "//*[@id='login_button_container']/div/form/h3")
        error = error.text
        #print(error)

        if(error == "Epic sadface: Password is required"):
            print("Password vacio")
            print("Prueba tres")

    def test_login4(self):
        self.driver.get("https://www.saucedemo.com/v1/")

        Username = self.driver.find_element("xpath","//*[@id='user-name']")
        Password = self.driver.find_element("xpath","//*[@id='password']")
        Button_Loggin = self.driver.find_element("xpath","//*[@id='login-button']")

        Username.send_keys("")
        Password.send_keys("")
        Button_Loggin.click()

        time.sleep(2)

        error = self.driver.find_element("xpath" , "//*[@id='login_button_container']/div/form/h3")
        error = error.text
        #print(error)

        if(error == "Epic sadface: Username is required"):
            print("Username vacio pero deberia decir que faltan los dos")
            print("Prueba cuatro")

    def test_login5(self):
        self.driver.get("https://www.saucedemo.com/v1/")

        Username = self.driver.find_element("xpath","//*[@id='user-name']")
        Password = self.driver.find_element("xpath","//*[@id='password']")
        Button_Loggin = self.driver.find_element("xpath","//*[@id='login-button']")

        Username.send_keys("standard_user")
        Password.send_keys("secret_sauce")
        Button_Loggin.click()

        time.sleep(2)

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(("xpath", "//*[@id='shopping_cart_container']/a")))
        carrito = self.driver.find_element("xpath", "//*[@id='shopping_cart_container']/a")
        carrito.is_displayed()


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
