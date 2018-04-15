class Node:
	def __init__ (self,symbol=None,freq=0,left=None,right=None):
		self.freq=freq
		self.symbol=symbol
		self.left=left
		self.right=right

class BinaryMinHeap:

    def __init__(self, heap=None):
        if heap is None:
            heap = []
        self.heap = heap
        self.len = len(heap)
        if heap is not None:
            self.buildHeap()


    @staticmethod
    def left(i):
        return i*2 + 1

    @staticmethod
    def right(i):
        return i*2 + 2

    @staticmethod
    def parent(i):
        if i == 0:
            return -1
        return (i-1) // 2

    def insert(self, k):
        self.heap.append(k)
        i = self.len
        self.len += 1
        while i > 0:
            p = BinaryMinHeap.parent(i)
            if self.heap[i].freq < self.heap[p].freq:
                self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
                i = p
            else:
                break

    def heapify(self, i):
        left = BinaryMinHeap.left(i)
        right = BinaryMinHeap.right(i)
        if left < self.len and self.heap[i].freq >= self.heap[left].freq:
            if right < self.len and self.heap[left].freq <= self.heap[right].freq:
                self.heap[i], self.heap[left] = self.heap[left], self.heap[i]
                i = left
            elif right < self.len:
                self.heap[i], self.heap[right] = self.heap[right], self.heap[i]
                i = right
            else:
                self.heap[i], self.heap[left] = self.heap[left], self.heap[i]
                i = left
            self.heapify(i)
        elif right < self.len and self.heap[i].freq >= self.heap[right].freq:
            self.heap[i], self.heap[right] = self.heap[right], self.heap[i]
            i = right
            self.heapify(i)

    def minimum(self):
        if self.len == 0:
            return None
        return self.heap[0]

    def extractMin(self):
        val = self.heap[0]
        self.len -= 1
        if self.len > 1:
            self.heap[0] = self.heap.pop(self.len)
            self.heapify(0)
        else:
            self.heap.pop(0)
        return val

    def buildHeap(self):
        for i in range(BinaryMinHeap.parent(self.len - 1), -1, -1):
            self.heapify(i)

    def updateHeap(self, i):
        while i > 0:
            p = BinaryMinHeap.parent(i)
            if self.heap[i].freq < self.heap[p].freq:
                self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
                i = p
            else:
                break

    def __str__(self):
        s = ""
        for i in self.heap:
            s += str(i) + " "
        return s

def huffman(symbList,freqList):
	n = len(symbList)
	symbNodes = []
	for i in range(n):
		symbNodes.append(Node(symbList[i],freqList[i]))
	H=BinaryMinHeap(symbNodes)
	for i in range(n-1):
		min1=H.extractMin()
		min2=H.extractMin()
		parent=Node(None,min1.freq+min2.freq,min2,min1)
		H.insert(parent)
	return parent

def traverseHuffTree(root,codeArr):
	if root.symbol is not None :
		print(root.symbol,"".join(codeArr))
		return
	else :
		codeArr.append("0")
		traverseHuffTree(root.left,codeArr)
		codeArr.pop()
		codeArr.append("1")
		traverseHuffTree(root.right,codeArr)
		codeArr.pop()

n=int(input("Enter no. of symbols"))
symbList=[]
freqList=[]
for i in range(n):
	inp=str(input()).split()
	symbList.append(inp[0])
	freqList.append(int(inp[1]))
codeArr=[]
traverseHuffTree(huffman(symbList,freqList),codeArr)