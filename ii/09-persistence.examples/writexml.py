from xml.etree.ElementTree import Element, SubElement, tostring

html = Element("html")
head = SubElement(html, "head")
body = SubElement(html, "body")
paragraph = SubElement(body, "p")
paragraph.text = "Monthy Python's Flying Circus"

print(tostring(html, method="html").decode('utf-8'))
