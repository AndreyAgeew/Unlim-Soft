from .media_channel import MediaChannel


class TV(MediaChannel):
    """
    Класс для телевизионного канала, подкласс MediaChannel.
    """

    def publish_news(self, hero_name, city_name, attack_description):
        """
        Публикация новостей на телевизионном канале.
        """
        return f"Watch on the first channel: {hero_name} saved {city_name}!"
