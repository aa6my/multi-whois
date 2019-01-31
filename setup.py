from distutils.core import setup

version = '1.1.0'

long_description = '''\
Whois client capable of finding multiple available domains via a file or list type.
It's a good way to search for domains that are available to buy.'''

setup(name='mwhois-client',
      version=version,
      long_description=long_description,
      author='jrosco',
      author_email='joel_c@zoho.com',
      license='GPL',
      package_dir={'mwhois-client': 'src'},
      packages=['mwhois-client'])
