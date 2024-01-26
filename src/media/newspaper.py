from .media_channel import MediaChannel


class Newspaper(MediaChannel):
    """
    Класс для газеты, подкласс MediaChannel.
    """

    def publish_news(self, hero_name, city_name, attack_description):
        """
        Публикация новостей в газете.
        """
        return f"Today in newspapers: {hero_name} saved {city_name}!"
