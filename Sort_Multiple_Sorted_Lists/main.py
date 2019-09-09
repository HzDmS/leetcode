import heapq


def sort(lists, k=300):
    n = len(lists)
    ans = []
    heap = [(lists[i][0], i) for i in range(n)]
    idx = {i: 1 for i in range(n)}
    heapq.heapify(heap)
    for _ in range(k):
        val, i = heapq.heappop(heap)
        ans.append(val)
        heapq.heappush(heap, (lists[i][idx[i]], i))
        idx[i] += 1
    
    return ans


if __name__ == "__main__":

    ans = sort([[1, 4, 7, 9], [2, 5, 6, 7], [1, 3, 4, 7], [5, 7, 8, 9]], k=10)
    print(ans)
