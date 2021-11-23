from distutils.core import setup

CONFIG = {
    'name'             : 'lsystems',
    'description'      : 'Implementation of L-Systems',
    'version'          : '0.1.1',

    'author'           : 'Krzysztof Voss',
    'author_email'     : 'k.voss@usask.ca',

    'license'          : 'BSD',
    'platforms'        : ['POSIX',],
    'keywords'         : 'LSystem, turtle, fractals, rewrite',
    'py_modules'       : ['lsystem'],
    'url'              : 'https://github.com/kvoss/lsystem',
    'download_url'     : 'https://github.com/kvoss/lsystem',
    'classifiers'      : [
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    }


setup(**CONFIG)

