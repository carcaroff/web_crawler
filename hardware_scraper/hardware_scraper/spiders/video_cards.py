import scrapy


class VideoCardsSpider(scrapy.Spider):
    name = 'video_cards'
    allowed_domains = ['kabum.com.br/']
    start_urls = ['https://www.pichau.com.br/hardware/placa-de-video']

    def parse(self, response):
        products = response.css('div.MuiCardContent-root')
        for product in products:
            product_data = {
                'nome': product.css('h2::text').get(),
                'preco_a_vista': product.css('div::text')[1].get(),
                'preco_parcelado': product.css('div::text')[2].get(),
            }
            yield product_data
