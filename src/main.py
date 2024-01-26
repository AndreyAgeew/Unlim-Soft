from entities.city import City
from entities.superhero import Superhero
from entities.scenario import Scenario
from media.newspaper import Newspaper
from media.tv import TV


def main():
    # Создание экземпляров классов
    city_tokyo = City("Tokyo", "Godzilla")
    city_kostroma = City("Kostroma", "Aliens")

    superhero = Superhero("Chuck Norris", "PIU PIU")

    media_newspaper = Newspaper()
    media_tv = TV()

    # Сценарий для Токио и газеты
    scenario_tokyo_newspaper = Scenario(superhero, city_tokyo, media_newspaper)
    scenario_tokyo_newspaper.play_out("stands near a skyscraper")

    print("--------------------")

    # Сценарий для Костромы и телевидения
    scenario_kostroma_tv = Scenario(superhero, city_kostroma, media_tv)
    scenario_kostroma_tv.play_out("abduct cows in the meadow")


if __name__ == "__main__":
    main()
