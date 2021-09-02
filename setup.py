from setuptools import setup

setup(
    name='even_odd',
    version='1.0',
    description='Software Engineering Homework 2b',
    author='Neha Agarwal',
    author_email='nehaagarwal121@gmail.com',     
    url="https://github.com/Software-Engineering-Group-15-Fall-2021/HW-2b",
     long_description="""\
       It computes whether a number is odd or even.
      """,
    license="MIT",
    classifiers=[
          "License :: OSI Approved :: MIT",
          "Programming Language :: Python",       
          "Intended Audience :: Developers",
          "Topic :: Programming example",
      ],      
      install_requires=['numpy','matplotlib','pandas'],
      )
