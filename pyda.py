#import wolframalpha

#input = input("What's Your Question:  ")
#app_id = "65U2P2-LX969RK234"
#client = wolframalpha.Client(app_id)
#res = client.query(input)
#answer = next(res.results).text
#print (answer)

import wikipedia
while True:
    input = raw_input("\nQ: ")
    wikipedia.set_lang("en")
    print wikipedia.summary(input, sentences=2)
