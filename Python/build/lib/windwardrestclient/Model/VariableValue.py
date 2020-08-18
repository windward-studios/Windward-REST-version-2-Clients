import six


class VariableValue(object):

    attributeMap = {
        'label': 'Label',
        'name': 'Name',
        'value': 'Value',
        'valueReference': 'ValueReference'
    }

    def __init__(self, label=None, name=None, value=None, valueReference=None):

        self._label = None
        self._name = None
        self._value = None
        self._valueReference = None

        if label is not None:
            self.label = label
        if name is not None:
            self.name = name
        if value is not None:
            self.value = value
        try:
            if valueReference is not None:
                self.valueReference = valueReference
        except Exception as e:
            print(e)

    @property
    def label(self):
        """Gets the label of this VariableValue.

        The display text for a value.

        :return: The label of this VariableValue.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this VariableValue.

        The display text for a value.

        :param label: The label of this VariableValue.
        :type: str
        """

        self._label = label

    @property
    def name(self):
        """Gets the name of this VariableValue.

        The name of this value.

        :return: The name of this VariableValue.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VariableValue.

        The name of this value.

        :param name: The name of this VariableValue.
        :type: str
        """

        self._name = name

    @property
    def value(self):
        """Gets the value of this VariableValue.


        :return: The value of this VariableValue.
        :rtype: ParamValue
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this VariableValue.


        :param value: The value of this VariableValue.
        :type: ParamValue
        """

        self._value = value

    @property
    def valueReference(self):
        """Gets the value_reference of this VariableValue.

        What the value is returning.

        :return: The value_reference of this VariableValue.
        :rtype: str
        """
        return self._valueReference

    @valueReference.setter
    def valueReference(self, value_reference):
        """Sets the value_reference of this VariableValue.

        What the value is returning.

        :param value_reference: The value_reference of this VariableValue.
        :type: str
        """
        allowed_values = ["literal", "param_value", "select"]
        if value_reference not in allowed_values:
            raise ValueError(
                "Invalid value for `value_reference` ({0}), must be one of {1}"
                    .format(value_reference, allowed_values)
            )

        self._valueReference = value_reference

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
