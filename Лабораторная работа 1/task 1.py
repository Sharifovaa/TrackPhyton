# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Tree:
    def __init__(self, species: str, height: float, age: int):
        """
        Создание и подготовка к работе объекта "Дерево"

        :param species: Вид дерева
        :param height: Высота дерева в метрах
        :param age: Возраст дерева в годах

        Примеры:
        >>> tree = Tree("Дуб", 15.5, 50)
        """
        if not isinstance(species, str):
            raise TypeError("Вид дерева должен быть строкой")
        if not species:
            raise ValueError("Вид дерева не может быть пустым")
        self.species = species

        if not isinstance(height, (int, float)):
            raise TypeError("Высота дерева должна быть числом")
        if height <= 0:
            raise ValueError("Высота дерева должна быть положительным числом")
        self.height = float(height)

        if not isinstance(age, int):
            raise TypeError("Возраст дерева должен быть целым числом")
        if age < 0:
            raise ValueError("Возраст дерева не может быть отрицательным")
        self.age = age

    def grow(self, years: int) -> float:
        """
        Рост дерева в течение определенного количества лет.

        :param years: Количество лет для роста
        :return: Новая высота дерева
        :raise ValueError: Если количество лет отрицательное

        Примеры:
        >>> tree = Tree("Дуб", 15.5, 50)
        """
        ...

    def produce_oxygen(self, hours: int) -> float:
        """
        Производство кислорода деревом.

        :param hours: Количество часов производства кислорода
        :return: Количество произведенного кислорода в литрах
        :raise ValueError: Если количество часов отрицательное

        Примеры:
        >>> tree = Tree("Дуб", 15.5, 50)
        """
        ...

    def is_deciduous(self) -> bool:
        """
        Проверка, является ли дерево лиственным.

        :return: True если дерево лиственное, False если хвойное

        Примеры:
        >>> tree = Tree("Дуб", 15.5, 50)
        """
        ...


class Table:
    def __init__(self, material: str, width: float, height: float):
        """
        Создание и подготовка к работе объекта "Стол"

        :param material: Материал стола (дерево, стекло, металл и т.д.)
        :param width: Ширина стола в метрах
        :param height: Высота стола в метрах

        Примеры:
        >>> table = Table("дерево", 1.2, 0.8)
        """
        if not isinstance(material, str):
            raise TypeError("Материал стола должен быть строкой")
        if not material:
            raise ValueError("Материал стола не может быть пустым")
        self.material = material

        if not isinstance(width, (int, float)):
            raise TypeError("Ширина стола должна быть числом")
        if width <= 0:
            raise ValueError("Ширина стола должна быть положительным числом")
        self.width = float(width)

        if not isinstance(height, (int, float)):
            raise TypeError("Высота стола должна быть числом")
        if height <= 0:
            raise ValueError("Высота стола должна быть положительным числом")
        self.height = float(height)

    def calculate_area(self) -> float:
        """
        Расчет площади поверхности стола.

        :return: Площадь поверхности стола в квадратных метрах

        Примеры:
        >>> table = Table("дерево", 1.2, 0.8)
        """
        ...

    def set_table(self, number_of_plates: int) -> bool:
        """
        Накрыть стол для определенного количества персон.

        :param number_of_plates: Количество тарелок (количество персон)
        :return: True если стол можно накрыть, False если недостаточно места
        :raise ValueError: Если количество тарелок отрицательное

        Примеры:
        >>> table = Table("дерево", 1.2, 0.8)
        """
        ...

    def can_hold_weight(self, weight: float) -> bool:
        """
        Проверка, может ли стол выдержать определенный вес.

        :param weight: Вес в килограммах
        :return: True если стол может выдержать вес, False если нет
        :raise ValueError: Если вес отрицательный

        Примеры:
        >>> table = Table("дерево", 1.2, 0.8)
        """
        ...


class SocialMedia:
    def __init__(self, name: str, user_count: int, year_founded: int):
        """
        Создание и подготовка к работе объекта "Социальная сеть"

        :param name: Название социальной сети
        :param user_count: Количество пользователей
        :param year_founded: Год основания

        Примеры:
        >>> social_media = SocialMedia("ExampleSocial", 1000000, 2010) 
        """
        if not isinstance(name, str):
            raise TypeError("Название социальной сети должно быть строкой")
        if not name:
            raise ValueError("Название социальной сети не может быть пустым")
        self.name = name

        if not isinstance(user_count, int):
            raise TypeError("Количество пользователей должно быть целым числом")
        if user_count < 0:
            raise ValueError("Количество пользователей не может быть отрицательным")
        self.user_count = user_count

        if not isinstance(year_founded, int):
            raise TypeError("Год основания должен быть целым числом")
        if year_founded < 2000 or year_founded > 2024:
            raise ValueError("Год основания должен быть между 2000 и 2024")
        self.year_founded = year_founded

    def create_post(self, user_id: int, content: str) -> str:
        """
        Создание поста в социальной сети.

        :param user_id: ID пользователя
        :param content: Содержимое поста
        :return: ID созданного поста
        :raise ValueError: Если ID пользователя отрицательный или содержание пустое

        Примеры:
        >>> social_media = SocialMedia("ExampleSocial", 1000000, 2010)
        """
        ...

    def get_user_info(self, user_id: int) -> dict:
        """
        Получение информации о пользователе.

        :param user_id: ID пользователя
        :return: Словарь с информацией о пользователе
        :raise ValueError: Если ID пользователя отрицательный

        Примеры:
        >>> social_media = SocialMedia("ExampleSocial", 1000000, 2010)
        """
        ...


if __name__ == "__main__":
    doctest.testmod(verbose=True)  # тестирование примеров, которые находятся в документации
    # TODO работоспособность экземпляров класса проверить с помощью doctest
