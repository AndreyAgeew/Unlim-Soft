from random import shuffle

from .match import Match


class Tournament:
    """
    Класс представляющий турнир, управляющий проведением матчей и сохранением результатов.
    """

    def __init__(self, players):
        """
        Инициализация объекта турнира.

        :param players: Список игроков, участвующих в турнире.
        """
        self.players = players
        self.matches = []

    def play_group_stage(self, groups):
        """
        Проведение матчей в групповом этапе.

        :param groups: Разбиение игроков на группы.
        """
        for group in groups:
            shuffle(group)
            for i in range(len(group)):
                for j in range(i + 1, len(group)):
                    match = Match(group[i], group[j], 'play')
                    self.matches.append(match)

    def get_group_results(self):
        """
        Получение результатов группового этапа и формирование общего списка для плей-офф.

        :return: Упорядоченный список игроков для плей-офф.
        """
        return self.players  # Простая заглушка, здесь должна быть логика подсчета результатов

    def play_playoffs(self, bracket):
        """
        Проведение матчей в плей-офф.

        :param bracket: Турнирная сетка для плей-офф.
        """
        for pair in bracket:
            match = Match(pair[0], pair[1], 'playoff')
            self.matches.append(match)
