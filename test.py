from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configura Chrome para que no se cierre
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Inicializa el navegador
browser = webdriver.Chrome(options=chrome_options)

# Carga la página
browser.get('https://www.google.com')
print("Carga satisfactoria.")

# Esperar ventana de Cookies y hacer click en aceptar ( codigo ID inspeccionar elemento)
try:
    accept_cookies_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="L2AGLb"]')) 
    )
    accept_cookies_button.click()
except Exception as e:
    print(f"Error: {e}")

# Timeout
browser.implicitly_wait(5)

# search_box.send_keys(webdriver.Keys.COMMAND + 'l') // Se supone que COMMAND + 'l' busca en la barra superior
search_box = browser.find_element('name', 'q') # De esta manera busca el primer elemento 'buscable'

# Escribe algo en el elemento de busqueda
search_box.send_keys('Buenos días')

# Simula presionar Enter
search_box.send_keys(webdriver.Keys.ENTER)
print("Busqueda realizada")


# Entra en el primer resultado de la pagina de Google ( normalmente son una H3 )
first_result = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.XPATH, '(//h3)[1]'))
)

# Haz clic en el primer resultado
first_result.click()
