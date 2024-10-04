from scrapy.spiders import Spider

class ValidMindSpider(Spider):
    name = 'valid'
    start_urls = ['https://validmind.com/blog/']  # FIRST LEVEL
    pagination_links = ['https://validmind.com/blog/?_paged=2', 'https://validmind.com/blog/?_paged=3', 'https://validmind.com/blog/?_paged=4', 'https://validmind.com/blog/?_paged=5']

    custom_settings = {
        'FEEDS': {
            'validmind-blogs.json': {
                'format': 'json',
                'overwrite': True
            }
        }
    }

    # 1. FOLLOWING
    def parse(self, response):
        # Extract all the blog post links from the current page
        links = response.xpath('//div[contains(@class, "x-row-inner")][1]/a/@href').getall()

        # Extract data from each blog post on the blog page
        for link in links:
            yield response.follow(link, self.extract_blog)

        # 3. PAGINATION
        # Paginate through the next page if available
        next_page_url = self.pagination_links.pop(0) if self.pagination_links else None

        # Recursively follow the next page if available
        if next_page_url:
            yield response.follow(next_page_url, self.parse)

    # 2. DATA EXTRACTION
    def extract_blog(self, response):
        # Extract blog post data from the individual blog post
        data = {
            "heading": response.xpath('//h1/text()').get(),
            "author": response.xpath('//div[contains(@class, "pp-author-boxes-name")]/a/@title').get(),
            "date": response.xpath('//div[@class="x-text-content-text"]//span[@class="x-text-content-text-subheadline"]/text()').get(),
            # "content": response.xpath('//div[@class="x-text x-content e129323-e11 m2rsb-y m2rsb-z"]/p/text()').getall()
        }
        return data