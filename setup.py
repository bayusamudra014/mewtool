from setuptools import setup, find_packages

setup(
    name='mewtool',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'sympy==1.12',
        'pycryptodome==3.20.0',
        'numpy==1.24.4',
        'scipy==1.12.0'
    ],
    tests_require=[
        'pytest',
    ],
    setup_requires=['pytest-runner'],
)