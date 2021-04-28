import unittest
import pages
from selenium import webdriver

class TestBasico(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.google.com")
        self.driver.implicitly_wait(10)
        
        
    def test_a_go_to_wikipedia_through_google_and_get_title(self):
        google_page = pages.GooglePage(self.driver)
        google_page.accept_cookies()
        google_page.search_text("wikipedia")
        search_results_page = pages.SearchResultsPage(self.driver)
        assert search_results_page.have_result_page("wikipedia"), "no estamos en la página correcta :("
        search_results_page.go_to_first_result()
        wikipedia_page = pages.WikipediaPage(self.driver)
        assert "Wikipedia, la enciclopedia libre" in wikipedia_page.get_page_title()
        title_articulo_bueno_hoy = wikipedia_page.get_articulo_bueno_title()        
        self.assertEqual("Torre del Catalán",title_articulo_bueno_hoy)
        
    def tearDown(self):
        self.driver.quit()
        
        
        
if __name__ == "__main__":
    unittest.main()