from heapq import *
def online_median(stream):
    result = []
    minHeap = []
    maxHeap = []
    
    for n in stream:
        if len(minHeap) == len(maxHeap):
            heappush(minHeap, -heappushpop(maxHeap, -n))
            result.append(minHeap[0])
            
        else:
            heappush(maxHeap, -heappushpop(minHeap, n))
            result.append((minHeap[0] - maxHeap[0])//2)
            
    return result
