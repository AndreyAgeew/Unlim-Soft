from random import shuffle


def create_groups(players, group_size):
    """
    Функция для случайного распределения игроков по группам.

    :param players: Список игроков.
    :param group_size: Размер группы.
    :return: Список групп с игроками.
    """
    shuffle(players)
    return [players[i:i + group_size] for i in range(0, len(players), group_size)]


def create_tournament_bracket(group_results):
    """
    Функция для формирования турнирной сетки на основе результатов группового этапа.

    :param group_results: Результаты группового этапа.
    :return: Турнирная сетка для плей-офф.
    """
    # Простая логика: формируем пары для игры в плей-офф
    bracket = []
    while group_results:
        player1 = group_results.pop(0)  # Берем первого игрока
        player2 = group_results.pop(0) if group_results else None  # Берем второго игрока, если он есть
        bracket.append((player1, player2))
    return bracket
