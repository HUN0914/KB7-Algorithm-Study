#include <iostream>
#include <vector>
#include <queue>

using namespace std;

vector<pair<int,int>> adj[51];
int dist[51];

const int INF = 1e9;

int dijkstra(int N, vector<vector<int> > road, int K) {
    
    int cnt=0;
    
    for(int i=0; i<=N; i++) dist[i]=INF;
    
    for(int i=0; i<road.size(); i++){
        
        int u=road[i][0];
        int v=road[i][1];
        int w=road[i][2];
        
        adj[u].push_back({w,v});
        adj[v].push_back({w,u});
    }
    
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
    
    dist[1]=0;
    
    pq.push({0,1});
    
    while(!pq.empty()){
        auto cur = pq.top();
        pq.pop();
        
        int curCost=cur.first;
        int curNode=cur.second;
        
        if(dist[curNode]!=curCost) continue;
        
        for(auto nxt: adj[curNode]){
            if(dist[nxt.second]<=dist[curNode]+nxt.first) continue;
            dist[nxt.second]=dist[curNode]+nxt.first;
            pq.push({dist[nxt.second], nxt.second});
        }
    }
    
    for(int i=1; i<=N; i++){
        if(dist[i]<=K) cnt++;
    }
    
    return cnt;
}

int solution(int N, vector<vector<int> > road, int K) {
    int answer = dijkstra(N,road,K);

    return answer;
}
