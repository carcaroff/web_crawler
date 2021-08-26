import scrapy
import re


class VideoCardsSpider(scrapy.Spider):
    name = 'video_cards'
    allowed_domains = [
        'pichau.com.br/',
        'localhost:8050/',
    ]
    start_urls = [
        'http://localhost:8050/render.html?url=https://www.pichau.com.br/hardware/placa-de-video',
        'http://localhost:8050/render.html?url=https://www.amazon.com.br/b?node=16364811011&ref=lp_16364750011_nr_n_9',
        'http://localhost:8050/render.html?url=https://www.chipart.com.br/placa-de-video',
    ]

    def parse(self, response):
        if response.url.split('=', 1)[1].split('/', 3)[2] == 'www.pichau.com.br':
            page = 1
            products = response.css('div.MuiCardContent-root')

            for product in products:
                if not product.css('div::text'):
                    page = 0
                    break
                product_data = {
                    'nome': product.css('h2::text').get(),
                    'preco_a_vista': 'R$' + product.css('div::text')[1].get(),
                    'preco_parcelado': re.sub('[^R$0-9,]', '', product.css('div::text')[2].get()),
                    'url': response.url.split('=', 1)[1],
                }
                yield product_data
            if page:
                page += 1
                yield scrapy.Request('http://localhost:8050/render.html?url=https://www.pichau.com.br/hardware/placa-de'
                                     '-video?page=%s' % page, callback=self.parse)

        elif response.url.split('=', 1)[1].split('/', 3)[2] == 'www.amazon.com.br':
            products = response.css('div.sg-col-4-of-12')
            for product in products:
                product_data = {
                    'nome': product.css('h2').css('span::text').get(),
                    'preco_a_vista': re.sub('[^R$0-9,]', '', product.css('span.a-offscreen::text').get()),
                    'preco_parcelado': re.sub('[^R$0-9,]', '', product.css('span.a-offscreen::text').get()),
                    'url': response.url.split('=', 1)[1],
                }
                if not product_data['preco_a_vista']:
                    continue

                yield product_data
            next_page = response.xpath(
                '//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[32]/span/div/div/ul/li[7]/a/@ref')

            if next_page:
                yield scrapy.Request('http://localhost:8050/render.html?url=https://www.amazon.com.br' + next_page,
                                     callback=self.parse)

        elif response.url.split('=', 1)[1].split('/', 3)[2] == 'www.chipart.com.br':
            products = response.css('div.product-card')

            for product in products:
                product_data = {
                    'nome': product.css('div.product-title').css('h2::text').get(),
                    'preco_a_vista': product.css('div.billet').css('span.price.total::text').get(),
                    'preco_parcelado': product.css('div.creditcard').css('span.price.total::text').get(),
                    'url': response.url.split('=', 1)[1],
                }
                if not product_data['preco_a_vista']:
                    return
                yield product_data

            next_page = response.xpath('/html/body/div[1]/main/div[1]/div[2]/div/div[2]/div[2]/section/div/div['
                                       '3]/div/div/div[3]/div/div[3]/a/@href')
            if next_page:
                yield scrapy.Request('http://localhost:8050/render.html?url=https://www.chipart.com.br' + next_page,
                                     callback=self.parse)
