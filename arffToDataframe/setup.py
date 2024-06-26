from setuptools import setup, find_packages

setup(
    name='arffToDataframe',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'liac-arff>=2.5.0',
        'pandas>=2.2.1'
    ],
    entry_points={
        'console_scripts': [
            'arffToDataframe=main:convertToDataFrame',
        ],
    },
    author='Ammar Haider',
    author_email='ammarhaider1629@gmail.com',
    description='A package to convert ARFF files to pandas DataFrames.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ammarhaider16/arff-to-dataframe'
)
