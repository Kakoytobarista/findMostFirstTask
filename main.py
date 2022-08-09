from pprint import pprint
from typing import Callable
from collections import defaultdict

from handlers import (get_rows, get_columns, get_days_with_objects, get_day_by_predicate,
                      get_month, get_months_with_average_value_for_month,
                      get_month_by_predicate, get_months_with_average_value_for_days,
                      get_days_with_average_temperature,
                      get_days_with_average_wind, get_days_with_average_rainy)
from helpers import get_rainy, group_by_weeks
from row import Row


class WeatherStatistic:

    @staticmethod
    def getting_months_with_average_value_month(rows_: list, days_predicate: Callable):
        """Method for getting list with key date of month
        and value average value of month"""
        month_dict = get_month(row_=rows_)
        day_objects = get_days_with_objects(objects=rows_)
        months_with_average_temp = get_months_with_average_value_for_days(day_objects=day_objects,
                                                                          month_dict=month_dict,
                                                                          get_days_by_predicate=days_predicate)
        months_with_average_temp_for_month = get_months_with_average_value_for_month(months_with_average_temp)
        return months_with_average_temp_for_month

    def get_coldest_month(self, rows_: list):
        """Method for getting the coldest month with params
        temperature and date"""
        months_with_average_temp_for_month = self.getting_months_with_average_value_month(
            rows_,
            days_predicate=get_days_with_average_temperature)
        date_with_coldest_temp = get_month_by_predicate(func=min,
                                                        month_dict=months_with_average_temp_for_month)
        return (f"Coldest month: Month: {date_with_coldest_temp[0]}, "
                f"Average temperature: {date_with_coldest_temp[1]}")

    def find_windiest_month(self, rows_: list):
        """Method for getting the windiest month with params
        date and speed"""
        months_with_average_wind_for_month = self.getting_months_with_average_value_month(
            rows_,
            days_predicate=get_days_with_average_wind)
        date_with_strongest_wind = get_month_by_predicate(func=max,
                                                          month_dict=months_with_average_wind_for_month)
        return (f"Strongest wind Month: Month: {date_with_strongest_wind[0]}, "
                f"Average wind speed: {date_with_strongest_wind[1]}")

    @staticmethod
    def get_coldest_day(rows_: list):
        """Method for getting the coldest day with params
        date and temperature"""
        day_objects = get_days_with_objects(objects=rows_)
        days_with_average_temp = get_days_with_average_temperature(days=day_objects)
        coldest_day = get_day_by_predicate(func=min,
                                           days=days_with_average_temp)
        return (f"Coldest day: Day: {coldest_day[0]}, "
                f"Average temperature: {coldest_day[1]}")

    def get_hottest_month(self, rows_: list):
        """Method for getting the hottest month with params
        date and temperature"""
        months_with_average_temp_for_month = self.getting_months_with_average_value_month(
            rows_,
            days_predicate=get_days_with_average_temperature)
        date_with_hottest_temp = get_month_by_predicate(func=max,
                                                        month_dict=months_with_average_temp_for_month)
        return (f"Hottest month: Month: {date_with_hottest_temp[0]}, "
                f"Average temperature: {date_with_hottest_temp[1]}")

    @staticmethod
    def get_hottest_day(rows_: list):
        """"Method for getting the hottest day with params
        date and temperature"""
        day_objects = get_days_with_objects(objects=rows_)
        days_with_average_temp = get_days_with_average_temperature(days=day_objects)
        hottest_day = get_day_by_predicate(func=max,
                                           days=days_with_average_temp)
        return (f"Hottest day: Day: {hottest_day[0]}, "
                f"Average temperature: {hottest_day[1]}")

    @staticmethod
    def get_rainiest_week(rows_: list):
        """Method for getting the rainiest week with params
        date and rainy"""
        day_objects = get_days_with_objects(objects=rows_)
        days_with_average_rainy = get_days_with_average_rainy(days=day_objects)

        weeks = defaultdict(list)
        group_by_weeks(func=days_with_average_rainy,
                       weeks=weeks)
        for key, value in weeks.items():
            weeks[key] = sum(value)

        week_start, week_end, rainy = get_rainy(weeks=weeks)
        return (f"The most rainy Week: {week_start} - {week_end} "
                f"Average rainy {rainy[1]}")


if __name__ == "__main__":
    rows: list = get_rows()
    cols: list = get_columns()
    rows_objects: list = [Row(cols, line) for line in rows if line]

    weather = WeatherStatistic()

    pprint('_________DAY___________')
    pprint(weather.get_coldest_day(rows_objects), width=40)
    pprint(weather.get_hottest_day(rows_objects),width=40)
    pprint('_________MONTH___________')
    pprint(weather.get_coldest_month(rows_objects), width=40)
    pprint(weather.get_hottest_month(rows_objects), width=40)
    pprint(weather.find_windiest_month(rows_objects), width=40)
    pprint('_________WEEK___________')
    pprint(weather.get_rainiest_week(rows_objects), width=50)
