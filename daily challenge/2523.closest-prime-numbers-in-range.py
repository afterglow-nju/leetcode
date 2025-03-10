class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:
        sieve = [True] * (right + 1)
        sieve[0] = sieve[1] = False
        
        for i in range(2, int(right**0.5) + 1):
            if sieve[i]:
                for j in range(i*i, right + 1, i):
                    sieve[j] = False
        
        primes = [i for i in range(left, right + 1) if sieve[i]]
        
        if len(primes) < 2:
            return [-1, -1]
        
        min_gap = float('inf')
        result = [-1, -1]
        
        for i in range(1, len(primes)):
            gap = primes[i] - primes[i-1]
            if gap < min_gap:
                min_gap = gap
                result = [primes[i-1], primes[i]]
        
        return result
    
    
    
    
class Trie():
    def __init__(self):
        self.children = {}
        self.isEnd = False
    
    def insert(self, word):
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = Trie()
            node = node.children[char]
        node.isEnd = True
    
    def search(self, word, start, count):
        node = self
        for i in range(start, len(word)):
            if word[i] not in node.children:
                return False
            node = node.children[word[i]]
            if node.isEnd:
                if i == len(word) - 1:
                    return count >= 1
                if self.search(word, i + 1, count + 1):
                    return True
        return False

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            if word:
                trie.insert(word)
        
        result = []
        for word in words:
            if word and trie.search(word, 0, 0):
                result.append(word)
        
        return result

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        