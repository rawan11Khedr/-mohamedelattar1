import heapq


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq



class Huffman:
    def __init__(self, file):
        self.file = file
        self.freqTable = {}
        self.huffmanCode = {}
        self.encodeText = ''
        self.decodeText = ''

    def GetFreq(self):
        with open(self.file, 'r') as file:
            data = file.read()
        for char in data:
            if char in self.freqTable:
                self.freqTable[char] += 1
            else:
                self.freqTable[char] = 1
        with open('FreqTable.txt', 'w') as file:
            file.write(str(self.freqTable))

    def Tree(self):
        nodes = []
        for char, freq in self.freqTable.items():
            node = Node(char, freq)
            heapq.heappush(nodes, node)
        while len(nodes) > 1:
            node1 = heapq.heappop(nodes)
            node2 = heapq.heappop(nodes)
            merge = Node(None, node1.freq + node2.freq)
            merge.left = node1
            merge.right = node2
            heapq.heappush(nodes, merge)
        return nodes[0]

    def Huffman_code(self, nodes, current):
        if nodes is None:
            return
        if nodes.char is not None:
            self.huffmanCode[nodes.char] = current


        self.Huffman_code(nodes.left, current + "0")
        self.Huffman_code(nodes.right, current + "1")

    def Encode(self):
        with open(self.file, 'r') as file:
            data = file.read()
        for char in data:
            self.encodeText += self.huffmanCode[char]

        with open('EncodeText.txt', 'w') as file:
            file.write(self.encodeText)

    def Decode(self):
        with open('EncodeText.txt', 'r') as file:
            data = file.read()
        reverse_Huffman = {Number: Char for Char, Number in self.huffmanCode.items()}
        current = ''
        for bit in data:
            current += bit
            if current in reverse_Huffman:
                self.decodeText += reverse_Huffman[current]
                current = ''
        with open('DecodeText.txt', 'w') as file:
            file.write(self.decodeText)

    def Link(self):
        self.GetFreq()
        mergedNode = self.Tree()
        self.Huffman_code(mergedNode, '')
        self.Encode()
        self.Decode()


file = input("Enter File Name : ")
huffman = Huffman(file)
huffman.Link()

print("Done :), please check your files ")
