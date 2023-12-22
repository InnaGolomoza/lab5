"""Дано базу даних про продажі деякого інтернет-магазину. Кожен рядок вхідного файлу є записом виду Покупець Товар Кількість, де Покупець - ім’я покупця (рядок без пропусків), Товар - назва товару (рядок без пропусків), Кількість - кількість придбаних одиниць товару. Створіть список всіх покупців, а для кожного покупця підрахуйте кількість придбаних ним одиниць кожного виду товарів. Вводяться відомості про покупки в зазначеному форматі як у вхідних даних. Виведіть список всіх покупців в лексикографічному порядку, після імені кожного покупця виведіть двокрапка, потім виведіть список назв всіх придбаних даними покупцем товарів в лексикографічному порядку, після назви кожного товару виведіть кількість одиниць товару, придбаних даними покупцем. Інформація про кожен товар виводиться в окремому рядку.
Вхідні дані:
Вхідний файл input.txt з текстом
Sasha paper 10
Iryna pens 5
Sasha marker 3
Sasha paper 7
Iryna envelope 20
Sasha envelope 5
Вихідні дані:
Iryna:
envelope 20
pens 5
Sasha:
envelope 5
marker 3
paper 17

Голомоза Інна Андріївна"""
# Ініціалізація словника
customer_data = {}

# Зчитування та обробка вхідних даних
with open('input.txt', 'r') as file:
    for line in file:
        if not line.strip():
            continue

        customer, product, quantity = line.strip().split()
        quantity = int(quantity)

        # Додавання інформації до словника
        if customer not in customer_data:
            customer_data[customer] = {}
        if product not in customer_data[customer]:
            customer_data[customer][product] = 0
        customer_data[customer][product] += quantity

# Сортування імен покупців у лексикографічному порядку
sorted_customers = sorted(customer_data.keys())

# Запис результатів у вихідний файл
with open('output.txt', 'w') as file:
    for customer in sorted_customers:
        file.write(f"{customer}:\n")
        for product, quantity in sorted(customer_data[customer].items()):
            file.write(f"{product} {quantity}\n")          



