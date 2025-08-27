from nl_to_logic_translator.pipelines.nl_to_logic import NLtoLogicTranslator

statements = [
    "Event A will occur before Event B",
    "Event C is likely to happen within 5 days of Event D"
]

translator = NLtoLogicTranslator()
logic_programs = translator.translate(statements)

print("Natural Language to Temporal Logic Translation Results:")
for stmt, logic in zip(statements, logic_programs):
    print(f"NL: {stmt}\nLogic: {logic}\n")
