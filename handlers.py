import collections
import csv
from collections import defaultdict
from typing import Union, Any, Dict, Callable

from csv_enum import CsvEnum
from helpers import is_number


def get_columns() -> list:
    """Function for getting columns from csv"""
    try:
        with open(CsvEnum.PATH_TO_DATA.value) as csv_data:
            reader = csv.reader(csv_data, delimiter=';')
            return [i.lower() for i in next(reader)]
    except IOError as err:
        return err
    finally:
        csv_data.close()


def get_rows() -> list:
    """Function for getting rows from csv"""
    try:
        with open(CsvEnum.PATH_TO_DATA.value) as csv_data:
            reader = csv.reader(csv_data, delimiter=';')
            return list(reader)[1:]
    except IOError as err:
        return err
    finally:
        csv_data.close()


def get_average_temperature(objects: collections.Iterable,
                            len_interval: int) -> float:
    """Function for getting average temperature"""
    avg_temp = sum([float(day.t) for day in objects]) // len_interval
    return avg_temp


def get_average_rainy(objects: collections.Iterable,
                      len_interval: int) -> float:
    """Function for getting average temperature"""
    avg_rainy = (sum([
        float(day.rrr) 
        for day in objects 
        if is_number(day.rrr)
    ]) // len_interval)
    return avg_rainy


def get_average_wind(objects: collections.Iterable,
                     len_interval: int) -> float:
    """Function for getting average temperature"""
    avg_wind = sum([float(day.ff) for day in objects]) // len_interval
    return avg_wind


def get_days_with_objects(objects: collections.Iterable) -> dict:
    """Function for getting defaultdict
    with day in keys and collections.Iterable in values"""
    day_dict = defaultdict(list)
    for i in objects:
        day_dict[i.time[:-6]].append(i)

    return day_dict


def get_month(row_: list) -> dict:
    """Getting dict with key: month
    and value: zero"""
    month_dict = defaultdict(list)
    for i in row_:
        month_dict[i.time[3:-6]].append(0)

    return month_dict


def get_days_with_average_wind(days: dict) -> dict:
    """Getting average dict with key: date
    and value average temperature"""
    avg_day = {}
    for key, value in days.items():
        avg_day[key] = (get_average_wind(objects=value,
                                         len_interval=len(days[key])))

    return avg_day


def get_days_with_average_temperature(days: dict) -> dict:
    """Getting average dict with key: date
    and value average temperature"""
    avg_day = {}
    for key, value in days.items():
        avg_day[key] = (get_average_temperature(objects=value,
                                                len_interval=len(days[key])))

    return avg_day


def get_days_with_average_rainy(days: dict) -> dict:
    """Getting average dict with key: date
    and value average temperature"""
    avg_day = {}
    for key, value in days.items():
        avg_day[key] = (get_average_rainy(objects=value,
                                          len_interval=len(days[key])))

    return avg_day


def get_day_by_predicate(func: Union[min, max],
                         days: dict) -> Any:
    """Function for getting min or max value of
    any attributes"""
    return func(days.items(), key=lambda x: x[1])


def get_months_with_average_value_for_days(day_objects: dict,
                                           month_dict: dict,
                                           get_days_by_predicate: Callable) -> dict:
    """Function for getting dict with month date in keys
    and average value of days"""
    month_dict.clear()
    for date, avg_temp in get_days_by_predicate(day_objects).items():
        month_dict[date[3:]].append(avg_temp)
    return month_dict


def get_months_with_average_value_for_month(month_dict: Dict) -> dict:
    """Getting date (month interval) with average value
    for months"""
    result = {}
    for key, value in month_dict.items():
        result[key] = sum(value) // len(value)
    return result


def get_month_by_predicate(func: Callable, month_dict: dict) -> list:
    """Getting month with minimal or maximum
    value"""
    return func(month_dict.items(), key=lambda x: x[1])
