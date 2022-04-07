

class News:
    def __init__(self, _id: int, name: str, pages: int, author: str):
        self.id = _id
        self.name = name
        self.pages = pages
        self.author = author

    def __repr__(self):
        return "News - id: {0} name: {1} pages: {2} author: {3}".format(
            self.id, self.name, self.pages, self.author)




