import wikipedia
import wolframalpha

while True:
    input = raw_input("Q: ")

    try:
        #wolframalpha
        app_id = "65U2P2-LX969RK234"
        client = wolframalpha.Client(app_id)
        res = client.query(input)
        answer = next(res.results).text
        print (answer)

    except:
        #wikipedia
            print wikipedia.summary(input, sentences=2)
