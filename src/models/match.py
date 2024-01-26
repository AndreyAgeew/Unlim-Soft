class Match:
    """
    Класс представляющий матч между двумя игроками.
    """

    def __init__(self, player1, player2, match_type):
        """
        Инициализация объекта матча.

        :param player1: Первый игрок.
        :param player2: Второй игрок.
        :param match_type: Тип матча (например, 'play' или 'playoff').
        """
        self.player1 = player1
        self.player2 = player2
        self.match_type = match_type
        self.winner = None
        self.loser = None
        self.rating_change = 0

    def set_result(self, winner, rating_change):
        """
        Установка результата матча, включая победителя, проигравшего и изменение рейтинга.

        :param winner: Победитель матча.
        :param rating_change: Изменение рейтинга.
        """
        self.winner = winner
        self.loser = self.player2 if self.player1 == winner else self.player1
        self.rating_change = rating_change
