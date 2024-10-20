from doubly_linked_list import DoublyLinkedList


test_list = DoublyLinkedList()
test_list.add_to_head(9)
test_list.remove_tail()
test_list.add_to_tail(8)
test_list.add_to_tail(2)
test_list.remove_head()
test_list.add_to_tail(4)
test_list.remove_by_value(9)
test_list.remove_head()
print(test_list.head_node.get_value())
