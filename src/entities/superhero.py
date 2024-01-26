class Superhero:
    """
    Класс, представляющий супергероя и его уникальные способы атаки.
    """
    def __init__(self, name, attack_style):
        """
        Инициализация супергероя с именем и стилем атаки.
        """
        self.name = name
        self.attack_style = attack_style

    def attack(self):
        """
        Возвращает описание атаки супергероя.
        """
        return self.attack_style
