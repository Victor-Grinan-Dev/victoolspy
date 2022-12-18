class DividendStock:

    def __init__(self, name, tag):
        self.name = name.title()
        self.tag = tag
        self.current_price = float()
        self.all_opened_position_price_amount = []  # (price, amount) reffers to opening price and amount of money in it
        self.profit_loss = float()
        self.dividend = float()


MyDividendStocks = []

mo = {'tag': 'mo', 'dividend': 7.3, 'amount': 1000, 'value': 1056.07}
t = {'tag': 't', 'dividend': 8.75, 'amount': 1000, 'value': 1124.68}
cinel = {'tag': 'cinel', 'dividend': 37.1, 'amount': 50, 'value': 51.26}
rio = {'tag': 'rio', 'dividend': 10.5, 'amount': 100, 'value': 100.77}
enb = {'tag': 'enb', 'dividend': 7.19, 'amount': 100, 'value': 102.05}
hk1988 = {'tag': 'hk1988', 'dividend': 13.4, 'amount': 10, 'value': 10.13}
hk1966 = {'tag': 'hk1966', 'dividend': 15.4, 'amount': 10, 'value': 10.11}
irm = {'tag': 'irm', 'dividend': 4.83, 'amount': 200, 'value': 215.17}
ibm = {'tag': 'ibm', 'dividend': 6.55, 'amount': 200, 'value': 218.82}
wu = {'tag': 'wu', 'dividend': 5.41, 'amount': 150, 'value': 155.63}
cvx = {'tag': 'cvx', 'dividend': 4.67, 'amount': 200, 'value': 208.01}
xom = {'tag': 'xom', 'dividend': 5.81, 'amount': 200, 'value': 209.01}
# hk1958 = {'tag': 'hk1958', 'dividend': 5.49, 'amount': 0, 'value': 0}
glpi = {'tag': 'glpi', 'dividend': 5.7, 'amount': 100, 'value': 100.76}
spg = {'tag': 'spg', 'dividend': 5.54, 'amount': 100, 'value': 102.04}
o = {'tag': 'o', 'dividend': 4.16, 'amount': 100, 'value': 101.50}
abbv = {'tag': 'abbv', 'dividend': 4.10, 'amount': 10, 'value': 10}
avgo = {'tag': 'avgo', 'dividend': 2.35, 'amount': 50, 'value': 60.18}
ko = {'tag': 'ko', 'dividend': 2.91, 'amount': 100, 'value': 109.95}
# bmy = {'tag': 'bmy', 'dividend': 3.27, 'amount': 50, 'value': 55.62}
# mcd = {'tag': 'mcd', 'dividend': 2.01, 'amount': 10, 'value': 10.06}
vz = {'tag': 'vz', 'dividend': 4.77, 'amount': 200, 'value': 201.70}
# br = {'tag': 'br', 'dividend': 1.38, 'amount': 10, 'value': 10.38}
# pep = {'tag': 'pep', 'dividend': 2.52, 'amount': 10, 'value': 10.04}
# sklz = {'tag': 'sklz', 'dividend': 2.22, 'amount': 10, 'value': 11.18}
# pfe = {'tag': 'pfe', 'dividend': 2.64, 'amount': 10, 'value': 10.16}
wdc = {'tag': 'wdc', 'dividend': 2.96, 'amount': 10, 'value': 10.93}
# csco = {'tag': 'csco', 'dividend': 2.45, 'amount': 10, 'value': 10.41}
# trow = {'tag': 'trow', 'dividend': 2.23, 'amount': 10, 'value': 10.25}
# abb = {'tag': 'abb', 'dividend': 2.34, 'amount': 10, 'value': 10.35}
# gis = {'tag': 'gis', 'dividend': 3.02, 'amount': 10, 'value': 10.02}
# hp = {'tag': 'hp', 'dividend': 2.27, 'amount': 10, 'value': 10.52}
gawl = {'tag': 'gawl', 'dividend': 2.22, 'amount': 10, 'value': 10.23}
# tm = {'tag': 'tm', 'dividend': 2.20, 'amount': 10, 'value': 10.18}
# ntdoy = {'tag': 'ntdoy', 'dividend': 3.15, 'amount': 10, 'value': 10.44}
# txn = {'tag': 'txn', 'dividend': 2.26, 'amount': 0, 'value': 0}
# bby = {'tag': 'bby', 'dividend': 2.80, 'amount': 10, 'value': 10.26}
agnc = {'tag': 'agnc', 'dividend': 9.61, 'amount': 100, 'value': 102.29}
# f = {'tag': 'f', 'dividend': 3.03, 'amount': 10, 'value': 10.45}
# hk1997 = {'tag': 'hk1997', 'dividend': 3.41, 'amount': 0, 'value': 0}
# lmt = {'tag': 'lmt', 'dividend': 3.08, 'amount': 10, 'value': 10.24}
# All = {'tag': 'All', 'dividend': 2.84, 'amount': 10, 'value': 10.23}
# jnj = {'tag': 'jnj', 'dividend': 2.49, 'amount': 10, 'value': 10.02}
# mmm = {'tag': 'mmm', 'dividend': 3.39, 'amount': 10, 'value': 10.19}
# bip = {'tag': 'bip', 'dividend': 3.50, 'amount': 10, 'value': 10.29}
# mrk = {'tag': 'mrk', 'dividend': 3.49, 'amount': 10, 'value': 10.01}
# xel = {'tag': 'xel', 'dividend': 2.73, 'amount': 0, 'value': 0}
# ma = {'tag': 'ma', 'dividend': 0.40, 'amount': 10, 'value': 10.59}
# atvi = {'tag': 'atvi', 'dividend': 0.77, 'amount': 10, 'value': 11.05}
# blk = {'tag': 'blk', 'dividend': 1.44, 'amount': 10, 'value': 10.13}
# v = {'tag': 'v', 'dividend': 0.54, 'amount': 10, 'value': 10.41}
# nke = {'tag': 'nke', 'dividend': 0.56, 'amount': 10, 'value': 10.07}
# ccmp = {'tag': 'ccmp', 'dividend': 0.98, 'amount': 10, 'value': 10.27}
# ea = {'tag': 'ea', 'dividend': 0.53, 'amount': 10, 'value': 10.41}
# msft = {'tag': 'msft', 'dividend': 0.73, 'amount': 10, 'value': 10.46}
# hd = {'tag': 'hd', 'dividend': 1.70, 'amount': 0, 'value': 0}
aapl = {'tag': 'aapl', 'dividend': 0.51, 'amount': 10, 'value': 10.36}
# dis = {'tag': 'dis', 'dividend': 1.18, 'amount': 10, 'value': 10.50}
# bam = {'tag': 'bam', 'dividend': 1.12, 'amount': 0, 'value': 0}
# orcl = {'tag': 'orcl', 'dividend': 1.32, 'amount': 0, 'value': 0}
# msi = {'tag': 'msi', 'dividend': 1.13, 'amount': 10, 'value': 10.21}
# sie = {'tag': 'sie', 'dividend': 2.54, 'amount': 10, 'value': 10.13}
lvs = {'tag': 'lvs', 'dividend': 8.3, 'amount': 100, 'value': 105.16}
nwgl = {'tag': 'nwgl', 'dividend': 11.04, 'amount': 100, 'value': 101.80}
epd = {'tag': 'epd', 'dividend': 8.26, 'amount': 100, 'value': 101.70}
pnlnv = {'tag': 'pnlnv', 'dividend': 10.25, 'amount': 10, 'value': 10.39}
ngl = {'tag': 'ngl', 'dividend': 4.56, 'amount': 50, 'value': 50.35}
copa = {'tag': 'copa', 'dividend': 13.56, 'amount': 10, 'value': 10.03}
nvda = {'tag': 'nvda', 'dividend': 0.0006, 'amount': 50, 'value': 51.52}
plusl = {'tag': 'plusl', 'dividend': 7.40, 'amount': 100, 'value': 100.79}
hdv = {'tag': 'hdv', 'dividend': 4, 'amount': 100, 'value': 100.47}
sun = {'tag': 'sun', 'dividend': 7.94, 'amount': 100, 'value': 102.70}

