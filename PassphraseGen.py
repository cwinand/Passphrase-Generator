from HTMLParser import HTMLParser
import string, random

class NewHTMLParser(HTMLParser):
    def handle_data(self, data):
    	w = str(data).strip()
        if w.isalpha() and len(w) > 1 and w != "else" and w.islower():
            words.append(str(data.strip()))

words = []
mapped_words = {}
parser = NewHTMLParser()

f = open("nounhtml.txt", "r")

for i in f:
	parser.feed(i)
f.close()

for i in range(0, len(words)):
	mapped_words[i] = words[i]

def create_pw():
	pw = ''
	ser = raw_input("What account is this for?  -->  ")
	acc = raw_input("What is the account name?  -->  ")
	for i in range(0, 4):
		num = random.randint(0, len(words))
		pw =  "%s %s" % (pw, mapped_words[num])
	f = open("", "a") #Put a file here for writing down all generated passphrases
	f.write("%s\n%s\n%s\n\n" % (ser, acc, pw))
	f.close()
	return pw


print create_pw()