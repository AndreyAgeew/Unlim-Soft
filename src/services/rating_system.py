import random


class RatingSystem:
    """
    Сервис для управления рейтингом игроков.
    """

    @staticmethod
    def update_ratings(matches):
        """
        Обновление рейтинга игроков на основе результатов матчей.

        :param matches: Список матчей с результатами.
        """
        for match in matches:
            rating_change = 10 if match.match_type == 'play' else 20
            winner = match.player1 if random.random() > 0.5 else match.player2
            winner.rating += rating_change
            loser = match.player2 if winner is match.player1 else match.player1
            loser.rating -= rating_change
            match.set_result(winner, rating_change)
