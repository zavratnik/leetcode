class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Problem211:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.is_end = True

    def search(self, word: str) -> bool:
        def dfs(j: int, node: TrieNode) -> bool:
            if j == len(word):
                return node.is_end

            c = word[j]

            if c == ".":
                for child in node.children.values():
                    if dfs(j + 1, child):
                        return True
                return False
            else:
                if c in node.children:
                    return dfs(j + 1, node.children[c])
                else:
                    return False

        return dfs(0, self.root)


if __name__ == "__main__":
    wd = Problem211()

    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")

    print(wd.search("pad"))  # False
    print(wd.search("bad"))  # True
    print(wd.search(".ad"))  # True
    print(wd.search("b.."))  # True
