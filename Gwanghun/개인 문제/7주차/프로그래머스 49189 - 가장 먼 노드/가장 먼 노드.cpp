#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int cal(int n, vector<vector<int>> edge) {
    
    int ans=0;

    vector<vector<int>> near(n+1);
    
    for(int i=0; i<edge.size(); i++){
        int fir=edge[i][0];
        int sec=edge[i][1];
        
        near[fir].push_back(sec);
        near[sec].push_back(fir);
    }
    
    vector<int> dist(n+1,-1);
    
    dist[1]=0;
    queue<int> q;
    q.push(1);
    
    while(!q.empty()){
        int cur=q.front();
        q.pop();
        
        for(int i=0; i<near[cur].size(); i++){
            if(dist[near[cur][i]]!= -1) continue;
            
            dist[near[cur][i]]=dist[cur]+1;
            
            q.push(near[cur][i]);            
        }
    }
    
    sort(dist.begin(),dist.end());
    
    for(int i=0; i<dist.size(); i++){
        if(dist[i]==dist.back()) ans++;
    }
    
    return ans;
}

int solution(int n, vector<vector<int>> edge) {
    int answer = cal(n,edge);
    return answer;
}