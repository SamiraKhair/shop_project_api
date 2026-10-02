from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock']
        read_only_fields = ['id']
        extra_kwargs = {
            'name': {
                'error_messages': {
                    'blank': 'Name cannot be empty.',
                    'required': 'Name is required.',
                },
            },
            'stock': {
                'min_value': 0,
                'error_messages': {
                    'invalid': 'Stock must be a whole number.',
                    'min_value': 'Stock cannot be negative.',
                    'required': 'Stock is required.',
                },
            },
        }

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError('Price must be greater than zero.')
        return value