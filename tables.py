import unittest
from selenium import webdriver

ROWS = 5 # Filas incluyendo el header
COLUMNS = 5

class Tables(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = './chromedriver')
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element_by_link_text("Sortable Data Tables").click()

    def test_sort_tables(self):
        driver = self.driver

        table_data = [[] for i in range(ROWS)]

        print()
        for fila in range(ROWS):
            for columna in range(COLUMNS):
                if fila == 0:
                    header = driver.find_element_by_xpath(f'//*[@id="table1"]/thead/tr/th[{columna + 1}]/span')
                    table_data[fila].append(header.text)
                else:
                    row_data = driver.find_element_by_xpath(f'//*[@id="table1"]/tbody/tr[{fila}]/td[{columna + 1}]')
                    table_data[fila].append(row_data.text)
            print(table_data[fila])
            

    
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity= 2)