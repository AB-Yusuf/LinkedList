#class Node:

#    def __init__(self, value):
#        self.info = value
#        self.link = None

#class SingleLinkedList:

#    def __init__(self):
#        self.startingNode = None

#    def display_list(self):
#        if self.startingnode is none:
#            print("list is empty")
#            return
#        else:
#            print("List is: ")
#            p = 0
#            p = self.startstartingNode
#            while p is not None:
#                print(p.info, " ", end='')
#                p = p.link
#            print()

#    def count_nodes(self):
#        p = self.startingNode
#        n = 0
#        while p is not None:
#            n+=1
#            p = p.link
#        print("Number of nodes in the list = ", n)
    
#    def search(self, x):
#        position = 1
#        p = self.startingNode
#        while p is not None:
#            if p.info == x:
#                print(x, "is at position", position)
#                return True
#            position+=1
#            p = p.link
#        else: 
#            print(x, "not found in list")
#            return false

#    def insert_in_beginning(self, data):
#        pass

#    def insert_at_end(self, data):
#        pass

#    def create_list(self):
#        pass

#    def insert_after(self, data, x):
#        pass

#    def insert_before(self, data, x):
#        pass

#    def insert_at_position(self, data, k):
#        pass

#    def delete_node(self, x):
#        pass

#    def delete_first_node(self):
#        pass

#    def delete_last_node(self):
#        pass

#    def reverse_list(self):
#        pass

#    def bubble_sort_exdata(self):
#        pass

#    def bubble_sort_exLinks(self):
#        pass

#    def has_cycle(self):
#        pass

#    def find_cycle(self):
#        pass

#    def remove_cycle(self):
#        pass
     
#    def insert_cycle(self, x):
#        pass

#    def merge2(self, list2):
#        pass

#    def _merge2(self, p1, p2):
#        pass

#    def merge_sort(self):
#        pass

#    def _merge_sort_rec(self, listStart):
#        pass

#    def _divide_list(self, p):
#        pass


#list = SingleLinkedList()

#list.create_list()

#while True:
#    print("1. Display List")
#    print("2. Count the number of nodes")
#    print("3. Search for an element")
#    print("4. Insert in empty List/Insert in beginning of the list")
#    print("5. Insert a node at the end of the list")
#    print("6. Insert a node after a specified node")
#    print("7. Insert a node before a specified node")
#    print("8. Insert a node at a given position")
#    print("9. Delete first node")
#    print("10. Delete last node")
#    print("11. Delete any node")
#    print("12. Reverse the list")
#    print("13. Bubble sort by exchanging data")
#    print("14. Bubble sort by exchanging links")
#    print("15. MergeSort")
#    print("16. Insert Cycle")
#    print("17. Detect Cycle")
#    print("18. Remove Cycle")
#    print("19. Quit")

#    option = int(input("Enter your choice : "))

#    if option == 1:
#        list.display_list()
#    elif option == 2:
#        list.count_nodes()
#    elif option == 3:
#        data = int(input("Enter the element to be searched :"))
#    elif option == 4:
#        data = int(input("Enter the element to be inserted: "))
#        list.insert_in_beginning(data)
#    elif option == 5:
#        data = int(input("Enter the element to be inserted at the end: "))
#        list.insert_at_end(data)
#    elif option == 6:
#        data = int(input("Enter the element to be inserted"))
#        x = int(input("Enter the element after which to insert: "))
#        list.insert_after(data, x)
#    elif option == 7:
#        data = int(input("Enter the element to be inserted : "))
#        x = int(input("Enter the element before which to insert : "))
#        list.insert_before(data, x)
#    elif option == 8:
#        data = int(input("Enter the element to be inserted: "))
#        k = int(input("Enter the position at which to insert: "))
#    elif option == 9:
#        list.delete_first_node()
#    elif option == 10:
#        list.delete_last_node()
#    elif option == 11:
#        data = int(input("Enter the element to be deleted :"))
#        list.delete_node(data)
#    elif option == 12:
#        list.reverse_list()
#    elif option == 13:
#        list.bubble_sort_exdata()
#    elif option == 15:
#        list.merge_sort()
#    elif option == 16:
#        data = int(input("Enter the element at which the cycle has to be inserted: "))
#        list.insert_cycle(data)
#    elif option == 17:
#        if list.has_cycle():
#            print("List has a cycle")
#        else:
#            print("List does not have a cycle")
#    elif option == 18:
#        list.remove_cycle()
#    elif option == 19:
#        break
#    else:
#        print("Wrong option")
#    print()

class SomeClass:
    variable_1 = "This is a class variable"
    variable_2 = 100 #This is also a class variable

    def __init__(self, param1, param2):
        self.instance_var1 = param1
        #instance_var1 is a instance variable
        self.instance_var2 = param2
        #instance_var2 is a instance variable

obj1 = SomeClass("some thing", 18)
obj2 = SomeClass(28, 6)

print(obj1.variable_1)
print(obj2.variable_1)


















































    






