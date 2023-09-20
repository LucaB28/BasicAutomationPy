from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
import time
from  selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

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
driver.get("https://pixabay.com/es/")
#Implicit wait
driver.implicitly_wait(10)

t=6

#El try es como un if, que dice si linea por linea se cumple sino..
#Aqui se usa el driver.execute_script con la sigueinte funcion hasta el elemento que se mando a buscar si existe para no hacer scroll
try:
    Buscar = WebDriverWait(driver,5).until(EC.visibility_of_element_located(("xpath" , "//*[@id='app']/div[1]/div[2]/div[1]/div[2]/div[2]/a/span")))
    Buscar = driver.find_element("xpath" , "//*[@id='app']/div[1]/div[2]/div[1]/div[2]/div[2]/a/span")
    ir: driver.execute_script("arguments[0].scrollIntoView();", Buscar)

    time.sleep(t)

except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible men")

# Cierra el navegador
driver.close()

