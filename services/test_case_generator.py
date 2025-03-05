from utils.llm_client import LLMClient

class TestCaseGenerator:
    def __init__(self):
        self.llm = LLMClient()

    def generate_test_cases(self, business_justification: str) -> str:
        prompt = f'''
        Given the business justification: "{business_justification}", generate comprehensive test cases covering:
        - Positive cases
        - Negative cases
        - Edge cases

        Provide test cases in JSON format including API endpoint, request body, and expected response.
        '''
        return self.llm.generate_response(prompt)
