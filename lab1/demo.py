from AgencyManagement import AgencyManagement as AM
from xml_validator import validate_by_xsd
from xml_validator import validate_by_dtd
import os


def demo_test_validators():
    print(" test validate xml with xsd:\n")
    validate_by_xsd("resources/invalid_xml/invalid1.xml", "resources/agency.xsd")
    validate_by_xsd("resources/invalid_xml/invalid2.xml", "resources/agency.xsd")
    print("\n test validate xml with dtd:\n")
    validate_by_dtd("resources/invalid_xml/invalid_1.xml")
    validate_by_dtd("resources/invalid_xml/invalid_2.xml")

    print("test was is successful")


def demo_work_with_xml():
    agency = AM("resources/agency.xml")

    # load from xml
    print("\n\n\n**************** initial data  *******************\n\n\n")
    agency.print_all_categories()

    # test adding
    print("\n\n\n****************  adding news and categories   *******************\n\n\n")
    agency.add_news(1, 1, "fight klychko-joshua", 5,  "ivan stoltenberg")
    agency.add_news(1, 2, "tennis tournament final", 67, "tom garfild")
    agency.add_news(1, 3, "uefa 2026", 14, "ivan stoltenberg")
    agency.add_news(2, 4, "impichment", 4, "ronald rixkon" )
    agency.add_news(2, 5, "default in venesuella", 23, "anna kovalenko")
    agency.add_category(3, "financial")
    agency.add_news(3, 6, "tesla motors", 22, "anna kovalenko")
    agency.print_all_categories()
    os.system('PAUSE')

    # test invalid adding
    print("\n\n\n**************** invaild adding news and categories   *******************\n\n\n")
    agency.add_news(50, 7, "fight", 6, "john johnson")
    print()
    agency.add_news(1, 2, "final ufc", 6, "john johnson")
    print()
    agency.add_category(1, "cooking")
    print()
    agency.print_all_categories()
    os.system('PAUSE')

    # test search
    print("\n\n\n******************** search  *********************\n\n\n")
    print(" search category by id \n")
    agency.print_category(2)
    print("\n search all news by category id \n")
    agency.print_news_by_category(1)
    print("\n search news by id \n")
    agency.print_news_by_id(6)
    print("\n search news by range (num pages) \n")
    agency.print_news_by_range(3,23)

    # data change testing
    print("\n\n\n****************  change data   *******************\n\n\n")
    agency.upgrade_news(6, "tesla motors", 26, "kateryna kovalenko")
    agency.upgrade_category(1, "cooking")
    print()
    agency.print_all_categories()
    print()
    os.system('PAUSE')

    # removal test
    print("\n\n\n****************  removal  *******************\n\n\n")
    agency.remove_category(3)
    agency.remove_news(3)
    print()
    agency.print_all_categories()
    os.system('PAUSE')

    # test cleaning
    print("\n\n\n****************  cleaning   *******************\n\n\n")
    agency.clear()
    agency.print_all_categories()
    os.system('PAUSE')


    # end testing
    print("\n\n\n**************** final   *******************\n\n\n")
    agency.add_category(1, "sport")
    agency.add_news(1, 11, "karate", 5, "ivan stoltenberg")
    agency.add_category(2, "politic")
    agency.add_news(2, 12, "kanzas meeting", 90, "andrew")
    agency.print_all_categories()

