from nl_to_logic_translator.pipelines.nl_to_logic import NLtoLogicTranslator

def test_translation():
    translator = NLtoLogicTranslator()
    statements = ["Event X happens before Event Y"]
    results = translator.translate(statements)
    assert results[0].startswith("logic_representation_of")
    print("Test passed!")

if __name__ == "__main__":
    test_translation()
