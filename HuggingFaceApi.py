import requests

class HuggingFaceApi:

    summerizer_url = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    legal_url = "https://api-inference.huggingface.co/models/atharvamundada99/bert-large-question-answering-finetuned-legal"
    token = "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"
    
    @classmethod
    def makeSummarizerApiCall(cls, prompt, min_length, max_length):
        headers = {
            'Authorization': f'Bearer {cls.token}'
        }

        def query(payload):
            response = requests.post(cls.summerizer_url, headers=headers, json=payload)
            return response.json()

        output = query({
            "inputs": prompt,
            "parameters": {"do_sample": True, "min_length": min_length, "max_length": max_length},
            #"parameters": {"max_new_tokens": 50},
            "options": {"wait_for_model": True, "use_gpu": True},
        })

        #return output["generated_text"]
        return output

    @classmethod
    def makeLegalApiCall(cls, prompt, min_length, max_length):
        headers = {
            'Authorization': f'Bearer {cls.token}'
        }

        def query(payload):
            response = requests.post(cls.legal_url, headers=headers, json=payload)
            return response.json()

        output = query({
            "inputs": prompt,
            "parameters": {"do_sample": True, "min_length": min_length, "max_length": max_length},
            #"parameters": {"max_new_tokens": 50},
            "options": {"wait_for_model": True, "use_gpu": True},
        })

        #return output["generated_text"]
        return output

    @staticmethod
    def summarizeTOS(tos):
        prompt = tos
        tos_summarized = HuggingFaceApi.makeSummarizerApiCall(prompt, 30, 50)
        return tos_summarized

    @staticmethod
    def expandOnSection(section):
        prompt = section
        section_expanded = HuggingFaceApi.makeLegalApiCall(prompt, 30, 50)
        return section_expanded
