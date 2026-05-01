#include <string>
#include <vector>
#include <algorithm>

using namespace std; 

long long binarySearch(int n, vector<int> times){
    
    sort(times.begin(), times.end());
    long long end= (long long)times.back()*(long long)n;
    long long start = 1;
    
    while(start<=end){
        long long mid = (start+end)/2;
        long long sum=0;
        
        for(int i=0; i<times.size(); i++) sum+=(mid/times[i]);
        
        if(sum>=n) end=mid-1;
        else if (sum<n) start=mid+1;
        
    }
    
    return start;
}


long long solution(int n, vector<int> times) {
    long long answer = binarySearch(n,times);
    return answer;
}
