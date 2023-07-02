import json
from jsonformer import Jsonformer
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


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
    tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-xxl")
    model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-xxl")

    @classmethod
    def parse(cls, website_html: str) -> dict:
        prompt = f'''
        Use this document: {website_html}
        Extract important fields into a JSON object
        If a field can't be found, return "Not Found"
        Use the following schema:'''
        jsonformer = Jsonformer(cls.model, cls.tokenizer, cls.json_schema, prompt)
        generated_data = jsonformer()
        return generated_data
