import setuptools

setuptools.setup(
    name= 'windwardrestapi',
    version = '1.0.1',
    description = 'Python client for the Windward RESTful Engine',
    long_description = '',
    url = 'http://www.windward.net/products/restful/',
    author = 'Windward Studios',
    author_email ='support@windward.net',
    install_requires = ['requests', 'six'],
    packages = setuptools.find_packages(where='src'),
    package_dir = {'': 'src'}
)
