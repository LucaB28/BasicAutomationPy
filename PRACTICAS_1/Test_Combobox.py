from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
import time
from  selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
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
driver.get("https://demoqa.com/webtables")
#Implicit wait
driver.implicitly_wait(10)

t=2
time.sleep(t)
#driver.execute_script("window.scrollTo(0,300)")
#Hace clic en el elemento checkbox, aveces el xpath viene con el icono SVG y no el elemento, donde termina el label,cuidado
#paginado = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(("xpath", "//*[@id='app']/div/div/div[2]/div[2]/div[2]/div[3]/div[2]/div/div[2]/span[2]/select")))

paginadoselector=driver.find_element("xpath","//*[@id='app']/div/div/div[2]/div[2]/div[2]/div[3]/div[2]/div/div[2]/span[2]/select")

ds=Select(paginadoselector)

#Una opcion es buscar el elemento del combo por el texto exacto
###ds.select_by_visible_text("25 rows")
#otra opcion y la mas recomendada es por el index
ds.select_by_index(2)
# otra opcion es por el valor, este valor es el xpath de la opcion del combo
####ds.select_by_value("VALOR DEL BOTON")
time.sleep(t)