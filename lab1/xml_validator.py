from lxml import etree
from lxml.etree import XMLSyntaxError

def validate_by_xsd(xml_path: str, xsd_path: str)->bool:
    xml_validator = etree.XMLSchema(file=xsd_path)
    try:
        xml_file = etree.parse(xml_path)
        is_valid = xml_validator.validate(xml_file)
    except XMLSyntaxError as e:
        print(e)
        return False
    if not is_valid:
        print(xml_validator.error_log)
    return is_valid



def validate_by_dtd(xml_path: str) -> bool:
    parser = etree.XMLParser(dtd_validation=True)
    try:
        etree.parse(xml_path, parser)
    except XMLSyntaxError as e:
        print(e)
        return False
    return True


