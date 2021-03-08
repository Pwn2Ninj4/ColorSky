import os
import re
import codecs

from setuptools import find_packages, setup


def abs_path(*relative_path_parts):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)),
                        *relative_path_parts)


name = 'ColorSky'

with codecs.open(abs_path(name, '__init__.py'), 'r', 'utf-8') as fp:
    try:
        version = re.findall(r"^__version__ = '([^']+)'.*?$",
                             fp.read(), re.M)[0]
    except IndexError:
        raise RuntimeError('Unable to determine version.')

setup(
    name=name,
    version=version,
    url='https://github.com/Pwn2Ninja/ColorSky',
    download_url='https://github.com/Pwn2Ninja/ColorSky/tarball/master',
    author='Pwn2Ninja',
    author_email='danex251@gmail.com',
    description='Imprime cadenas coloridas en tu terminal!',
    packages=find_packages(),
    py_modules=['ColorSky'],
    data_files=[('', ['LICENSE'])],
    include_package_data=True,
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Intended Audience :: Developers',
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
        'Environment :: Console',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ])
