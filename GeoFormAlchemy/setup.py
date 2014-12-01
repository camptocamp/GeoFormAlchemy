from setuptools import setup, find_packages

setup(
    name='GeoFormAlchemy2',
    version='2.0',
    author='Camptocamp',
    url='http://github.com/camptocamp/GeoFormAlchemy',
    description="GeoFormAlchemy - a extension for FormAlchemy that adds support for spatial databases",
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Pylons',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Text Processing :: Markup :: HTML'
    ],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='gis sqlalchemy geoalchemy formalchemy',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'FormAlchemy>=1.3.0',
        'GeoAlchemy2'
    ],
    entry_points={
        'paste.paster_create_template': [
            "geo_fa = geoformalchemy.pylons.paster_template:PylonsTemplate"
        ]
    }
)
