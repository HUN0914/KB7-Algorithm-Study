#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int countWork(int time, vector<int>& cores) {
    int cnt = cores.size(); 

    for (int c : cores) {
        cnt += time/c;
    }

    return cnt;
}

int solution(int n, vector<int> cores) {
    int coreCount = cores.size();

    if (n <= coreCount) {
        return n;
    }

    long long left = 0;
    long long right = 10000LL * n;
    long long time = 0;

    while (left <= right) {
        long long mid = (left + right) / 2;

        if (countWork(mid, cores) >= n) {
            time = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }

    long long done = countWork(time - 1, cores);

    for (int i = 0; i < coreCount; i++) {
        if (time % cores[i] == 0) {
            done++;

            if (done == n) {
                return i + 1; 
            }
        }
    }

    return -1;
}
