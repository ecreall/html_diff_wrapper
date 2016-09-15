import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

requires = [
    'diff-match-patch',
    'Genshi',
    'html5lib',
    'html2text',
    'beautifulsoup4'
    ]


setup(
    name='html_diff_wrapper',
    version='0.1',
    description='A html diff wrapper',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.4",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        ],
    author='Amen Souissi',
    author_email="amensouissi@ecreall.com",
    url='https://github.com/ecreall/html_diff_wrapper/',
    keywords='web htmldiff diff',
    license="AGPLv3+",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    test_suite="html_diff_wrapper"
    )

