import json
import os
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

class LLMParser:
    fields = [
        # Nomenclature
        "name",
        "family",
        "origin",
        "fish size",
        # Tank
        "tank size",
        # Care
        "diet",
        "care difficulty",
        "breeding difficulty",
        "aggressiveness",
        # Water
        "pH",
        "hardness",
        "carbonate hardness",
        "temperature",
    ]
    tokenizer = AutoTokenizer.from_pretrained(os.environ['LLM_SOURCE'])
    model = AutoModelForSeq2SeqLM.from_pretrained(os.environ['LLM_SOURCE'])

    @classmethod
    def parse(cls, website_html: str) -> dict:
        generator = pipeline("text2text-generation", model=cls.model, tokenizer=cls.tokenizer)
        results = {}
        for field in cls.fields:
            prompt = f'''
            Use this document: {website_html}
            What is the required {field}?'''
            generated_data = generator(prompt, max_length=100)
            results[field] = generated_data[0]["generated_text"]

        breakpoint()
        return results
