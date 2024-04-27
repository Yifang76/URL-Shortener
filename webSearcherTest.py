from websearch import WebSearch as web


whichURL = input("Search Fake Google ")
imageOrLink = input("Image or Website? ").upper()
if imageOrLink == "Image" or imageOrLink == "I":

elif imageOrLink == "Website" or imageOrLink == "W":
  
while True:
  for page in web(whichURL).pages[:100]:
    print(page)
  searchAgain = input("Would you like to load more pages? ").upper()
  if searchAgain == "YES" or searchAgain == "Y":
    try:
      for page in web(whichURL).next_page().pages[:100]:
        print(page)
      #broken?
    except:
      print("No more pages")
      break
  else:
    break
    

