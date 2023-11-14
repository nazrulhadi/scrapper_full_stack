from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "zus"
    
    start_urls = [
        "https://zuscoffee.com/category/store/melaka/"
    ]
    # def start_requests(self):
    #     # urls = [
    #     #     "https://zuscoffee.com/category/store/melaka/"]
    #     # for url in urls:
    #     #     yield scrapy.Request(url=url, callback=self.parse)
    #     start_urls = ["https://zuscoffee.com/category/store/melaka/"]

    def parse(self, response):
        stop_condition = "Are you ready"
        # data = response.css('p')
        list_of_outlet = []
        list_of_address = []
        for i in range(len(response.css('p'))):
            if stop_condition not in response.css('p::text')[i].get():
                if i % 2 == 0:
                    print(response.css('p::text')[i].get())
                    list_of_outlet.append(response.css('p::text')[i].get())
                else:
                    print(response.css('p::text')[i].get())
                    list_of_address.append(response.css('p::text')[i].get())
            else:
                break
        next_page = response.css('a.page-numbers.next::attr(href)').get()
        print(next_page)
        if next_page:
            yield response.follow(url=next_page, callback=self.parse)
             
                        
        

        for j in range(len(list_of_outlet)):
            yield {
                'outlet_name': list_of_outlet[j],
                'address': list_of_address[j]
            }
        
        print("finish scrapping")  