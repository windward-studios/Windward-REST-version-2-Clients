# This is a sample Python script.
# import src.Api.TestWindwardClient as client
# from Model.Datasource import Datasource

from windwardrestclient.Model import ParameterValue, Template, Parameter, Xml_10DataSource

from windwardrestclient.Api import WindwardClient as client
# import src.Model as modelApi
import time

if __name__ == '__main__':

   testClient = client.WindwardClient("http://localhost:64228/")
   testVersion = testClient.getVersion()
   print(testVersion.toString())

   file = "./files/Manufacturing.docx"
   data = "./files/Manufacturing.xml"
   # cwd = os.getcwd()
   # print("CWD: ", cwd)
   # testSalesForceDS = JsonDataSource.JsonDataSource(name="Homeowners_JSON", connectionString="http://windwardwebsitestorage.blob.core.windows.net/windwardsoftware/SampleData/Homeowners.json")
   testJsonDS = Xml_10DataSource.Xml_10DataSource(name="MANF_DATA_2009", data=data)
   # print(testJsonDS)
   testParam = Parameter.Parameter(name="varName1", wrappedValue=ParameterValue.ParameterValue(paramType="string", rawValue="zaid"))
   # testTemplate = testClient.createTemplate(data=file, outputType=Template.outputFormatEnum.DOCX, datasource=testJsonDS, )
   testTemplate = Template.Template(data=file, outputFormat=Template.outputFormatEnum.DOCX, datasources=testJsonDS, parameters=testParam)
   # print("TEMPLATE\n", json.dumps(testTemplate.toDict(), indent=4))
   # print("Template: ", testTemplate.toDict())

   testDocument = testClient.postDocument(testTemplate)
   print("GUID: ", testDocument.guid)
   while True:
      testDocumentStatus = testClient.getDocumentStatus(testDocument.guid)
      if testDocumentStatus != 302:
         print("Not ready: ", testDocumentStatus)
         time.sleep(1)
      else:
         print("Ready: ", testDocumentStatus)
         break
   testGetDocument = testClient.getDocument(testDocument.guid)
   print("here: ", testGetDocument.guid)

   # testDeleteDocument = testClient.deleteDocument(testGetDocument.guid)
   # print("Delete document Status: ", testDeleteDocument)
   #
   testMetricsPost = testClient.postMetrics(testTemplate)
   print("GUID: ", testMetricsPost.guid)
   while True:
      testMetricsStatus = testClient.getMetricsStatus(testMetricsPost.guid)
      if testMetricsStatus != 302:
         # print("Not ready: ", testMetricsStatus)
         time.sleep(1)
      else:
         # print("Ready: ", testMetricsStatus)
         break
   testGetMetrics = testClient.getMetrics(testMetricsPost.guid)
   print("METRICS\n", testGetMetrics.toDict())
   # testMetricsDelete = testClient.deleteMetrics(testGetMetrics.guid)
   # print("Metrics delete status: ", testMetricsDelete)
   #
   # testPostTagTree = testClient.postTagTree(testTemplate)
   # while True:
   #    testTagTreeStatus = testClient.getTagTreeStatus(testPostTagTree.guid)
   #    if testTagTreeStatus != 200:
   #       print("Not ready: ", testTagTreeStatus)
   #       time.sleep(1)
   #    else:
   #       print("Ready: ", testTagTreeStatus)
   #       break
   #
   # testGetTagTree = testClient.getTagTree(testPostTagTree.guid)
   # print("TAGTREE\n", testGetTagTree.toDict())
   #
   # testTagTreeDelete = testClient.deleteTagTree(testPostTagTree.guid)
   # print("TagTree delete status: ", testTagTreeDelete)
