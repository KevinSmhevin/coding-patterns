# Tries or Prefix Trees

Tries or prefix trees, are tree like data structures that efficiently store strings that take advantage of shared prefixes.

![trie example](/images/trie_one.png)
pic example from GeeksforGeeks

### Tries/prefix trees core properties and methods: 
    - property: `root node` that is a Trienode(explained below)
    - method: `add` that adds strings to the trie 
    - method: `search`  that searchs if a string is in the Trie

### Trienodes are the nodes in Tries and have the follow properties:
    - a children hash map or array to store references to its child nodes.
        - for example in the image above the root node would have the following children object below:
        - `children = {a: TrieNode_A, d: TrieNode_D}`
        - hashmaps are typically used to store the children Trienodes, but an array of size 26 can also be used
    - an end of word indicator typically a boolean or a string
        - a boolean attribute is to confirm if the node is the end of the word
        - a string variable representing the word itself that is stored in the node. (if we want to return the specific word).
        - in the example above `dad`, `and` and `ant` are all words and would have an end of word indicator set to `true`
    
    a prefix can be part of a trie, for example above we can set `an` to be an end of word and set an end of word indicator set to `true`

### Trie example

    ```python

    class TrieNode:
        def __init__(self):
            self.children = {} # hash map of children nodes -> key = character, value = TrieNode 
            self.is_end_of_word = False # end of word indicator

    
    class Trie:
        def __init__(self):
            self.root = TrieNode() # root Trie node with references to all children nodes

        def add(self, word):
            current_node = self.root

            for char in word:
                # check if char is not in children --> create it if so
                if char not in current_node.children:
                    current_node.children[char] = TrieNode()
                
                # move down the trie tree
                current_node = current_node.children[char]
            
            # set end of word indicator
            current_node.is_end_of_word = True
        
        def search(self, word):
            current_nodew = self.root

            for char in word:

                if char not in current_node.children:
                    return False
                
                current_node = current_node.children[char]
            
            return current_node.is_end_of_word



    ```


    



