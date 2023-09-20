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
driver.get("https://testpages.herokuapp.com/styled/file-upload-test.html")
#Implicit wait
driver.implicitly_wait(10)

t=6

#El try es como un if, que dice si linea por linea se cumple sino..
try:
    Buscar = WebDriverWait(driver,5).until(EC.visibility_of_element_located(("xpath" , "//*[@id='fileinput']")))
    Buscar = driver.find_element("xpath" , "//*[@id='fileinput']")
    Buscar.send_keys("C://Users//Luca//PycharmProjects//pythonProject7//imagen//WhatsApp-Image-2023-04-23-at-19.15.29.jpg")
    time.sleep(t)
    driver.find_element("xpath" , "//*[@id='itsanimage']" ).click()
    driver.find_element("xpath", "/html/body/div/div[3]/form/div[3]/input" ).click()
    time.sleep(t)

except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible men")


time.sleep(t)
# Cierra el navegador
driver.close()

