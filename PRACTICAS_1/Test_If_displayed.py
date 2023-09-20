
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

# Validar que existe la imagen o elemento

imagen = driver.find_element("xpath" , "//*[@id='app']/header/a/img")
print(imagen.is_displayed())

# al encontrar el elemento se puede realizar otra acción a partir del mismo
# Se selecciona primero que otro elemento quiere ser interactuado
boton = driver.find_element("xpath","//*[@id='item-1']/span")

if (imagen.is_displayed()==True):
    print("existe la imagen")
    boton.click()
else:
    print("no existe")

#Se puede utilizar ENABLED  para verificar si esta activo

time.sleep(2)

# Cierra el navegador
driver.quit()