dividend_stocks = [mo, t, cinel, rio, enb, hk1988, hk1966, irm, ibm, wu, cvx, xom, glpi, spg, o, abbv, ko,
                   vz, wdc, agnc, plusl, ngl, hdv, pnlnv, copa, sun]  # gawl, nvda, aapl, avgo,

all_ = 'all'
low = 'low'
mid = 'mid'
mid_plus = 'mid_plus'
mid_plus_plus = 'mid_plus_plus'
high = 'high'
stock_groups = [all_, low, mid, mid_plus, mid_plus_plus, high]

year = ['e', 'f', 'm', 'a', 'm', 'jun', 'jul', 'ag', 's', 'o', 'n', 'd']

TAX = 0.3

FILENAME = 'last_values_record.csv'


def my_choice(stock_type):
    choice_ = []
    if stock_type == all_:
        for stock in dividend_stocks:
            if stock['dividend'] > 0:
                choice_.append(stock['dividend'])
    elif stock_type == low:
        for stock in dividend_stocks:
            if stock['dividend'] <= 3:
                choice_.append(stock['dividend'])
    elif stock_type == mid:
        for stock in dividend_stocks:
            if 2 <= stock['dividend'] <= 5:
                if stock['amount'] > 0:
                    choice_.append(stock['dividend'])
    elif stock_type == mid_plus:
        for stock in dividend_stocks:
            if 3 <= stock['dividend'] <= 9:
                choice_.append(stock['dividend'])
    elif stock_type == mid_plus_plus:
        for stock in dividend_stocks:
            if stock['dividend'] >= 3:
                choice_.append(stock['dividend'])
    elif stock_type == high:
        for stock in dividend_stocks:
            if stock['dividend'] >= 4:
                choice_.append(stock['dividend'])
    return choice_


