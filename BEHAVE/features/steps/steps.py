from behave import *
import pages

@given(u'Nos encontramos en google')
def nos_encontramos_en_google(context):
    context.driver.get("https://www.google.com")
    google_page = pages.GooglePage(context.driver)
    google_page.accept_cookies()    
    

@when(u'Buscamos la cadena \"{texto}\"')
def buscamos_la_cadena(context, texto):
    google_page = pages.GooglePage(context.driver)
    google_page.search_for_string(texto)
    

@then(u'La URL del primer resultado es \"{url}\"')
def url_primer_resultado(context, url):
    search_results_page = pages.SearchResultsPage(context.driver)
    assert url == search_results_page.get_first_result_url()



