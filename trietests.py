import unittest

class Node:
    
    def __init__(self, value):
        self.value = value
        self.children = {}

    def insert(self, s, idx):
        if idx != len(s):
            if s[idx] not in self.children:
                self.children[s[idx]] = Node(s[idx])
            self.children.get(s[idx]).insert(s, idx + 1)

    def query(self, s, idx):
        if idx == len(s):
            return True
        elif s[idx] not in self.children:
            return False
        else:
            return self.children.get(s[idx]).query(s, idx + 1)
    

def trie_tests(trie_words, test_words):
    trie = Node('$')
    is_in_arr = []
    for word in trie_words:
        trie.insert(word, 0)
    
    for word_x in test_words:
        is_in_arr.append(trie.query(word_x, 0))
    return is_in_arr

class TrieUnitTests(unittest.TestCase):

    def setUp(self):
        self.trie_list = ["austin", "lizzy", "test", "word"]
        self.test_word = ["liz", "w", "aus", "text"]
        self.exp_output = [True, True, True, False]
        

    def test_empty_input(self):
        result = trie_tests('', '')
        self.assertEqual(result, [])

    def test_valid_input(self):
        result = trie_tests(self.trie_list, self.test_word)
        self.assertEqual(result, self.exp_output)


# if __name__ == '__main__':
#     unittest.main()

trie = ["austin", "lizzy", "test", "word"]
test_word = ["liz", "w", "aus", "text"]
exp_output = [True, True, True, False]
# print(trie_tests(trie, test_word))



    
        