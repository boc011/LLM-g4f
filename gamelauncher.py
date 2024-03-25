import g4f



from g4f.Provider import You



gameName = input("Enter the name of the game you want to launch:")



request = "Write a " + gameName + " game in Python code"



response = g4f.ChatCompletion.create(

    model="gpt-3.5-turbo",

    provider=g4f.Provider.You,

    messages=[{"role": "user", "content": "write a Number Guessing Game in python code"}],

)

responseLines = response.splitlines()



fname = "generated.py"



with open(fname, "w") as f:

    # only start to write when this flag is True

    startPythonCode = False

    for line in responseLines:

        # 1 the line equals to "```python"

        # 2 the line equals to "```"

        if (line == "```python"):

            startPythonCode = True

        elif (line == "```"):

            break

        elif (startPythonCode):

            f.write(line + "\n")



with open(fname) as f:

    exec(f.read())



#print(response)



























 
