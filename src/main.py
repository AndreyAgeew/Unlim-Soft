from models.player import Player
from models.tournament import Tournament
from services.rating_system import RatingSystem
from services.match_history import MatchHistory
from utils.grouping import create_groups, create_tournament_bracket


def main():
    """
    Основная функция для запуска турнира. Создает игроков, организует турнир,
    проводит матчи, обновляет рейтинги и сохраняет историю матчей.
    """
    players = [Player(f'Player {i}', rating=1000 + i * 10) for i in range(1, 17)]
    tournament = Tournament(players)

    groups = create_groups(players, group_size=4)
    tournament.play_group_stage(groups)

    bracket = create_tournament_bracket(tournament.get_group_results())
    tournament.play_playoffs(bracket)

    RatingSystem.update_ratings(tournament.matches)
    MatchHistory.save(tournament.matches)


if __name__ == "__main__":
    main()
