import urllib

def read_text():
    quotes = open("C:\Users\kamat_sn\Downloads\movie_quotes.txt")
    file_content = quotes.read()
    #print (file_content)
    quotes.close()
    check_curse(file_content)

def check_curse(text_check):
    connectn = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_check)
    outpt = connectn.read()
    #print (outpt)
    connectn.close()
    if outpt=="true":
        print "Curse Word detectded :("
    elif outpt=="false":
        print "No curse word detected :)"
    else:
        print "Unable to read file :|"

read_text()