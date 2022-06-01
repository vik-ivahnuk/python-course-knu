# variant 6


class Concert:
    def __init__(self, place, genre, data, price, authors):
        self.place = place
        self.genre = genre
        self.data = data
        self.price = price
        self.authors = authors




class VirtualConcert(Concert):
    def __init__(self, place, genre, data, price, authors):
        super.__init__(place, genre, data, price, authors)

    def ticket_booking(self):
        return True  # всігда бесплатно


class LiveConcert(Concert):
    def __init__(self, place, genre, data, price, authors, num_tikets):
        super.__init__(place, genre, data, price, authors)
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
            if (isinstance(a,LiveConcert) and place == a.place) or live == True:
                return a.ticket_booking()
        return False

    def sort_by_name(self):
        self.concerts.sort(key=lambda x: x.name)

