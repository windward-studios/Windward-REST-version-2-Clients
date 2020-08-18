import six


class TagTree(object):

    attributeMap = {
        'guid': 'Guid',
        'tag': 'Tag',
        'xml': 'Xml'
    }

    def __init__(self, guid=None, tag=None, xml=None):

        self._guid = None
        self._tag = None
        self._xml = None

        if guid is not None:
            self.guid = guid
        if tag is not None:
            self.tag = tag
        if xml is not None:
            self.xml = xml

    @property
    def guid(self):
        """Gets the guid of this TagTree.

        The guid of this async job.

        :return: The guid of this TagTree.
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this TagTree.

        The guid of this async job.

        :param guid: The guid of this TagTree.
        :type: str
        """

        self._guid = guid

    @property
    def tag(self):
        """Gets the tag of this TagTree.

        Anything you want. This is set in the Template and passed in to the repository & job handlers and is set in the final generated TagTree object. The RESTful engine ignores this setting, it is for the caller's use.

        :return: The tag of this TagTree.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this TagTree.

        Anything you want. This is set in the Template and passed in to the repository & job handlers and is set in the final generated TagTree object. The RESTful engine ignores this setting, it is for the caller's use.

        :param tag: The tag of this TagTree.
        :type: str
        """

        self._tag = tag

    @property
    def xml(self):
        """Gets the xml of this TagTree.

        The tag tree which is an XML document.

        :return: The xml of this TagTree.
        :rtype: str
        """
        return self._xml

    @xml.setter
    def xml(self, xml):
        """Sets the xml of this TagTree.

        The tag tree which is an XML document.

        :param xml: The xml of this TagTree.
        :type: str
        """

        self._xml = xml

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
