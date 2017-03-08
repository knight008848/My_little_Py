# -*- coding:utf-8 -*-

# xml文件的读取与生成

import xml.sax


class xmlContentHandler(xml.sax.handler.ContentHandler):

    def __init__(self):
        xml.sax.handler.ContentHandler.__init__(self)

    def startDocument(self):
        print("start handler document")

    def endDocument(self):
        print("end handler document")

    def startElement(self, name, attrs):
        print('sax:start_element: %s' % name)

    def endElement(self, name):
        print('sax:end_element: %s' % name)

    def characters(self, content):
        content = content.strip().replace("\n", "").replace("\r", "")
        if "" != content:
            print('sax:char_data: %s' % content)


class CountrySaxHandler(xml.sax.handler.ContentHandler):

    def __init__(self):
        xml.sax.handler.ContentHandler.__init__(self)
        self.cd = {}
        self.pd = {}
        self.inContinent = False
        self.inPopulation = False

    def startElement(self, name, attrs):
        if name == 'RECORD':
            self.cbuffer = ''
            self.pbuffer = ''

        if name == 'Continent':
            self.inContinent = True

        if name == 'Population':
            self.inPopulation = True

    def endElement(self, name):
        if name == 'Continent':
            self.inContinent = False
            if self.cbuffer in self.cd.keys():
                self.cd[self.cbuffer] += 1
            else:
                self.cd[self.cbuffer] = 1

        if name == 'Population':
            self.inPopulation = False
            if self.cbuffer in self.pd.keys():
                self.pd[self.cbuffer] += self.pbuffer
            else:
                self.pd[self.cbuffer] = self.pbuffer

    def characters(self, content):
        content = content.strip().replace("\n", "").replace("\r", "")
        if self.inContinent:
            self.cbuffer = content
        if self.inPopulation:
            self.pbuffer = int(content)


def get_continent(datasource):
    saxParser = xml.sax.make_parser()
    handler = CountrySaxHandler()
    saxParser.setContentHandler(handler)
    saxParser.parse(datasource)
    return handler.cd


def get_population(datasource):
    saxParser = xml.sax.make_parser()
    handler = CountrySaxHandler()
    saxParser.setContentHandler(handler)
    saxParser.parse(datasource)
    return handler.pd
