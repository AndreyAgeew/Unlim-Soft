class Scenario:
    """
    Класс, координирующий сценарий атаки, спасения города и публикации новостей.
    """
    def __init__(self, hero, city, media):
        """
        Инициализация сценария с супергероем, городом и медиаканалом.
        """
        self.hero = hero
        self.city = city
        self.media = media

    def play_out(self, attack_description):
        """
        Воспроизведение сценария.
        """
        print(self.city.under_attack(attack_description))
        print(self.hero.attack())
        print(self.media.publish_news(self.hero.name, self.city.name, attack_description))
