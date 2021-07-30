import requests,re

class MyCrawler:
    def __init__(self, filename):
        self.filename = filename
#采
    def download(self, url):
        r = requests.get(url)
        return r.text
#抽
    def extract(self, content, pattern):
        result = re.findall(pattern, content)
        return result
#存
    def save(self, info):
        with open(self.filename, "a") as f:
            for item in info:
                f.write(item[0] + ' ' + item[1] + '\n')

    def crawl(self, url, pattern):
        content = self.download(url)
        info = self.extract(content, pattern)
        self.save(info)

a = MyCrawler("mobile.txt")
urltext = a.download('https://wap.zol.com.cn/top/cell_phone/')
a.crawl('https://wap.zol.com.cn/top/cell_phone/','<p class="pro-info-name f28">(.*?)（(.*?)）<\/p>')