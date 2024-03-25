import g4f

from g4f.Provider import You

response=g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    provider=g4f.Provider.You,
    messages=[{"role":"user","content":"请为我介绍一石家庄 "}],
    )

print(response)
























 
