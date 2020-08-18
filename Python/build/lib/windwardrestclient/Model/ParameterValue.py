import six


class ParameterValue(object):

    attributeMap = {
        'paramType': 'ParamType',
        'rawValue': 'RawValue'
    }

    def __init__(self, paramType=None, rawValue=None):

        self._paramType = None
        self._rawValue = None

        if paramType is not None:
            self.paramType = paramType
        if rawValue is not None:
            self.rawValue = rawValue

    @property
    def paramType(self):
        """Gets the param_type of this ParamValue.

        What type the raw value needs to be converted back to.

        :return: The param_type of this ParamValue.
        :rtype: str
        """
        return self._paramType

    @paramType.setter
    def paramType(self, param_type):
        """Sets the param_type of this ParamValue.

        What type the raw value needs to be converted back to.

        :param param_type: The param_type of this ParamValue.
        :type: str
        """

        self._paramType = param_type

    @property
    def rawValue(self):
        """Gets the raw_value of this ParamValue.

        The parameter value as a string.

        :return: The raw_value of this ParamValue.
        :rtype: str
        """
        return self._rawValue

    @rawValue.setter
    def rawValue(self, raw_value):
        """Sets the raw_value of this ParamValue.

        The parameter value as a string.

        :param raw_value: The raw_value of this ParamValue.
        :type: str
        """

        self._rawValue = raw_value

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
