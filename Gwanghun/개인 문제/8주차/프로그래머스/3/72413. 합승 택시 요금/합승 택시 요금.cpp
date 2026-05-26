#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <algorithm>

using namespace std;

/*
양방향, 그리고 무조건 양쪽 들려야함.
만약 꼭짓점 (목표지점) 만났을 경우에만 continue해주기.
(바깥 반복문에서. 안에서는 해줘서 거기에 값 들어가게는 하기)
처음 위치에서 A 위치로 가는 최단경로 + A위치에서 B위치로 가는 최단경로 vs
처음 위치에서 B 위치로 가는 최단경로 + B위치에서 A위치로 가는 최단경로
의 min 값 구하기
다익스트라 2번
*/

vector<int> dijkstra(int n, int s, vector<vector<int>> fares) {
    
    vector<pair<int,int>> adj[201];
    vector<int> dist(201);
    
    for(int i=0; i<=n; i++) dist[i]=1e9;
    
    for(int i=0; i<fares.size(); i++){
        
        int u=fares[i][0];
        int v=fares[i][1];
        int w=fares[i][2];
        
        adj[u].push_back({w,v});
        adj[v].push_back({w,u});
        
    }
    
    priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> pq;
    
    dist[s]=0;
    
    pq.push({0,s});
    
    while(!pq.empty()){
        
        auto cur=pq.top();
        pq.pop();
        
        int curCost=cur.first;
        int curNode=cur.second;
        
        if(dist[curNode]!=curCost) continue;
        
        for(auto val : adj[curNode]){
            
            if(dist[val.second]<=dist[curNode]+val.first) continue;
            dist[val.second]=dist[curNode]+val.first;
            
            pq.push({dist[val.second], val.second});
        }
    }
    
    return dist;
}

int game(int n, int s, int a, int b, vector<vector<int>> fares) {
    
    int minimum=1e9;
    
    vector<int> fromS=dijkstra(n,s,fares);
    vector<int> fromA=dijkstra(n,a,fares);
    vector<int> fromB=dijkstra(n,b,fares);
    
    for(int i=1; i<=n; i++){
        
        if(fromS[i]==1e9||fromA[i]==1e9||fromB[i]==1e9) continue;
        
        minimum=min((fromS[i]+fromA[i]+fromB[i]), minimum);
    }
    
    return minimum;
}

int solution(int n, int s, int a, int b, vector<vector<int>> fares) {
    
    int answer = game(n,s,a,b,fares);
    
    return answer;
}
