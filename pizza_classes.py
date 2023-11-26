from abc import ABC, abstractmethod


class Pizza(ABC):
    """Абстрактный класс для пиццы"""

    def __init__(self, size="L"):
        """Инициализирует пиццу"""
        self.size = size

    def change_size(self, new_size):
        """
        Меняет размер пиццы, при вызове метода
        в скобках указать новый размер
        """
        if new_size in ["L", "XL"]:
            self.size = new_size
        else:
            print("Invalid size")

    @staticmethod
    @abstractmethod
    def dict():
        """Абстрактный метод для вывода рецепта пиццы"""
        pass


class Margherita(Pizza):
    """Содержит информацию о пицце Маргарита"""

    @staticmethod
    def dict():
        """Выводит рецепт пиццы"""
        return {"Margherita": ["tomato sauce", "mozzarella", "tomatoes"]}


class Pepperoni(Pizza):
    """Содержит информацию о пицце Пепперони"""

    @staticmethod
    def dict():
        """Выводит рецепт пиццы"""
        return {"Pepperoni": ["tomato sauce", "mozzarella", "pepperoni"]}


class Hawaiian(Pizza):
    """Содержит информацию о Гавайской пицце"""

    @staticmethod
    def dict():
        """Выводит рецепт пиццы"""
        return {"Hawaiian": ["tomato sauce", "mozzarella",
                             "chicken", "pineapples"]}


assert Margherita(size="XL").dict() == {"Margherita": ["tomato sauce", "mozzarella", "tomatoes"]}
assert Pepperoni().dict() == {'Pepperoni': ['tomato sauce', 'mozzarella', 'pepperoni']}
assert Hawaiian().dict() == {'Hawaiian': ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']}
