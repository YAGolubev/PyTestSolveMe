# PyTestSolveMe
--------------------------------------------------------------------------------
- >python -m venv venv
- >venv\Scripts\activate
- (venv) >python -V
--------------------------------------------------------------------------------
https://www.youtube.com/playlist?list=PLB2iiSfKWtvykq9s0plSVI_Du60i0iphU
- 1 Пишем свои первые автотесты
  - в названии каталога, файла и функции должно быть "test" в начале или конце
  - (venv) >python.exe -m pip install --upgrade pip
  - (venv) >pip install pytest
  - (venv) >pip freeze > requirements.txt
  - (venv) >pytest .
  - (venv) >pytest tests/.        (windows)
  - (venv) >pytest tests/*        (linux?) `В папке у тебя лежит __init__, который запускает все тесты и сам файл с тестами. Таким образом, когда ты запускаешь тесты через *, они запускаются дважды: сначала через init, потом из something_test. А когда пишешь просто something_test, то тесты проходят один раз`
    `pytest` - выводит названия тестов (файлов) и процент выполнения от числа файлов  
    `pytest -v` - выводит название "файл.py::test_имя_функции PASSED" и процент выполнения от числа функций/методов
    `pytest -s` - выводит все print() внутри тестов
    `pytest -s -v test_name.py` выполнит только методы указанного файла теста
  - 
- 2 Усложняем задачу, добавив первый реквест
  - (venv) >pip install requests
  - (venv) >pip freeze > requirements.txt
  - My JSON Server - Fake online REST server for teams https://my-json-server.typicode.com/
  - https://my-json-server.typicode.com/typicode/demo/posts
  - (venv) >pytest -s -v tests\somesing_test.py
- 
- 3.1 Улучшаем валидацию объектов и работаем с jsonschema
  - (venv) >pip install jsonschema
  - (venv) >pip freeze > requirements.txt
  - Мне кажется плохая практика возвращать self. Можно отдельно сделать response.validate(POST_SCHEMA)

- 3.2 Используем pydantic для валидации данных в тестах
  - (venv) >pip install pydantic==1.10.12
  - (venv) >pip freeze > requirements.txt
  - 
- 3.3 Пишем тесты близкие к боевым условиям и бустим AssertError log
- 4.1 Fixtures, conftest. Зачем они и как с ними работать.
  - `@pytest.fixture(scope="function")` default выполняется каждый раз
  - `@pytest.fixture(scope="session")` выполняется единожды и результат кэшируется (логин, подключение к БД)
  - `@pytest.fixture(autouse=True, scope="session")` выполняется для каждого теста и не требует указания имени `def test_getting_users_list(say_hello):` опасно без `scope="session"`
- 4.2 Fixtures и conftest интересные фичи которые стоит знать
- 5 Декораторы для тестов. Parametrize, skip, duration, custom params
- 6 Создаём красивый allure report для результатов тестов
- 7.1 Пишем простенький и элегантный билдер для генерации данных
- 7.2 Работаем с билдерами и данными на любом уровне вложенности
- 8 Детальный разбор pydantic и способы работы с ним в автотестах
- 9.1 Подключаем SQLAlchemy к проекту и делаем простые запросы в базу
- 9.2 Используем SQLAlcmemy в автотестах в связке с билдерами
- 10.1 Создаём Dockerfile и запускаем наши тесты внутри контейнера
- 10.2 Оптимизируем наш Docker контейнер с автотестами
- 11 Дополнительная информация о fixtures, parametrize, run options