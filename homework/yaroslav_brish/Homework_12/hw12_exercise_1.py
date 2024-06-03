# Задание №1

# Создать классы цветов: общий класс для всех цветов и классы для нескольких видов.
# Создать экземпляры (объекты) цветов разных видов.
# Собрать букет (букет - еще один класс) с определением его стоимости.
# В букете цветы пусть хранятся в списке. Это будет список объектов.

# Для букета создать метод, который определяет время его увядания по среднему
# времени жизни всех цветов в букете.

# Позволить сортировку цветов в букете на основе различных параметров
# (свежесть/цвет/длина стебля/стоимость)(это тоже методы)

# Реализовать поиск цветов в букете по каким-нибудь параметрам
# (например, по среднему времени жизни) (и это тоже метод).


class Flower:
    def __init__(self, name, color, stem_length, freshness, cost, lifespan):
        self.name = name
        self.color = color
        self.stem_length = stem_length
        self.freshness = freshness
        self.cost = cost
        self.lifespan = lifespan


class Rose(Flower):
    def __init__(self, color, stem_length, freshness, cost, lifespan=7):
        super().__init__("Rose", color, stem_length, freshness, cost, lifespan)


class Tulip(Flower):
    def __init__(self, color, stem_length, freshness, cost, lifespan=5):
        super().__init__("Tulip", color, stem_length, freshness, cost, lifespan)


class Lily(Flower):
    def __init__(self, color, stem_length, freshness, cost, lifespan=10):
        super().__init__("Lily", color, stem_length, freshness, cost, lifespan)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def total_cost(self):
        return sum(flower.cost for flower in self.flowers)

    def average_lifespan(self):
        if not self.flowers:
            return 0
        return sum(flower.lifespan for flower in self.flowers) / len(self.flowers)

    def sort_by(self, attribute):
        self.flowers.sort(key=lambda flower: getattr(flower, attribute))

    def find_by(self, attribute, value):
        return [flower for flower in self.flowers if getattr(flower, attribute) == value]


# Пример использования:
bouquet = Bouquet()
bouquet.add_flower(Rose(color="red", stem_length=40, freshness=9, cost=10))
bouquet.add_flower(Tulip(color="yellow", stem_length=35, freshness=8, cost=7))
bouquet.add_flower(Lily(color="white", stem_length=50, freshness=10, cost=15))

print(f"Букет содержит {len(bouquet.flowers)} цветов")
print(f"Общая стоимость букета: {bouquet.total_cost()}")
print(f"Среднее время увядания букета: {bouquet.average_lifespan().__round__(2)}")

bouquet.sort_by('cost')
print(f"Букет, отсортированный по стоимости: {[flower.name for flower in bouquet.flowers]}")

found_flowers = bouquet.find_by('color', 'red')
# print(f"Найденные цветы по цвету 'red': {found_flowers}")
print(f"Найденные цветы по цвету 'red': {[flower.name for flower in found_flowers]}")
