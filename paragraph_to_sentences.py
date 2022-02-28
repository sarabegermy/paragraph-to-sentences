#from collections import deque
#test cases: Hello! I'm Sarah. "fjalfajfl. jfksjla", said Mac. That's too much, Mac's mother. Dr. W. Watson is amazing.
#references:
#https://pythex.org/
#https://www.debuggex.com/cheatsheet/regex/python
#https://www.youtube.com/watch?v=AEE9ecgLgdQ
#https://www.youtube.com/watch?v=K8L6KVGG-7o
#https://docs.python.org/3/library/re.html

import re
def get_sentences(paragraph):
    #pattern = re.compile(r'[^.!?]+([.]|[!]|[?])')#any characters then . or ? or !
    #(?! ...): negative assertion>>> remove space from beginning
    # consider the abbreviations that consists of less than 3 letters then dot.
    #pattern = re.compile(r'(?!\s)(.{,3}[.]){0,}[^.!?]{4,}?([.]|[!]|[?])')
    pattern = re.compile(r'(?!\s)(\".*\")?(.{,3}[.]){0,}[^.!?]{4,}?([.]|[!]|[?])')
    matches = re.finditer(pattern, paragraph)#pattern.finditer(paragraph)
    #matches = re.findall(pattern, paragraph)  # pattern.finditer(paragraph)
    return matches

'''
	sentences = []
	single_quotations = paragraph.find_all("\'") #may be apostrophe
	double_quotations = paragraph.find_all('\"')

	sentences_initially = paragraph.split(sep=['?', '.', '!'])
	if len(double_quotations)&1 == len(double_quotations):#even

		while i<len(double_quotations)-1:
			paragraph[double_quotations[i]] paragraph[double_quotations[i+1]]
			i += 1

		if paragraph.find()
		#ignore all '.','!','?'
	else
		print("Error: The quotations are not closed")
	return sentences
	
'''
#pattern = re.compile(r'''((?:[^.!?"']|"[^"]*"|'[^']*')+)''')
#matches = pattern.search(paragraph)
#begin from index 1 and step=2
#matches = pattern.split(paragraph)[1::2]
if __name__ == '__main__':
    paragraph = input()
    sentences = get_sentences(paragraph)
    for sentence in sentences:
        print(sentence.group())
        #print(sentence)
