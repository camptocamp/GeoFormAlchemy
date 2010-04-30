from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='GeoFormAlchemy',
      version=version,
      author='Camptocamp',
      description="GeoFormAlchemy",
      long_description="""\
""",
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Pylons',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Text Processing :: Markup :: HTML'
        ], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='gis sqlalchemy geoalchemy formalchemy',
      license='LGPLv3',
      packages=find_packages(exclude=['tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
            'FormAlchemy>=1.3.0,<=1.3.99',
            'GeoAlchemy>=0.2,<=0.2.99'
      ],
      entry_points="""
       [paste.paster_create_template]
        geo_fa = geoformalchemy.pylons.paster_template:PylonsTemplate
      """,
      )
