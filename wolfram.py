import wolframalpha

input = input("What's Your Question:  ")
app_id = "65U2P2-LX969RK234"
client = wolframalpha.Client(app_id)
res = client.query(input)
answer = next(res.results).text
print (answer)
