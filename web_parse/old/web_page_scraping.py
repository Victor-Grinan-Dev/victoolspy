from web_parse.old.web_parser_module import url_decoder_requester as uReq
from web_parse.web_parser_mods import soup_parser_decoder as soup

# standard procedure to parse pages
# @staticmethod

# untill here

page_soup = uReq('http://www.bolterandchainsword.com/forum/17-army-list-reviews/')
main_container = soup(page_soup, "strong", "highlight_unread")

# print(len(main_header_container))

carpeta = r'C:\Users\victo\Desktop\army list'

for element in main_container:
    """accessing to each army set of name:link"""
    link = element.a["href"]
    army_class = element.a["title"]
    print("************************" * 4)
    print(army_class, "\n", link)
    print("************************" * 4)
    page_soup = uReq(link)
    army_list_container = soup(page_soup, "td", "col_f_content")
    file_name = army_class

    for item in army_list_container[:10]:
        try:
            list_link = item.h4.a["href"]
            list_name = item.h4.a["title"]
            print("----------------------------" * 4)
            print("\t" * 2, list_name, "\n", list_link)
            page_soup = uReq(list_link)
            list_data_container = page_soup.findAll("div", {"class": "post_body"})
        except:
            pass

        for posted_list in list_data_container:
            data = posted_list.div.text
            print(data)
