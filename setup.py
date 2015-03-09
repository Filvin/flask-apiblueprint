"""
Flask-APIBlueprint
-------------

Route inheritance for Flask Blueprints.

"""
from setuptools import setup

try:
    with open('LONG_DESCRIPTION.rst') as f:
        long_description = f.read()
except:
    long_description = 'Route inheritance for Flask Blueprints'


setup(
    name='Flask-APIBlueprint',
    version='1.0',
    url='http://example.com/flask-sqlite3/',
    license='BSD',
    author='Grace Wong',
    author_email='gwongz@gmail.com',
    description='Route inheritance for Flask Blueprints',
    long_description=long_description,
    packages=['flask_apiblueprint'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    test_suite='test_apiblueprint',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    ]
)