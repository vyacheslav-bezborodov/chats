import os

from setuptools import (
    find_packages,
    setup,
)

setup(
    name='chats',
    version='0.0.1',
    author='Vyacheslav Bezborodov',
    author_email='vyacheslav.bezborodov@gmail.com',
    description='chats',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    entry_points={
        'console_scripts': [
            'chats=chats.cli:cli',
        ],
    },
    packages=find_packages('src'),
    package_dir={'': 'src'},
)
