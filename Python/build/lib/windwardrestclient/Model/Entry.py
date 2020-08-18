import six


class Entry(object):

    attributeMap = {
        'key': 'Key',
        'value': 'Value'
    }

    def __init__(self, key=None, value=None):

        self._key = None
        self._value = None
        self.discriminator = None
        if key is not None:
            self.key = key
        if value is not None:
            self.value = value

    @property
    def key(self):
        """Gets the key of this Entry.

        The key (name) of the property.

        :return: The key of this Entry.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this Entry.

        The key (name) of the property.

        :param key: The key of this Entry.
        :type: str
        """

        self._key = key

    @property
    def value(self):
        """Gets the value of this Entry.

        The value of the property.

        :return: The value of this Entry.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Entry.

        The value of the property.

        :param value: The value of this Entry.
        :type: str
        """

        self._value = value

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
