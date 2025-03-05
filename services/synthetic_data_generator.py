import random
from config import TABLE_SCHEMA

class SyntheticDataGenerator:
    def __init__(self):
        pass

    def get_attributes(self, test_cases: str):
        attributes = set()
        for case in eval(test_cases):  
            if "request_body" in case:
                attributes.update(case["request_body"].keys())
        return attributes

    def generate_synthetic_data(self, attributes: set):
        synthetic_data = {}
        for table, columns in TABLE_SCHEMA.items():
            for attr in attributes:
                if attr in columns:
                    synthetic_data[attr] = self.generate_fake_value(attr)
        return synthetic_data

    def generate_fake_value(self, attr: str):
        fake_data = {
            "transaction_id": lambda: str(random.randint(100000, 999999)),
            "amount": lambda: round(random.uniform(10.0, 1000.0), 2),
            "timestamp": lambda: "2025-03-06T10:00:00Z",
            "merchant_id": lambda: str(random.randint(100, 999)),
            "card_number": lambda: "4000123456789010",
            "cvv": lambda: str(random.randint(100, 999)),
            "expiry_date": lambda: "12/27",
            "account_holder": lambda: "John Doe"
        }
        return fake_data.get(attr, lambda: "N/A")()
