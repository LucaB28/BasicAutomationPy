
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
driver.get("https://demoqa.com/links")
time.sleep(2)

#Obtener links
links = driver.find_elements("tag name", "a")
print("el numero de links es: " + str(len(links)))

for num in links:
    print(num.text)

# Cierra el navegador
driver.quit()
