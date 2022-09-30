from setuptools import setup, find_packages

setup(
    name='ilikeapples',
    version="1.0.0",
    author_email='',
    packages=find_packages(),
    install_requires=[
        'deprecated==1.2.13',
        'hdfs==2.6.0',
        'ibis-framework[impala]==2.0.0',
        'numpy==1.21.4',
        'pandas==1.3.4'
    ]
)
