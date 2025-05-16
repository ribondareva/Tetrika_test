# Репозиторий с решениями задач на Python

## Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/ribondareva/Tetrika_test.git
cd Tetrika_test
```
2. Создайте виртуальное окружение и активируйте его (реализация в зависимости от Вашей ОС)
3. Установите зависимости
```bash
pip install -r requirements.txt
```
4. Запуск тестов (все тесты написаны с использованием unittest)
```bash
python -m unittest discover -s tests
```
Или запуск конкретного теста:
```bash
python -m unittest tests.test_solution_1
```
```bash
python -m unittest tests.test_solution_2
```
```bash
python -m unittest tests.test_solution_3
```
## Требования
Python 3.10+
