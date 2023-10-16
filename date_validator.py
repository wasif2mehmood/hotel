import re



def validate_date(date_str):
    date_regex = r'^\d{2}-[A-Z][a-z]{2}-\d{4}$'
    if not re.match(date_regex, date_str):
        return False

    day, month, year = date_str.split('-')

    try:
        day = int(day)
        year = int(year)
    except ValueError:
        return False

    if month not in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']:
        return False

    if day < 1 or day > 31:
        return False

    if month == 'Feb':
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            if day > 29:
                return False
        elif day > 28:
            return False
    elif month in ['Apr', 'Jun', 'Sep', 'Nov']:
        if day > 30:
            return False

    if year > 2023:
        return False

    return True

