from windwardrestclient.Model import Datasource


class SalesforceDataSource(Datasource.Datasource):
    def __init__(self, name=None, connectionString=None, data=None):
        super().__init__(name=name, connectionString=connectionString, data=data, type= Datasource.datasouceTypeEnum.SALESFORCE)