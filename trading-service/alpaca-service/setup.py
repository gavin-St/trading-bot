from setuptools import setup, find_packages

setup(
    name="alpaca_service",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "alpaca-trade-api>=1.4.0",
    ],
)
