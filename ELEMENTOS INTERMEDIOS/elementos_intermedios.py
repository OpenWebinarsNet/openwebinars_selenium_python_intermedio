from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException

import time


def iframe_changing():

    iniciar_navegador()
    
    #nos dirigimos a la sección de iFrames
    driver.find_element(By.LINK_TEXT, "iFrames").click()
    
    iframe1 = "inception_1"
    iframe2 = "inception_2"
    
    iframe_button = (By.ID, "iframebutton")
    
    #Cambiamos al primer frame y pulsamos el botón
    driver.switch_to.frame(iframe1)
    driver.find_element(*iframe_button).click()
    time.sleep(2)
    
    
    #Cambiamos al segundo frame y pulsamos el botón
    # podemos utilizar el mismo localizador, pues no varía
    # sólo dependerá de en qué contexto (iframe) nos encontremos
    driver.switch_to.frame(iframe2)
    driver.find_element(*iframe_button).click()
    time.sleep(2)
  
  
    #Volvemos al contenido por defecto (top) de la página
    # y tratamos de volver a buscarlo capturando el error: 
    # NoSuchElementException
    
    driver.switch_to.default_content()
    try:
        driver.find_element(*iframe_button)
    except NoSuchElementException as nsee:
        print(nsee.with_traceback)
  
    
    cerrar_navegador()


    
    
    
    

def javascript_execute():

    iniciar_navegador()
    
    #nos dirigimos a la sección de XPaths
    driver.find_element(By.LINK_TEXT, "XPaths").click()
    
    #Boton Cancelar -> Contenedor Principal - Opción 116
    # EL XPATH SETEADO PUEDE SER MUCHO MÁS ÓPTIMO, PERO
    # ESTÁ SETEADO ASÍ POR MOTIVOS DIDÁCTICOS. ESTUDIAD
    # LO QUE ESTÁ HACIENDO.
    cancelar_116_principal = (By.XPATH, "(//button[text()='Cancelar' and ../preceding-sibling::div[p[contains(text(),'Principal') and contains(text(),'116')]]])[1]")
    
    cancelar_116_principal_element = driver.find_element(*cancelar_116_principal)
    #EJECUTAMOS SCRIPT 
    #window.scrollTo -> Lleva el scroll hacia la posición donde se le indica.
    #window.scrollBy -> Desliza el scroll las cantidades que se le indiquen en la función.
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, arguments[0])", cancelar_116_principal_element.location["y"])
    time.sleep(2)

    #EJECUTAMOS UN ALERT
    mensaje = "envío este mensaje desde python!"
    driver.execute_script("alert(arguments[0])", mensaje)
    time.sleep(2)
    driver.switch_to.alert.accept()
    time.sleep(2)

    cerrar_navegador()






def shadowdom_action():

    iniciar_navegador()
    
    #nos dirigimos a la sección de ShadowDom
    driver.find_element(By.LINK_TEXT, "ShadowDOM").click()
    
    shadowhost_location = (By.ID, "nodoShadowHost")
     
    
    #POR MOTIVOS DE CARGA DE LA PÁGINA, AGREGAMOS UN MECANISMO DE ESPERA EXPLICITA
    #QUE AGUARDE A QUE EL ELEMENTO SEA VISIBLE
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(shadowhost_location))
    
    
    #CAPTURAMOS EL NODO SHADOWHOST
    nodoShadowHost = driver.find_element(*shadowhost_location)
    
    #A PARTIR DEL ELEMENTO SHADOWHOST, NOS AYUDAMOS DE JAVASCRIPT
    #PARA RECUPERAR EL NODO DE SHADOWROOT
    nodoShadowRoot = driver.execute_script("return arguments[0].shadowRoot;", nodoShadowHost)
    
    #Pulsamos el botón DENTRO del shadowDOM, y posteriormente
    #pulsaremos el del top llamando al driver.
    time.sleep(1)
    nodoShadowRoot.find_element(By.ID, "boton2").click()
    
    time.sleep(1)
    driver.find_element(By.ID, "boton1").click()
    time.sleep(1)
    
    cerrar_navegador()



### FUNCIONES COMUNES A TODAS LAS FUNCIONES DE LOCALIZACION
def iniciar_navegador():
    '''
    PARA PODER SETEAR LA VARIABLE DE MANERA GLOBAL DENTRO DE LAS FUNCIONES,
    INDICAMOS A LA VARIABLE QUE ES DE TIPO GLOBAL. POSTERIORMENTE PODEMOS
    MODIFICARLA
    '''
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("http://localhost:3000")
         
def cerrar_navegador():
    driver.quit()
   
def ir_a_waits():
    driver.find_element(By.LINK_TEXT, "Waits").click()   
   
   

'''
 PODÉIS IGNORAR ESTA FUNCIÓN HASTA CONOCER EL USO DE execute_script.
 ESTAMOS EJECUTANDO SCRIPTS DE JAVASCRIPT EN LA PÁGINA PARA HACER
 SCROLL HASTA EL ELEMENTO Y SETEARLE UN HIGHLIGHT
'''
def iluminar_elemento(elemento):
    driver.execute_script("window.scrollTo(0, arguments[0]);", (elemento.location["y"]-100))
    driver.execute_script("arguments[0].setAttribute('style', 'background: yellow;');", elemento)
##########################################################



if __name__ == "__main__":
    shadowdom_action()
