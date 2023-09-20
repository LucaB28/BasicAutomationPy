
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
driver.get("https://accounts.spotify.com/es/login?continue=https%3A%2F%2Fopen.spotify.com%2Fintl-es")

#Click en iniciar sesion o un campo para ver el mensaje
iniciar_sesion = driver.find_element("xpath","//*[@id='login-button']/span[1]/span")
iniciar_sesion.click()
time.sleep(2)


# captar el mensaje de error y imprimirlo y luego valida
save_valor = driver.find_element("xpath" , "/html/body/div[1]/div/div[2]/div/div/div[1]/div/span")
error = save_valor.text
#print("El valor del error es: " + error)
if (save_valor == "Nombre de usuario o contraseña incorrectos."):
    #print("falta nombre")
    campo_nombre = driver.find_element("xpath","//*[@id='login-username']")
    campo_nombre.send_keys("Luca")
    time.sleep(2)
    print("nombre no ingresado")
else:
    print("falta nombre")

# Cierra el navegador
driver.quit()
