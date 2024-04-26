InputOrOutput = input("Add URL or Open URL? ").upper()
with open("URLlist.txt", "r") as url:
    url.readline()
    print(url.read())
    URLdict = url.readline()
    print(URLdict)
URLdict = {"google" : "https.google.co.uk"}


match InputOrOutput:
    case "ADD" | "A":
        URLInput, URLInputConcat = input("Please enter a URL "), input("Please enter the shortened URL ")
        URLdict.update({URLInputConcat : URLInput})
        print(URLdict)
    case "OPEN" | "O":
        inputURL = input("Input a URL ")
        if inputURL in URLdict:
            print(URLdict[inputURL])
        else:
            print("invalid")
    case _:
        print("Invalid")
with open("URLlist.txt", "w") as url:
    url.write(str(URLdict).replace("{","").replace("}",""))
    print(str(URLdict))
