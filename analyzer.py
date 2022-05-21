from functools import reduce
from string import punctuation

class TextAnalyzer:
    def __init__(self, text) -> None:
        text = text.strip()
        text = text.lower()
        self.wordsString = self.removeSymbols(text)
        self.wordsArray = (self.removeSymbols(text)).split(' ')
        self.wordsArray = list(filter(lambda x: x != '' and x != ' ', self.wordsArray))

    def findMedianOfSorted(self):
        arr = sorted(self.wordsArray, key=len)
        n = len(arr)
        if(n == 0):
            return 'No words was in the input!'
        # If n is even it will return the lower index and if it is odd then it'll be middle one so it'll use the same index number.
        return arr[n // 2]

    def findMedianLength(self):
        n = len(self.wordsArray)
        if(n == 0):
            return 0
        # If n is odd then the len of the middle element
        if(n % 2 == 1):
            return len(self.wordsArray[n // 2])
        # If n is even then the len is the average of the two middle elements
        return (len(self.wordsArray[(n-1) // 2]) + len(self.wordsArray[n  // 2])) / 2
    
    def removeSymbols(self, text):
        escapeChars = '\\\\"\n\t\r\b\f'
        for s in punctuation:
            text = text.replace(s, '')
        for s in escapeChars:
            text = text.replace(s, ' ')
        return text

    def sortWords(self):
        return self.wordArray.sort(key=len)

    def getNumberOfWords(self):
        return len(self.wordsArray)

    def getNumberOfLetters(self):
        return len(self.wordsString.replace(' ', ''))

    def getLongestWord(self):
        return reduce(lambda currLongest, currWord: currWord if (len(currWord) > len(currLongest)) else currLongest, self.wordsArray)

    def getAvgWordLength(self):
        if self.wordsString == '':
            return 0.00
        return round(self.getNumberOfLetters() / self.getNumberOfWords(),2)

    def getReadingDuration(self):
        # Assuming 250 wpm (which is 4.1666 we round it to 4.2 wps) is average rate. Source: Google
        return round(self.getNumberOfWords()/4.2,2)

    # Bonuses:
    def getMedianLength(self):
        # Without sorting the array of words, it will return the *length* of the median word.
        return round(self.findMedianLength(),2)

    def getMedianOfSorted(self):
        # Sorts the array of words and then returns the median word of it
        return self.findMedianOfSorted()

    def getMostCommonWords(self):
        mostCommonWords = []
        wordList = []
        for word in self.wordsArray:
            if(word in wordList):
                continue
            currCount = self.wordsArray.count(word)
            mostCommonWords.append((word, currCount))
            wordList.append(word)
        mostCommonWords = sorted(mostCommonWords, key=lambda x: x[1], reverse=True)
        return [x[0] for x in mostCommonWords[:5]]

    def getLanguage(self):
        countEnglish = 0
        countTurkish = 0
        englishWords= ['w', 'x', 'q', 'about', 'after', 'all', 'am', 'an', 'and', 'are', 'as', 'at', 'back', 'be', 'because', 'been', 'big', 'but', 'by', 'came', 'can', 'come', 'could', 'day', 'did', 'do', 'down', 'first', 'for', 'from', 'get', 'go', 'going', 'got', 'had', 'has', 'have', 'he', 'her', 'here', 'him', 'his', 'I', 'if', 'in', 'into', 'is', 'it', 'just', 'like', 'little', 'look', 'made', 'make', 'me', 'more', 'my', 'no', 'not', 'now', 'of', 'off', 'on', 'one', 'only', 'or', 'our', 'out', 'over', 'said', 'saw', 'see', 'she', 'so', 'some', 'that', 'the', 'their', 'them', 'then', 'there', 'they', 'this', 'to', 'two', 'up', 'very', 'was', 'we', 'well', 'went', 'were', 'what', 'when', 'where', 'which', 'who', 'will', 'with', 'would', 'you', 'your', 'million']
        turkishWords = ['ğ', 'ş', 'ç', 'ö', 'ü', 'ı' , 'hafta', 'yıl', 'bugün', 'yarın', 'dün', 'zor', 'ben', 'kim', 'hep', 'hepsi', 'bir', 'sen', 'bu', 'bunu', 'burada', 'nerede', 'ama', 'acaba', 'belki', 'için', 'şu', 'erkek', 'kadın', 'çok', 'yoksa','veya', 've', 'siz', 'biz', 'iki', 'üç', 'dört', 'altı', 'yedi', 'sekiz', 'dokuz', 'yirmi', 'otuz', 'kırk', 'elli', 'altmış', 'yetmiş', 'seksen', 'doksan', 'trilyon', 'milyar', 'milyon', 'var', 'dir', 'dır', 'onlar']
        
        # We will count the number of occurences of each English & Turkish stopwords, if Turkish stopwords are strictly more than
        # English then most probably the text is Turkish otherwise it is English.
        for i in turkishWords:
            if(i in self.wordsString):
                countTurkish += 1
        for i in englishWords:
            if(i in self.wordsString):
                countEnglish += 1
        return ('tr' if(countTurkish>countEnglish) else 'en')



