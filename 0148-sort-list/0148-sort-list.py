# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# APPROACH 1: Merge Sort (O(n log n) time, O(1) space) - OPTIMAL
class Solution:
    def sortList(self, head):
        """
        Sorts linked list using merge sort with O(n log n) time and O(1) space.
        This is the optimal solution for the follow-up requirement.
        """
        if not head or not head.next:
            return head
        
        # Split the list into two halves
        mid = self.getMid(head)
        left = head
        right = mid.next
        mid.next = None  # Break the link
        
        # Recursively sort both halves
        left = self.sortList(left)
        right = self.sortList(right)
        
        # Merge the sorted halves
        return self.merge(left, right)
    
    def getMid(self, head):
        """Find middle node using slow and fast pointers."""
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def merge(self, l1, l2):
        """Merge two sorted linked lists."""
        dummy = ListNode(0)
        curr = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        # Attach remaining nodes
        curr.next = l1 if l1 else l2
        
        return dummy.next


# APPROACH 2: Convert to Array (O(n log n) time, O(n) space) - SIMPLER
class SolutionArray:
    def sortList(self, head):
        """
        Simpler approach: convert to array, sort, rebuild list.
        Uses O(n) extra space but easier to understand.
        """
        if not head:
            return None
        
        # Convert linked list to array
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next
        
        # Sort the array
        values.sort()
        
        # Rebuild the linked list
        dummy = ListNode(0)
        curr = dummy
        for val in values:
            curr.next = ListNode(val)
            curr = curr.next
        
        return dummy.next


# Helper functions for testing
def create_linked_list(values):
    """Create a linked list from a list of values."""
    if not values:
        return None
    
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    
    return head

def linked_list_to_array(head):
    """Convert linked list to array for easy visualization."""
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result


# Test examples
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1: [4,2,1,3] -> [1,2,3,4]
    head1 = create_linked_list([4, 2, 1, 3])
    sorted1 = solution.sortList(head1)
    print("Example 1: " + str(linked_list_to_array(sorted1)))  # [1, 2, 3, 4]
    
    # Example 2: [-1,5,3,4,0] -> [-1,0,3,4,5]
    head2 = create_linked_list([-1, 5, 3, 4, 0])
    sorted2 = solution.sortList(head2)
    print("Example 2: " + str(linked_list_to_array(sorted2)))  # [-1, 0, 3, 4, 5]
    
    # Example 3: [] -> []
    head3 = create_linked_list([])
    sorted3 = solution.sortList(head3)
    print("Example 3: " + str(linked_list_to_array(sorted3)))  # []
    
    # Additional test: Single element
    head4 = create_linked_list([1])
    sorted4 = solution.sortList(head4)
    print("Single element: " + str(linked_list_to_array(sorted4)))  # [1]
    
    # Additional test: Already sorted
    head5 = create_linked_list([1, 2, 3, 4, 5])
    sorted5 = solution.sortList(head5)
    print("Already sorted: " + str(linked_list_to_array(sorted5)))  # [1, 2, 3, 4, 5]