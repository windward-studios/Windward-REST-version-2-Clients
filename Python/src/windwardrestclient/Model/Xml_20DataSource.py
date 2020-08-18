from windwardrestclient.Model import Datasource


class Xml_20DataSource(Datasource.Datasource):
    def __init__(self, name, connectionString=None, schemaConnectionString=None):
        super().__init__(name=name, connectionString=connectionString, schemaConnectionString=schemaConnectionString, type= Datasource.datasouceTypeEnum.XML2)