def dividend_promedio(stock_list):
    total_ = 0
    for item in stock_list:
        total_ += item

    promedio = total_ / len(stock_list)

    return promedio


def is_multiplo_de_3(number):
    return number % 3 == 0


def add_to_savings(money, savings):
    savings += money
    return savings


def reform_dividend(percent):
    return percent / 100


def anual_yield(amount):
    yearly_yield = 0

    for month in year:
        if is_multiplo_de_3(year.index(month)):
            yearly_yield += amount * dividend

    return yearly_yield


def apply_taxes(amount):
    tax_to_pay = amount * TAX
    return amount - tax_to_pay, tax_to_pay


def total_invested(dict_of_stocks):
    total_invested_ = 0

    for item in dict_of_stocks:
        if item['amount'] > 0:
            total_invested_ += item['amount']

    return total_invested_


def add_found(money, stock_tag):
    for stock_item in dividend_stocks:
        if stock_item == stock_tag:
            stock_item['amound'] += money


def substract_found(money, stock_tag):
    for stock_item in dividend_stocks:
        if stock_item == stock_tag:
            stock_item['amound'] -= money


def change_of_value(value, stock_tag):
    for stock_item in dividend_stocks:
        if stock_item == stock_tag:
            stock_item['value'] = value


def find_yesterday_value(stock_tag):
    with open(FILENAME, 'r') as file:
        data = file.readlines()

        for line in data:
            if stock_tag == line[0]:
                return int(line[2])


def find_todays_value(stock_tag, manual=True):
    if manual:
        for stock_item in dividend_stocks:
            if stock_tag == stock_item:
                todays_value = input(f'input value for {stock_tag}')
                return todays_value
    return 0


def log_closing_values():
    # filename = 'testing.csv'
    with open(FILENAME, 'w') as file:
        for stock_item in dividend_stocks:
            yesterday_value = find_yesterday_value(stock_item)
            todays_value = find_todays_value(stock_item)
            difference = todays_value - yesterday_value

            line = [stock_item['tag'].upper(), stock_item['amount'], stock_item['value'], difference]
            file.writelines(line)


def dollars_to_euros(amount):
    return amount * 0.89


def euros_to_dollars(amount):
    return amount / 0.89


def dividend_saving(monthly_save_from_salary, dividend_percent, base_savings: int = 0, time_frame=1, exclu_summer=True):
    entered_money_ = base_savings

    for _ in range(time_frame):

        for month in year:
            if exclu_summer:
                if month == 'jul' or month == 'ag':
                    pass
                else:
                    entered_money_ += monthly_save_from_salary
                    base_savings = add_to_savings(monthly_save_from_salary, base_savings)
            else:
                entered_money_ += monthly_save_from_salary
                base_savings = add_to_savings(monthly_save_from_salary, base_savings)

            if is_multiplo_de_3(year.index(month)):
                base_savings += base_savings * dividend_percent

    return base_savings, entered_money_


if __name__ == '__main__':
    """stock groups: all_, low, mid, mid_plus_plus, high, custom"""

    monthly_save = 500
    starting_money = 5000  # dollars(/0.89)
    saving = starting_money
    period = 2  # años

    student_loan = 650 * 5

    choice = all_
    stock_choice = my_choice(choice)
    # print(f'{stock_choice}')
    divident_percent = dividend_promedio(stock_choice)
    print(f'{divident_percent:.2f}')
    dividend = reform_dividend(divident_percent)
    # print(f'{dividend:.4f}')
    total, input_money = dividend_saving(monthly_save, dividend, starting_money, time_frame=2)
    print(f'{total:.2f}, {input_money:.2f}, {total - input_money:.2f}')
    # earnings = total - input_money
    # # print(f'{earnings:.2f}')
    # earnings_netto, taxes = apply_taxes(earnings)  # taxes are on earnings not all
    # # print(f'{earnings_netto:.2f}, {taxes:.2f}')
    # total_netto = input_money + earnings_netto
    # yields = total * dividend
    # # print(f'{yields:.2f}')
    # netto, _ = apply_taxes(yields)
    # # print(f'{netto:.2f}')
    # yearly = netto * 4
