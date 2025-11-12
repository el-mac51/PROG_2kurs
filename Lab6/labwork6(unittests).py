from labwork6 import get_currencies
import unittest

class TestGetCurrencies(unittest.TestCase):
    def test_normal_operation(self):
        """тест нормальной работы"""
        result = get_currencies(['USD', 'EUR'])
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 2)
        self.assertIn('USD', result)
        self.assertIn('EUR', result)

    def test_nonexistent_currency(self):
        """тест с несуществующей валютой"""
        result = get_currencies(['USD', 'NOT_EXIST'])
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 1)  #должен вернуть  только usd
        self.assertIn('USD', result)

    def test_empty_currency_list(self):
        """тест с пустым списком"""
        result = get_currencies([])
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 0)  #должен вернуть пустой словарь

    def test_network_error(self):
        """тест с неправильным юрл"""
        result = get_currencies(['USD'], url='https://not-exist.ru/')
        self.assertIsNone(result)  #должен вернуть NOne и Error of network, без этой ошибки проверить работу с нерабочим юрл иначе не получится 

    def test_currency_case_sensitivity(self):
        """тест с регистром"""
        result = get_currencies(['usd', 'Eur']) 
        self.assertEqual(len(result), 0)   # должен вернуть пустой словарь, потому что используется только верхний регистр

    def test_rate_calculation(self):
        """тест вычисления курса """
        result = get_currencies(['USD', 'JPY'])
        if 'USD' in result:
            self.assertGreater(result['USD'], 1)  #курс должен быть > 1 рубля
        if 'JPY' in result:
            self.assertLess(result['JPY'], 1)  #курс йены должен быть < 1 рубля

if __name__ == "__main__":
    unittest.main()