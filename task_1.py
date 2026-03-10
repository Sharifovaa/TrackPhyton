if __name__ == "__main__":
    from abc import ABC, abstractmethod
    from typing import List, Optional, Dict, Any
    from datetime import date


    class ConiferousTree(ABC):
        """
        Базовый класс для хвойных деревьев.

        Атрибуты:
            _species (str): Вид дерева (непубличный, защищен от изменений после создания)
            _age (int): Возраст дерева в годах (непубличный, инкапсулирован для контроля корректности)
            _height (float): Высота дерева в метрах (непубличный, изменяется только через рост)
            location (str): Местоположение дерева
            _is_healthy (bool): Здорово ли дерево (непубличный, состояние здоровья)

        Причина инкапсуляции:
            - _species: Вид не должен меняться после создания дерева
            - _age: Возраст должен увеличиваться только через специальный метод
            - _height: Высота изменяется только в процессе роста
            - _is_healthy: Состояние здоровья изменяется через методы ухода/болезни
        """

        def __init__(self, species: str, age: int, height: float, location: str = "Не указано") -> None:
            """
            Инициализация хвойного дерева.

            Args:
                species: Вид дерева (ель, сосна и т.д.)
                age: Возраст в годах
                height: Высота в метрах
                location: Местоположение
            """
            self._species = species
            self._age = max(0, age)
            self._height = max(0.1, height)
            self.location = location
            self._is_healthy = True
            self._last_watering_date: Optional[date] = None

        def __str__(self) -> str:
            health_status = "здорово" if self._is_healthy else "требует ухода"
            return (f"{self._species} (возраст: {self._age} лет, высота: {self._height:.1f} м, "
                    f"местоположение: {self.location}, состояние: {health_status})")

        def __repr__(self) -> str:
            return (f"ConiferousTree(species='{self._species}', age={self._age}, "
                    f"height={self._height}, location='{self.location}')")

        @property
        def age(self) -> int:
            return self._age

        @property
        def height(self) -> float:
            return self._height

        def grow(self, years: int = 1) -> None:

            if years <= 0:
                raise ValueError("Количество лет должно быть положительным")

            self._age += years
            self._height += years * 0.3

        def water(self) -> None:
            self._last_watering_date = date.today()
            print(f"{self._species} полит(о)")

        def get_watering_status(self) -> str:

            if self._last_watering_date:
                days_since = (date.today() - self._last_watering_date).days
                return f"Последний полив был {days_since} дней назад"
            return "Дерево еще не поливалось"

        def get_info(self) -> Dict[str, Any]:

            return {
                'species': self._species,
                'age': self._age,
                'height': self._height,
                'location': self.location,
                'is_healthy': self._is_healthy,
                'watering_status': self.get_watering_status()
            }

        @abstractmethod
        def get_wood_density(self) -> float:

            pass


    class Spruce(ConiferousTree):
        """
        Класс Ели, наследующийся от ConiferousTree.

        Дополнительные атрибуты:
            _cone_size (str): Размер шишек (мелкие, средние, крупные) - непубличный
            has_decorations (bool): Украшено ли дерево (для новогодних елей)
            _needle_softness (int): Мягкость иголок (1-10) - непубличный

        Причина инкапсуляции:
            - _cone_size: Характеристика вида, не должна меняться произвольно
            - _needle_softness: Определяется видом и условиями роста, изменяется через методы
        """

        def __init__(self, age: int, height: float, location: str = "Не указано",
                     cone_size: str = "средние", has_decorations: bool = False) -> None:
            """
            Расширенный конструктор для Ели.

            Args:
                age: Возраст в годах
                height: Высота в метрах
                location: Местоположение
                cone_size: Размер шишек (мелкие/средние/крупные)
                has_decorations: Украшено ли дерево
            """
            super().__init__("Ель", age, height, location)
            self._cone_size = cone_size
            self.has_decorations = has_decorations
            self._needle_softness = 3

        def __str__(self) -> str:
            """
            Перегруженный метод строкового представления.

            Причина перегрузки: Необходимо добавить информацию о шишках и украшениях,
            которые специфичны только для елей.
            """
            base_str = super().__str__()
            decoration_status = "украшена" if self.has_decorations else "не украшена"
            return (f"{base_str} [Ель: шишки {self._cone_size}, {decoration_status}, "
                    f"мягкость иголок: {self._needle_softness}/10]")

        def __repr__(self) -> str:
            """
            Перегруженный метод для отладки.

            Причина перегрузки: Для корректного воссоздания объекта Spruce необходимы
            все специфические атрибуты ели.
            """
            return (f"Spruce(age={self._age}, height={self._height}, location='{self.location}', "
                    f"cone_size='{self._cone_size}', has_decorations={self.has_decorations})")

        def get_wood_density(self) -> float:
            """
            Перегруженный метод получения плотности древесины для ели.

            Причина перегрузки: Каждый вид хвойных деревьев имеет свою плотность
            древесины. У ели она составляет около 450 кг/м³.

            Returns:
                float: Плотность древесины ели в кг/м³
            """
            return 450.0

        def grow(self, years: int = 1) -> None:
            """
            Перегруженный метод роста для ели.

            Причина перегрузки: Ели растут медленнее среднего (особенно в первые годы),
            поэтому формула роста должна быть скорректирована с учетом возраста.

            Args:
                years: Количество лет роста
            """
            if years <= 0:
                raise ValueError("Количество лет должно быть положительным")

            super().grow(years)

            growth_rate = 0.2
            if self._age < 10:
                growth_rate = 0.15
            elif self._age > 50:
                growth_rate = 0.1

            self._height += years * growth_rate

        def drop_needles(self) -> int:
            """
            Специфический для ели метод - сбрасывание иголок.

            Returns:
                int: Количество сброшенных иголок (условно)
            """
            dropped = int(self._height * 1000)
            print(f"Ель сбросила примерно {dropped} иголок")
            return dropped

        def decorate(self) -> None:
            """
            Украшение ели (специфический метод).
            """
            self.has_decorations = True
            print(f"Ель в {self.location} украшена к празднику!")

        def get_watering_status(self) -> str:

            return super().get_watering_status()


    class Pine(ConiferousTree):
        """
        Класс Сосны, наследующийся от ConiferousTree.

        Дополнительные атрибуты:
            _needle_length (float): Длина иголок в см (непубличный)
            _resin_content (float): Содержание смолы (1-10) - непубличный
            has_pine_nuts (bool): Есть ли шишки с орешками

        Причина инкапсуляции:
            - _needle_length: Зависит от вида и условий, изменяется в процессе роста
            - _resin_content: Важная характеристика, используется для расчета качества древесины
        """

        def __init__(self, age: int, height: float, location: str = "Не указано",
                     needle_length: float = 8.0, has_pine_nuts: bool = False) -> None:
            """
            Расширенный конструктор для Сосны.

            Args:
                age: Возраст в годах
                height: Высота в метрах
                location: Местоположение
                needle_length: Длина иголок в см
                has_pine_nuts: Есть ли шишки с орешками
            """
            super().__init__("Сосна", age, height, location)
            self._needle_length = needle_length
            self.has_pine_nuts = has_pine_nuts
            self._resin_content = 7

        def __str__(self) -> str:
            """
            Перегруженный метод строкового представления.

            Причина перегрузки: Необходимо отобразить специфические для сосны
            характеристики (длина иголок, наличие орешков).
            """
            base_str = super().__str__()
            nuts_status = "есть орешки" if self.has_pine_nuts else "нет орешков"
            return (f"{base_str} [Сосна: иголки {self._needle_length} см, {nuts_status}, "
                    f"смолистость: {self._resin_content}/10]")

        def __repr__(self) -> str:
            """
            Перегруженный метод для отладки.

            Причина перегрузки: Для точного воссоздания объекта Pine нужны
            специфические атрибуты сосны.
            """
            return (f"Pine(age={self._age}, height={self._height}, location='{self.location}', "
                    f"needle_length={self._needle_length}, has_pine_nuts={self.has_pine_nuts})")

        def get_wood_density(self) -> float:
            """
            Перегруженный метод получения плотности древесины для сосны.

            Причина перегрузки: Плотность древесины сосны отличается от ели
            и составляет около 520 кг/м³.

            Returns:
                float: Плотность древесины сосны в кг/м³
            """
            return 520.0

        def grow(self, years: int = 1) -> None:
            """
            Перегруженный метод роста для сосны.

            Причина перегрузки: Сосны растут быстрее елей, особенно в молодости,
            и формула роста должна это учитывать.

            Args:
                years: Количество лет роста
            """
            if years <= 0:
                raise ValueError("Количество лет должно быть положительным")

            self._age += years


            growth_rate = 0.4
            if self._age > 30:
                growth_rate = 0.25

            self._height += years * growth_rate


            self._needle_length += years * 0.1

        def collect_resin(self) -> float:
            """
            Специфический для сосны метод - сбор смолы.

            Returns:
                float: Количество собранной смолы в литрах
            """
            collected = self._height * self._resin_content * 0.1
            print(f"Собрано {collected:.1f} л смолы с сосны")
            return collected

        def get_watering_status(self) -> str:
            """
            Унаследованный метод без изменений.

            Используется реализация из базового класса ConiferousTree.
            """
            return super().get_watering_status()

pass