"""
工具函数 Alt+Shift+Enter
"""


def is_isbn_or_key(word):
    """
    判断是否为isbn，如果是则返回true，否则返回false
    isbn: isbn13 13个0至9的数字组成,3个-
    :param word:
    :return:
    """
    short_word = word.replace('-', "")
    if '-' in word and len(short_word) > 10 and short_word.isdigit():
        return True
    return False
