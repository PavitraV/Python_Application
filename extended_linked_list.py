# Written by Pavitra for COMP9021

from linked_list_adt import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L=None):
        super().__init__(L)

    # def getendoflist(self, head):
    #     node = self.head
    #     while (node.next) :
    #         node = node.next
    #     return node

    def rearrange(self, step):
        node = self.head
        while (node.next_node):
            node = node.next_node
        endOfList = node
        node = self.head
        start = Node(-1)
        start.next_node = self.head
        endOfList.next_node = start.next_node
        solution = Node(-2)
        count = 0
        currentNodePointer = start
        lastNodeOfTheSolutionList = solution
        isTheLastNodeOfTheListCrossed = False
        while (True):
            count = 1
            while (count+1 < step):
                if (currentNodePointer.next_node == endOfList):
                    isTheLastNodeOfTheListCrossed = True
                currentNodePointer = currentNodePointer.next_node
                count +=1

            lastNodeOfTheSolutionList.next_node = currentNodePointer.next_node
            lastNodeOfTheSolutionList = lastNodeOfTheSolutionList.next_node
            currentNodePointer.next_node = lastNodeOfTheSolutionList.next_node
            lastNodeOfTheSolutionList.next_node = None

            if (isTheLastNodeOfTheListCrossed):
                isTheLastNodeOfTheListCrossed = False
                step-=1
                if (step <= 1) :
                    lastNodeOfTheSolutionList.next_node = currentNodePointer.next_node
                    break
    # print(solution, endOfList);

        endOfList.next_node = None
        #print(solution.next)

    # def rearrange(self, step):
    #     L1 = self.duplicate()
    #     node = L1.head
    #     length = len(L1)
    #     count2 = 0
    #     count = 0
    #     counter = step
    #     #while node:
    #     #    L1.tail = node
    #     #    node = node.next_node
    #     #node = L1.head
    #     while count <= length:
    #         count1 = 0
    #         while counter <= length:
    #             count += 1
    #             count1 += 1
    #             if(count1 == counter):
    #                 x = L1.value_at(count1-1)
    #                 print(L1.value_at(count2), x)
    #                 self.swap(L1.value_at(count2),x)
    #                 count2+=1
    #                 counter = counter + step
    #             if(not node.next_node):
    #                 node = L1.head
    #             else:
    #                 node = node.next_node
    #
    #         node = L1.head
    #         counter = counter - length
    #     #return self
    #
    # def swap(self, old, new):
    #     node = Node()
    #     node = self.head
    #     temp = Node()
    #     while node:
    #         if(node.value == old):
    #             print('looping')
    #             temp = node
    #             break
    #         node = node.next_node
    #     node = self.head
    #     while node:
    #         if(node.value == new):
    #             temp1 = node
    #             break
    #         node = node.next_node
    #     node = self.head
    #     while(node.next_node):
    #         if(node.next_node.value == new):
    #             node.next_node = node.next_node.next_node
    #             next_node = temp.next_node
    #             temp1.next_node = temp
    #             temp.next_node = next_node
    #             temp1.next_node = temp
    #             #self.head = temp1
    #             break
    #         node = node.next_node
    #     self.print()





