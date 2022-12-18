import requests
from datetime import date, timedelta
from colorama import Fore


class StockReader:
    STOCK_NAME = "NVDA"
    COMPANY_NAME = "Tesla Inc"

    STOCK_ENDPOINT = "https://www.alphavantage.co/query"
    NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
    FUNCTION = 'TIME_SERIES_DAILY'
    FUNCTION2 = 'TIME_SERIES_DAILY_ADJUSTED'  # only premium members
    API_KEY = "38D9160HKQSMCJVQ"

    HOLLYDAYS = ['2021-12-24', '2021-12-25', '2022-01-06']

    def __init__(self, symbol, recent_date='yesterday', far_date='before_yesterday'):
        """
         If this api is called many times a day or the changing date-data is currently happening while this program is
        being run you migh get some exceptions risen
        :param symbol: company tag
        :param recent_date: most recent reference date for market data extraction
        :param far_date: less recent reference date for market data extraction
        """
        self.symbol = symbol
        self.recent_date = recent_date
        self.far_date = far_date

    @staticmethod
    def week_day(date_day):
        """

        :param date_day: datetime format (yyyy-mm-dd)
        :return: str weekday.title()
        """

        if date_day is None:
            print(date_day)
            return None

        year, month, day = date_day.split('-')
        year = int(year)
        month = int(month)
        day = int(day)
        off_set = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        week = ['Sunday',
                'Monday',
                'Tuesday',
                'Wednesday',
                'Thursday',
                'Friday',
                'Saturday']
        after_feb = 1
        if month > 2:
            after_feb = 0
        aux = year - 1700 - after_feb
        # dayOfWeek for 1700/1/1 = 5, Friday
        day_of_week = 5
        # partial sum of days betweem current date and 1700/1/1
        day_of_week += (aux + after_feb) * 365
        # leap year correction
        day_of_week += aux / 4 - aux / 100 + (aux + 100) / 400
        # sum monthly and day offsets
        day_of_week += off_set[month - 1] + (day - 1)
        day_of_week %= 7
        day_of_week = int(day_of_week)
        return week[day_of_week]

    @staticmethod
    def get_yesterday_date():
        today = date.today()
        yesterday = today - timedelta(1)
        return str(yesterday)

    @staticmethod
    def get_before_yesterday_date():
        today = date.today()
        before_yesterday = today - timedelta(2)
        return str(before_yesterday)

    def read_a_stock(self):
        stock_params = {'function': self.FUNCTION,
                        'symbol': self.symbol,
                        'apikey': self.API_KEY
                        }
        response = requests.get(url=self.STOCK_ENDPOINT, params=stock_params)
        return response.json()

    def get_date_data(self, date_data):
        """
        return  maximum about 6 month ago, before that will rise error
        :param date_data: desired str of date in datetime format -> 2022-01-04
        :return: data dictionary of that date for that stock tag (symbol)
        """
        weekday = self.week_day(date_data)
        if weekday == 'Saturday' or weekday == 'Sunday':
            print(f'{weekday} -> Market closed')
            return None
        data = self.read_a_stock()
        for day_data, values in data['Time Series (Daily)'].items():
            if day_data == date_data:
                return values

    def compare_same_day_stock(self, date_day='yesterday', print_on=True):
        if date_day == 'yesterday':
            date_day = self.get_yesterday_date()
        weekday = self.week_day(date_day)
        if weekday == 'Saturday' or weekday == 'Sunday':
            print(f'{weekday} -> Market closed')
            return 0
        if date_day in self.HOLLYDAYS:
            print(f'{weekday} -> Market closed')
            return 0

        elif date_day == 'yesterday':
            date_day = self.get_yesterday_date()
        temp_data = dict(self.get_date_data(date_day))
        market_open = float(temp_data['4. close'])
        market_close = float(temp_data['1. open'])
        diff = market_close - market_open
        if print_on:
            tag = self.reset(self.symbol)
            print(tag)
            quote = f'{market_open}\n {market_close}'
            quote = self.reset(quote)
            print(quote)
            if diff > 0:
                diff = self.green(f'{diff}')
            else:
                diff = self.red(f'{diff}')
            print(f' {diff}')
        return diff

    def get_yesterday_data(self):
        yesterday = self.get_yesterday_date()
        weekday = self.week_day(yesterday)
        if weekday == 'Saturday' or weekday == 'Sunday':
            print(f'{weekday} -> Market closed')
            return 0

        data = self.get_date_data(yesterday)
        return data

    def compare_two_dates(self, far_date='before_yesterday', recent_date='yesterday', print_on=True):
        if far_date == 'before_yesterday':
            far_date = self.get_before_yesterday_date()
        week_day = self.week_day(far_date)
        if week_day == 'Saturday' or week_day == 'Sunday' or far_date in self.HOLLYDAYS:
            return f'{far_date} is weekend or hollyday'

        if recent_date == 'yesterday':
            recent_date = self.get_yesterday_date()
        week_day = self.week_day(recent_date)
        if week_day == 'Saturday' or week_day == 'Sunday' or recent_date in self.HOLLYDAYS:
            return f'{recent_date} is weekend or hollyday'

        far_data = self.get_date_data(far_date)
        recent_data = self.get_date_data(recent_date)

        far_data_open = float(far_data['1. open'])
        recent_data_close = float(recent_data['4. close'])

        diff = recent_data_close - far_data_open
        if print_on:

            tag = self.reset(self.symbol)
            quote = f'{far_date}: {far_data_open:.2f}\n {recent_date}: {recent_data_close:.2f}'
            # quote = self.reset(quote)
            print(tag)
            print(quote)
            if diff > 0:
                diff = self.green(f'{diff}')
            else:
                diff = self.red(f'{diff}')
            print(f' {diff}')
        return diff

    @staticmethod
    def red(text=''):
        return f"{Fore.RED}{text}"

    @staticmethod
    def green(text=''):
        return f"{Fore.GREEN}{text}"

    @staticmethod
    def reset(text=''):
        return f"{Fore.RESET} {text}"

    @staticmethod
    def report_my_choice(list_of_tags):
        for tag in list_of_tags:
            response = StockReader(tag)
            response.compare_same_day_stock()


if __name__ == '__main__':
    stocks = ['NVDA', 'TSLA', 'MSFT', 'AAPL', 'T']
    StockReader.report_my_choice(stocks)
