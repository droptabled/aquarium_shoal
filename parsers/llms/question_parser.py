from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline
from parsers.llms.base_parser import BaseParser

class QuestionParser(BaseParser):
    tokenizer = AutoTokenizer.from_pretrained("./llm_models/tinyroberta-squad2")
    model = AutoModelForQuestionAnswering.from_pretrained("./llm_models/tinyroberta-squad2")

    @classmethod
    def parse(cls, website_html: str) -> dict:
        generator = pipeline("question-answering", model=cls.model, tokenizer=cls.tokenizer)
        results = {}
        for field in cls.fields:
            generated_data = generator(question=cls.question.format(field=field), context=website_html, max_length=50)
            results[field] = generated_data["answer"]
            breakpoint()

        breakpoint()
        return results
