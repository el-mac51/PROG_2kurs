import requests
import logging
import sys

def setup_logging(): #настраиваем систему логирования
    logger = logging.getLogger('currency_app')
    logger.setLevel(logging.DEBUG) #настраиваем уровень важности, условно важность 1 из 5
    formatter = logging.Formatter( #формат для сообщений
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s', #задаем вид вывода лога, время-имя-уровень-сообщение
        datefmt = '%Y-%m-%d %H:%M:%S'   #вид вывода времени в логе
    )

    console_handler = logging.StreamHandler(sys.stdout) #задаем вывод логов в консоль
    console_handler.setLevel(logging.INFO) #в консоль идет все от уровня INFO 
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler('currency_errors.log', encoding='utf-8') #задаем вывод логов в файл
    file_handler.setLevel(logging.WARNING) #в файл отправляем только сообщения уровня WARNING и ERROR
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler) #для обработки логгера
    logger.addHandler(file_handler)

    return logger

def log_errors(func): #ДЕКОРАТОР!!
    logger = setup_logging()
    def wrapper(currency_codes, url='https://www.cbr-xml-daily.ru/daily_json.js'):
        logger.info("Launching function {func.__name__}") #для красивого вывода логов, да и чтобы было что выводить, можно спустить на уровень ниже до дебага
        logger.info(f"Asked valutes: {currency_codes}")
        logger.debug(f" {url}") #это видно только на уровне debug, убедится можно если в 14й строке INFO  заменить на DEBUG

        try: #структура try/except добавлена для понтов и упрощения жизни, каюсь, к такой идее пришел не своей головой
            result = func(currency_codes, url)
            if result is not None:
                logger.info(f"Function is completed successfully, found {len(result)} valutes")
            else:
                logger.warning("Fucntion returned None") #warning - дла некритичных ошибок
            return result
        
        except requests.exceptions.RequestException as e:
            logger.error(f"Error of network: {e}") 
            return None
        except Exception as e:
            logger.error(f"Critical error: {e}")
            return None
    return wrapper

@log_errors
def get_currencies(currency_codes, url='https://www.cbr-xml-daily.ru/daily_json.js'):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Server returned status {response.status_code}")
    data = response.json() #преобразуем данны
    if "Valute" not in data:
        raise Exception("No 'Valute' in data")
    all_currencies = data["Valute"]
    result = {} #словарь для резулььтатов
    for currency_code in currency_codes:
        if currency_code in all_currencies:
            currency_data = all_currencies[currency_code]
            nominal = currency_data["Nominal"]
            value = currency_data["Value"]
            rate = value / nominal #вычисляем курс валюты
            result[currency_code] = rate
    return result

# if __name__ == "__main__":
#     print("=== test1: normal work ===")
#     result1 = get_currencies(['USD', 'EUR', 'JPY'])
#     print(f"result is {result1}\n")

#     print("=== test2: with non existant value ===")
#     result2 = get_currencies(['USD', 'NOT_EXIST'])
#     print(f"result is {result2}\n")

#     print("=== test3: with wrong url ===")
#     result3 = get_currencies(['USD'], url='https://несуществует.ру')
#     print(f"result: {result3}\n")

#     print("for mistakes logs check 'currency_errors.log'")