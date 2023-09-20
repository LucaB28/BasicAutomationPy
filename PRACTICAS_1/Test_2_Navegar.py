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


#variable para controlar el tiempo si todos son iguales..
t=4
# Abre la URL y espera
driver.get("https://demoqa.com/text-box")
time.sleep(t)

driver.get("https://www.starplus.com/es-419/home")
time.sleep(t)

driver.get("https://www.linkedin.com/feed/")
time.sleep(t)

#Volver a la pagina anterior
driver.back()
time.sleep(t)
driver.execute_script("window.history.go(-1)")

driver.close()

