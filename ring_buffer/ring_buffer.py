from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # check if list exists
        if len(self.storage) == 0:
            # add item to list and set to current
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
        # check if list is full
        elif len(self.storage) == self.capacity:
            # check if oldest node is tail
            if self.current == self.storage.tail:
                self.storage.remove_from_tail()
                self.storage.add_to_tail(item)
                self.current = self.storage.head
                return
            # remove oldest node and add new node at tail
            # update current node to second oldest node
            oldestNode = self.current
            self.current = self.current.next
            self.storage.delete(oldestNode)
            self.storage.add_to_tail(item)
            # set addedNode to self.storage.tail
            addedNode = self.storage.tail
            # move current node to current.next
            self.current = self.current.next
            # while current node != addedNode:
            # move current.prev to tail
            while self.current.prev is not addedNode:
                self.storage.move_to_end(self.current.prev)
                self.current = self.current.next
        else:
            self.storage.add_to_tail(item)

    def get(self):
        list_buffer_contents = []
        gotNode = self.storage.head
        while True:
            list_buffer_contents.append(gotNode.value)
            if gotNode.next == None:
              break
            gotNode = gotNode.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0
        self.current = 0
        self.storage = [0] * capacity

    def append(self, item):
        if self.capacity == len(self.storage):
          self.storage[self.current] = item
          if self.current == self.capacity - 1:
            self.current = 0
          else:
            self.current += 1
        else:
          self.storage.append(item)
          self.length += 1

    def get(self):
        return [x for x in self.storage if not x == 0 and self.length < self.capacity]
