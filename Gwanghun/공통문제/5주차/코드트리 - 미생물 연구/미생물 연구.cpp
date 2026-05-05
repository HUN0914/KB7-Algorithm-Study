#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <set>

using namespace std;

/*
좌측 하단 (r1, c1) 우측 상단 (r2, c2)

1. 미생물 투입
새로 투입된 무리 A 때매 둘 이상으로 나눠질 경우
미생물은 배양용기에서 모두 사라짐
-> 둘 이상으로 나눠진 판단을 어떻게 할 수 있을까?
=> 개수 기준이 아니라 '영역' 기준으로 둘 이상 나눠지면
bfs


2. 배양 용기 이동
기존 용기에서 형태 유지한 상태에서
다른 미생물 영역과 겹치지 않게
이 조건에서 x가 가장 작은 위치로
그런게 둘 이상일 경우 y가 가장 작은 위치

3. 실험 결과 기록
상화자우로 맞닿은 면이 있는 무리끼리 인접 무리라함
한 곳 이상만 맞닿아도 쌍 하나로 확인 확인하는 무리 다 곱하기
*/

int N,Q;
int board[16][16];
int copyBoard[16][16];

int dy[4]={-1,1,0,0};
int dx[4]={0,0,-1,1};

struct creature {
    int r1;
    int c1;
    int r2;
    int c2;

    int number;
    int size;
};

int nearCheck() {
    int total=0;
    bool isNewVisited[16][16];

    for (int i=0; i<=15; i++)
        for (int j=0; j<=15; j++) isNewVisited[i][j]=false;

    vector<int> countList;

    for (int k=0; k<Q; k++) {
        int count=0;
        for (int i=0; i<N; i++) {
            for (int j=0; j<N; j++) {
                if (board[i][j]==k) count++;
            }
        }
        countList.push_back(count);
    }

    set<pair<int,int>> adj;

    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            int a =board[i][j];
            if (a<0) continue;

            for (int d=0; d<4; d++) {
                int ni=i+dy[d];
                int nj=j+dx[d];

                if (ni<0||ni>=N||nj<0||nj>=N) continue;

                int b=board[ni][nj];

                if (b<0||a==b) continue;

                if (a<b) adj.insert({a,b});
                else adj.insert({b,a});
            }
        }
    }

    for (auto val : adj) {
        total+=countList[val.first]*countList[val.second];
    }
    return total;
}

void boardToCopyBoard() {
    for (int j=0; j<N; j++)
        for (int k=0; k<N; k++) board[j][k]=copyBoard[j][k];
}

bool operate(creature v1, creature v2){
    //여기서 1번째로 size 2번째로 val로 리턴
    if (v1.size!=v2.size) return v1.size>v2.size;
    return v1.number<v2.number;
}

void realMoveCreature(vector<creature>& creatures) {
    sort(creatures.begin(), creatures.end(), operate);

    for (int j=0; j<N; j++)
        for (int k=0; k<N; k++) copyBoard[j][k]=-1;

    for (int i=0; i<creatures.size(); i++) {
        int r1=creatures[i].r1;
        int c1=creatures[i].c1;
        int r2=creatures[i].r2;
        int c2=creatures[i].c2;
        int number=creatures[i].number;

        bool isOk=false;

        for (int j=0; j<N; j++) {
            for (int k=0; k<N; k++) {
                if (isOk) break;
                if (j + (r2-r1) >= N || k + (c2-c1) >= N) continue;
                bool isChecked=false;
                for (int a=0; a<=r2-r1; a++) {
                    for (int b=0; b<=c2-c1; b++) {
                        if (board[r1+a][c1+b] ==number) {
                            if (copyBoard[j+a][k+b] !=-1) {
                                isChecked=true;
                                break;
                            }
                        }
                    }
                    if (isChecked) break;
                }

                if (!isChecked) {
                    for (int a =0; a <=r2-r1; a++) {
                        for (int b=0; b <=c2-c1; b++) {

                            if (board[r1+a][c1+b]==number){
                                copyBoard[j+a][k+b]=number;
                            }
                        }
                    }
                    isOk=true;
                    break;
                }
            }
        }
        
        if(!isOk) continue;
    }
    boardToCopyBoard();
}

// 상태 보존을 어떻게 그대로 갖고오지?
void moveCreature() {
    vector<creature> creatures;

    for (int i=0; i<Q; i++) {
        int curCount=0;
        int r1=1e9;
        int r2=-1;
        int c1=1e9;
        int c2=-1;

        for (int j=0; j<N; j++) {
            for (int k=0; k<N; k++) {
                if (board[j][k]==i) {
                    curCount++;
                    r1=min(r1,j);
                    c1=min(c1,k);
                    r2=max(r2,j);
                    c2=max(c2,k);
                }
            }
        }
        if (curCount>0) creatures.push_back({r1,c1,r2,c2,i,curCount});
    }
    realMoveCreature(creatures);
}

void remove(int number) {
    for (int i=0; i<N; i++)
        for (int j=0; j<N; j++)
            if (board[i][j]==number) board[i][j]=-1;
}

void bfs(int number) { 

    queue<pair<int,int>>q;
    bool isVisited[16][16];
    int cnt=0;

    for (int i=0; i<N; i++)
        for (int j=0; j<N; j++) isVisited[i][j]=false;

    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            if (board[i][j]==number) {
                if (isVisited[i][j]) continue;
                cnt++;
                q.push({i,j});
                isVisited[i][j]=true;

                while (!q.empty()) {
                    int curY=q.front().first;
                    int curX=q.front().second;
                    q.pop();

                    for (int k=0; k<4; k++) {
                        int py=curY+dy[k];
                        int px=curX+dx[k];

                        if (py<0||py>=N||px<0||px>=N) continue;
                        if (isVisited[py][px]) continue;

                        if (board[py][px]==number) {
                            isVisited[py][px]=true;
                            q.push({py,px});
                        }
                    }

                }
            }
        }
    }

    if (cnt>=2) remove(number);
}

void game(int r1, int c1, int r2, int c2, int number) {

    for (int i=r1; i<r2; i++) 
        for (int j=c1; j<c2; j++) board[i][j]=number;

    for (int i=0; i<number; i++) bfs(i);

    moveCreature();

    cout<<nearCheck()<<"\n";
}

void input() {
    cin>>N>>Q;

    for (int i=0; i<16; i++) {
        for (int j=0; j<16; j++) {
            board[i][j]=-1;
            copyBoard[i][j]=-1;
        }
    }

    for (int i=0; i<Q; i++) {
        int r1,c1,r2,c2;
        cin>>r1>>c1>>r2>>c2;
        game(r1,c1,r2,c2,i);
    }
}

int main() {
    input();
    return 0;
}
