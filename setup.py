from setuptools import setup, find_packages

setup(
    name='lopc',
    version='0.1',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    url='https://github.com/lukauskas/python-lopc',
    license='MIT',
    author='Saulius Lukauskas',
    author_email='saulius.lukauskas13@imperial.ac.uk',
    description='',
    install_requires=['numpy'],
    extras_require={'test': ['nose', 'scipy']},
)
