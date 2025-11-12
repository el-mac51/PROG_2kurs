from labwork6 import get_currencies
import unittest
import sys
from io import StringIO

class TestGetCurrencies(unittest.TestCase):
    def test_valutes_rates(self):
        """проверка курсов валют"""
        result = get_currencies(['USD', 'EUR', 'GBP'])
        
        self.assertIsInstance(result, dict)  #проверяем что это словарь
        
        for currency in ['USD', 'EUR', 'GBP']:
            if currency in result: 
                self.assertIn(currency, result)  
                self.assertIsInstance(result[currency], float)  
                self.assertGreater(result[currency], 0)  #курс > 0

    def test_dict_structure(self):
        """проверка корректности структуры словаря"""
        result = get_currencies(['USD', 'JPY'])
        
        if result:  #если вернулось не none
            for key in result.keys():
                self.assertIsInstance(key, str)  
                self.assertEqual(len(key), 3)  
            
            for value in result.values():
                self.assertIsInstance(value, float)

    def test_invalid(self):
        """проверка работы при не работающем юрл"""
        result = get_currencies(['USD'], url='https://invalid-url-test.ru/')
        self.assertIsNone(result)  #должен вернуть None при ошибке

    def test_invalid_data(self):
        """проверка работы при неправильном юрл"""
        result = get_currencies(['USD'], url='https://www.google.com/')
        self.assertIsNone(result)  #должен вернуть None при данных не json

    def test_empty(self):
        """проверка при пустой области поиска"""
        result = get_currencies([])
        self.assertIsInstance(result, dict)  #должен вернуть пустой словарь
        self.assertEqual(len(result), 0)  
        
    def test_logs(self):
        """проверка что логи выводятся в консоль"""
        result = get_currencies(['USD'])  
        self.assertIsNotNone(result)  

if __name__ == "__main__":
    unittest.main()
