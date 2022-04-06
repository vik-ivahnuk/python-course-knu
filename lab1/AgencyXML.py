
from xml.dom.minidom import Document
from xml.dom.minidom import Element
from xml.dom.minidom import parse
from lxml import etree

from xmlvalidator import validate_xml
from news.News import News
from news.NewsCategory import NewsCategory

class AgencyXML:

    XSD_PATH: str = "resources/agency.xsd"

    @staticmethod
    def get_all_categories_news(xml_path: str) -> [NewsCategory]:
        result: [NewsCategory] = []
        if(validate_xml(xml_path, AgencyXML.XSD_PATH)):
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
                                    News(int(nw.getAttribute("id")),
                                         nw.getAttribute("name"),
                                         nw.getAttribute("pages"),
                                         nw.getAttribute("author"))
                                )
                        result.append(
                            NewsCategory(category.getAttribute("id"),
                                     category.getAttribute("name"),
                                     news)
                            )


        return result



    @staticmethod
    def save_all(xml_path: str, categories_news: [NewsCategory] = []) -> None:
        validate_xml(xml_path, AgencyXML.XSD_PATH)
        document: Document = Document()
        agency: Element = document.createElement('Agency')
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








