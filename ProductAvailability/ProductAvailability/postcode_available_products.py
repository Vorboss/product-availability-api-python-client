# coding: utf-8

"""
    Vorboss Product Availability API

    This API is provided by Vorboss to allow customers to check which products are available at a given postcode.  # noqa: E501

    OpenAPI spec version: 0.2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PostcodeAvailableProducts(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'price': 'float',
        'lead_time_days': 'int',
        'currency': 'str',
        'bandwidth_provisioned': 'int',
        'bandwidth_capactity': 'int',
        'term': 'int'
    }

    attribute_map = {
        'name': 'name',
        'price': 'price',
        'lead_time_days': 'leadTimeDays',
        'currency': 'currency',
        'bandwidth_provisioned': 'bandwidthProvisioned',
        'bandwidth_capactity': 'bandwidthCapactity',
        'term': 'term'
    }

    def __init__(self, name=None, price=None, lead_time_days=None, currency=None, bandwidth_provisioned=None, bandwidth_capactity=None, term=None):  # noqa: E501
        """PostcodeAvailableProducts - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._price = None
        self._lead_time_days = None
        self._currency = None
        self._bandwidth_provisioned = None
        self._bandwidth_capactity = None
        self._term = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if price is not None:
            self.price = price
        if lead_time_days is not None:
            self.lead_time_days = lead_time_days
        if currency is not None:
            self.currency = currency
        if bandwidth_provisioned is not None:
            self.bandwidth_provisioned = bandwidth_provisioned
        if bandwidth_capactity is not None:
            self.bandwidth_capactity = bandwidth_capactity
        if term is not None:
            self.term = term

    @property
    def name(self):
        """Gets the name of this PostcodeAvailableProducts.  # noqa: E501


        :return: The name of this PostcodeAvailableProducts.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PostcodeAvailableProducts.


        :param name: The name of this PostcodeAvailableProducts.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def price(self):
        """Gets the price of this PostcodeAvailableProducts.  # noqa: E501


        :return: The price of this PostcodeAvailableProducts.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this PostcodeAvailableProducts.


        :param price: The price of this PostcodeAvailableProducts.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def lead_time_days(self):
        """Gets the lead_time_days of this PostcodeAvailableProducts.  # noqa: E501


        :return: The lead_time_days of this PostcodeAvailableProducts.  # noqa: E501
        :rtype: int
        """
        return self._lead_time_days

    @lead_time_days.setter
    def lead_time_days(self, lead_time_days):
        """Sets the lead_time_days of this PostcodeAvailableProducts.


        :param lead_time_days: The lead_time_days of this PostcodeAvailableProducts.  # noqa: E501
        :type: int
        """

        self._lead_time_days = lead_time_days

    @property
    def currency(self):
        """Gets the currency of this PostcodeAvailableProducts.  # noqa: E501


        :return: The currency of this PostcodeAvailableProducts.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this PostcodeAvailableProducts.


        :param currency: The currency of this PostcodeAvailableProducts.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def bandwidth_provisioned(self):
        """Gets the bandwidth_provisioned of this PostcodeAvailableProducts.  # noqa: E501


        :return: The bandwidth_provisioned of this PostcodeAvailableProducts.  # noqa: E501
        :rtype: int
        """
        return self._bandwidth_provisioned

    @bandwidth_provisioned.setter
    def bandwidth_provisioned(self, bandwidth_provisioned):
        """Sets the bandwidth_provisioned of this PostcodeAvailableProducts.


        :param bandwidth_provisioned: The bandwidth_provisioned of this PostcodeAvailableProducts.  # noqa: E501
        :type: int
        """

        self._bandwidth_provisioned = bandwidth_provisioned

    @property
    def bandwidth_capactity(self):
        """Gets the bandwidth_capactity of this PostcodeAvailableProducts.  # noqa: E501


        :return: The bandwidth_capactity of this PostcodeAvailableProducts.  # noqa: E501
        :rtype: int
        """
        return self._bandwidth_capactity

    @bandwidth_capactity.setter
    def bandwidth_capactity(self, bandwidth_capactity):
        """Sets the bandwidth_capactity of this PostcodeAvailableProducts.


        :param bandwidth_capactity: The bandwidth_capactity of this PostcodeAvailableProducts.  # noqa: E501
        :type: int
        """

        self._bandwidth_capactity = bandwidth_capactity

    @property
    def term(self):
        """Gets the term of this PostcodeAvailableProducts.  # noqa: E501


        :return: The term of this PostcodeAvailableProducts.  # noqa: E501
        :rtype: int
        """
        return self._term

    @term.setter
    def term(self, term):
        """Sets the term of this PostcodeAvailableProducts.


        :param term: The term of this PostcodeAvailableProducts.  # noqa: E501
        :type: int
        """

        self._term = term

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PostcodeAvailableProducts, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PostcodeAvailableProducts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
