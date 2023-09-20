from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from  selenium.webdriver.support.ui import WebDriverWait
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
driver.get("https://demoqa.com/automation-practice-form")
#Implicit wait
driver.implicitly_wait(10)

t=2

#El try es como un if, que dice si linea por linea se cumple sino..
try:
    campo_nombre = driver.find_element("xpath", "//*[@id='firstName']")
    campo_nombre.send_keys("Luca")
    campo_nombre.send_keys(Keys.TAB + "Banchero" + Keys.TAB + "lucaban28@hotmail.com")
    time.sleep(t)

    campo_gender = driver.find_element("xpath" , "//*[@id='genterWrapper']/div[2]/div[1]/label").click()
    time.sleep(t)

    campo_Mobile = driver.find_element("xpath", "//*[@id='userNumber']")
    campo_Mobile.send_keys("+598999332")

    time.sleep(t)

    campo_subjects = driver.find_element("xpath", "//*[@id='subjectsInput']")
    campo_subjects.send_keys("Maths")
    time.sleep(1)  # Dar tiempo para que aparezcan las opciones
    campo_subjects.send_keys(Keys.RETURN)  # Presionar Enter para seleccionar la opción

    time.sleep(t)

    campo_hobbies = driver.find_element("xpath", "//*[@id='hobbiesWrapper']/div[2]/div[1]").click()
    time.sleep(t)

    time.sleep(t)

    campo_Picture = driver.find_element("xpath", "//*[@id='uploadPicture']")
    campo_Picture.send_keys("C://Users//Luca//PycharmProjects//pythonProject7//imagen//WhatsApp-Image-2023-04-23-at-19.15.29.jpg")

    time.sleep(t)

    campo_CurrentAdress = driver.find_element("xpath" , "//*[@id='currentAddress']")
    campo_CurrentAdress.send_keys("VIVO POR AQUI WEY")

    time.sleep(t)

    paginadoselectorpais = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(("xpath", "//*[@id='state']/div/div[2]/div/svg/path")))
    paginadoselectorpais = driver.find_element("xpath", "//*[@id='state']/div/div[2]/div/svg/path")
    ds = Select(paginadoselectorpais)
    ds.select_by_index(2)
    ir: driver.execute_script("arguments[0].scrollIntoView();", paginadoselectorpais)
    time.sleep(t)

    paginadoselectorciudad = driver.find_element("xpath","//*[@id='city']/div/div[2]/div/svg")
    ds = Select(paginadoselectorciudad)
    ds.select_by_index(2)

    time.sleep(t)

except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible men")

# Cierra el navegador
    driver.close()

