"""Напишіть функцію для сортування рядка в алфавітному порядку без врахування регістру літер.
Вхідні дані:
JavaScript
Python
Вихідні дані:
aaciJprStv
hnoPty
Голомоза Інна Андріївна"""

def sort(input_str):
    sorted_str = ''.join(sorted(list(input_str), key=str.lower))
    return sorted_str


# Введення даних
input_str1 = input("Введіть перший рядок: ")
input_str2 = input("Введіть другий рядок: ")

# Виклик функції для сортування рядків
result1 = sort(input_str1)
result2 = sort(input_str2)

# Виведення результатів
print("Відсортований перший рядок:", result1)
print("Відсортований другий рядок:", result2)

