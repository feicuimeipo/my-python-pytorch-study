"""
Create by 卡门 on
"""

__author__ = "卡门"

from httper import HTTP


class YuShuBook:
    # 类变量
    # {} 是动态传入的
    isbn_url = 'https://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'https://t.yushu.im/v2/book/search?q={}&count={}start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        # 读读类变量的方式, YuShuBook.isbn_url 或 self.isbn_ur 后者称之为链式查找
        # 会将isbn变量的值填入{}中
        url = cls.isbn_url.format(isbn)

        # result由Get的json返回变直接会自动变为python的dic
        result = HTTP.GET(url)
        return result

    @classmethod
    def search_by_keyword(cls, keyword, count=15, start=0):
        url = cls.keyword_url.format(keyword,count,start)
        result = HTTP.GET(url);
        return result;
