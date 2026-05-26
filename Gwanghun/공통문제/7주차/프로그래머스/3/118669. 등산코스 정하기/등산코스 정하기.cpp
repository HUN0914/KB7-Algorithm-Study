#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

/*
Intensity 가장 최소 되는 등산코스에 포함된 산봉우리 번호와 
Intensity의 최솟값을 차례대로 정수에 담기 

처음 출발한 원래의 출구로 돌아오지 않으면 잘못된 등산코스
처음과 끝 외의 다른 출입구 방문하기 때문에 잘못된 등산 코스

intensity가 최소가 되는 등산코스가 여러 개라면 그중 산봉우리의 번호가 가장 낮은 등산코스 선택
*/

int v,e,st;

vector<pair<int,int>> adj[50001];

const int INF=1e9;

int dist[50001];
bool isSummit[50001];
bool isGate[50001];

vector<int> dijkstra(int n, vector<vector<int>> paths, vector<int> gates, vector<int> summits){
    
    vector<int>answer;

    for(int i=0; i<=n; i++) dist[i]=INF;
    
    for(int i=0; i<paths.size(); i++){
        int u=paths[i][0];
        int v=paths[i][1];
        int w=paths[i][2];
        
        adj[u].push_back({w,v});
        adj[v].push_back({w,u});
    }
    
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;

    for(int i=0; i<gates.size(); i++) isGate[gates[i]]=true;
    
    for(int i=0; i<summits.size(); i++) isSummit[summits[i]]=true;
    
    for(int i=0; i<gates.size(); i++) {
        pq.push({0, gates[i]});
        dist[gates[i]]=0;
    }
    
    while(!pq.empty()){
        auto cur=pq.top();
        pq.pop();
        
        int curIntensity=cur.first;
        int curNode=cur.second;
        
        if(dist[curNode]!= curIntensity) continue;
        
        if(isSummit[curNode]) continue;
        
        for(auto nxt: adj[cur.second]){
            int newIntensity=max(cur.first, nxt.first);
            
            int nextNode=nxt.second;
            
            if(newIntensity < dist[nextNode]){
                dist[nextNode]=newIntensity;
                
                pq.push({newIntensity, nextNode});
            }
        }
    }
    
    sort(summits.begin(), summits.end());
    
    int summitNum=0;
    int minIntensity=INF;
    
    for(int summit: summits){
        if(dist[summit] < minIntensity){
            minIntensity=dist[summit];
            summitNum=summit;
        }
    }
    
    answer.push_back(summitNum);
    answer.push_back(minIntensity);
    
    return answer;
}

vector<int> solution(int n, vector<vector<int>> paths, vector<int> gates, vector<int> summits) {
    vector<int> answer = dijkstra(n,paths,gates,summits);
    return answer;
}
