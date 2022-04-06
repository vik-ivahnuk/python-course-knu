from news.News import News
from news.NewsCategory import NewsCategory
from AgencyXML import AgencyXML as AXML

cat1 = NewsCategory(1,"sport",[
    News(3,"financial",7, "tom jonhson"),
    News(4,"fin", 50, "jack mickelson")
])
#print(cat1)

#cat2 = AXML.get_all_categories_news("resources/agency.xml")
#print(cat2)
AXML.save_all("resources/agency.xml",[cat1])
