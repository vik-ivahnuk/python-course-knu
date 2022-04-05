

class News:
    def __init__(self, _id: int, name: str, pages: int, author: str, id_category: int):
        self.id = _id
        self.name = name
        self.pages = pages
        self.author = author
        self.category = id_category