import wikipedia
while True:
    input = raw_input("\nQ: ")
    wikipedia.set_lang("en")
    print wikipedia.summary(input, sentences=2)
