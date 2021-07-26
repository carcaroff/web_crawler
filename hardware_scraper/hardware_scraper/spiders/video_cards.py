import scrapy


class VideoCardsSpider(scrapy.Spider):
    name = 'video_cards'
    allowed_domains = [
        'pichau.com.br/',
        'webcache.googleusercontent.com',
    ]
    start_urls = [
        'https://www.pichau.com.br/hardware/placa-de-video',
        'https://webcache.googleusercontent.com/search?q=cache:'
        'https://www.terabyteshop.com.br/hardware/placas-de-video',
        'https://webcache.googleusercontent.com/search?q=cache:https://www.kabum.com.br/hardware/placa-de-video-vga',
    ]

    def parse(self, response):
        products = response.css('div.MuiCardContent-root')
        for product in products:
            product_data = {
                'nome': product.css('h2::text').get(),
                'preco_a_vista': product.css('div::text')[1].get(),
                'preco_parcelado': product.css('div::text')[2].get(),
            }
            yield product_data
