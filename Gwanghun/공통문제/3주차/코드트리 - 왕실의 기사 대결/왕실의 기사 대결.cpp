#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int board[41][41];
int locationMap[41][41];

int dy[4]={-1,0,1,0};
int dx[4]={0,1,0,-1};

int originK[31];

struct knight{
    int r;
    int c;
    int h;
    int w;
    int k;
    bool isLive;
};

vector<knight> knights(31);
vector<int> minusKnight;

int L,N,Q;
int resultVal=0;

void rebuild(){
    for(int y=1;y<=L;y++){
        for(int x=1;x<=L;x++){
            locationMap[y][x]=0;
        }
    }

    for(int id=1; id<=N; id++){
        if(!knights[id].isLive) continue;

        int r=knights[id].r;
        int c=knights[id].c;
        int h=knights[id].h;
        int w=knights[id].w;

        for(int y=r;y<r+h;y++){
            for(int x=c;x<c+w;x++){
                locationMap[y][x]=id;
            }
        }
    }
}

void damege(){

    for(auto val : minusKnight){
        if(!knights[val].isLive) continue;

        int r=knights[val].r;
        int c=knights[val].c;
        int h=knights[val].h;
        int w=knights[val].w;

        for(int i=r; i<r+h; i++){
            for(int j=c; j<w+c; j++){
                if(board[i][j]==1) knights[val].k--;
            }
        }
        if(knights[val].k<=0) knights[val].isLive=false;
    }

    minusKnight.clear();
}

void game(int i, int d){ //i번 기사한테 방향 d로 '한 칸' 이동
    if(!knights[i].isLive) return;

    queue<int>q;
    bool isVisited[31]={false};
    vector<int> moved;

    q.push(i);
    isVisited[i]=true;
    moved.push_back(i);

    while(!q.empty()){
        int cur=q.front();
        q.pop();

        int nr = knights[cur].r+dy[d];
        int nc = knights[cur].c+dx[d];
        int h = knights[cur].h;
        int w = knights[cur].w;

        if(nr<1 || nc<1 || nr+h-1>L || nc+w-1>L) return;

        for(int y=nr; y<nr+h; y++){
            for(int x=nc; x<nc+w; x++){
                if(board[y][x]==2) return;

                int next=locationMap[y][x];
                if(next!=0 && !isVisited[next]){
                    isVisited[next]=true;
                    q.push(next);
                    moved.push_back(next);
                }
            }
        }
    }

    for(auto id : moved){
        knights[id].r+=dy[d];
        knights[id].c+=dx[d];
    }

    for(int y=1; y<=L; y++){
        for(int x=1; x<=L; x++){
            locationMap[y][x]=0;
        }
    }

    for(auto id : moved){
        if(id!=i) minusKnight.push_back(id);
    }
    
}

void input(){
    cin>>L>>N>>Q;
    for(int i=1; i<=L; i++){ //1 index
        for(int j=1; j<=L; j++){
            cin>>board[i][j];
        }
    }

    for(int i=1; i<=N; i++){
        int r,c,h,w,k;
        cin>>r>>c>>h>>w>>k;

        knights[i].r=r;
        knights[i].c=c;
        knights[i].h=h;
        knights[i].w=w;
        knights[i].k=k;
        knights[i].isLive=true;
        originK[i]=k;
        
        for(int y=r;y<r+h;y++){
            for(int x=c;x<c+w;x++){
                locationMap[y][x]=i;
            }
        }
    }

    for(int j=0; j<Q; j++){
        int i,d;
        cin>>i>>d;
        game(i,d);
        damege();
        rebuild();
    }

    for(int i=1; i<=N; i++){
        if(knights[i].isLive){
            resultVal += originK[i] - knights[i].k;
        }
    }
    cout<<resultVal;
}

int main() {
    input();
    return 0;
}

