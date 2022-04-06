from news.News import News

class NewsCategory:
    def __init__(self, id: int, name: str, news: [News]):
        self.id = id
        self.name = name
        self.news = news

    def __repr__(self):
        result = "id: {0} name: {1}".format(self.id, self.name)
        for nw in self.news:
            result = result+"\n\t"+nw.__repr__()
        return result


