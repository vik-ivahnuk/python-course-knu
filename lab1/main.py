from news.News import News
from news.NewsCategory import NewsCategory
from AgencyXML import AgencyXML as AXML

cat1 = NewsCategory(1,"sport",[
    News("fff","financial",7, "tom jonhson"),
    News(4,"fin", 50, "jack mickelson")
])
#print(cat1)

#cat2 = AXML.get_news_by_category("resources/agency.xml",4)
#print(cat2)

nw = AXML.get_new_by_id("resources/agency.xml",4)
print(nw)
#print(cat2)
#AXML.save_all("resources/agency.xml",[cat1])
