from setuptools import setup

setup(
    name=odd-even',
    version='0.1',
    description='Program to find if a number is odd or even',
    author='Group-15',
    author_email='nehaagarwal121@gmail.com',
    url='http://www-cse.ucsd.edu/~bmcfee/code/spatialtree/',
    packages=['numpy', 'matplotlib','pandas'],
      long_description="""\
        Module for building spatial spill trees.
      """,
      classifiers=[
          "License :: MIT",
          "Programming Language :: Python",
          "Development Status :: 3 - Alpha",
          "Intended Audience :: Developers",
          "Topic :: Programming example",
      ],
      license='MIT',
      install_requires=[
        'numpy',
        'matplotlib',
'pandas'
      ],
      )
