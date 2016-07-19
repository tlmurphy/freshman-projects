"""
Array Heap Class
"""

from AbstractCollection import AbstractCollection


class ArrayHeap(AbstractCollection):

    def __init__(self, sourceCollection=None):
        self._heap = list()
        AbstractCollection.__init__(self, sourceCollection)

    def add(self, item):
        self._size += 1
        self._heap.append(item)
        curPos = len(self._heap) - 1
        parent = (curPos - 1) // 2
        while curPos > 0 and self._heap[parent] > item:
            self._heap[curPos] = self._heap[parent]
            curPos = parent
            parent = (curPos - 1) // 2
        self._heap[curPos] = item

    def pop(self):
        if self.isEmpty():
            raise Exception("Heap is empty")
        self._size -= 1
        topItem = self._heap[0]
        bottomItem = self._heap.pop(len(self._heap) - 1)
        if len(self._heap) == 0:
            return bottomItem

        self._heap[0] = bottomItem
        lastIndex = len(self._heap) - 1
        curPos = 0
        while True:
            leftChild = 2 * curPos + 1
            rightChild = 2 * curPos + 2
            if leftChild > lastIndex:
                break
            if rightChild > lastIndex:
                minChild = leftChild
            else:
                leftItem = self._heap[leftChild]
                rightItem = self._heap[rightChild]
                if leftItem < rightItem:
                    minChild = leftChild
                else:
                    minChild = leftChild
            minItem = self._heap[minChild]
            if bottomItem <= minItem:
                break
            else:
                self._heap[curPos] = self._heap[minChild]
                self._heap[minChild] = bottomItem
                curPos = minChild
        return topItem

    def __str__(self):
        """Returns a string representation with the heap rotated
        90 degrees couterclockwise."""

        def recurse():
            pass