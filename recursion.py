def downup(string):
    if len(string) == 1:
        print(string)
    else:
        print(string)
        downup(string[:len(string)-1])
        print(string)

downup("greetings")

