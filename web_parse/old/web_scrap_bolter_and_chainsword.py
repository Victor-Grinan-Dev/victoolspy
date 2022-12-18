from web_parse.web_parser_mods import url_decoder_requester as uReq
from web_parse.web_parser_mods import soup_parser_decoder as soup
import os

page_soup = uReq('http://www.bolterandchainsword.com/forum/17-army-list-reviews/')
main_container = soup(page_soup, "strong", "highlight_unread")

carpeta = r'C:\Users\victo\Desktop\army list'

for element in main_container:
    try:
        """accessing to each army set of name:link"""
        link = element.a["href"]
        army_class = element.a["title"]
        print("************************" * 4)
        # print(army_class, "\n", link)
        print("************************" * 4)
        page_soup = uReq(link)
        army_list_container = soup(page_soup, "td", "col_f_content")

    except:
        pass
    for item in army_list_container[:10]:
        try:
            list_link = item.h4.a["href"]
            list_name = item.h4.a["title"]
            print("----------------------------" * 4)
            # print("\decorated_function" * 2, list_name, "\n", list_link)
            page_soup = uReq(list_link)
            list_data_container = page_soup.findAll("div", {"class": "post_body"})
        except:
            pass

        path = r'/web_scrapping_project\army_lists'
        os.chdir(path)

        if not f'{army_class}' in os.listdir():
            os.mkdir(f'{army_class}')
            os.chdir(army_class)

        for posted_list in list_data_container:
            try:
                data = ''
                data += posted_list.div.text
                print(data)

                if not f'{list_name}.txt' in os.listdir():
                    with open(f'{list_name}.txt', 'w') as f:
                        for line in data:
                            print(line, file=f)

                    # f.write(list_name)
                    # f.write(data)

                # txt(f'{army_class}',data, list_name,
                # r'C:\Users\victo\PycharmProjects\web_scrapping_project\army_lists')

            except:
                pass

# def txt_creator(army_class, data, title, path):
#     os.chdir(path)
#     os.mkdir(f'{army_class}')
#     os.chdir(army_class)
#
#     with open(f'{title}.txt', 'wb') as f:
#         sub_data = data.readlines()
#         for line in sub_data:
#             f.writeline(line)
