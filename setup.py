import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='irekua-summaries',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',
    description='Endpoints for Irekua summaries',
    long_description=README,
    url='https://github.com/CONABIO-audio/irekua-rest-api',
    author=(
        'CONABIO, '
        'Gustavo Everardo Robredo Esquivelzeta, '
        'Santiago Martínez Balvanera'),
    author_email='erobredo@conabio.gob.mx, smartinez@conabio.gob.mx',
    install_requires=[
        'irekua_database',
        'irekua_permissions',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
