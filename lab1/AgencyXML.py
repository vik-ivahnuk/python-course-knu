
from xml.dom.minidom import Document
from xml.dom.minidom import Element
from xml.dom.minidom import parse
from lxml import etree

from xml_validator import validate_by_xsd
from news.News import News
from news.NewsCategory import NewsCategory

class AgencyXML:

    XSD_PATH: str = "resources/agency.xsd"

    @staticmethod
    def get_category_by_id(xml_path: str, search_id: int) -> NewsCategory:
        if(validate_by_xsd(xml_path, AgencyXML.XSD_PATH)):
            with parse(xml_path) as dom:
                dom: Document = dom
                for category in dom.getElementsByTagName("Category"):
                    category: Element = category
                    if category.nodeType == category.ELEMENT_NODE:
                        if int(category.getAttribute("id")) == search_id:
                            news: [News] = []
                            for nw in category.childNodes:
                                nw: Element = nw
                                if nw.nodeType == nw.ELEMENT_NODE:
                                    news.append(
                                        News(int(nw.getAttribute("id")),
                                             nw.getAttribute("name"),
                                             int(nw.getAttribute("pages")),
                                             nw.getAttribute("author"))
                                    )
                            return NewsCategory(
                                int(category.getAttribute("id")),
                                category.getAttribute("name"),
                                news
                            )
        return None

    @staticmethod
    def get_news_by_category(xml_path: str, category_id: int) -> [News]:
        if (validate_by_xsd(xml_path, AgencyXML.XSD_PATH)):
            with parse(xml_path) as dom:
                dom: Document = dom
                for category in dom.getElementsByTagName("Category"):
                    category: Element = category
                    if category.nodeType == category.ELEMENT_NODE:
                        if int(category.getAttribute("id")) == category_id:
                            news: [News] = []
                            for nw in category.childNodes:
                                nw: Element = nw
                                if nw.nodeType == nw.ELEMENT_NODE:
                                    news.append(
                                        News(
                                             int(nw.getAttribute("id")),
                                             nw.getAttribute("name"),
                                             int(nw.getAttribute("pages")),
                                             nw.getAttribute("author")
                                        )
                                    )
                            return news
        return []

    @staticmethod
    def get_new_by_id(xml_path: str, news_id: int) -> News:
        if(validate_by_xsd(xml_path, AgencyXML.XSD_PATH)):
            with parse(xml_path) as dom:
                dom: Document = dom
                for nw in dom.getElementsByTagName("News"):
                    nw: Element = nw
                    if nw.nodeType == nw.ELEMENT_NODE:
                        if news_id == int(nw.getAttribute("id")):
                            return News(
                                int(nw.getAttribute("id")),
                                nw.getAttribute("name"),
                                int(nw.getAttribute("pages")),
                                nw.getAttribute("author")
                            )
        return None




    @staticmethod
    def get_all_categories(xml_path: str) -> [NewsCategory]:
        result: [NewsCategory] = []
        if(validate_by_xsd(xml_path, AgencyXML.XSD_PATH)):
            with parse(xml_path) as dom:
                dom: Document = dom
                for category in dom.getElementsByTagName("Category"):
                    category: Element = category
                    if category.nodeType == category.ELEMENT_NODE:
                        news: [News] = []
                        for nw in category.childNodes:
                            nw: Element = nw
                            if nw.nodeType == nw.ELEMENT_NODE:
                                news.append(
                                    News(
                                         int(nw.getAttribute("id")),
                                         nw.getAttribute("name"),
                                         int(nw.getAttribute("pages")),
                                         nw.getAttribute("author")
                                    )
                                )
                        result.append(
                            NewsCategory(
                                     int(category.getAttribute("id")),
                                     category.getAttribute("name"),
                                     news
                            )
                        )

        return result



    @staticmethod
    def save_all(xml_path: str, categories_news: [NewsCategory] = []) -> None:
        validate_by_xsd(xml_path, AgencyXML.XSD_PATH)
        document: Document = Document()
        agency: Element = document.createElement('Agency')
        agency.setAttribute("xmlns", "http://vik-ivahnuk.com.lab1/agency")
        document.appendChild(agency)
        for category in categories_news:
            category_element: Element = document.createElement('Category')
            category_element.setAttribute("id", str(category.id))
            category_element.setAttribute("name", category.name)
            for nw in category.news:
                news_element: Element = document.createElement('News')
                news_element.setAttribute("id", str(nw.id))
                news_element.setAttribute("name", nw.name)
                news_element.setAttribute("pages", str(nw.pages))
                news_element.setAttribute("author", nw.author)
                category_element.appendChild(news_element)

            agency.appendChild(category_element)

        element = etree.fromstring(document.toxml())
        etree.indent(element, space="\t")
        xml_content = etree.tostring(element, encoding="UTF-8",
                                pretty_print=True, xml_declaration=True)
        with open(xml_path, "wb") as f:
            f.write(xml_content)
