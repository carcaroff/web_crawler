import scrapy
import re


class VideoCardsSpider(scrapy.Spider):
    name = 'video_cards'
    allowed_domains = [
        'pichau.com.br/',
        'webcache.googleusercontent.com',
        'kabum.com.br',
    ]
    start_urls = [
        'https://www.pichau.com.br/hardware/placa-de-video',
        'https://webcache.googleusercontent.com/search?q=cache:https:'
        '//www.terabyteshop.com.br/hardware/placas-de-video',
        'https://webcache.googleusercontent.com/search?q=cache:'
        'https://kabum.com.br/hardware/placa-de-video-vga',
    ]

    def parse(self, response):
        if response.request.url == 'https://www.pichau.com.br/hardware/placa-de-video':
            self._parse_pichau(response)
        elif response.request.url == 'https://webcache.googleusercontent.com/search?q=cache:' \
                                     'https://www.terabyteshop.com.br/hardware/placas-de-video':
            self._parse_terabyte(response)
        elif response.request.url == 'https://kabum.com.br/hardware/placa-de-video-vga':
            self._parse_kabum(response)

    def _parse_pichau(self, response):
        products = response.css('div.MuiCardContent-root')
        for product in products:
            product_data = {
                'nome': product.css('h2::text').get(),
                'preco_a_vista': product.css('div::text')[1].get(),
                'preco_parcelado': product.css('div::text')[2].get(),
                'url': response.url,
            }
            yield product_data
        next_page = response.css('').attrib['href']

    def _parse_kabum(self, response):
        f = open('kabum_html.html', 'a')
        f.write(response.txt)
        f.close()

        # products = response.css('div.productCard')
        # for product in products:
        #     product_data = {
        #         'nome': product.css('a::text').get(),
        #         'preco_a_vista': product.css('div::text').get(),
        #         'preco_parcelado': product.css('span::text').get(),
        #         'url': response.url,
        #     }
        #     yield product_data

    def _parse_terabyte(self, response):
        products = response.css('div.commerce_columns_item_inner')

        for product in products:
            product_data = {
                'nome': product.css('a').attrib['title'],
                'preco_a_vista': product.css('div.prod-new-price').css('span::text').get(),
                'preco_parcelado': str(12 * float(re.sub('[^0-9,]', '', product.xpath(
                    '//*[@id="prodarea"]/div[1]/div/div[4]/div[1]/div[3]/span[2]').get()))),
                'url': response.url,
            }
            yield product_data
