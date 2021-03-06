import nltk
import re
import curses.ascii
from nltk.corpus import cmudict
from nltk.corpus import brown
from nltk.probability import *


class Comments:
	def __init__(self):
		self.comments = []
		self.sentTokenizer = nltk.tokenize.punkt.PunktSentenceTokenizer()		

		self.initFreqData()
		self.initMisusedWords()
		self.initMisusedPhrases()	

	def initMisusedWords(self):
		# Smriti :: add more words
		self.misusedList = [("accept", "VB", "except"),
			("than", "IN", "then"),
			("then", "RB", "than"),
			("affect", "VB", "effect"),
			("effect", "NN", "affect"),
			("elicit", "VB", "illicit"),
			("illicit", "JJ", "elicit")]

	def initMisusedPhrases(self):
		'''http://www.quora.com/India/What-are-some-English-words-phrases-colloquial-or-not-overused-or-even-misused-in-India
			http://www.policymic.com/articles/31309/10-most-commonly-misused-words
			http://www.rediff.com/getahead/slide-show/slide-show-1-career-top-english-mistakes-desi-make/20110719.htm
		'''
		self.misusedIndian = [("you gets", "you get"),
			("please do the needful","Please do what's necessary"),
			("pluck flowers", "pick flowers"),
			("yesterday evening", "last evening"),
			("yesterday night", "last night"),
			("updation", "update"),
			("please to", "please"),
			("cousin brother", "cousin"),
			("cousin sister", "cousin"),
			("prepone", "advance"),
			("anyways", "anyway"),
			("more better", "better"),
			("by the by", "by the way"),
			("listening music", "listening to music"),
			("repeat again", "repeat"),
			("return back", "return"),
			("good name", "name")]

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
		self.floweriness = []

		sents = []
		for para in data.split('\n'):
			sents.extend(self.sentTokenizer.tokenize(para, realign_boundaries=True))
		sentno = len(sents)
		
		for i in range(len(sents)):
			sents[i] = sents[i].strip()
			tokens = nltk.tokenize.word_tokenize(sents[i])
			
			for p in self.misusedIndian:
                		if(sents[i].lower().find(p[0])!=-1):
					self.comments.append([sents[i], 1, "\"" + sents[i][:20] + "...\" Consider using \'" + p[1] + "\' instead of \'" + p[0] + "\'."])

			rareno += self.rareCount(tokens)
			
			tagged = nltk.pos_tag(tokens)

			tagWords = list(t for t in tagged if curses.ascii.isalpha(t[1][0]))
			if len(tagWords) > 21:
				self.comments.append([sents[i], 0, "\"" + sents[i][:20] + "...\" may be too long."])

			if self.is_passive(tagged):
				self.comments.append([sents[i], 0, "\"" + sents[i][:20] + "...\" might be in passive voice."])

			adno += self.adCount(tagged)
			
			if self.endsWithPrep(tagged):
				self.comments.append([sents[i], 0, "\"" + sents[i][:20] + "...\": " + "ends with a preposition. Consider revising."])

			if not self.tenseConsistency(tagged):
				self.comments.append([sents[i], 1, "\"" + sents[i][:20] + "...\": " + " tense inconsistency detected."])

			for j in range(len(tagWords)):
				if curses.ascii.isalpha(tagWords[j][1][0]):
					temp = self.misused(tagWords[j])
					if (temp):
						self.comments.append([sents[i], 1, "\"" + sents[i][:20] + "...\": " + temp])

		# Floweriness and obscurity
		self.floweriness.append("Floweriness: " + dec(adno*1.0/sentno))
		self.floweriness.append("Obscurity: " + dec(rareno*1.0/sentno))

		return (self.comments, self.floweriness)

	def message(self, word):
		return "\'" + word + "\' might be more suitable in this sentence."

	def misused(self, token):
		for p in self.misusedList:
			if (token[0].lower() == p[0] and token[1][:2] != p[1] ):
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

	def is_passive(self, tags):
		passive = False
		state = ""
		i = 0
		while (i < len(tags) and passive == False):
			if tags[i][0] in ("is", "am", "was", "were", "are", "be"):
				state = "BE"
			elif tags[i][0] in ("has", "have", "had"):
				state = "H"
			elif state == "BE" and tags[i][0] == "being":
				pass
			elif state == "BE" and tags[i][1] in ("VBN", "VBD"):
				passive = True
			elif state == "H" and tags[i][0] == "been":
				state = "BE"
			else:
				state = ""
			i += 1
		return passive

	def endsWithPrep(self, tagged):
		if not len(tagged) > 1:
			return False
		pos = len(tagged) - 1 if curses.ascii.isalpha(tagged[len(tagged)-1][1][0]) else len(tagged) - 2 
		if tagged[pos][1] == "IN":
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

		self.sentTokenizer = nltk.tokenize.punkt.PunktSentenceTokenizer()		
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
		sents = []
		for para in data.split('\n'):
			sents.extend(self.sentTokenizer.tokenize(para, realign_boundaries=True))
		self.sentno = len(sents)

		for sent in sents:
			words = nltk.tokenize.word_tokenize(sent)

			for word in words:
				if curses.ascii.isalpha(word[0]):
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
