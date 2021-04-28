from behave import *
import pages
from selenium import webdriver


@given(u'nos encontramos en google')
def estamos_en_google(context):
    context.driver.get("http://www.google.com")
    google_page = pages.GooglePage(context.driver)
    google_page.accept_cookies()
    
    
    
@when(u'introducimos el texto: "{texto}" y buscamos los resultados')
def introducimos_texto_y_buscamos(context, texto):
    google_page = pages.GooglePage(context.driver)
    google_page.search_text(texto)    
  
    
@then(u'la URL del primer resultado es "{text}"')
def titulo_primer_resultado(context, text):
    search_results_page = pages.SearchResultsPage(context.driver)    
    print(text)
    assert text == search_results_page.get_first_result_url()
    
