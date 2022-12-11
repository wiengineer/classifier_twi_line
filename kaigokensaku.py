import scrapy
from kaigo.items import KaigoItem


class KaigokensakuSpider(scrapy.Spider):
    name = "kaigokensaku"
    allowed_domains = ["kaigokensaku.mhlw.go.jp"]
    start_urls = [
        "https://www.kaigokensaku.mhlw.go.jp/32/index.php?action_kouhyou_detail_033_kihon=true&JigyosyoCd=3270401916-00&ServiceCd=780",
        "https://www.kaigokensaku.mhlw.go.jp/32/index.php?action_kouhyou_detail_033_kihon=true&JigyosyoCd=3271600664-00&ServiceCd=780",
        "https://www.kaigokensaku.mhlw.go.jp/32/index.php?action_kouhyou_detail_025_kihon=true&JigyosyoCd=3272200167-00&ServiceCd=210",
        "https://www.kaigokensaku.mhlw.go.jp/32/index.php?action_kouhyou_detail_022_kihon=true&JigyosyoCd=3271500278-00&ServiceCd=320",
        "https://www.kaigokensaku.mhlw.go.jp/32/index.php?action_kouhyou_detail_023_kihon=true&JigyosyoCd=3270800224-00&ServiceCd=430",
        "https://www.kaigokensaku.mhlw.go.jp/32/index.php?action_kouhyou_detail_023_kihon=true&JigyosyoCd=3271600565-00&ServiceCd=430",
        "https://www.kaigokensaku.mhlw.go.jp/32/index.php?action_kouhyou_detail_033_kihon=true&JigyosyoCd=3270800703-00&ServiceCd=780",
        "https://www.kaigokensaku.mhlw.go.jp/32/index.php?action_kouhyou_detail_023_kihon=true&JigyosyoCd=3270300225-00&ServiceCd=430",
        "https://www.kaigokensaku.mhlw.go.jp/32/index.php?action_kouhyou_detail_001_kihon=true&JigyosyoCd=3270500022-00&ServiceCd=110",
        "https://www.kaigokensaku.mhlw.go.jp/32/index.php?action_kouhyou_detail_023_kihon=true&JigyosyoCd=3270103942-00&ServiceCd=430",
    ]

    def parse(self, response):
        for body in response.xpath("//body"):
            yield KaigoItem(
                meisyou=body.xpath(
                    '//div[@id="tableGroup-3"]/table/tbody/tr[3]/td/text()'
                ).extract_first(),
                syurui=body.xpath("//div[@id='serviceName']/text()").extract_first(),
                syozaiti=body.xpath(
                    '//div[@id="tableGroup-3"]/table/tbody//th[contains(text(),"都道府県")]/following-sibling::td/text()'
                ).extract_first(),
                denwa=body.xpath(
                    '(//div[@id="tableGroup-3"]/table/tbody//th[contains(text(),"電話番号")]/following-sibling::td/text()'
                ).extract_first(),
                fax=body.xpath(
                    '(//div[@id="tableGroup-3"]/table/tbody//th[contains(text(),"FAX番号")]/following-sibling::td/text()'
                ).extract_first(),
                houjinsyurui=body.xpath(
                    '//div[@id="tableGroup-1"]/table/tbody//th[contains(text(),"法人等の名称")]/following-sibling::td/text()'
                ).extract_first(),
                hounjinbangou=body.xpath(
                    '//p[@id="check_CorporateNumber"]'
                ).extract_first(),
            )
        pass
