# coding: utf-8

"""
    mixedbread-ai

    Discover how to convert text into embeddings with the Embeddings API. Ideal for NLP tasks like text similarity and clustering. Use top open source models or your own fine-tuned models.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from mixedbread_ai.models.error_response import ErrorResponse

class TestErrorResponse(unittest.TestCase):
    """ErrorResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ErrorResponse:
        """Test ErrorResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ErrorResponse`
        """
        model = ErrorResponse()
        if include_optional:
            return ErrorResponse(
                code = 56,
                message = '',
                data = { }
            )
        else:
            return ErrorResponse(
                code = 56,
                message = '',
                data = { },
        )
        """

    def testErrorResponse(self):
        """Test ErrorResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
