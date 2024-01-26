class MatchHistory:
    """
    Сервис для сохранения и восстановления истории матчей.
    """

    @staticmethod
    def save(matches):
        """
        Сохранение истории матчей.

        :param matches: Список матчей для сохранения.
        """
        for match in matches:
            print(
                f'Match saved: {match.player1.name} vs {match.player2.name} - Winner: {match.winner.name} - Rating Change: {match.rating_change} - Type: {match.match_type}')
