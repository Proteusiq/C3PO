from datetime import date

DAY_LOOKUP = {
    '01': 'st',
    '21': 'st',
    '31': 'st',
    '02': 'nd',
    '22': 'nd',
    '03': 'rd',
    '23': 'rd'
}

def today():
    return (f"{date.today(): %B %d{DAY_LOOKUP.get('%B', 'th')} %Y}")
