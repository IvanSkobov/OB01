class Store:
    def __init__(self, name, address):
        self.name = name  # Название магазина
        self.address = address  # Адрес магазина
        self.items = {}  # Словарь для хранения товаров и их цен

    def add_item(self, item_name, price): #Метод

        self.items[item_name] = price # Добавляем товар в магазин
        print(f"Товар '{item_name}' добавлен в магазин '{self.name}'.")

    def remove_item(self, item_name): #Метод

        if item_name in self.items: # Если товар есть в магазине
            del self.items[item_name]
            print(f"Товар '{item_name}' удален из магазина '{self.name}'.")
        else:
            print(f"Товар '{item_name}' отсутствует в магазине '{self.name}'.")

    def get_item_price(self, item_name): #Метод

        return self.items.get(item_name, None) # Возвращаем цену товара

    def update_item_price(self, item_name, new_price): #Метод

        if item_name in self.items: # Если товар есть в магазине
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' обновлена в магазине '{self.name}'.")
        else:
            print(f"Товар '{item_name}' отсутствует в магазине '{self.name}'.")

    def __str__(self): #Метод
        return (f"Магазин: {self.name}\n"
        f"Адрес: {self.address}\n"
        f"Ассортимент: {self.items}")


# Создаем несколько магазинов
store1 = Store("Фруктовый сад", "ул. Самарская, д. 21")
store2 = Store("Овощной дворик", "пр. Московская, д. 13")
store3 = Store("Молочный фермер", "ул. Уральская, д. 1")

# Добавляем товары в магазины
store1.add_item("яблоки", 150,)
store1.add_item("бананы", 100)
store1.add_item("апельсины", 180)

store2.add_item("картофель", 30)
store2.add_item("морковь", 25)
store2.add_item("лук", 20)

store3.add_item("молоко", 120)
store3.add_item("сыр", 250)
store3.add_item("йогурт", 100)

# Обновляем цену товара
store1.update_item_price("яблоки", 130)

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

# Выберем магазин "Фруктовый рай"
store = store1

# 1. Добавим новый товар
store.add_item("груши", 190)
print(store)  # Выведем информацию о магазине после добавления

# 2. Обновим цену товара
store.update_item_price("бананы", 95)
print(store)  # Выведем информацию о магазине после обновления цены

# 3. Удалим товар
store.remove_item("апельсины")
print(store)  # Выведем информацию о магазине после удаления

# 4. Запросим цену товара
price = store.get_item_price("груши")
print(f"Цена груш: {price}")

price = store.get_item_price("апельсины")  # Товар удален, должен вернуть None
print(f"Цена апельсинов: {price}")

# Выводим информацию о магазинах
print("\nИнформация о магазинах:")
print(store1)
print(store2)
print(store3)