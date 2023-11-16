import click
from random import randint


class Margherita:
    """Содержит информацию о пицце Маргарита"""

    def __init__(self, size: str = "L"):
        """Инициализирует пиццу"""
        self.size = size

    def change_size(self, new_size: str):
        """Меняет размер пиццы"""
        if new_size in ["L", "XL"]:
            self.size = new_size
        else:
            print("Invalid size")

    @staticmethod
    def dict():
        """Выводит рецепт пиццы"""
        return {"Margherita": ["tomato sauce", "mozzarella", "tomatoes"]}


class Pepperoni:
    """Содержит информацию о пицце Пепперони"""

    def __init__(self, size: str = "L"):
        """Инициализирует пиццу"""
        self.size = size

    def change_size(self, new_size: str):
        """Меняет размер пиццы"""
        if new_size in ["L", "XL"]:
            self.size = new_size
        else:
            print("Invalid size")

    @staticmethod
    def dict():
        """Выводит рецепт пиццы"""
        return {"Pepperoni": ["tomato sauce", "mozzarella", "pepperoni"]}


class Hawaiian:
    """Содержит информацию о Гавайской пицце"""

    def __init__(self, size: str = "L"):
        """Инициализирует пиццу"""
        self.size = size

    def change_size(self, new_size: str):
        """Меняет размер пиццы"""
        if new_size in ["L", "XL"]:
            self.size = new_size
        else:
            print("Invalid size")

    @staticmethod
    def dict():
        """Выводит рецепт пиццы"""
        return {"Hawaiian": ["tomato sauce", "mozzarella",
                             "chicken", "pineapples"]}


@click.group()
def cli():
    pass


@click.command()
@click.option("--delivery", default=False, is_flag=True)
@click.argument("pizza", nargs=1)
def order(pizza: str, delivery: bool):
    """
    Команда готовит пиццу, флаг --delivery передаёт её с курьером
    """
    click.echo(f"🧑‍🍳 ‍Приготовили {pizza} за {randint(1, 100)}с!")
    if delivery:
        click.echo(f"🛵 Доставили {pizza} за {randint(1, 100)}с!")


@click.command()
def menu():
    """Команда отображает доступное меню"""
    for pizza, ingredients in Margherita.dict().items():
        click.echo(f"- {pizza} 🧀: {', '.join(ingredients)}")
    for pizza, ingredients in Pepperoni.dict().items():
        click.echo(f"- {pizza} 🍕: {', '.join(ingredients)}")
    for pizza, ingredients in Hawaiian.dict().items():
        click.echo(f"- {pizza} 🍍: {', '.join(ingredients)}")


cli.add_command(order)
cli.add_command(menu)


def log(function):
    """Декоратор номер 1"""

    def wrapper(pizza):
        """Выводит название функции и время выполнения"""
        print(f"{function.__name__} - {randint(1, 100)}с")
        return pizza

    return wrapper


def log_second(text):
    """Бонусный декоратор"""

    def decorator(function):
        def wrapper_second(pizza):
            print(text.format(randint(1, 100)))
            return function, pizza

        return wrapper_second

    return decorator


@log
def bake(pizza):
    """Функция готовит пиццу"""
    print(f"Приготовили пиццу {pizza}")


@log_second("🛵 Доставили за {}с!")
def delivery_pizza(pizza):
    """Доставляет пиццу"""
    print(f"Доставили {pizza}")


@log_second("🏠 Забрали за {}с!")
def pickup(pizza):
    """Самовывоз"""
    print(f"Самовывоз {pizza}")


bake(Margherita())
delivery_pizza(Margherita())
pickup(Margherita())


if __name__ == "__main__":
    cli()
