#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int parent[101];

bool isGreater(vector<int>v1, vector<int>v2){
    return v1[2]<v2[2];
}

int find(int x){
    if(parent[x]==x) return x;
    return parent[x]=find(parent[x]);
}

void unite(int a, int b){
    a=find(a);
    b=find(b);
    
    if(a!=b){
        parent[b]=a;
    }
}

int kruskal(int n, vector<vector<int>> costs) {
    int answer=0;
    int cnt=0;
    
    for(int i=0; i<n; i++) parent[i]=i;
    
    sort(costs.begin(), costs.end(), isGreater);
    
    for(auto edge : costs){
        int a = edge[0];
        int b = edge[1];
        int cost = edge[2];
        
        if(find(a)!=find(b)){
            unite(a,b);
            answer+=cost;
            cnt++;
            
            if(cnt==n-1) break;
        }
    }
    
    return answer;
    
}

int solution(int n, vector<vector<int>> costs) {
    int answer = kruskal(n,costs);
    return answer;
}
