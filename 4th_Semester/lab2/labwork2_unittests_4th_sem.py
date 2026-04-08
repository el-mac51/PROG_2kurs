import unittest
import os

from labwork2_4th_sem import (
    centralbank_api,
    currency_decorator,
    yaml_decorator,
    csv_decorator,
)

class TestCentralBankApi(unittest.TestCase):
    """тесты для компонента получения данных с API ЦБ"""
    def test_get_data_returns_dict(self):
        """проверка что метод get_data возвращает словарь."""
        api = centralbank_api()
        result = api.get_data()
        
        self.assertIsInstance(result, dict)

    def test_get_data_contains_currency_keys(self):
        """проверка, что возвращаемый словарь содержит ключи валют"""
        api = centralbank_api()
        result = api.get_data()
        
        self.assertIn('Valute', result)
        self.assertIn('USD', result['Valute'])


class TestYamlDecorator(unittest.TestCase):
    """тесты для декоратора форматирования в YAML"""
    def setUp(self):
        self.api = centralbank_api()
        self.decorator = yaml_decorator(self.api)

    def test_get_data_returns_string(self):
        """проверка чтт get_data возвращает YAML-строку """
        result = self.decorator.get_data()
        self.assertIsInstance(result, str)

    def test_get_data_contains_yaml_content(self):
        """проверка что строка содержит данные в YAML-формате"""
        result = self.decorator.get_data()
        #YAML должен содержать и ключи и значения
        self.assertIn('USD', result)
        self.assertIn('90', result)

    def test_save_to_file_creates_file(self):
        """проверка save_to_file записывает в файл"""
        filename = 'test.yaml'
        self.decorator.save_to_file(filename)
        #проверяем, что файл был создан
        self.assertTrue(os.path.exists(filename))
        #удаляем тестовый файл после проверки
        os.remove(filename)


class TestCsvDecorator(unittest.TestCase):
    """тесты для декоратора форматирования в CSV"""
    def setUp(self):
        """подготовка создаём объект с замокированным API"""
        self.api = centralbank_api()
        self.decorator = csv_decorator(self.api)

    def test_get_data_returns_string(self):
        """проверка что get_data возвращает CSV-строку"""
        result = self.decorator.get_data()
        self.assertIsInstance(result, str)

    def test_get_data_contains_csv_format(self):
        """проверка что строка в CSV-формате"""
        result = self.decorator.get_data()
        #CSV должен иметь заголовки и значения через запятую
        self.assertIn('USD,EUR', result)

    def test_save_to_file_creates_file(self):
        """Проверка: save_to_file записывает данные в файл."""
        filename = 'test.csv'
        self.decorator.save_to_file(filename)
        #проверяем, что файл был создан
        self.assertTrue(os.path.exists(filename))
        #удаляем тестовый файл после проверки
        os.remove(filename)


class TestDecoratorChain(unittest.TestCase):
    """тесты для цепочки декораторов"""
    def test_decorator_delegation(self):
        """проверка что декоратор корректно делегирует вызов компоненту"""
        api = centralbank_api()
        decorator = currency_decorator(api)
        
        result = decorator.get_data()
        #проверяем, что результат тоже словарь (делегирование сработало)
        self.assertIsInstance(result, dict)

if __name__ == '__main__':
    unittest.main()