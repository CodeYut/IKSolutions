import heapq
def kth_largest_in_an_array(numbers, k):
    heap = numbers[:k]
    heapq.heapify(heap)
    
    for i in range(k, len(numbers)):
        if heap[0] < numbers[i]:
            heapq.heappushpop(heap, numbers[i])
    return heap[0]
