class MinMaxWordFinder:
    def __init__(self):
        self.all_words = []

    def add_sentence(self, sentence):
        words = sentence.split()
        self.all_words.extend(words)

    def shortest_words(self):
        if not self.all_words:
            return []
        min_len = min(len(w) for w in self.all_words)
        shortest = sorted(set(w for w in self.all_words if len(w) == min_len))
        return shortest

    def longest_words(self):
        if not self.all_words:
            return []
        max_len = max(len(w) for w in self.all_words)
        longest = sorted(set(w for w in self.all_words if len(w) == max_len))
        return longest