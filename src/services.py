from datetime import timedelta


# Функция для разжатия массива
def expand_dates(date_ranges):
    dates = []
    for start_date, end_date in date_ranges:
        current_date = start_date
        while current_date <= end_date:
            dates.append(current_date)
            current_date += timedelta(days=1)
    return dates
