import json
import os
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

class LLMParser:
    json_schema = {
        "type": "object",
        "properties": {
            # Nomenclature
            "name": {"type": "string"},
            "family": {"type": "string"},
            "origin": {"type": "string"},
            "size": {"type": "string"},
            # Tank
            "tankSize": {"type": "string"},
            "tankLevel": {"type": "string"},
            # Care
            "diet": {"type": "string"},
            "careDifficulty": {"type": "string"},
            "breeding": {"type": "string"},
            "aggressiveness": {"type": "string"},
            # Water Parameters
            "pH": {"type": "string"},
            "gH": {"type": "string"},
            "kH": {"type": "string"},
            "temperature": {"type": "string"},
        }
    }
    tokenizer = AutoTokenizer.from_pretrained(os.environ['LLM_SOURCE'])
    model = AutoModelForSeq2SeqLM.from_pretrained(os.environ['LLM_SOURCE'])

    @classmethod
    def parse(cls, website_html: str) -> dict:
        breakpoint()
        generator = pipeline("text2text-generation", model=cls.model)
        prompt = f'''
        Use this document: {website_html}
        Extract important fields into a JSON object
        If a field can't be found, return "Not Found"
        Use the following schema: {cls.json_schema}'''
        generated_data = generator(prompt)
        breakpoint()
        return generated_data
