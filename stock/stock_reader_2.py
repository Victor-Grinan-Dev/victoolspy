import requests
from datetime import date
from datetime import timedelta

STOCK_NAME = "NVDA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
FUNCTION = 'TIME_SERIES_DAILY'
FUNCTION2 = 'TIME_SERIES_DAILY_ADJUSTED'  # only premium members
SYMBOL = STOCK_NAME
API_KEY = "38D9160HKQSMCJVQ"

stock_params = {'function': FUNCTION,
                'symbol': SYMBOL,
                'apikey': API_KEY
                }
today = date.today()
yesterday = today - timedelta(1)
yesterday_date = None
# print(yesterday)  # 2022-01-04
# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
data = response.json()
for item in data['Time Series (Daily)']:
    if item == str(yesterday):
        yesterday_date = item
        break
yesterday_data = data['Time Series (Daily)'][yesterday_date]
# print(yesterday_data)
# for item in yesterday_data:
#     print(item)
stock_open = yesterday_data['1. open']
stock_high = yesterday_data['2. high']
stock_low = yesterday_data['3. low']
stock_close = yesterday_data['4. close']
stock_volume = yesterday_data['5. volume']
test = [stock_open, stock_high, stock_low, stock_close, stock_volume]
test = [float(item) for item in test]
for item in test:
    print(f'{item:.2f}')
# TODO 2. - Get the day before yesterday's closing stock price

# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

## STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

# TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

# TODO 9. - Send each article as a separate message via Twilio.


# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
