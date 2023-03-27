import unittest

from __seedwork.domain.validators import (
    ValidatorRules, ValidationException, ValidatorFieldsInterface, DRFValidator
)
from rest_framework import serializers


# pylint: disable=abstract-method
class StubSerializer(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.CharField()


class TestDRFValidatorsIntegration(unittest.TestCase):
    def test_validation_with_error(self):
        validator = DRFValidator()
        serializer = StubSerializer(data={})
        is_valid = validator.validate(serializer)
        self.assertFalse(is_valid)
        self.assertEqual(validator.errors, {
                         'name': ['This field is required.'], 'price': ['This field is required.']})

    def test_validation_without_error(self):
        validator = DRFValidator()
        serializer = StubSerializer(data={'name': 'some value', 'price': 7})
        is_valid = validator.validate(serializer)
        self.assertTrue(is_valid)
        self.assertEqual(validator.validated_data, {'name': 'some value', 'price': '7'})
