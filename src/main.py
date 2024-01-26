from config import periods
from services import expand_dates
if __name__ == '__main__':

    # Разжатие массива
    expanded_dates = expand_dates(periods)

    # Вывод результатов
    for date in expanded_dates:
        print(date)
