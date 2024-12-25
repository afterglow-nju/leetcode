import heapq
class Solution:
  def getMaxSumArr(self, item_weights: List[int]) -> int:
    
    
    n = len(item_weights) // 3
    first_sum = [-float('inf')] * len(item_weights)
    curr_sum = 0
    heap = []
    for i in range(n):
      curr_sum += item_weights[i]
      heapq.heappush(heap, item_weights[i])

    first_sum[n-1] = curr_sum
    for i in range(n, len(item_weights)):
      heapq.heappush(heap, item_weights[i])
      curr_sum += item_weights[i]
      node = heapq.heappop(heap)
      curr_sum -= node
      first_sum[i] = curr_sum


    second_sum = [float('inf')] * len(item_weights)
    curr_sum = 0
    heap = []
    for i in range(len(item_weights) - 1, len(item_weights) - n - 1, -1):
      curr_sum += item_weights[i]
      heapq.heappush(heap, -item_weights[i])

    second_sum[len(item_weights) - n] = curr_sum
    for i in range(len(item_weights) - n - 1, -1, -1):
      heapq.heappush(heap, -item_weights[i])
      curr_sum += item_weights[i]
      node = heapq.heappop(heap)
      curr_sum += node
      second_sum[i] = curr_sum
    # print(first_sum)
    # print(second_sum)
    ans = 0
    for i in range(len(item_weights)-1):
      ans = max(ans, first_sum[i] - second_sum[i + 1])

    return ans

    
      
    
    public int getMaxSumArr(int[] item_weights) {
  int x = n / 3;
    int midStart = x;
    int midEnd = 2 * x - 1;
    PriorityQueue<Integer> leftMinQ = new PriorityQueue<>();
    PriorityQueue<Integer> rightMaxQ = new PriorityQueue<>(new Comparator<Integer>() {
      @Override
      public int compare(Integer o1, Integer o2) {
        return o2 - o1;
      }
    });
    for(int i = 0; i <= midStart - 1; i++) {
      leftMinQ.offer(item_weights[i]);
    }
    for(int i = midEnd + 1; i < item_weights.length; i++) {
      rightMaxQ.offer(item_weights[i]);
    }

    for(int i = 0; i < x; i++) {
      boolean leftCompare = leftMinQ.peek() > item_weights[midStart];
      boolean rightCompare = rightMaxQ.peek() < item_weights[midEnd];
      if(leftCompare && rightCompare) {
        if(item_weights[midStart] < item_weights[midEnd]) {
          midStart++;
        } else {
          midEnd--;
        }
      } else if(!leftCompare && rightCompare) {
        leftMinQ.poll();
        leftMinQ.offer(item_weights[midStart]);
        midStart++;
      } else if(leftCompare && !rightCompare) {
        rightMaxQ.poll();
        rightMaxQ.offer(item_weights[midEnd]);
        midEnd--;
      } else {
        int leftDiff = leftMinQ.peek() - item_weights[midStart];
        int rightDiff = rightMaxQ.peek() - item_weights[midEnd];
        if(leftDiff < rightDiff) {
          rightMaxQ.poll();
          rightMaxQ.offer(item_weights[midEnd]);
          midEnd--;
        } else {
          leftMinQ.poll();
          leftMinQ.offer(item_weights[midStart]);
          midStart++;
        }
      }
    }

    int sum = 0;
    while(!leftMinQ.isEmpty()) {
      sum += leftMinQ.poll();
    }

    while(!rightMaxQ.isEmpty()) {
      sum -= rightMaxQ.poll();
    }

    return sum;
}