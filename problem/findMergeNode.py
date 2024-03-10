class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def findMergeNode(headA,headB):
    # 関数を完成させてください

    merge_node_data = -1

    reverse_headA = reverse(headA)
    reverse_headB = reverse(headB)

    if reverse_headA.data != reverse_headB.data: return merge_node_data

    while reverse_headA.data == reverse_headB.data:
        merge_node_data = reverse_headA.data
        reverse_headA = reverse_headA.next
        reverse_headB = reverse_headB.next
    
    return merge_node_data

# 片方向リストを逆に連結する関数
def reverse(head):
    reverse = head
    current_node = head.next
    while current_node is not None:
        temp = current_node
        current_node = current_node.next
        temp.next = reverse
        reverse = temp
    head = reverse
    return head