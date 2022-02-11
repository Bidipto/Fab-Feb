# we need to first travel m nodes and then remove n node
# for example in the linked list 1 2 3 4 5 6, notice if m is 1 we go to 2, therefore 2 is not removed

def skipMdeleteN(self, head, m, n):
        dummy = Node(0)
        dummy.next = head
        while head:
            #print(head.data, end=" ")
            # using m-1 cause it removes the last node
            M = m - 1
            N = n
            while M and head:
                head = head.next
                M -= 1
            if not head:
                return dummy.next
            ptr = head
            #print(ptr.data)
            while N and head:
                head = head.next
                N -= 1
            if not head:
                ptr.next = None
                return dummy.next
            ptr.next = head.next
            head = head.next