from xmlvalidator import validate_xml

class AgencyXML:

    xsd_path: str = "resources/agency.xsd"

    @staticmethod
    def save_all(xml_path) -> None:
        is_valid = validate_xml(xml_path, AgencyXML.xsd_path)