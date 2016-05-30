import os

from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))

try:
    with open(os.path.join(here, 'README.txt')) as f:
        README = f.read()
    with open(os.path.join(here, 'CHANGES.txt')) as f:
        CHANGES = f.read()
except:
    README = ''
    CHANGES = ''

requires = [
    'diff-match-patch',
    'Genshi',
    'html5lib',
    'html2text',
    'beautifulsoup4'
    ]


setupkw = dict(
    name='html_diff_wrapper',
    version='0.1',
    description='A html diff wrapper',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        ],
    keywords='web htmldiff diff',
    author="Amen SOUISSI",
    author_email="amensouissi@ecreall.com",
    url="",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    test_suite="html_diff_wrapper"
    )

# to update catalogs, use babel and lingua !
try:
    import babel
    babel = babel # PyFlakes
    # if babel is installed, advertise message extractors (if we pass
    # this to setup() unconditionally, and babel isn't installed,
    # distutils warns pointlessly)
    setupkw['message_extractors'] = { "html_diff_wrapper": [
        ("**.py",     "lingua_python", None ),
        ("**.pt", "lingua_xml", None ),
        ]}
except ImportError:
    pass

setup(**setupkw)
