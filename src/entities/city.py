class City:
    """
    Класс, представляющий город и связанного с ним антагониста.
    """
    def __init__(self, name, antagonist):
        """
        Инициализация города с его названием и антагонистом.
        """
        self.name = name
        self.antagonist = antagonist

    def under_attack(self, attack_description):
        """
        Возвращает описание атаки антагониста на город с использованием заданного сценария.
        """
        return f"{self.antagonist} {attack_description}"
