import nltk
import re
import postagger
import curses.ascii
from nltk.corpus import cmudict
from nltk.corpus import brown
from nltk.probability import *
from itertools import dropwhile


class IsPassive:
	def __init__(self):
		self.TAGGER = postagger.get_tagger()

	def tag_tokens(self, tokens):
		"""Take tokens and return 
			a list of (word, tag) tuples."""

		return self.TAGGER.tag(tokens)

	def passivep(self, tags):
		"""Takes a list of tags, returns true if 
			we think this is a passive sentence."""
		
		postToBe = list(dropwhile(lambda(tag): not tag.startswith("BE"), tags))

		nongerund = lambda(tag): tag.startswith("V") and not (tag.startswith("VBG") or tag == "VB")

		filtered = filter(nongerund, postToBe)
		out = any(filtered)

		return out

	def is_passive(self, tokens):
		"""Given tokens, tag it and print if we think 
		it's a passive-voice formation."""
		tagged = self.tag_tokens(tokens)
		tags = map( lambda(tup): tup[1], tagged)

		return self.passivep(tags)

class Comments:
	def __init__(self):
		self.comments = []
		self.passive = IsPassive()
		self.regexp = re.compile('\A[^a-zA-Z]')
		
		self.initFreqData()
		
		# Smriti :: add more words
		self.misused_list = [("accept", "VB", "except"),
			("except", "NN", "accept"),
			("than", "IN", "then"),
			("then", "RB", "than"),
			("affect", "VB", "effect"),
			("effect", "NN", "affect")]

	def initFreqData(self):
		self.words = FreqDist()
		for sentence in brown.sents():
			for word in sentence:
				self.words.inc(word.lower())

	#	(Cleaned up class. Further clean up is possible)	
	def getComments(self, data) :
		sentno = 0
		adno = 0
		rareno = 0
		
		self.comments = []

		sents = nltk.tokenize.sent_tokenize(data)

		for i in range(len(sents)):
			tokens = nltk.tokenize.word_tokenize(sents[i])

			if self.passive.is_passive(tokens):
				self.comments.append([sents[i], 0, "\"" + sents[i][:20] + "...\" might be in passive voice."]) 

			rareno += self.rareCount(tokens)
			
			if (len(tokens) > 21):
				self.comments.append([sents[i], 0, "\"" + sents[i][:20] + "...\" may be too long."])

			sentno += 1
			tagged = nltk.pos_tag(tokens)
			adno += self.adCount(tagged)
			
			if self.endsWithPrep(tagged):
				self.comments.append([sents[i], 0, "\"" + sents[i][:20] + "...\": " + "ends with a preposition. Consider revising."])

			if not self.tenseConsistency(tagged):
				self.comments.append([sents[i], 1, "\"" + sents[i][:20] + "...\": " + " tense inconsistency detected."])

			for j in range(len(tokens)):
				if (self.regexp.search(tokens[j])) :
					pass
				else :	
					temp = self.misused(tagged[j])
					if (temp):
						self.comments.append([sents[i], 1, "\"" + sents[i][:20] + "...\": " + temp])

		# I have currently put floweriness along with the comments
		# will have to reorg later
		self.comments.append(["", 2, "Number of Adjectives per Sentence: " + dec(adno*1.0/sentno)])

		self.comments.append(["", 2, "Number of Rare/Difficult words per Sentence: " + dec(rareno*1.0/sentno)])

		return self.comments

	def message(self, word):
		return "\'" + word + "\' might be more suitable in this sentence."

	# Sidhi :: fix error
	# Gives error for words containing words in the misused list.
	# eg: exceptional, affection
	# Must be corrected.
	def misused(self, token):
		for p in self.misused_list:
			if (token[0][:len(p[0])].lower() == p[0] and token[1][:2] != p[1] ):
				return self.message(p[2])
		return None
		
	def rareCount(self, tokens):
		count = 0
		for token in tokens:
			if(self.words[token]<=5 and self.words[token]>0):				
				count+=1
		return count
	
	def adCount(self, tagged):
		adj = 0
		adv = 0
		for i in tagged:
			if (i[1] == 'JJ' or i[1] == 'JJR' or i[1] == 'JJS'):
				adj += 1
			if (i[1] == 'RB' or i[1] == 'RBR' or i[1] == 'RBS'):
				adv += 1
		return adj + adv

	def endsWithPrep(self, tagged):
		if len(tagged) > 1 and tagged[len(tagged) - 2][1] == "IN":
			return True
		return False

	def tenseConsistency(self, tagged):
		isPast = False
		isPresent = False
		quotes = False
		for tag in tagged:
			if tag[0] in ("''", "``"):
				quotes = not quotes
			if not quotes:
				if tag[1] == "VBD":
					if isPresent:
						return False
					else:
						isPast = True
				elif tag[1] in ("VBP", "VBZ"):
					if isPast == True:
						return False
					else:
						isPresent = True
		return True
	
