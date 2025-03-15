import scrapy

class QuotesSpider(scrapy.Spider):

    name = 'quotes'

    start_urls = ['https://quotes.toscrape.com']  

    def parse(self, response):

        quotes = response.css('div.quote')

        self.log(f"Found {len(quotes)} quotes on the page")

        # Iterate over each quote found and yield the extracted data
        for current_quote in quotes:
            yield {
                'quote': current_quote.css('span.text::text').get(),
                'author': current_quote.css('small.author::text').get()
            }

        # Follow pagination link (Next button)
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)