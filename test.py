# Пространство имён
calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()  # Учитываем вызов функции
    length = len(string)
    upper_case = string.upper()
    lower_case = string.lower()
    return (length, upper_case, lower_case)

def is_contains(string, list_to_search):
    count_calls()  # Учитываем вызов функции
    # Приводим и строку, и элементы списка к нижнему регистру для сравнения
    string_lower = string.lower()
    return any(string_lower == item.lower() for item in list_to_search)

# Примеры вызовов функций
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))    # No matches

# Вывод количества вызовов
print(calls)

