import requests
from datetime import date, timedelta
from pprint import pprint

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "38D9160HKQSMCJVQ"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "e627148ddedc445e8983f92ec0ea876c"
#
# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock_item price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# TODO 1. - Get yesterday's closing stock_item price. Hint: You can perform list comprehensions on Python dictionaries.
#  e.g. [new_value for (key, value) in dictionary.items()]
today = date.today()
weekday = date.weekday()
yesterday_date = today - timedelta(days=1)
# before_yesterday_date = today - timedelta(days=2)
# year, month, day = str(yesterday_date).split('-')
# yesterday_date = int(year), int(month), int(day)
print(yesterday_date)

# before_yesterday_date = yesterday_date - timedelta(days=2)

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "interval": "60min",
    "apikey": STOCK_API_KEY
}
response = requests.get(
    url=STOCK_ENDPOINT,
    params=stock_params
)
data = response.json()  # this gives everyday from a year ago time
pprint(data)

# # data_list = [value for (key, value) in data.items()]
# # pprint(data_list)
# # yesterday_data = data_list[-1][yesterday_date][yesterday_date]
# # pprint(yesterday_data)
# # yesterday_closing_price = yesterday_data['4. close']
# # print(yesterday_closing_price)
#
# yesterday_closing = response.json()['Time Series (Daily)'][yesterday_date]['4. close']
# print(yesterday_closing)
#
# # TODO 2. - Get the day before yesterday's closing stock_item price
# before_yesterday_closing = response.json()['Time Series (Daily)'][before_yesterday_date]['4. close']
# print(before_yesterday_closing)
#
# # TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
# up_down = None
# price_diff = float(yesterday_closing) - float(before_yesterday_closing)
# if price_diff > 0:
#     up_down = "🔺"
# else:
#     up_down = "🔻"
#
# print(price_diff)
#
# # TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day
# #  before yesterday.
# diff_percentt = round((price_diff / float(yesterday_closing)) * 100)
# print(diff_percentt)
#
# # TODO 5. - If TODO 4 percentage is greater than 5 then print("Get News").
# # TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
#
# if abs(diff_percentt) > 0:
#     params = {
#         'apiKey': NEWS_API_KEY,
#         'qInTitle': COMPANY_NAME,
#     }
#
#     response = requests.get(NEWS_ENDPOINT, params=params)
#     data = response.json()['articles']
#     # pprint(data)
#
#     ## STEP 2: https://newsapi.org/
#
#     # TODO 7. - Use Python slice operator to create a list that contains the first 3 articles.
#     def full_fromat_news(title, content, author, publishedAt, source):
#         return f'\n"{publishedAt}\n{title.upper()}"\n\n{content}\n\n{author}\n{source}'
#
#
#     three_articles = data[:3]
#     # for art in three_articles:
#     #     print(fromat_news(art['title'], art['content'], art['author'], art['publishedAt'], art['source'] ))
#
# # TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
#     all_ready_msg = [f"{STOCK_NAME}: {up_down}{diff_percentt}\nHeadline: {item['title']}. \nDescription: {item['description']}" for item in data]
#
#     for msg in all_ready_msg:
#         print(msg)
#
# # TODO 9. - Send each article as a separate message via Twilio.
#
#
#
#
#
