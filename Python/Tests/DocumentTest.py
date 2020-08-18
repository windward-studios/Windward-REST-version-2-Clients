from windwardrestclient.Model import Template, Xml_10DataSource
import requests
import time
import base64
import zipfile

class testDocument:
    baseUri = "http://localhost:64228/"
    dataPath = "../files/"
    xmlDocumentPath = dataPath + 'Manufacturing.docx'
    print(xmlDocumentPath)
    xmlDataPath = dataPath + 'Manufacturing.xml'
    print(xmlDataPath)

    def readTemplateAndData(self):
        client = WindwardClient.WindwardClient(self.baseUri)
        xmlDS = Xml_10DataSource.Xml_10DataSource(name="MANF_DATA_2009", data=self.xmlDataPath)
        template = Template.Template(data=self.xmlDocumentPath, outputFormat=Template.outputFormatEnum.DOCX, datasources=[xmlDS])
        template.tag = "Zaid"

        #start request
        document = client.postDocument(template)
        guid = document.guid
        assert(document.tag == "Zaid")

        #wait for request to complete
        while True:
            status = client.getDocumentStatus(guid)
            if(status == requests.codes["found"]):
                break;
            else:
                time.sleep(1)
            assert(status == requests.codes["created"] or status == requests.codes["accepted"])

        #get the document
        response = client.getDocument(guid)
        document = response

        assert(guid == document.guid)
        assert("Zaid" == document.tag)
        assert(4 == document.numberOfPages)

        #check we got a single document
        assert(document.data is not None)
        assert(len(document.data) > 0)
        assert(document.pages is None)

        with open("test.docx", "wb") as fh:
            fh.write(base64.standard_b64decode(document.data))
            assert(zipfile.is_zipfile("test.docx"))
            zip = zipfile.ZipFile("test.docx")
            assert(zip.read('word/document.xml') is not None)

        assert (guid == document.guid)
        assert ("Zaid" == document.tag)
        assert (4 == document.numberOfPages)

        # check we got a single document
        assert (document.data is not None)
        assert (len(document.data) > 0)
        assert (document.pages is None)

        status2 = client.deleteDocument(guid)
        assert(status2 == requests.codes["ok"])

        status2 = client.getDocumentStatus(guid)
        assert(status2 == requests.codes["not_found"])
        print("passed read template and data file")

    def testGetDocumentDocxPassUrl(self):
        client = WindwardClient.WindwardClient(self.baseUri)
        uri = "https://wnd-unittest-resources.s3.amazonaws.com/Test/InvestmentFactSheet.docx"
        template = Template.Template(connectionString=uri, outputFormat=Template.outputFormatEnum.DOCX)
        template.tag = "Zaid"

        # start request
        document = client.postDocument(template)
        guid = document.guid
        assert (document.tag == "Zaid")

        # wait for request to complete
        while True:
            status = client.getDocumentStatus(guid)
            if (status == requests.codes["found"]):
                break;
            else:
                time.sleep(1)
            assert (status == requests.codes["created"] or status == requests.codes["accepted"])

        # get the document
        response = client.getDocument(guid)
        document = response

        assert (guid == document.guid)
        assert ("Zaid" == document.tag)
        assert (3 == document.numberOfPages)

        # check we got a single document
        assert (document.data is not None)
        assert (len(document.data) > 0)
        assert (document.pages is None)

        with open("testUrl.docx", "wb") as fh:
            fh.write(base64.standard_b64decode(document.data))
            assert (zipfile.is_zipfile("test.docx"))
            zip = zipfile.ZipFile("test.docx")
            assert (zip.read('word/document.xml') is not None)

        assert (guid == document.guid)
        assert ("Zaid" == document.tag)
        assert (3 == document.numberOfPages)

        # check we got a single document
        assert (document.data is not None)
        assert (len(document.data) > 0)
        assert (document.pages is None)

        status2 = client.deleteDocument(guid)
        assert (status2 == requests.codes["ok"])

        status2 = client.getDocumentStatus(guid)
        assert (status2 == requests.codes["not_found"])
        print("passed read template and data file from Url")






if __name__ == '__main__':
   t = testDocument
   t.readTemplateAndData(t)
   t.testGetDocumentDocxPassUrl(t)