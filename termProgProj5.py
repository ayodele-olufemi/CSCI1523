def reverse1(lyst):
    """Returns the reversed list. It reverses a copy of the list by splicing it in reverse order. 
    Time complexity: O(n), but more space since it creates a copy. """
    return lyst[::-1]

def reverse2(lyst):
    """Returns the reversed list. It reverses by swapping the items in-place. 
    Time complexity: O(n) and Space complexity O(1) since no auxilliary space are involved. """
    for a in range(round(len(lyst)/2)):
        lyst[a], lyst[len(lyst)-1-a] = lyst[len(lyst)-1-a], lyst[a]
    return lyst

lyst = [1,2,3,4,5,6,7,8,9]
print(reverse1(lyst))
print(lyst)


lyst = [1,2,3,4,5,6,7,8,9]
print(reverse2(lyst))
print(lyst)
