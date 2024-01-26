from abc import ABC, abstractmethod


class MediaChannel(ABC):
    """
    Абстрактный класс для медиаканалов.
    """

    @abstractmethod
    def publish_news(self, hero_name, city_name, attack_description):
        """
        Абстрактный метод публикации новостей.
        """
        pass
