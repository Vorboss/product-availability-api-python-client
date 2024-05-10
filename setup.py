# coding: utf-8

"""
    Vorboss Product Availability API

    This API is provided by Vorboss to allow customers to check which products are available at a given postcode.  # noqa: E501

    OpenAPI spec version: 0.2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "ProductAvailability"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Vorboss Product Availability API",
    author_email="",
    url="",
    keywords=["Swagger", "Vorboss Product Availability API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    This API is provided by Vorboss to allow customers to check which products are available at a given postcode.  # noqa: E501
    """
)
