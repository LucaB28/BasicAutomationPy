from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
import time

# Ruta al controlador de Chrome
chromedriver_path = "C:/Users/Luca/OneDrive/Escritorio/LUCA/chromedriver.exe"

# Configura el servicio del controlador de Chrome
service = ChromeService(executable_path=chromedriver_path)

# Configura las opciones del navegador
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")  # Maximiza la ventana del navegador

# Inicializa el controlador de Chrome con el servicio y las opciones
driver = webdriver.Chrome(service=service, options=chrome_options)


# Abre la URL y espera
driver.get("https://demoqa.com/text-box")
#Implicit wait
driver.implicitly_wait(10)

t=2

#El try es como un if, que dice si linea por linea se cumple sino..
try:
    campo_nombre = driver.find_element("xpath", "//*[@id='userName']")
    campo_nombre.send_keys("Luca")
    campo_nombre.send_keys(Keys.TAB + "Luca@hotmail.com" + Keys.TAB + "PORAHI" + Keys.TAB + "PORAHIDIJE" + Keys.TAB + Keys.ENTER)
    time.sleep(t)

    driver.execute_script("window.scrollTo(0,300)")
    time.sleep(t)
finally:

# Cierra el navegador
    driver.close()

