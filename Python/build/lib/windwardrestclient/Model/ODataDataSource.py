from windwardrestclient.Model import Datasource


class ODataDataSource(Datasource.Datasource):
    def __init__(self, name, connectionString=None, data=None):
        super().__init__(name=name, connectionString=connectionString, data=data, type= Datasource.datasouceTypeEnum.ODATA)