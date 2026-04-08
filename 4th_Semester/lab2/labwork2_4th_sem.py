
import requests
import yaml
import csv 
import io

from abc import ABC, abstractmethod 

class currency_component(ABC):
    """базовый интерфейс для компонентов получения курсов валют"""
    @abstractmethod
    def get_data(self) -> dict:
        """получить данные о курсах валют в виде словаря"""
        pass

class centralbank_api(currency_component):
    '''конкретный компонент который получает данные с api цб'''
    def get_data(self) -> dict:
        '''запросить актульные курсы и вернуть их в виде словаря'''
        response = requests.get(url = 'https://www.cbr-xml-daily.ru/daily_json.js')
        data = response.json()
        return data

class currency_decorator(currency_component):
    '''базовый декоратор который хранит ссылку на обернутый компоент'''
    def __init__(self, component: currency_component):
        '''инициализация декоратора с обернутым компонентом'''
        self._component = component

    def get_data(self) -> dict:
        '''делегировать получение данных обернутому компоненту'''
        return self._component.get_data()

class yaml_decorator(currency_decorator):
    '''декоратор для преобразования данных в формате YAML'''
    def get_data(self) -> str:
        '''получить данные и вернуть их как YAML строку'''
        data = self._component.get_data()
        result = yaml.dump(data, default_flow_style=False, allow_unicode=True)
        return result
    
    def save_to_file(self, filename: str) -> None:
        '''сохранить YAML-данные в файл'''
        text_data = self.get_data()
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(text_data)

class csv_decorator(currency_decorator):
    '''декоратор для преобразования данных в csv'''
    def get_data(self) -> str:
        full_data = self._component.get_data()
        simple_data = {}
        for code, info in full_data['Valute'].items():
            simple_data[code] = info['Value']    
        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames = simple_data.keys())
        writer.writeheader()
        writer.writerow(simple_data)
        return output.getvalue()
    
    def save_to_file(self, filename: str) -> None:
        '''сохранить csv данные в фай'''
        text_data = self.get_data()
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(text_data)
