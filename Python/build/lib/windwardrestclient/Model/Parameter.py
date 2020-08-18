import six


class Parameter(object):

    attributeMap = {
        'name': 'Name',
        'wrappedValue': 'WrappedValue'
    }

    def __init__(self, name=None, wrappedValue=None):

        self._name = None
        self._wrappedValue = None

        if name is not None:
            self.name = name
        if wrappedValue is not None:
            self.wrappedValue = wrappedValue

    @property
    def name(self):
        """Gets the name of this Parameter.

        Name of the parameter (the var in ${var}).

        :return: The name of this Parameter.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Parameter.

        Name of the parameter (the var in ${var}).

        :param name: The name of this Parameter.
        :type: str
        """

        self._name = name

    @property
    def wrappedValue(self):
        """Gets the wrapped_value of this Parameter.


        :return: The wrapped_value of this Parameter.
        :rtype: ParamValue
        """
        return self._wrappedValue

    @wrappedValue.setter
    def wrappedValue(self, wrapped_value):
        """Sets the wrapped_value of this Parameter.


        :param wrapped_value: The wrapped_value of this Parameter.
        :type: ParamValue
        """

        self._wrappedValue = wrapped_value

    #Takes in the object and returns a serialized dictionary for requests.
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
