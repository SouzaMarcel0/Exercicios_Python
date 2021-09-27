"""
##### RASPANDO DADOS com SCRAPY ######

1. pip install scrapy  
2. scrapy startproject 'nomedesuaesolha'  
3. acessa diretorio com nome escolhido por você com CD..
4. gerar modelo com o comando: scrapy genspider + iniciais do nome do projeto + nomedosite.com
5. acessar arquivo spider: o que contem as iniciais atribuidas por você
6. Removar o allowed_domains e por o ***kwargs no argumento da função def
7. remova o pass
8. insirar a função FOR para começar a trabalhar na página
9. Faça uma inspeção na página alvo e verifique quais são as CLASS/SPANS que remetem ao objeto de destino para raspagem
10. O conteúdo poderá está em muitas páginas, por isso é importante criar um LAÇO de repetção dentro do FOR, para apontar a condição para continuar a crawlear a PROXIMA página.
11. No arquivo de SETTINGS.py você irá alterar os seguintes parametros:
    a) ROBOTSTXT_OBEY = True Mude para False
    b) USER_AGENT = Tire o # e insira o seu (no google, pesquise: My user agent)
    c) AUTOTHROTTLE_ENABLED = True - Retire o #, pois irá ajudar no acesso à página, não forçando a qte de requisições.
    d) Ative o programa com o comando: scrapy crawl ml -o nomedoqrquivo.json
    e) Virique se está tudo ok e aguarde, ele vai gerar um JSON, que você poderá consumir...
"""

import scrapy


class MlSpider(scrapy.Spider):
    name = 'ml'
    
    start_urls = ['https://www.mercadolivre.com.br/ofertas?page=1']

    def parse(self, response, **kwargs):
        for i in response.xpath ('//li[@class="promotion-item"]') :
            title = i.xpath ('.//p[@class="promotion-item__title"]/text()').get()
            price = i.xpath ('.//span[@class="promotion-item__price"]//text()').getall()
            oldprice = i.xpath ('.//span[@class="promotion-item__oldprice"]//text()').getall()            
            link = i.xpath ('./a/@href').get()

            yield{
                'title': title,
                'price': price,
                'oldprice': oldprice,
                'link': link 
            }

        next_page = response.xpath('//a[contains(@title, "Próxima")]/@href').get()
        if next_page:
            yield scrapy.Request (url=next_page, callback=self.parse)
