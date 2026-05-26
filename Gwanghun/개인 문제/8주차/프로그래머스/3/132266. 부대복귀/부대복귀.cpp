#include <string>
#include <vector>
#include <queue>

using namespace std;

/*
sources : 각 부대원들이 위치한 서로 다른 지역 
destination : 도착해야할 곳
n: 총 지역의 수 (강철부대가 이거보다 이하의 값 가짐)
*/

vector<pair<int,int>> adj[100001];
int dist[100001];

void dijkstra(int n, vector<vector<int>> roads, int destination){
    
    for(int i=1; i<=n; i++) dist[i]=1e9;
    
    for(int i=0; i<roads.size(); i++){
        int u=roads[i][0];
        int v=roads[i][1];
        
        adj[u].push_back({1,v});
        adj[v].push_back({1,u});
    }
    
    dist[destination]=0;
    
    priority_queue<pair<int,int>,vector<pair<int,int>>, greater<pair<int,int>>> pq;
    
    pq.push({0,destination});
    
    while(!pq.empty()){
        
        auto cur=pq.top();
        pq.pop();
        
        int curCost=cur.first;
        int curNode=cur.second;
        
        if(dist[curNode]!=curCost) continue;
        
        for(auto val : adj[curNode]){
            
            int curCost=val.first;
            int curDist=val.second;
            
            if(dist[curDist]<=curCost+dist[curNode]) continue;
            dist[curDist]=curCost+dist[curNode];
            
            pq.push({dist[curDist],curDist});
        }
    }
}

vector<int> solution(int n, vector<vector<int>> roads, vector<int> sources, int destination) {
    vector<int> result;
    dijkstra(n,roads, destination);
    
    for(auto val : sources){
        if(dist[val]==1e9) result.push_back(-1);
        else result.push_back(dist[val]);
    }
    
    return result;
}