class Readability:
	def __init__(self):
		self.res = []
		
		self.clearAll()
	
		self.rep = []
		self.rep.append(["Number of characters", 0])
		self.rep.append(["Number of syllables", 0])
		self.rep.append(["Number of polysyllables", 0])
		self.rep.append(["Number of words", 0])
		self.rep.append(["Number of sentences", 0])

		self.regexp = re.compile('\A[^a-zA-Z]')
		self.di = cmudict.dict() 

	def clearAll(self):
		self.chno = 0
		self.charno = 0
		self.sylno = 0
		self.wordno = 0
		self.sentno = 0
		self.polyno = 0	

	def getStats(self, data):
		self.clearAll()
		sents = nltk.tokenize.sent_tokenize(data)
		self.sentno = len(sents)

		for sent in sents:
			words = nltk.tokenize.word_tokenize(sent)

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
		
		if self.charno == 0:
			return False

		return True

	def getResultData(self):
		self.rep[0][1] = self.charno
		self.rep[1][1] = self.sylno
		self.rep[2][1] = self.polyno
		self.rep[3][1] = self.wordno
		self.rep[4][1] = self.sentno
		
		return self.rep

	def getReadability(self, data):
		self.res = []
		if not self.getStats(data):
			return []
		total = 0

		#Flesch Reading ease 
		score = 206.835 - 1.015 * self.wordno / self.sentno - 84.6 * self.sylno / self.wordno
		self.res.append(["Flesch-Kincaid Reading Ease", dec(score)])

		#Flesch-Kincaid Grade Level
		score = 0.39 * self.wordno / self.sentno + 11.8 * self.sylno / self.wordno - 15.59
		total += score
		self.res.append(["Flesch-Kincaid Grade Level", dec(score)])

		#Gunning-Fog Score
		score = 0.4 * (float(self.wordno) / self.sentno + 100.0 * self.polyno / self.wordno)
		total += score
		self.res.append(["Gunning-Fog Score", dec(score)])

		#Coleman-Liau Index
		l = 100.0 * self.charno / self.wordno
		s = 100.0 * self.sentno / self.wordno
		score = 0.0588 * l - 0.296 * s - 15.8 
		total += score
		self.res.append(["Coleman-Liau Index", dec(score)])

		#SMOG Index
		score = 1.043 * pow(self.polyno * 30.0 / self.sentno, 0.5) + 3.1291
		total += score
		self.res.append(["SMOG Index", dec(score)])

		#Automated Readability Index
		score = 4.71 * self.charno / self.wordno + 0.5 * self.wordno / self.sentno - 21.43
		total += score
		self.res.append(["Automated Readability Index", dec(score)])

		self.res.append(["-------------------------------", ""])
		self.res.append(["Average readability score", dec(total/5)])

		return self.res		

	def nsyl(self, word):
		try:
			return [len(list(y for y in x if curses.ascii.isdigit(y[-1]))) for x in self.di[word.lower()]]
		except:
			# use reg ex. find an alternative to syllable counting
			return [0]
		
def dec(decnum):
	return "%.2f" %decnum

