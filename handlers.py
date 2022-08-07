import collections
import csv
from collections import defaultdict
from typing import Union, List, Any, Dict

from csv_enum import CsvEnum


def get_columns() -> list:
    """Function for getting columns from csv"""
    with open(CsvEnum.PATH_TO_DATA.value) as csv_data:
        reader = csv.reader(csv_data, delimiter=';')
        return [i.lower() for i in next(reader)]


def get_rows() -> list:
    """Function for getting rows from csv"""
    with open(CsvEnum.PATH_TO_DATA.value) as csv_data:
        reader = csv.reader(csv_data, delimiter=';')
        return list(reader)[1:]


def get_average_temperature(objects: collections.Iterable,
                            len_interval: int) -> float:
    """Function for getting average temperature"""
    avg_temp = 0
    for i in objects:
        avg_temp += float(i.t)

    result = avg_temp // len_interval
    return result


def get_days_with_objects(objects: collections.Iterable) -> dict:
    """Function for getting defaultdict
    with day in keys and collections.Iterable in values"""
    day_dict = defaultdict(list)
    for i in objects:
        day_dict[i.time[:-6]].append(i)
    return day_dict


def get_days_with_average_temperature(array: dict) -> dict:
    """Getting average dict with key: date
    and value average temperature"""
    avg_day = {}
    for key, value in array.items():
        avg_day[key] = (get_average_temperature(objects=value,
                                                len_interval=len(array[key])))

    return avg_day


def get_day_with_min_or_max_temp(func: Union[min, max],
                                 array) -> Any:
    """Function for getting min or max value of
    any attributes"""
    return func(array.items(), key=lambda x: x[1])


def get_month(arr: List[Any]) -> dict:
    """Getting dict with key: month
    and value: zero"""
    month_dict = defaultdict(list)
    for i in arr:
        month_dict[i.time[3:-6]].append(0)

    return month_dict


def get_months_with_average_temp_for_days(day_objects: dict,
                                          month_dict: dict) -> dict:
    """Function for getting dict with month date in keys
    and average temperature of days"""
    month_dict.clear()
    for date, avg_temp in get_days_with_average_temperature(day_objects).items():
        month_dict[date[3:]].append(avg_temp)
    return month_dict


def get_months_with_average_temp_for_month(month_dict: Dict) -> dict:
    """Getting date (month interval) with average temperature
    for months"""
    result = {}
    for key, value in month_dict.items():
        result[key] = sum(value) // len(value)
    return result


def get_month_with_min_or_max_temp(func: Any, month_dict) -> Any:
    """Getting month with minimal or maximum
    temperature"""
    return func(month_dict.items(), key=lambda x: x[1])

