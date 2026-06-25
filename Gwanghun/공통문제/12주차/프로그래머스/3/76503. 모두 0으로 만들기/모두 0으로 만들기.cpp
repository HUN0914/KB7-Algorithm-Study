#include <string>
#include <vector>

using namespace std;

vector<vector<int>> graph(300001);

bool isVisited[300001];
long long result=0;
long long total=0;

void init(vector<vector<int>> edges){
    
    for(int i=0; i<edges.size(); i++){
        int fir=edges[i][0];
        int sec=edges[i][1];
                
        graph[fir].push_back(sec);
        graph[sec].push_back(fir);
    }    
}

long long dfs(vector<int>& a, int curVal) {
    
    isVisited[curVal]=true;
    
    long long sum=a[curVal];
    
    for(int i=0; i<graph[curVal].size(); i++){
        int val=graph[curVal][i];
        
        if(isVisited[val]) continue;
        
        long long child = dfs(a, val);
        
        result+=abs(child);
        sum+=child;
        
    }
    
    return sum;
}

long long solution(vector<int> a, vector<vector<int>> edges) {
    
    bool isZero=true;
    long long v=0;
    
    for(auto val : a){
        if(val!=0) isZero=false;
        v+=val;
    }
    if(isZero) return 0;
    if(v!=0) return -1;
    
    init(edges);
    
    dfs(a,0); 
    
    return result;
}
