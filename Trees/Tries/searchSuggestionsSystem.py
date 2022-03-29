class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.suggestions = []

        root = TrieNode()
        products.sort() #onlogn
        #build the trie
        for product in products:
            curr = root
            for c in product:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
                if len(curr.suggestions) < 3:
                    curr.suggestions.append(product)
        res = []            
        for char in searchWord:
            root = root.children.get(char, TrieNode())
            res.append(root.suggestions)
        return res    
                    
        