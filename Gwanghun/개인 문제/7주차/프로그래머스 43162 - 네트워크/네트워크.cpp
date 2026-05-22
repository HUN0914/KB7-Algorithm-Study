#include <string>
#include <vector>
#include <queue>

using namespace std;

bool visited[201];

int cal(int n, vector<vector<int>> computers) {
    
    int answer=0;
    
    vector<vector<int>> edge(n+1);
    
    for(int i=0; i<computers.size(); i++){
        for(int j=0; j<computers[i].size(); j++){
            if(i==j) continue;
            
            if(computers[i][j]==1){
                edge[i].push_back(j);
                edge[j].push_back(i);
            }
        }
    }
    
    queue<int>q;
    
    for(int i=0; i<n; i++){
        if(visited[i]) continue;
        
        answer++;
        q.push(i);
        visited[i]=true;
        
        while(!q.empty()){
            int val=q.front();
            q.pop();
            
            for(int i=0; i<edge[val].size(); i++){
                
                if(visited[edge[val][i]]) continue;
                visited[edge[val][i]]=true;
                q.push(edge[val][i]);
            }
            
        }
    } 
    
    return answer;
}

int solution(int n, vector<vector<int>> computers) {
    int answer = cal(n,computers);
    return answer;
}