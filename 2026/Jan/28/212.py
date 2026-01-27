class TrieNode:
    def __init__(self):
        self.children={}
        self.word=False

class Solution:
    def __init__(self):
        self.root=TrieNode()

    def addWord(self,word):
        curr=self.root
        for c in word:
            if c not in curr.children:
                curr.children[c]=TrieNode()
            curr=curr.children[c]
        curr.word=word


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        for w in words:
            self.addWord(w)
        curr=self.root
        res=set()
        seen=set()
        def search(root,i,j,board):
            curr=root
            if curr.word:
                res.add(curr.word)
            if j+1<len(board[0]) and (i,j+1) not in seen and board[i][j+1] in curr.children:
                seen.add((i,j+1))
                search(curr.children[board[i][j+1]],i,j+1,board)
                seen.remove((i,j+1))
            if i+1<len(board) and (i+1,j) not in seen and board[i+1][j] in curr.children:
                seen.add((i+1,j))
                search(curr.children[board[i+1][j]],i+1,j,board)
                seen.remove((i+1,j))
            if j-1>=0 and (i,j-1) not in seen and board[i][j-1] in curr.children:
                seen.add((i,j-1))
                search(curr.children[board[i][j-1]],i,j-1,board)
                seen.remove((i,j-1))
            if i-1>=0 and (i-1,j) not in seen and board[i-1][j] in curr.children:
                seen.add((i-1,j))
                search(curr.children[board[i-1][j]],i-1,j,board)
                seen.remove((i-1,j))
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] in curr.children:
                    seen.add((i,j))
                    search(curr.children[board[i][j]],i,j,board)
                    seen.remove((i,j))
        return list(res)