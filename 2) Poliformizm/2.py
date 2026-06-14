class LeftParagraph:
    def __init__(self, width):
        self.width = width
        self.words = []

    def add_word(self, word):
        self.words.append(word)

    def end(self):
        line = []
        current_len = 0
        for word in self.words:
            if line:
                need = current_len + 1 + len(word)
            else:
                need = len(word)
            if need > self.width:
                out = ""
                for i, w in enumerate(line):
                    if i > 0:
                        out += " "
                    out += w
                print(out)
                line = [word]
                current_len = len(word)
            else:
                if line:
                    current_len += 1
                line.append(word)
                current_len += len(word)
        if line:
            out = ""
            for i, w in enumerate(line):
                if i > 0:
                    out += " "
                out += w
            print(out)
        self.words = []

class RightParagraph:
    def __init__(self, width):
        self.width = width
        self.words = []

    def add_word(self, word):
        self.words.append(word)

    def end(self):
        line = []
        current_len = 0
        for word in self.words:
            if line:
                need = current_len + 1 + len(word)
            else:
                need = len(word)
            if need > self.width:
                out = ""
                for i, w in enumerate(line):
                    if i > 0:
                        out += " "
                    out += w
                spaces = self.width - len(out)
                print(" " * spaces + out)
                line = [word]
                current_len = len(word)
            else:
                if line:
                    current_len += 1
                line.append(word)
                current_len += len(word)
        if line:
            out = ""
            for i, w in enumerate(line):
                if i > 0:
                    out += " "
                out += w
            spaces = self.width - len(out)
            print(" " * spaces + out)
        self.words = []