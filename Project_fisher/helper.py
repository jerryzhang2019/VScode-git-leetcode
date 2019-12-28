# 子函数 # 以下代码是用来判断q是isbn还是关键字
def is_isbn_or_key(word):
    """
    以下代码是用来判断q是isbn还是关键字
    :param word:
    :return:
    """
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    # if '-' in q and len(q.replace('-', '')) == 10 and q.replace('-', '').isdigit:  # 代码太长更改一下
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit:
        isbn_or_key = 'isbn'
    return isbn_or_key