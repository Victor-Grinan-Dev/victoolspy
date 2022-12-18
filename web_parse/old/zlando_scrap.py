from web_parse import web_parser_mods as scrap
from pprint import pprint

container = scrap.url_decoder_requester('https://www.zalando.es/collections/dT1vanCBQ4-/')

brands = scrap.full_parse('https://www.zalando.es/collections/dT1vanCBQ4-/', 'div',
                          "cat_brandName-2XZRz cat_ellipsis-MujnT")
articleName = scrap.full_parse('https://www.zalando.es/collections/dT1vanCBQ4-/', 'div',
                               'cat_articleName--arFp cat_ellipsis-MujnT')
prices = scrap.full_parse('https://www.zalando.es/collections/dT1vanCBQ4-/', 'div', "cat_prices-2-Zhx")
original_price = scrap.full_parse('https://www.zalando.es/collections/dT1vanCBQ4-/', 'div',
                                  "cat_originalPrice-2Oy4G")
if "cat_promotionalPrice-3GRE7" in prices:
    sale_price = scrap.full_parse('https://www.zalando.es/collections/dT1vanCBQ4-/', 'div',
                                  "cat_flag-2CGUe cat_sale-3Tti_")
    pprint('have promotional price')

image = scrap.full_parse('https://www.zalando.es/collections/dT1vanCBQ4-/', 'div', "cat_imageCnt-2orIb")

# print(len(container))
# print(len(brands))#32
# print(len(articleName))
# print(len(prices))
# print(len(original_price))

j = 0

for element in range(32):

    try:
        i = j
        pprint(brands[i].text)
        pprint(articleName[i].text)
        pprint(prices[i].text)
        pprint(sale_price[i].text)
        j += 1
    except:
        pass
