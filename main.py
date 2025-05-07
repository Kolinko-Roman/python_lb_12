from tabulate import tabulate

# Завдання 1. «Інвентаризація товарів»
inventory = [
    {"назва": "Ноутбук", "кількість": 10, "ціна": 25000, "категорія": "електроніка"},
    {"назва": "Футболка", "кількість": 30, "ціна": 400, "категорія": "одяг"},
    {"назва": "Телевізор", "кількість": 5, "ціна": 15000, "категорія": "електроніка"},
    {"назва": "Хліб", "кількість": 50, "ціна": 25, "категорія": "продукти"},
    {"назва": "Куртка", "кількість": 3, "ціна": 2500, "категорія": "одяг"},
    {"назва": "Молоко", "кількість": 20, "ціна": 30, "категорія": "продукти"},
    {"назва": "Навушники", "кількість": 15, "ціна": 1200, "категорія": "електроніка"},
]

print("Інвентаризація товарів:\n")
print(tabulate(inventory, headers="keys", tablefmt="grid"))

# Завдання 2. «Складний пошук та редагування»
def search_and_update():
    criteria = input("\nПошук за назвою або категорією (введіть 'назва' або 'категорія'): ").strip().lower()
    keyword = input("Введіть ключове слово для пошуку: ").strip()

    found = [item for item in inventory if item.get(criteria, "").lower() == keyword.lower()]
    if not found:
        print("Товар не знайдено.")
        return

    print("\nЗнайдені товари:")
    print(tabulate(found, headers="keys", tablefmt="grid"))

    try:
        name = input("\nВведіть назву товару для оновлення: ").strip()
        product = next(item for item in inventory if item["назва"].lower() == name.lower())
        field = input("Що хочете змінити? ('кількість' або 'ціна'): ").strip().lower()
        if field not in ["кількість", "ціна"]:
            print("Невірне поле для редагування.")
            return
        new_value = float(input(f"Введіть нове значення для {field}: "))
        if new_value < 0:
            print("Значення не може бути менше 0.")
            return
        product[field] = int(new_value) if field == "кількість" else new_value
        print(f"{field.capitalize()} оновлено успішно.")
    except StopIteration:
        print("Товар не знайдено.")
    except ValueError:
        print("Некоректне значення. Введіть число.")

search_and_update()

# Завдання 3. «Аналітика складу та фінансів»
print("\nАналітика складу:\n")
category_totals = {}
low_stock = []

for item in inventory:
    total = item["кількість"] * item["ціна"]
    category = item["категорія"]
    category_totals[category] = category_totals.get(category, 0) + total
    if item["кількість"] < 5:
        low_stock.append(item)

print("Загальна вартість по категоріях:")
for cat, total in category_totals.items():
    print(f"- {cat.capitalize()}: {total:.2f} грн")

max_category = max(category_totals.items(), key=lambda x: x[1])
print(f"\nКатегорія з найбільшою сумарною вартістю: {max_category[0].capitalize()} ({max_category[1]:.2f} грн)")

print("\nТовари, які потребують поповнення (менше 5 шт.):")
if low_stock:
    print(tabulate(low_stock, headers="keys", tablefmt="grid"))
else:
    print("Усі товари в достатній кількості.")
