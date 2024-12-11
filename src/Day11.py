

class LinkedList:
    def __init__(this, value, next = None):
        this.value = value
        this.next = next


def init_stones(filepath):
    with open(filepath) as file:
        stones = file.read().rstrip().split(" ")
    
    head = None
    for stone in stones[::-1]:
        head = LinkedList(stone, head)

    return head


def perform_zero_rule(node):
    if node.value == "0":
        node.value = "1"
        return True
    return False


def perform_spliting_rule(node):
    if len(node.value) % 2 != 0:
        return False
    
    lhs = node.value[:int(len(node.value) / 2)]
    rhs = node.value[int(len(node.value) / 2):]

    node.value = lhs
    node.next = LinkedList(str(int(rhs)), node.next)

    return True


def perform_basic_turn(head):
    while head:
        are_rules_performed = perform_zero_rule(head) 
        
        if not are_rules_performed and perform_spliting_rule(head):
            are_rules_performed = True
            head = head.next

        if not are_rules_performed:
            head.value = str(int(head.value) * 2024)
        
        head = head.next


def star_one(filepath):
    head_stone = init_stones(filepath)

    for _ in range(25):
        perform_basic_turn(head_stone)

    number_of_stones = 1
    while head_stone.next:
        number_of_stones += 1
        head_stone = head_stone.next
    
    return number_of_stones

def star_two(filepath):
    pass


if __name__=="__main__":
    print(star_one("inputs/Day11.txt"))
    print(star_two("inputs/Day11.txt")) 
