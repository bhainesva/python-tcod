#!/usr/bin/env python2

from setuptools import setup

exec(open('tdl/version.py').read()) # get __version__

setup(
    name='tdl',
    version=__version__,
    author='Kyle Stewart',
    author_email='4B796C65+tdl@gmail.com',
    description='Pythonic cffi port of libtcod.',
    long_description='\n'.join([open('README.rst', 'r').read(),
                                open('CHANGELOG.rst', 'r').read()]),
    url='https://github.com/HexDecimal/python-tdl',
    download_url='https://pypi.python.org/pypi/tdl',
    packages=['tdl'],
    package_data={'tdl': ['*.txt', '*.rst', '*.bmp', '*.png']},
    install_requires=["libtcod-cffi>=2.3.0,<3"],
    classifiers=['Development Status :: 5 - Production/Stable',
               'Environment :: Win32 (MS Windows)',
               'Environment :: MacOS X',
               'Environment :: X11 Applications',
               'Intended Audience :: Developers',
               'License :: OSI Approved :: BSD License',
               'Natural Language :: English',
               'Operating System :: POSIX',
               'Operating System :: MacOS',
               'Operating System :: Microsoft :: Windows',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Programming Language :: Python :: 3.3',
               'Programming Language :: Python :: 3.4',
               'Programming Language :: Python :: 3.5',
               'Programming Language :: Python :: Implementation :: CPython',
               'Programming Language :: Python :: Implementation :: PyPy',
               'Topic :: Games/Entertainment',
               'Topic :: Multimedia :: Graphics',
               'Topic :: Software Development :: Libraries :: Python Modules',
               ],
    keywords = 'rogue-like rogue-likes text cffi ASCII ANSI Unicode libtcod fov',
    platforms = ['Windows', 'Mac OS X', 'Linux'],
    license = 'Simplified BSD License',
    tests_require = ['nose2', 'cov-core'],
    test_suite='nose2.collector.collector',
    )
