#!/usr/bin/python3
"""Module for XML serialization"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serializes a dictionary to an XML file"""
    root = ET.Element("root")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = value

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Deserializes an XML file to a dictionary"""
    tree = ET.parse(filename)
    root = tree.getroot()
    data = {}
    for child in root:
        data[child.tag] = child.text

    return data
