from news.News import News

class NewsCategory:
    def __init__(self, _id: int, name: str, news: [News] = None):
        self.id = _id
        self.name = name
        self.news = [] if news is None else news

    def __repr__(self):
        result = "Category - id: {0} name: {1}".format(self.id, self.name)
        for nw in self.news:
            result = result+"\n\t"+nw.__repr__()
        return result


