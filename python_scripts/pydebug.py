# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution1:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l = ListNode()
        last_node = l

        val1 = l1.val
        val2 = l2.val

        rip = 0
        while True:
            v = val1 + val2 + rip
            last_node.val = v % 10
            if v >= 10:
                rip = 1
            else:
                rip = 0

            if l1.next is None and l2.next is None:
                if rip == 0:
                    break
                else:
                    val1 = 0
                    val2 = 0
            elif l1.next is None:
                val1 = 0
                l2 = l2.next
                val2 = l2.val
            elif l2.next is None:
                l1 = l1.next
                val1 = l1.val
                val2 = 0
            else:
                l1 = l1.next
                l2 = l2.next
                val1 = l1.val
                val2 = l2.val

            last_node.next = ListNode()
            last_node = last_node.next

        return l

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = 0
        b = 0
        
        i = 1
        flag1 = True; flag2 = True
        while True:
            a += l1.val * i
            i *= 10

            if l1.next is None:
                break
            else:
                l1 = l1.next
        
        i = 1
        while True:
            b += l2.val * i
            i *= 10

            if l2.next is None:
                break
            else:
                l2 = l2.next
        
        c = a + b
        i = 10
        l = ListNode(val=(c % i))

        jj = str(c)[::-1]
        last_node = l
        for i in range(1, len(jj)):
            last_node.next = ListNode(int(jj[i]))
            last_node = last_node.next

        return l

def main():
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))

    l3 = Solution1.addTwoNumbers(None, l1, l2)
    node = l3
    while node.next is not None:
        print(f'Valore letto:{node.val}')
        node = node.next

    print('Di prova')

if __name__ == '__main__':
    main()