import unittest
from selenium import webdriver

class TestingMercadoLibre(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = './chromedriver')
        driver = self.driver
        driver.get('https://mercadolibre.com/')
        driver.maximize_window()

    def test_search_ps4(self):
        driver = self.driver

        country = driver.find_element_by_id('CO')
        country.click()

        search_field = driver.find_element_by_name('as_word')
        search_field.click()
        search_field.clear()
        search_field.send_keys('playstation 4')
        search_field.submit()

        location = driver.find_element_by_partial_link_text('Bogotá D.C.')
        driver.execute_script("arguments[0].click();", location)

        condition = driver.find_element_by_partial_link_text('Nuevo')
        driver.execute_script("arguments[0].click();", condition)

        order_menu = driver.find_element_by_class_name('andes-dropdown__trigger')
        order_menu.click()
        higher_price = driver.find_element_by_xpath('//*[@id="root-app"]/div/div/section/div[1]/div/div/div[2]/div[1]/div/div/div/ul/li[3]/a/div/div')
        higher_price.click()

        articles = []
        prices = []

        for contador in range(5):
            if contador == 2:
                article_name = driver.find_element_by_xpath(f'/html/body/main/div/div/section/ol/li[{contador + 1}]/div/div/div[2]/div[2]/a/h2').text
                articles.append(article_name)
                article_price = driver.find_element_by_xpath(f'/html/body/main/div/div/section/ol/li[{contador + 1}]/div/div/div[2]/div[3]/div[1]/div[1]/div/div/span[1]/span[2]').text
                prices.append(article_price)
            else:
                article_name = driver.find_element_by_xpath(f'/html/body/main/div/div/section/ol/li[{contador + 1}]/div/div/div[2]/div[1]/a/h2').text
                articles.append(article_name)
                article_price = driver.find_element_by_xpath(f'/html/body/main/div/div/section/ol/li[{contador + 1}]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/span[1]/span[2]').text
                prices.append(article_price)

        print()
        print(articles)
        print(prices)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity= 2)