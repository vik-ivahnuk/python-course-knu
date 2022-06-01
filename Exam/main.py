# variant 6


class Concert:
    def __init__(self, place, genre, data, price, authors):
        self.place = place
        self.genre = genre
        self.data = data
        self.price = price
        self.authors = authors

    def __repr__(self):
        return "place {0} genre {1} data {2} price {3} authors".format(self.place, self.genre,
                                                                       self.data, self.price, self.authors)


class VirtualConcert(Concert):
    def __init__(self, place, genre, data, price, authors):
        super().__init__(place, genre, data, price, authors)

    def ticket_booking(self):
        return True  # всігда бесплатно


class LiveConcert(Concert):
    def __init__(self, place, genre, data, price, authors, num_tikets):
        super().__init__(place, genre, data, price, authors)
        self.num_tikets = num_tikets

    def ticket_booking(self):
        self.num_tikets -= 1
        if self.num_tikets < 1:
            return False
        else:
            return True


class Manager:
    concerts: [Concert] = []

    def tiket_booking(self, place, live: bool):
        for a in self.concerts:
            if (isinstance(a, LiveConcert) and place == a.place) or live :
                return a.ticket_booking()
        return False

    def sort_by_price(self):
        self.concerts.sort(key=lambda x: x.price)

    def get_concert_by_genre(self, genre):
        res = list()
        for a in self.concerts:
            if a.genre == genre:
                res.append(a)
        return res



if __name__ == "__main__":
    manager = Manager()
    manager.concerts= [
        VirtualConcert("kiyv", "vocal", "11.11.22", 11, "jamala"),
        VirtualConcert("kiyv", "vocal", "12.11.22", 14, "noize"),
        LiveConcert("New York", "vocal", "12.11.22", 41, "noize", 44),
        LiveConcert("New York", "danse", "12.11.22", 11, "noize", 44),
    ]

    print(manager.tiket_booking("New York", False))
    manager.sort_by_price()
    for a in manager.concerts:
        print(a)
    print("#"*20,"\n")
    print(manager.get_concert_by_genre("vocal"))
