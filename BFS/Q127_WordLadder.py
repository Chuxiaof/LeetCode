class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not beginWord:
            return 0
        wordList = set(wordList)
        queue = collections.deque([beginWord])
        distances = {beginWord : 1}
        while queue:
            curr_word = queue.popleft()
            if curr_word == endWord:
                return distances[curr_word]
            for word in self.get_next_words(curr_word, wordList):
                if word in distances:
                    continue
                queue.append(word)
                distances[word] = distances[curr_word] + 1
                
        return 0

    def get_next_words(self, word, wordList):
        neighbor_words = []
        for i in range(len(word)):
            left, right = word[:i], word[i+1:]
            for char in "abcdefghijklmnopqrstuvwxyz":
                if word[i] == char:
                    continue
                neighbor_word = left + char + right
                if neighbor_word in wordList:
                    neighbor_words.append(neighbor_word)
        return neighbor_words
