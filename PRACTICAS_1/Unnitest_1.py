from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
import time
import unittest

chromedriver_path = "C:/Users/Luca/OneDrive/Escritorio/LUCA/chromedriver.exe"
service = ChromeService(executable_path=chromedriver_path)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=service, options=chrome_options)


#AL UTILIZAR UNNITEST SIEMPRE SE COMIENZA CON LA CLASE (UNITTEST.TESTCASE)
#LUEGO LA FUNCION SETUP , LUEGO LOS TEST Y LUEGO TEARDOWN Y PARA CERRAR LA CLASE EL MAIN
class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = driver
        self.driver.get("https://accounts.spotify.com/es/login?continue=https%3A%2F%2Fopen.spotify.com%2Fintl-es")
        time.sleep(2)

    def test_open_spotify_login(self):
        self.driver.get("https://accounts.spotify.com/es/login?continue=https%3A%2F%2Fopen.spotify.com%2Fintl-es")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
