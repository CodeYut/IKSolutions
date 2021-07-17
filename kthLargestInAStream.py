import heapq
def kth_largest(k, initial_stream, append_stream):
    # Write your code here
    heap = []
    result = []
    
    for i in initial_stream:
        if len(heap) < k:
            heapq.heappush(heap, i)
        else:
            if i > heap[0]:
                heapq.heappushpop(heap, i)
            
    for i in append_stream:
        if len(heap) < k:
            heapq.heappush(heap, i)
        else:
            if i > heap[0]:
                heapq.heappushpop(heap, i)
        result.append(heap[0])
        
    return result
