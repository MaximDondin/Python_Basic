class Node:
    def __init__(self, val: any = None) -> None:
        self.val = val
        self.next_val = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        
    def __iter__(self) -> iter:
        return self
    
    def __next__(self) -> any:
        if self.head:
            count = self.head.val
            self.head = self.head.next_val
            return count
        else:
            raise StopIteration

    def append(self, new_val: any) -> None:
        new_Node = Node(new_val)
        if self.head is None:
            self.head = new_Node
            return
        last_Node = self.head
        while last_Node.next_val:
            last_Node = last_Node.next_val
        last_Node.next_val = new_Node

    def get(self, index: int) -> any:
        last_Node = self.head
        NodeIndex = 0
        while NodeIndex <= index:
            if NodeIndex == index:
                return last_Node.val
            NodeIndex = NodeIndex + 1
            last_Node = last_Node.next_val

    def remove(self, index: int) -> None:
        head_val = self.head
        count = 0
        if head_val:
            if count == index:
                self.head = head_val.next_val
                head_val = None
                return
        while head_val:
            if count == index:
                break
            last_val = head_val
            head_val = head_val.next_val
            count += 1
        if head_val == None:
            print('Такого элемента нет!')
            return
        last_val.next_val = head_val.next_val
        head_val = None

    def __str__(self) -> str:
        currentval = self.head
        my_str = '['
        while currentval:
            my_str += str(currentval.val) + ' '
            currentval = currentval.next_val
        return my_str[:len(my_str) - 1] + ']'


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.append(50)
my_list.append(60)
my_list.append(70)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)

print('\nУдаление элемента вне границ списка.')
my_list.remove(10)

print('\nИтерация по списку')
for data in my_list:
    print(data, end = ' ')