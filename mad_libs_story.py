
story = """Once upon a time, there was a _______ (adjective) _______ (noun) who loved to _______ (verb) every day.
One day, they met a _______ (adjective) _______ (noun) and together they _______ (verb) until sunset."""

adj1 = input("Enter an adjective: ").strip()
noun1 = input("Enter a noun: ").strip()
verb1 = input("Enter a verb: ").strip()
adj2 = input("Enter another adjective: ").strip()
noun2 = input("Enter another noun: ").strip()
verb2 = input("Enter another verb: ").strip()

finished_story = print(f"""Once upon a time, there was a {adj1} {noun1} who loved to {verb1} every day.
One day, they met a {adj2} {noun2} and together they {verb2} until sunset.""")