# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        Solution.solnHelper(head, None, None, None, True)
        return head
        
    
    @staticmethod
    def solnHelper(head, lastOdd, firstEven, lastEven, isHeadOdd):

        if (head == None):
            if (not isHeadOdd):
                lastEven.next = None
                
            return

        elif (lastOdd == None):
            # first swap

            nextOne = head.next # firstEven and lastEven

            # error check on 2nd element
            if (not nextOne):
                return
            else:
                # error check on 3rd element
                nextTwo = nextOne.next # lastOdd

                if (not nextTwo):
                    return
                else:
                    nextThree = nextTwo.next

                    # change order
                    head.next = nextTwo
                    nextTwo.next = nextOne

                    Solution.solnHelper(nextThree, nextTwo, nextOne, nextOne, False)

        else:
            if (isHeadOdd):
                nextOne = head.next

                # change order
                lastOdd.next = head
                head.next = firstEven

                Solution.solnHelper(nextOne, head, firstEven, lastEven, False)

            else:
                lastEven.next = head

                Solution.solnHelper(head.next, lastOdd, firstEven, head, True)




soln = Solution();
