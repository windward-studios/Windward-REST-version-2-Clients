import setuptools

setuptools.setup(
    name= 'windwardrestclient-zaido',
    version = '0.0.6',
    description = 'Python client for the Windward RESTful Engine',
    long_description = '',
    url = 'http://www.windward.net/products/restful/',
    author = 'Windward Studios',
    author_email ='support@windward.net',
    install_requires = ['requests'],
    packages = setuptools.find_packages(where='src'),
    package_dir = {'': 'src'}
)
