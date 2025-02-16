class Store:
    def __init__(self, name, address):
        self.name = name  # Название магазина
        self.address = address  # Адрес магазина
        self.items = {}  # Словарь для хранения товаров и их цен

    def add_item(self, item_name, price):
        """Добавляет товар в ассортимент."""
        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен в магазин '{self.name}'.")

    def remove_item(self, item_name):
        """Удаляет товар из ассортимента."""
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален из магазина '{self.name}'.")
        else:
            print(f"Товар '{item_name}' отсутствует в магазине '{self.name}'.")

    def get_item_price(self, item_name):
        """Возвращает цену товара по его названию."""
        return self.items.get(item_name, None)

    def update_item_price(self, item_name, new_price):
        """Обновляет цену товара."""
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' обновлена в магазине '{self.name}'.")
        else:
            print(f"Товар '{item_name}' отсутствует в магазине '{self.name}'.")

    def __str__(self):
        """Возвращает строковое представление магазина."""
        return (f"Магазин: {self.name}\n"
                f"Адрес: {self.address}\n"
                f"Ассортимент: {self.items}")


# Создаем несколько магазинов
store1 = Store("Фруктовый рай", "ул. Пушкина, д. 10")
store2 = Store("Овощной дворик", "пр. Ленина, д. 25")
store3 = Store("Молочная ферма", "ул. Гагарина, д. 7")

# Добавляем товары в магазины
store1.add_item("яблоки", 0.5)
store1.add_item("бананы", 0.75)
store1.add_item("апельсины", 0.8)

store2.add_item("картофель", 0.3)
store2.add_item("морковь", 0.4)
store2.add_item("лук", 0.2)

store3.add_item("молоко", 1.2)
store3.add_item("сыр", 2.5)
store3.add_item("йогурт", 1.0)

# Обновляем цену товара
store1.update_item_price("яблоки", 0.6)

# Удаляем товар
store2.remove_item("лук")

# Получаем цену товара
price = store3.get_item_price("сыр")
print(f"Цена сыра в магазине '{store3.name}': {price}")

# Выводим информацию о магазинах
print("\nИнформация о магазинах:")
print(store1)
print(store2)
print(store3)