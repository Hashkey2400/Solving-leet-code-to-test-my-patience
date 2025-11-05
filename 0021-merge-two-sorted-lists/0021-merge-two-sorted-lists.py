# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        """
        Merge two sorted linked lists into one sorted list.
        
        Args:
            list1: Head of first sorted linked list
            list2: Head of second sorted linked list
            
        Returns:
            Head of merged sorted linked list
        """
        # Create a dummy node to simplify edge cases
        dummy = ListNode(0)
        current = dummy
        
        # Traverse both lists and merge
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Attach remaining nodes (if any)
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        
        # Return the head of merged list (skip dummy node)
        return dummy.next


# Helper function to create a linked list from a Python list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Helper function to convert linked list to Python list for display
def linked_list_to_array(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    merged = solution.mergeTwoLists(list1, list2)
    print("Example 1:", linked_list_to_array(merged))
    
    # Example 2
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    merged = solution.mergeTwoLists(list1, list2)
    print("Example 2:", linked_list_to_array(merged))
    
    # Example 3
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    merged = solution.mergeTwoLists(list1, list2)
    print("Example 3:", linked_list_to_array(merged))
    
    # Additional test case
    list1 = create_linked_list([1, 3, 5, 7])
    list2 = create_linked_list([2, 4, 6, 8])
    merged = solution.mergeTwoLists(list1, list2)
    print("Additional:", linked_list_to_array(merged))