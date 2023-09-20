from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
import time
from  selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
driver.get("https://demoqa.com/checkbox")
#Implicit wait
driver.implicitly_wait(10)

t=5

#Hace clic en el elemento checkbox, aveces el xpath viene con el icono SVG y no el elemento, donde termina el label,cuidado
btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", "//*[@id='tree-node']/ol/li/span/label")))

btn.click()

time.sleep(t)