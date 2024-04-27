try:
  f = open("URLlist.txt")
  URLdict = f.readline()
  print(URLdict) 
  print(type(URLdict)) #str
  URLdict = URLdict.strip("{} \n")  # remove curly braces, spaces, and newline
  URLdict = URLdict.split(", ")  # split by comma and space
  URLdict = [i.split(": ") for i in URLdict]  # split by colon and space
  #Can be interchanged with a for loop
  URLdict = {i[0].strip("'"): i[1].strip("'") for i in URLdict}  # remove single quotes and create dictionary
  #Can be interchanged with a for loop
  print(URLdict)
  print(type(URLdict)) # dict
  print(URLdict['google'])
except:
  URLdict = {}

finally:
  InputOrOutput = input("Add URL or Open URL? ").upper()
  print(URLdict)
  
  
  match InputOrOutput:
      case "ADD" | "A":
          URLInput, URLInputConcat = input("Please enter a URL "), input("Please enter the shortened URL ")
          URLdict.update({URLInputConcat : URLInput})
          print(URLdict)
      case "OPEN" | "O":
          inputURL = input("Input shortened URL ")
          if inputURL in URLdict or inputURL in URLdict.values():
              print(URLdict[inputURL])
          else:
              print("invalid")
      case _:
          print("Invalid")
  with open("URLlist.txt", "w") as url:
      url.write(str(URLdict))
      print(str(URLdict))