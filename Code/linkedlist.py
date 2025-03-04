#!python

class Node(object):
    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return f'Node({self.data})'


class LinkedList:
    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        if items is not None:
            for item in items:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list."""
        ll_str = ""
        for item in self.items():
            ll_str += f'({item}) -> '
        return ll_str

    def items(self):
        """Return a list of all items in this linked list."""
        items = []
        node = self.head
        while node is not None:
            items.append(node.data)
            node = node.next
        return items

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes."""
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next
        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list."""
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list."""
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def search(self, matcher):
        """Return an item from this linked list if it is present.

        Now supports both functions and direct value lookup.
        """
        node = self.head
        while node is not None:
            if callable(matcher):  # If matcher is a function, call it
                if matcher(node.data):
                    return node.data
            elif node.data == matcher:  # If matcher is a string, compare directly
                return node.data
            node = node.next
        return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError."""
        if self.is_empty():
            raise ValueError('Item not found: {}'.format(item))

        if self.head.data == item:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return

        node = self.head
        while node.next is not None:
            if node.next.data == item:
                node.next = node.next.next
                if node.next is None:
                    self.tail = node
                return
            node = node.next

        raise ValueError('Item not found: {}'.format(item))

    def replace(self, old_item, new_item):
        """Replace the old_item with new_item in the linked list."""
        node = self.head
        while node is not None:
            if node.data == old_item:
                node.data = new_item
                return
            node = node.next
        raise ValueError('Item not found: {}'.format(old_item))

def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))
    
    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    print('\nTesting search:')
    print('Search "B":', ll.search("B"))  # Should return "B"
    print('Search with lambda (x=="C"):', ll.search(lambda x: x == "C"))  # Should return "C"
    print('Search "X" (not in list):', ll.search("X"))  # Should return None

    print('\nTesting delete:')
    for item in ['B', 'C', 'A']:
        print('delete({!r})'.format(item))
        ll.delete(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

if __name__ == '__main__':
    test_linked_list()
