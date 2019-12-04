from setuptools import setup, find_packages
from glob import glob
from os.path import basename
from os.path import splitext

setup(
    name='pygeng',
    version='0.0.0',
    description='python based generic gui generator',
    author='James Grider, JJ Quisenberry',
    author_email='grider.james@gmail.com johnny.e.quisenberry@gmail.com',
    packages=find_packages('src/pygeng'),
    package_dir={'': 'src/pygeng'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/pygeng/*.py')],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
    ],
    entry_points='''
        [console_scripts]
        pygeng=pygeng:main
    ''',
)
