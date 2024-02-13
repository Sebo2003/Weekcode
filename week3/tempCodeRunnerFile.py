#print my list of linked lists
print("final:", end=" ")
print("[", end=" ")
for sublist in finalh:
    current = sublist
    print("[", end=" ")
    while current:
        print(current.val, end=", ")
        current = current.next
    print("\b\b]", end=" ")
print("]", end=" ")