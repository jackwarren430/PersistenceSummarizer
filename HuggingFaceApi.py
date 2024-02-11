import requests
import re

class HuggingFaceApi:

    tos_summarizer_url = "https://api-inference.huggingface.co/models/ml6team/distilbart-tos-summarizer-tosdr"
    summerizer_url = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    analysis_url = "https://api-inference.huggingface.co/models/atharvamundada99/bert-large-question-answering-finetuned-legal"
    token = "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"
    
    @classmethod
    def makeSummaryApiCall(cls, prompt, max_tokens, min_length, max_length):
        headers = {
            'Authorization': f'Bearer {cls.token}'
        }

        def query(payload):
            response = requests.post(cls.summerizer_url, headers=headers, json=payload)
            return response.json()

        output = query({
            "inputs": prompt,
            "parameters": {"do_sample": False, "max_new_tokens": max_tokens, "min_length": min_length, "max_length": max_length},
            "options": {"wait_for_model": True, "use_gpu": True},
        })
        if isinstance(output, dict):
            print("\n---\nsummary output returned an error!\n---")
            print(output)
            print("---")
            return ""
        else:
            return output[0]["generated_text"]

    @classmethod
    def makeAnalysisApiCall(cls, prompt, max_tokens, min_length, max_length):
        headers = {
            'Authorization': f'Bearer {cls.token}'
        }

        def query(payload):
            response = requests.post(cls.analysis_url, headers=headers, json=payload)
            return response.json()

        output = query({
            "inputs": prompt,
            #"parameters": {"do_sample": True, "max_new_tokens": max_tokens, "min_length": min_length, "max_length": max_length},
            #"parameters": {"max_new_tokens": 50},
            "options": {"wait_for_model": True, "use_gpu": True},
        })

        if 'error' in output:
            print("\n---\nanalysis output returned an error!\n---")
            print(output)
            print("---")
            return ""
        else:
            return output["answer"]

    @classmethod
    def makeTosSummaryApiCall(cls, prompt, max_tokens, min_length, max_length):
        headers = {
            'Authorization': f'Bearer {cls.token}'
        }

        def query(payload):
            response = requests.post(cls.tos_summarizer_url, headers=headers, json=payload)
            return response.json()

        output = query({
            "inputs": prompt,
            "parameters": {"do_sample": False, "max_new_tokens": max_tokens, "min_length": min_length, "max_length": max_length},
            #"parameters": {"max_new_tokens": 50},
            "options": {"wait_for_model": True, "use_gpu": True},
        })
        if isinstance(output, dict):
            print("\n---\ntos summary output returned an error!\n---")
            print(output)
            print("---")
            return ""
        else:
            return output[0]["generated_text"]

    
    @staticmethod
    def split_into_chunks(text, max_words=800):
        words = text.split()
        chunks = []
        current_chunk = []
        for word in words:
            current_chunk.append(word)
            if len(current_chunk) >= max_words:
                chunks.append(' '.join(current_chunk))
                current_chunk = []
        if current_chunk:
            chunks.append(' '.join(current_chunk))
        return chunks

    @staticmethod
    def splitTOS(tos):
        pattern = re.compile(r'(\n|^)(Section \d+|CHAPTER \d+|[IVXLCDM]+\.|\d\d)', re.IGNORECASE)
        matches = pattern.finditer(tos)
        sections = []
        last_pos = 0
        for match in matches:
            start_pos = match.start()
            if start_pos != last_pos:
                sections.append(tos[last_pos:start_pos].strip())
            last_pos = start_pos
        sections.append(tos[last_pos:].strip())
        processed_sections = []
        for section in sections:
            if len(section.split()) <= 800:
                processed_sections.append(section)
            else:
                chunks = HuggingFaceApi.split_into_chunks(section, 800)
                processed_sections.extend(chunks)
        return processed_sections

    @staticmethod
    def processTOS(tos):
        chunks = HuggingFaceApi.splitTOS(tos)[1:]
        summary_total = ""
        analysis_total = []
        for chunk in chunks:
            summary = HuggingFaceApi.makeSummaryApiCall(chunk, 100, 20, 100)
            summary_total += f'{summary}. '
            prompt = {
                "question": "Is this section in my terms of service taking away my rights? Should I be concerned about this section of my terms of service?",
                "context": summary,
            }
            #analysis = HuggingFaceApi.makeAnalysisApiCall(prompt, 20, 40)
            #analysis_total.append(analysis)
            print(f'\n----\n{summary}\n')
        summary = HuggingFaceApi.makeSummaryApiCall(summary_total, 250, 50, 300)
        return summary, analysis_total

    def testSection(section):
        summary = HuggingFaceApi.makeSummaryApiCall(section, 100, 20, 100)
        #print(f'\n{summary}\n')
        prompt = {
            "question": "Why should I be concerned about this clause in my Terms of Service?",
            "context": section,
        }
        response = HuggingFaceApi.makeAnalysisApiCall(prompt, 15, 10, 20)
        return response





   



