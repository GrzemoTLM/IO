from lxml import etree

def validate_xml(xml_path, xsd_path):
    # Parsowanie plików XML i XSD
    xml_doc = etree.parse(xml_path)
    xsd_doc = etree.parse(xsd_path)
    xml_schema = etree.XMLSchema(xsd_doc)
    
    # Walidacja XML względem XSD
    result = xml_schema.validate(xml_doc)
    return result

if __name__ == "__main__":
    xml_file = 'przychodnia.xml'
    xsd_file = 'przychodnia.xsd'
    is_valid = validate_xml(xml_file, xsd_file)
    
    if is_valid:
        print("Plik XML jest poprawny względem XSD.")
    else:
        print("Plik XML nie jest poprawny względem XSD.")
