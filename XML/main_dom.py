# -*- coding:utf-8 -*-

# xml文件的读取与生成

import xml.dom.minidom


def get_continent(datasource):

    with xml.dom.minidom.parse(datasource) as dom:
        root = dom.documentElement

        cd = {}
        pd = {}

        for child in root.childNodes:
            if child.nodeType == child.ELEMENT_NODE:
                continent = child.getElementsByTagName('Continent')[0].firstChild.data
                population = int(child.getElementsByTagName('Population')[0].firstChild.data)
                if continent in cd.keys():
                    cd[continent] += 1
                    pd[continent] += population
                else:
                    cd[continent] = 1
                    pd[continent] = population

    return cd


def get_population(datasource):

    with xml.dom.minidom.parse(datasource) as dom:
        root = dom.documentElement

        cd = {}
        pd = {}

        for child in root.childNodes:
            if child.nodeType == child.ELEMENT_NODE:
                continent = child.getElementsByTagName('Continent')[0].firstChild.data
                population = int(child.getElementsByTagName('Population')[0].firstChild.data)
                if continent in cd.keys():
                    cd[continent] += 1
                    pd[continent] += population
                else:
                    cd[continent] = 1
                    pd[continent] = population

    return pd

print(get_continent('country.xml'), get_population('country.xml'))
