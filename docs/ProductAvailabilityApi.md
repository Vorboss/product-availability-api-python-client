# ProductAvailability.ProductAvailabilityApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**confirm_postcode**](ProductAvailabilityApi.md#confirm_postcode) | **GET** /product-availability/postcode/{postcode} | Check a postcode

# **confirm_postcode**
> Postcode confirm_postcode(postcode)

Check a postcode

Check which products are available at the given postcode.

### Example
```python
from __future__ import print_function
import time
import ProductAvailability
from ProductAvailability.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ProductAvailability.ProductAvailabilityApi(ProductAvailability.ApiClient(configuration))
postcode = 'postcode_example' # str | UK Postcode to check availability for.

try:
    # Check a postcode
    api_response = api_instance.confirm_postcode(postcode)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductAvailabilityApi->confirm_postcode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **postcode** | **str**| UK Postcode to check availability for. | 

### Return type

[**Postcode**](Postcode.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

