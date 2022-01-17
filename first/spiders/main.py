import subprocess


def crawl_work():
    subprocess.Popen('scrapy crawl anquangongcheng', shell=True).wait()
    subprocess.Popen('scrapy crawl Shuilidianli', shell=True).wait()
    subprocess.Popen('scrapy crawl Gongshang', shell=True).wait()
    subprocess.Popen('scrapy crawl Shengtaizhiye', shell=True).wait()
    subprocess.Popen('scrapy crawl Jidian', shell=True).wait()


if __name__ == '__main__':
    crawl_work()
