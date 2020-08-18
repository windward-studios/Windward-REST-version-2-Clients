from windwardrestclient.Model import VersionInfo


class testVersion:
    baseUri = "http://localhost:64228/"

    client = WindwardClient.WindwardClient(baseUri)
    versionInfo = client.getVersion()
    assert(isinstance(versionInfo, VersionInfo.VersionInfo))
    assert len(versionInfo._engineVersion) > 0
    assert len(versionInfo._serviceVersion) > 0
    assert len(versionInfo._serverApiVersion) > 0

if __name__ == '__main__':
   t = testVersion