#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int cal(int n, vector<int> weak, vector<int> dist) {
    
    int answer=1e9;
    
    int W=weak.size();
    weak.resize(2*W);
    
    for(int i=W; i<2*W; i++){
        weak[i]= weak[i-W]+n;
    }
    
    sort(dist.begin(),dist.end());
    
    do{
        for(int i=0; i<W; i++){
            int start=weak[i];
            int finish=weak[i+W-1];
            for(int j=0; j<dist.size(); j++){
                start +=dist[j];
                if(start>=finish){
                    answer = min(answer,j+1);
                    break;
                }
                
                int next = upper_bound(weak.begin(), weak.end(), start) - weak.begin();
                start=weak[next];
            }
        }
    }while(next_permutation(dist.begin(), dist.end()));
    
    if(answer==1e9) return -1;
    
    return answer;
    
}

int solution(int n, vector<int> weak, vector<int> dist) {
    int answer = cal(n,weak,dist);;
    return answer;
}
