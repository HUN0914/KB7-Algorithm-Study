#include <string>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

/*
벽 : 1
칸 비어있음 : 0
직선 도로 : 100원
코너 : 500원 [상하 <-> 좌우 변경 시 필요] 
최소비용 만들기

dfs 로 모든 경우의 수 다 구하고 제일 작은 값 넣어야 하는 듯
dfs 했을 때 만약 그 방법이 되면 dfs (ex. 직선이 되거나 방향이 바뀌거나)

만약 가지 못하는 범위일 때, 그때 curY,x가 n-1인지 확인하고 아니면 그냥 리턴
맞으면 그 값 넣고 리턴
dir에 대한 값 추가해줘야함.
*/

struct ROAD {
    int y;
    int x;
    int cost;
    int dir;
};

int dx[4]={0,0,1,-1};
int dy[4]={1,-1,0,0};

int bfs(vector<vector<int>> board){
    int maxSize=board.size();
    int Cost[26][26][4];
    
    for(int i=0;i<maxSize;i++){
        for(int j=0;j<maxSize;j++){
            for(int d=0;d<4;d++){
                Cost[i][j][d] = 2e9;
            }
        }
    }    
    
    int answer=2e9;
    queue<ROAD>q;
    
    q.push({0,0,0,-1});
    
    while(!q.empty()){
        int curY=q.front().y;
        int curX=q.front().x;
        int cost=q.front().cost;
        int dir=q.front().dir;
        q.pop();
        
        if(curX==maxSize-1&&curY==maxSize-1){
            answer=min(answer,cost);
            continue;
        }
        
        for(int i=0; i<4; i++){
            int py=curY+dy[i];
            int px=curX+dx[i];
            
            if(px<0||py<0||px>=maxSize||py>=maxSize) continue;
            
            if(board[py][px]==1) continue;
            
            int nCost;
            if(dir==-1||dir==i) nCost=cost+100;
            else nCost=cost+600;
            
            if(Cost[py][px][i]>nCost){
                Cost[py][px][i]=nCost;
                q.push({py,px,nCost,i});
            }
        }
    }
    
    return answer;
}

int solution(vector<vector<int>> board) {
    
    int answer = bfs(board);
    return answer;
}
