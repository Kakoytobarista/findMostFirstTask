from pprint import pprint


from csv_enum import CsvEnum
from handlers import (get_rows, get_columns, get_days_with_objects, get_day_with_min_or_max_temp,
    get_days_with_average_temperature, get_month, get_months_with_average_value_for_month,
    get_month_with_min_or_max_temp, get_months_with_average_temp_for_days)

enum = CsvEnum


def create_applier(columns):
    def apply(cls):
        for name in columns:
            setattr(cls, name.lower(), None)
        return cls

    return apply


rows = []
reader = get_rows()
cols = get_columns()


@create_applier(get_columns())
class Row:
    pass


for line in reader:
    if not line:
        break
    r = Row()
    for i, attr in enumerate(line, start=0):
        try:
            setattr(r, cols[i], line[i])
        except IndexError:
            continue
    rows.append(r)


class WeatherStatistic:

    @staticmethod
    def getting_months_with_average_temp_month():
        month_dict = get_month(arr=rows)
        day_objects = get_days_with_objects(objects=rows)
        months_with_average_temp = get_months_with_average_temp_for_days(day_objects=day_objects,
                                                                         month_dict=month_dict)
        months_with_average_temp_for_month = get_months_with_average_value_for_month(months_with_average_temp)
        return months_with_average_temp_for_month



    def get_coldest_month(self):
        months_with_average_temp_for_month = self.getting_months_with_average_temp_month()
        date_with_coldest_temp = get_month_with_min_or_max_temp(func=min,
                                                                month_dict=months_with_average_temp_for_month)
        return (f"Coldest month:\n Month: {date_with_coldest_temp[0]}, "
                f"Average temperature: {date_with_coldest_temp[1]}")


# """
# Самый ветреный месяц

# Разбить на месяца
# 1. разбить на дни
# 2. для каждого дня получить среднюю скорость ветра
# 3. разбить на месяца
# 4. для каждого месяца получить среднюю скорость ветра
# 5. max(array(в котором все месяца в csv)

# """

    # def find_windiest_month():
    #     months_with_average_temp_for_month = self.getting_months_with_average_temp_month()
    #     date_with_coldest_temp = get_month_with_min_or_max_temp(func=min,
    #                                                             month_dict=months_with_average_temp_for_month)
    #     return (f"Coldest month:\n Month: {date_with_coldest_temp[0]}, "
    #             f"Average temperature: {date_with_coldest_temp[1]}")

        

    @staticmethod
    def get_coldest_day():
        day_objects = get_days_with_objects(objects=rows)
        days_with_average_temp = get_days_with_average_temperature(array=day_objects)
        coldest_day = get_day_with_min_or_max_temp(func=min,
                                                   array=days_with_average_temp)
        return (f"Coldest day: Day: {coldest_day[0]}, " 
                f"Average temperature: {coldest_day[1]}")



    def get_hottest_month(self):
        months_with_average_temp_for_month = self.getting_months_with_average_temp_month()
        date_with_hottest_temp = get_month_with_min_or_max_temp(func=max,
                                                                month_dict=months_with_average_temp_for_month)
        return (f"Hottest month:\n Month: {date_with_hottest_temp[0]}, "
                f"Average temperature: {date_with_hottest_temp[1]}")

    @staticmethod
    def get_hottest_day():
        day_objects = get_days_with_objects(objects=rows)
        days_with_average_temp = get_days_with_average_temperature(array=day_objects)
        hottest_day = get_day_with_min_or_max_temp(func=max,
                                                   array=days_with_average_temp)
        return (f"Hottest day: Day: {hottest_day[0]}, " 
                f"Average temperature: {hottest_day[1]}")

    def get_rainiest_week(self):
        pass

    def get_windiest_month(self):
        pass


if __name__ == "__main__":
    weather = WeatherStatistic()
    pprint('_________DAY___________')
    pprint(weather.get_coldest_day())
    pprint(weather.get_hottest_day())
    pprint('_________MONTH___________')
    pprint(weather.get_coldest_month())
    pprint(weather.get_hottest_month())
    pprint('_________WEEK___________')
