public long[] getRelativeRatings(int[] skill, int[] rating, int k) {
  // write your code here
  int N = skill.length;
        int[][] arr = new int[N][3];
        for(int i = 0; i < N; i++){
            arr[i][0] = skill[i];
            arr[i][1] = rating[i];
            arr[i][2] = i;
        }

        Arrays.sort(arr, (o1, o2) -> o1[0]-o2[0]);
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>((a, b)->b-a);
        int curSum = 0;
        long[] ans = new long[N];
        for(int i = 0; i < k; i++){
            ans[i] = curSum;
            pq.add(arr[i][1]);
            curSum+=arr[i][1];
        }

        for(int i = k; i < N; i++){
            ans[i] = curSum;
            pq.add(arr[i][1]);
            curSum = curSum + arr[i][1] - pq.poll();
        }

        long[] result = new long[N];
        for(int i = 0; i < N; i++) {
            result[arr[i][2]] = ans[i];
        }

        return result;
}