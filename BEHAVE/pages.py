from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
        
    def get_title(self):
        return self.driver.title


class GooglePage(BasePage):

    aceptar_cookies = (By.XPATH, "//div[text()='Acepto']/ancestor::button")
    search_bar = (By.NAME, "q")
    
    def accept_cookies(self):
        self.driver.find_element(*self.aceptar_cookies).click()
        
    def search_for_string(self, string_to_search):
        search_bar = self.driver.find_element(*self.search_bar)
        search_bar.send_keys(string_to_search)
        search_bar.send_keys(Keys.ENTER)
        
    
class SearchResultsPage(BasePage):
    
    first_result = (By.XPATH, "(//div[@id='search']/descendant::div[@class='g'])[1]/descendant::a[1]")    
    
    def click_on_first_result(self):
        self.driver.find_element(*self.first_result).click()
    
    def we_are_on_results_page(self, texto_buscado):
        return str(texto_buscado + " - Buscar con Google") in self.driver.title
    
    def get_first_result_url(self):
        return self.driver.find_element(*self.first_result).get_attribute("href")
    
class WikipediaPage(BasePage):
    
    articulo_bueno = (By.XPATH, "//div[@id='Artículo_bueno']/following-sibling::h2/descendant::a")
    
    def get_articulo_bueno_title(self):        
        return self.driver.find_element(*self.articulo_bueno).get_attribute("title")
    
    
    