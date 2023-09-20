
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
driver.get("https://demoqa.com/alerts")

t = 2
time.sleep(t)

driver.find_element("xpath" , "//*[@id='alertButton']").click()

#Ejecutar botón aceptar
alert = driver.switch_to.alert
alert.accept()

'''
#Ejecutar botón CERRAR/noaceptar
alert = driver.switch_to.alert
alert.dismiss()
'''
time.sleep(t)

# Cierra el navegador
driver.quit()
