#!/usr/bin/env python
from setuptools import setup, find_packages


# Parse version number from msaFeature/__init__.py:
with open('msaFeature/__init__.py') as f:
    info = {}
    for line in f:
        if line.startswith('version'):
            exec(line, info)
            break


setup_info = dict(
    name='msaFeature',
    version=info['version'],
    author='Stefan Welcker',
    author_email='stefan@u2d.ai',
    url='https://github.com/swelcker/msaFeature',
    download_url='http://pypi.python.org/pypi/msaFeature',
    project_urls={
        'Documentation': 'http://msaFeature.u2d.ai/',
        'Source': 'https://github.com/swelcker/msaFeature',
        'Tracker': 'https://github.com/swelcker/msaFeature/issues',
    },
    description='msaFeature - Feature switch management with conditions',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: FastAPI',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Database',
        'Topic :: Database :: Front-Ends',
        'Topic :: Documentation',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Server',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    # Package info
    packages=['msaFeature'] + ['msaFeature.' + pkg for pkg in find_packages('msaFeature')],

    # Add _ prefix to the names of temporary build dirs
    options={'build': {'build_base': '_build'}, },
    zip_safe=True,
)

setup(**setup_info)
