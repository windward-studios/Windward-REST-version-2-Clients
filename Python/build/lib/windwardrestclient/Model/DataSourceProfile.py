import six

from windwardrestclient.Model import DataSet


class DataSourceProfile(object):

    attributeMap = {
        'name': 'Name',
        'rootPath': 'RootPath',
        'vendorType': 'VendorType',
        'properties': 'Properties',
        'datasets': 'Datasets'
    }

    def __init__(self, name=None, rootPath=None, vendorType=None, properties=None, datasets=None):

        self._name = None
        self._rootPath = None
        self._vendorType = None
        self._properties = None
        self._datasets = []

        if name is not None:
            self.name = name
        if rootPath is not None:
            self.rootPath = rootPath
        if vendorType is not None:
            self.vendorType = vendorType
        if properties is not None:
            self.properties = properties
        if datasets is not None:
            self.datasets = datasets

    @property
    def name(self):
        """Gets the name of this DataSourceProfile.

        The name used to reference this datasource.

        :return: The name of this DataSourceProfile.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DataSourceProfile.

        The name used to reference this datasource.

        :param name: The name of this DataSourceProfile.
        :type: str
        """

        self._name = name

    @property
    def rootPath(self):
        """Gets the root_path of this DataSourceProfile.

        The root path set for any relative files accessed by this datasource.

        :return: The root_path of this DataSourceProfile.
        :rtype: str
        """
        return self._rootPath

    @rootPath.setter
    def rootPath(self, root_path):
        """Sets the root_path of this DataSourceProfile.

        The root path set for any relative files accessed by this datasource.

        :param root_path: The root_path of this DataSourceProfile.
        :type: str
        """

        self._rootPath = root_path

    @property
    def vendorType(self):
        """Gets the vendor_type of this DataSourceProfile.

        The datasource vendor type.

        :return: The vendor_type of this DataSourceProfile.
        :rtype: str
        """
        return self._vendorType

    @vendorType.setter
    def vendorType(self, vendor_type):
        """Sets the vendor_type of this DataSourceProfile.

        The datasource vendor type.

        :param vendor_type: The vendor_type of this DataSourceProfile.
        :type: str
        """
        allowed_values = ["json", "odata", "salesforce", "sql", "xml", "xml2"]
        if vendor_type not in allowed_values:
            raise ValueError(
                "Invalid value for `vendor_type` ({0}), must be one of {1}"
                    .format(vendor_type, allowed_values)
            )

        self._vendorType = vendor_type

    @property
    def properties(self):
        """Gets the properties of this DataSourceProfile.

        All information defining this dataset as a collection of properties.

        :return: The properties of this DataSourceProfile.
        :rtype: list[Entry]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this DataSourceProfile.

        All information defining this dataset as a collection of properties.

        :param properties: The properties of this DataSourceProfile.
        :type: list[Entry]
        """

        self._properties = properties

    @property
    def datasets(self):
        """Gets the datasets of this DataSourceProfile.

        The datasets for this datasource.

        :return: The datasets of this DataSourceProfile.
        :rtype: list[DataSetProfile]
        """
        return self._datasets

    @datasets.setter
    def datasets(self, datasets):
        """Sets the datasets of this DataSourceProfile.

        The datasets for this datasource.

        :param datasets: The datasets of this DataSourceProfile.
        :type: list[DataSetProfile]
        """

        if not isinstance(datasets, list):
            self._datasets.append(DataSet.DataSet(name=datasets["Name"], query=datasets["Query"]))
        else:
            for dSet in datasets:
                self._datasets.append(DataSet.DataSet(name=dSet["Name"], query=dSet["Query"]))

    def toDict(self):
        responseDict = {}
        for key, value in six.iteritems(self.attributeMap):
            tempVal = getattr(self, key)
            if tempVal is None:
                pass
            elif isinstance(tempVal, (str, int, dict)):
                responseDict.update({value: tempVal})
            elif isinstance(tempVal, list):
                responseDict.update({value: []})
                for item in tempVal:
                    if isinstance(item, (str, int, dict)):
                        responseDict.update({value: tempVal})
                    else:
                        responseDict[value].append(item.toDict())
            else:
                responseDict.update({value: tempVal.toDict()})
        return responseDict
