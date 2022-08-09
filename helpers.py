from collections import defaultdict
from datetime import datetime as dt, timedelta
from typing import Union


def is_number(n: Union[str, int, float]) -> bool:
    try:
        float(n)    
    except ValueError:
        return False
    return True


def get_year_week(date: str) -> str:
    """Method for getting """
    date_object = dt.strptime(date, '%d.%m.%Y')
    week_num = date_object.strftime("%V")
    year = date_object.strftime("%Y")
    return f"{year}:{week_num}"


def get_week_date(year_week: str) -> tuple:
    year, week = year_week.split(":")
    year_week = f"{year}-W{week}"
    monday = dt.strptime(year_week + '-1', "%Y-W%W-%w")
    return monday.strftime("%d.%m.%Y"), (monday + timedelta(days=6)).strftime("%d.%m.%Y")


def get_rainy(weeks: dict) -> tuple:
    rainy = max(weeks.items(), key=lambda x: x[1])
    week_start, week_end = get_week_date(rainy[0])
    return week_start, week_end, rainy


def group_by_weeks(func: dict, weeks: defaultdict) -> None:
    for date, value in func.items():
        year_week = get_year_week(date)
        weeks[year_week].append(value)
        return
