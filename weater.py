import xml.dom.minidom
dom = xml.dom.minidom.parse("37.xml");
dom.normalize()

node1 = dom.getElementsByTagName("HEAT")[0]

a = node1.getAttribute("min")
b = node1.getAttribute("max")

if a >= b:
 print a
else:
 print b