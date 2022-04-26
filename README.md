# Практика использования TDD
Задача: Требуется найти самую длинную непрерывную цепочку нулей в последовательности нулей и единиц.
## Алгоритм разработки

1) Пишем падающий тест (tests/tests.py)
2) Пишем решение задачи
3) Проверяем прохождение теста
4) В случае падения найти и исправть ошибку
5) В случае успешного прохождения написать следующий тест
6) Повторяем предыдущие шаги

## Описание тестов

- Проверям работоспособность функции, когда на вход подается строка различных видов. Тест пройден, если ответ функции совпадает с ожиданием.
- Проверям работоспособность функции, когда на вход подается не строка (bool, float, int). Тест пройден, если функция выдает ошибку (-1).
