class BaseParser():
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
    context = "Use this document:\n{html:}\n"
    question = "What is the value of the required {field:}?"
