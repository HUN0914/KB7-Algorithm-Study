#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<string> answer;
bool flag=false;
bool isVisited[10001];

void dfs(vector<vector<string>>& tickets, string cur, vector<string>&path, int cnt){

    if(flag) return;
    path.push_back(cur);
    
    if(cnt==tickets.size()){
        answer=path;
        flag=true;
        return;
    }
    
    for(int i=0; i<tickets.size(); i++){
        if(tickets[i][0]!=cur) continue;
        if(isVisited[i]) continue;
        
        isVisited[i]=true;
        dfs(tickets, tickets[i][1], path, cnt+1);
        isVisited[i]=false;
    }
    path.pop_back();
    return;
}

vector<string> solution(vector<vector<string>> tickets) {
    
    sort(tickets.begin(), tickets.end());
    
    vector<string> path;
    
    dfs(tickets, "ICN", path,0);
    return answer;
}
