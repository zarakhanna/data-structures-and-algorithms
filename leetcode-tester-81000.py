 a = headA
        b = headB
        while a != None:
            while b != None:
                if b == a:
                    return a
                b = b.next
            a = a.next
            b = headB
        return None
        # hold curr node in A,
        #   check every 