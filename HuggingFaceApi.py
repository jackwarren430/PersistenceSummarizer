import requests
import re

class HuggingFaceApi:

    tos_summarizer_url = "https://api-inference.huggingface.co/models/ml6team/distilbart-tos-summarizer-tosdr"
    summerizer_url = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    analysis_url = "https://api-inference.huggingface.co/models/google/flan-t5-large"

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
            "parameters": {"do_sample": True, "max_new_tokens": max_tokens, "min_length": min_length, "max_length": max_length},
            "options": {"wait_for_model": True, "use_gpu": True},
        })
        if 'error' in output:
            print("\n---\nanalysis output returned an error!\n---")
            print(output)
            print("---")
            return ""
        else:
            return output[0]["generated_text"]
    
    @staticmethod
    def split_into_chunks(text, max_words=700):
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
            if len(section.split()) <= 700:
                processed_sections.append(section)
            else:
                chunks = HuggingFaceApi.split_into_chunks(section, 700)
                processed_sections.extend(chunks)
        return processed_sections

    @staticmethod
    def processTOS(tos):
        chunks = HuggingFaceApi.splitTOS(tos)[1:]
        summary_total = ""
        analysis_total = []
        for chunk in chunks:
            summary = HuggingFaceApi.makeSummaryApiCall(chunk, 250, 20, 500)
            summary_total += f'{summary}\n'
            question = "Explain why this Terms of Service clause is important:"
            prompt = f"{question}\n\n{chunk}"
            analysis = HuggingFaceApi.makeAnalysisApiCall(prompt, 250, 20, 500)
            duo = [summary, analysis]
            analysis_total.append(duo)

        summary2 = HuggingFaceApi.makeSummaryApiCall(summary_total, 250, 20, 500)
        analysis_total.insert(0, [summary2, ""])
        return analysis_total

    def testSection(section):
        summary = HuggingFaceApi.makeSummaryApiCall(section, 250, 20, 500)
        question = "Explain why this Terms of Service clause is important:"
        prompt = f"{question}\n\n{section}"
        responseF = HuggingFaceApi.makeAnalysisApiCall(section, 250, 20, 500)
        responseS = HuggingFaceApi.makeAnalysisApiCall(summary, 250, 20, 500)
        print(f'Summary:\n{summary}\n\n*****\nTranslation with full section:\n\n{responseF}\n*****\nTranslation with summary:\n\n{responseS}')
        return responseF


    


   



