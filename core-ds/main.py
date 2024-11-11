from singlylinkedlist import LinkedList

linkedList = LinkedList()
print("Head:", linkedList.head)
print("Tail:", linkedList.tail)
print("Length:", linkedList.length())
print()

linkedList.append(1)
linkedList.append(2)
linkedList.append(3)
print("Head:", linkedList.head.value)
print("Tail:", linkedList.tail.value)
print("Length:", linkedList.length())
print()