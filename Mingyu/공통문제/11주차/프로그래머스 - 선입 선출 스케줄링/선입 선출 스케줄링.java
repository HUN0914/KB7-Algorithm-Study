class Solution {
    public int solution(int n, int[] cores) {
        int coreCnt = cores.length;
        
        // if num of tasks less than num of cores 
        if (n <= coreCnt) return n;

        int left = 0;

        // slowest core's time
        int maxCoreTime = 0;
        for (int core : cores) {
            maxCoreTime = Math.max(maxCoreTime, core);
        }

        // if slowest core takes all tasks
        int right = maxCoreTime * n;
        int ansTime = 0;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;

            long cnt = getWorkCnt(mid, cores);

            if (cnt >= n) {
                // can we assign tasks faster?
                ansTime = mid;
                right = mid - 1;
            } else {
                // need more time
                left = mid + 1;
            }
        }

        // number of tasks assigned just before ansTime
        long beforeCnt = getWorkCnt(ansTime - 1, cores);

        for (int i = 0; i < coreCnt; i++) {
            if (ansTime % cores[i] == 0) {
                beforeCnt++;

                if (beforeCnt == n) return i + 1;
            }
        }

        return -1;
    }

    private long getWorkCnt(int time, int[] cores) {
        long cnt = 0;
        for (int core : cores) {
            cnt += time / core + 1;
        }

        return cnt;
    }
}