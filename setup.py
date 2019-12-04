from setuptools import setup, find_packages
from glob import glob
from os.path import basename
from os.path import splitext

setup(
    name='pygeng',
    version='0.1.0',
    description='python based generic gui generator',
    author='James Grider, JJ Quisenberry',
    author_email='grider.james@gmail.com johnny.e.quisenberry@gmail.com',
    packages=find_packages('pygeng'),
    package_dir={'': 'pygeng'},
    py_modules=[splitext(basename(path))[0] for path in glob('pygeng/*.py')],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
    ],
    entry_points='''
        [console_scripts]
        pygeng=pygeng:main
    ''',
)
