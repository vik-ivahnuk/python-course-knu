from AgencyXML import AgencyXML as axml
from news.NewsCategory import NewsCategory
from news.News import News


class AgencyManagement:
    def __init__(self, xml_path: str):
        self.__xml_path = xml_path
        self.__news_categories = axml.get_all_categories(xml_path)

    def get_category_by_id(self, _id: int) -> NewsCategory:
        for category in self.__news_categories:
            if category.id == _id:
                return category
        return None

    def get_news_by_id(self, _id: int) -> News:
        for category in self.__news_categories:
            for nw in category.news:
                if nw.id == _id:
                    return nw
        return None

    def get_news_by_category(self, category_id: int) -> [News]:
        for category in self.__news_categories:
            if category.id == category_id:
                return category.news
        return []

    def id_in_categories(self, _id: int) -> bool:
        for category in self.__news_categories:
            if _id == category.id:
                return True
        return False

    def id_in_news(self, _id: int) -> bool:
        for category in self.__news_categories:
            for nw in category.news:
                if _id == nw.id:
                    return True
        return False

    def print_category(self, _id: int) -> None:
        for category in self.__news_categories:
            if category.id == _id:
                print(category)
                return None
        print("categories with this ID were not found")

    def print_news_by_category(self, category_id: int) -> None:
        for category in self.__news_categories:
            if category.id == category_id:
                for nw in category.news:
                    print(nw)
                return None
        print("news with this ID were not found")

    def print_news_by_id(self, _id: int) -> None:
        for category in self.__news_categories:
            for nw in category.news:
                if nw.id == _id:
                    print(nw)
                    return None
        print("news with this ID were not found")

    def print_all_categories(self) -> None:
        if len(self.__news_categories) == 0:
            print("the list of categories is empty")
        for category in self.__news_categories:
            print(category)

    def print_news_by_range(self, min: int, max: int) -> None:
        availability = False
        for category in self.__news_categories:
            for nw in category.news:
                if min < nw.pages < max:
                    availability = True
                    print(nw)
        if not availability:
            print("no news found for the specified size")

    def add_category(self, _id: int, name: str) -> None:
        if not self.id_in_categories(_id):
            self.__news_categories.append(NewsCategory(_id, name))
            axml.save_all(self.__xml_path, self.__news_categories)
        else:
            print("category with such ID already exists")

    def add_news(self, category_id: int, news_id: int, name: str, pages: int, author: str) -> None:
        category_id_find = False
        if not self.id_in_news(news_id):
            for category in self.__news_categories:
                if category.id == category_id:
                    category_id_find = True
                    category.news.append(News(news_id, name, pages, author))
                    axml.save_all(self.__xml_path, self.__news_categories)
                    break
        else:
            category_id_find = True
            print("news with such ID already exists")
        if not category_id_find:
            print("there is no category with this ID")

    def upgrade_category(self, category_id: int, new_name: str) -> None:
        if self.id_in_categories(category_id):
            for category in self.__news_categories:
                if category.id == category_id:
                    category.name = new_name
                    axml.save_all(self.__xml_path, self.__news_categories)
                    print("the category upgrade was successful")
                    break
        else:
            print("category with such ID already exists")

    def upgrade_news(self, news_id: int, new_name: str ,
                     new_pages: int, new_author: str) -> None:
        if self.id_in_news(news_id):
            _exit = False
            for category in self.__news_categories:
                for nw in category.news:
                    if nw.id == news_id:
                        nw.name = new_name
                        nw.pages = new_pages
                        nw.author = new_author
                        _exit = True
                        axml.save_all(self.__xml_path, self.__news_categories)
                        print("the news upgrade was successful")
                    if _exit:
                        return None
        print("news with such ID already exists")

    def remove_category(self, _id: int) -> None:
        deleted_element = None
        for category in self.__news_categories:
            if _id == category.id:
                deleted_element = category
                break
        if deleted_element is not None:
            self.__news_categories.remove(deleted_element)
            axml.save_all(self.__xml_path, self.__news_categories)
            print("removal was successful")
        else:
            print("removal failed")

    def remove_news(self, _id: int) -> None:
        for category in self.__news_categories:
            deleted_element = None
            for nw in category.news:
                if nw.id == _id:
                    deleted_element = nw
                    break
            if deleted_element is not None:
                category.news.remove(deleted_element)
                axml.save_all(self.__xml_path, self.__news_categories)
                print("removal was successful")
                return None

        print("removal failed")

    def clear(self):
        self.__news_categories.clear()
        axml.save_all(self.__xml_path, self.__news_categories)

