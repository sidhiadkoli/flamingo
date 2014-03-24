import nltk
#import sys
import re
import postagger
import curses.ascii
from nltk.corpus import cmudict
from itertools import dropwhile

class IsPassive:

	def __init__(self):
		self.TAGGER = postagger.get_tagger()

	def tag_sentence(self, sent):
		"""Take a sentence as a string and return 
			a list of (word, tag) tuples."""

		tokens = nltk.word_tokenize(sent)
		return self.TAGGER.tag(tokens)

	def passivep(self, tags):
		"""Takes a list of tags, returns true if 
			we think this is a passive sentence."""
		
		postToBe = list(dropwhile(lambda(tag): not tag.startswith("BE"), tags))
		nongerund = lambda(tag): tag.startswith("V") and not tag.startswith("VBG")

		filtered = filter(nongerund, postToBe)
		out = any(filtered)

		return out

	def is_passive(self, sent):
		"""Given a sentence, tag it and print if we think 
		it's a passive-voice formation."""
		tagged = self.tag_sentence(sent)
		tags = map( lambda(tup): tup[1], tagged)

		return self.passivep(tags)

# Do we really need regexp? Consider.
class Comments:
	def __init__(self):
		self.comments = []
		self.passive = IsPassive()
		self.regexp = re.compile('\A[^a-zA-Z]')
		
		# must add more words
		self.misused_list = [("accept", "VB", "except"),
			("except", "NN", "accept"),
			("than", "IN", "then"),
			("then", "RB", "than"),
			("affect", "VB", "effect"),
			("effect", "NN", "affect")]

	def dec(self, decnum):
		return "%.2f" %decnum

	# There is redundancy here. We do not need to calculate statistics
	#	(Cleaned up class. Further clean up is possible)	
	# Must change the first item in comments to a suitable format.
	#	It currently calculates line number.
	def getComments(self, data) :
		## variables
		chno = 0
		sentno = 0
		adno = 0
		##
		self.comments = []

		sents = nltk.tokenize.sent_tokenize(data)

		for i in range(len(sents)):
			if self.passive.is_passive(sents[i]):
				self.comments.append([chno/100+1, "\"" + sents[i][:20] + "...\" might be in passive voice."]) 

			tokens = nltk.tokenize.word_tokenize(sents[i][:-1])
			if (len(tokens) > 21):
				self.comments.append([chno/100+1, "\"" + sents[i][:20] + "...\" may be too long."])

			adno += self.adCount(tokens)
			sentno += 1
			tagged = nltk.pos_tag(tokens)
			for j in range(len(tokens)):
				if (self.regexp.search(tokens[j])) :
					pass
				else :	
					temp = self.misused(tagged[j])
					if (temp):
						self.comments.append([chno/100+1, "\"" + sents[i][:20] + "...\": " + temp])
			chno += len(sents[i])

		# I have currently put floweriness along with the comments
		#	will have to reorg later
		self.comments.append([0, "Floweriness: " + self.dec(adno*1.0/sentno) + "/sentence"])

		return self.comments

	def message(self, word):
		return "\'" + word + "\' might be more suitable in this sentence."

	# Gives error for words containing words in the misused list.
	# eg: exceptional, affection
	# Must be corrected.
	def misused(self, token):
		for p in self.misused_list:
			if (token[0][:len(p[0])].lower() == p[0] and token[1][:2] != p[1] ):
				return self.message(p[2])
		return None

	def adCount(self, tokens):
		tagged = nltk.pos_tag(tokens)
		mydict = dict(tagged)
		pos2 = nltk.Index((value, key) for (key, value) in mydict.items())
		adj =  pos2['JJ']	 #adj
		adj += pos2['JJR']	#adj, comparative
		adj += pos2['JJS']	#adj, superlative
		adv =  pos2['RB']	 #adv
		adv += pos2['RBR']	#adv, comparative
		adv += pos2['RBS']	#adv, superlative
		
		return len(adj)+len(adv)

