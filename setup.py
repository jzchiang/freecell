from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='freecell',
    version='0.1.0',
    description='Freecell clone',
    long_description=readme,
    author='Jonathan Chiang',
    author_email='jchiang@caltech.edu',
    url='https://github.com/jzchiang/freecell',
    license=license,
    packages=find_packages(exclude=('tests'))
)