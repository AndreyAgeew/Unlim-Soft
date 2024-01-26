class Player:
    """
    Класс представляющий игрока в турнире.
    """

    def __init__(self, name, rating):
        """
        Инициализация объекта игрока.

        :param name: Имя игрока.
        :param rating: Начальный рейтинг игрока.
        """
        self.name = name
        self.rating = rating

    def __str__(self):
        """
        Возвращает строковое представление игрока.

        :return: Строковое представление.
        """
        return f"{self.name} (Rating: {self.rating})"