# Should think about exact format of data we return
class Readability:
	def __init__(self):
		self.res = []
		self.chno = 0
		self.charno = 0
		self.sylno = 0
		self.wordno = 0
		self.sentno = 0
		self.polyno = 0
	
		self.rep = []
		self.rep.append(["Number of characters", 0])
		self.rep.append(["Number of syllables", 0])
		self.rep.append(["Number of polysyllables", 0])
		self.rep.append(["Number of words", 0])
		self.rep.append(["Number of sentences", 0])

		self.regexp = re.compile('\A[^a-zA-Z]')
		self.di = cmudict.dict() 

	
	def getStats(self, data):
		sents = nltk.tokenize.sent_tokenize(data)
		self.sentno = len(sents)

		for sent in sents:
			words = nltk.tokenize.word_tokenize(sent[:-1])

			for word in words:
				if (self.regexp.search(word)) :
					pass
				else :
					self.charno += len(word) 
					result = self.nsyl(word)[0]
					self.sylno += result
					self.polyno += (1 if result >= 3 else 0)
					self.wordno += 1
	
			self.chno += len(sent)

	def getResultData(self):
		self.rep[0][1] = self.charno
		self.rep[1][1] = self.sylno
		self.rep[2][1] = self.polyno
		self.rep[3][1] = self.wordno
		self.rep[4][1] = self.sentno
		
		return self.rep

	def getReadability(self, data):
		self.res = []
		self.getStats(data)	

		#Flesch Reading ease 
		score = 206.835 - 1.015 * self.wordno / self.sentno - 84.6 * self.sylno / self.wordno
		self.res.append(["Flesch-Kincaid Reading Ease", score])

		#Flesch-Kincaid Grade Level
		score = 0.39 * self.wordno / self.sentno + 11.8 * self.sylno / self.wordno - 15.59
		self.res.append(["Flesch-Kincaid Grade Level", score])

		#Gunning-Fog Score
		score = 0.4 * (float(self.wordno) / self.sentno + 100.0 * self.polyno / self.wordno)
		self.res.append(["Gunning-Fog Score", score])

		#Coleman-Liau Index
		l = 100.0 * self.charno / self.wordno
		s = 100.0 * self.sentno / self.wordno
		score = 0.0588 * l - 0.296 * s - 15.8 
		self.res.append(["Coleman-Liau Index", score])

		#SMOG Index
		score = 1.043 * pow(self.polyno * 30.0 / self.sentno, 0.5) + 3.1291
		self.res.append(["SMOG Index", score])

		#Automated Readability Index
		score = 4.71 * self.charno / self.wordno + 0.5 * self.wordno / self.sentno - 21.43
		self.res.append(["Automated Readability Index", score])

		return self.res		

	def nsyl(self, word):
		try:
			return [len(list(y for y in x if curses.ascii.isdigit(y[-1]))) for x in self.di[word.lower()]]
		except:
			# use reg ex. find an alternative to syllable counting
			return [0]
		

	''' COMMENTED OUT!
	# we no longer need the below functions. But let them be
	# 	in case we require some of their functionality,
	#	of for testing purposes.
	def printLineNo(num):
		print "(" + str(num) + ")",

	def display(data):
		print "\n"
		x = len(data)/100 + 1
		for i in xrange(x):
			printLineNo(i+1)
			print data[i*100:(i+1)*100]

		print "\n\nComments"
		for p in comments:
			printLineNo(p[0])
			print p[1]

		print "\nReadability"
		for r in res:
			print r[0] + ": " + dec(r[1])

		print "\nInfo"
		for i in rep:
			print i[0] + ": " + str(i[1])

		print

	def main():
		f = open(sys.argv[1])
		text = f.read()
		readblty(text)

		display(text)

if __name__ == "__main__":
	main()

if __name__ == "__main__":
	f = open(sys.argv[1])
	text = f.read()
	
	#c = Comments()
	#print c.getComments(text)

	r = Readability()
	print r.getReadability(text)
	print r.getResultData()
	
if __name__ == "__main__":
	f = open(sys.argv[1])
	text = f.read()
	
	#c = Comments()
	#print c.getComments(text)

	r = Readability()
	print r.getReadability(text)
	print r.getResultData()

	'''