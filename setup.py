from setuptools import setup, find_packages

setup(
    name='mewtool',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'sympy~=1.12',
        'pycryptodome~=3.20.0',
        'numpy~=1.26.4',
        'scipy~=1.13.0',
        'cryptography'
    ],
    tests_require=[
        'pytest',
    ],
    setup_requires=['pytest-runner'],
    include_package_data=True,
    author="Bayu Samudra",
    author_email="bayusamudra.55.02.com@gmail.com",
    license="MIT",
    description="A collection of tools for CTF",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)