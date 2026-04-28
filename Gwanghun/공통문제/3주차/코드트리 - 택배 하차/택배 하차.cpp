#include <iostream>
#include <vector>

using namespace std;

int n,m;
struct box{
    bool isLive=false;
    int cy;
    int c;
    int w;
    int h;
};

vector<box> boxes(101);
vector<int> numberss;
int curCountmax=-1;

int curBoard[51][51];
bool isOkayNumber[101];

void minusBoxes(int number){

    for(int i=1; i<=n; i++)
        for(int j=1; j<=n ; j++)
            if(curBoard[i][j]==number) curBoard[i][j]=0;
}

int minusLeftNumbers() {
    int minK = 0;

    // 1번부터 100번까지 번호 순서대로 전수 조사
    for (int k = 1; k <= 100; k++) {
        if (!boxes[k].isLive) continue;

        int cy = boxes[k].cy;
        int c = boxes[k].c;
        int h = boxes[k].h;
        int w = boxes[k].w;

        bool isBlocked = false;
        // 박스의 세로 범위(cy ~ cy+h-1) 전체에 대해 왼쪽 길(1 ~ c-1) 확인
        for (int r = cy; r < cy + h; r++) {
            for (int col = 1; col < c; col++) {
                // 내 번호가 아닌 다른 박스가 길을 막고 있다면
                if (curBoard[r][col] != 0 && curBoard[r][col] != k) {
                    isBlocked = true;
                    break;
                }
            }
            if (isBlocked) break;
        }

        // 막히지 않았다면 이 박스가 "하차 가능한 가장 작은 번호"임
        if (!isBlocked) {
            minK = k;
            break;
        }
    }
    return minK;
}

int minusRightNumbers() {
    int minK = 0;

    for (int k = 1; k <= 100; k++) {
        if (!boxes[k].isLive) continue;

        int cy = boxes[k].cy;
        int c = boxes[k].c;
        int h = boxes[k].h;
        int w = boxes[k].w;

        bool isBlocked = false;
        // 박스의 세로 범위 전체에 대해 오른쪽 길(c+w ~ n) 확인
        for (int r = cy; r < cy + h; r++) {
            for (int col = c + w; col <= n; col++) {
                if (curBoard[r][col] != 0 && curBoard[r][col] != k) {
                    isBlocked = true;
                    break;
                }
            }
            if (isBlocked) break;
        }

        if (!isBlocked) {
            minK = k;
            break;
        }
    }
    return minK;
}



// k: 택배 번호, h: 세로크기, w: 가로크기, c: 좌측좌표 , 맨 처음 떨어질떄
void fallInitBoxes(int number, int h, int w, int c) {
    // 1. 일단 맨 위(1행)에 박스를 둬.
    boxes[number].cy = 1;
    
    // 2. 밑으로 한 칸씩 내려가며 "진짜로" 갈 수 있는지 체크해.
    int gap = 0;
    while (true) {
        int nextBottom = 1 + h + gap; // 내 박스 바닥의 바로 다음 칸
        if (nextBottom > n) break;    // 바닥 뚫고 나갈 순 없지.

        bool canGo = true;
        for (int j = c; j < c + w; j++) {
            if (curBoard[nextBottom][j] != 0) { // 어? 누가 막고 있네?
                canGo = false;
                break;
            }
        }
        
        if (canGo) gap++; // 안 막혔으면 한 칸 더 내려가.
        else break;       // 막혔으면 거기서 멈춰.
    }
    
    // 3. 최종 위치에 안착!
    boxes[number].cy += gap;
    for (int i = boxes[number].cy; i < boxes[number].cy + h; i++) {
        for (int j = c; j < c + w; j++) {
            curBoard[i][j] = number;
        }
    }
}

bool compareBoxes(int a, int b) {
    // 바닥에 더 가까운(cy + h 가 큰) 박스를 먼저 처리
    return (boxes[a].cy + boxes[a].h) > (boxes[b].cy + boxes[b].h);
}

void fallBoxes() {
    vector<int> liveBoxIndices;
    for (int i = 1; i <= curCountmax; i++) {
        if (boxes[i].isLive) liveBoxIndices.push_back(i);
    }

    sort(liveBoxIndices.begin(), liveBoxIndices.end(), compareBoxes);

    for (int idx : liveBoxIndices) {
        int cy = boxes[idx].cy;
        int c = boxes[idx].c;
        int w = boxes[idx].w;
        int h = boxes[idx].h;

        for (int i = cy; i < cy + h; i++) {
            for (int j = c; j < c + w; j++) {
                curBoard[i][j] = 0;
            }
        }

        int gapCnt = 0;
        while (true) {
            int nextY = cy + h + gapCnt;
            if (nextY > n) break;

            bool canGoDown = true;
            for (int j = c; j < c + w; j++) {
                if (curBoard[nextY][j] != 0) {
                    canGoDown = false;
                    break;
                }
            }

            if (canGoDown) gapCnt++;
            else break;
        }

        // 4. 새로운 위치 업데이트 및 격자 재배치
        boxes[idx].cy += gapCnt;
        int newCy = boxes[idx].cy;
        for (int i = newCy; i < newCy + h; i++) {
            for (int j = c; j < c + w; j++) {
                curBoard[i][j] = idx;
            }
        }
    }
}

void game(){

    while(true){
        bool isEmpty=false;

        for(int i=1; i<=n; i++){
            for(int j=1; j<=n; j++){
                if(curBoard[i][j]>0){
                    isEmpty=true;
                    break;
                }
            }
        }

        if (!isEmpty) break;

        int numbers;

        numbers=minusLeftNumbers();
        boxes[numbers].isLive=false;
        cout<<numbers<<"\n";
        //test cout<<numbers<<"!!!!"<<"\n"; //test
        minusBoxes(numbers);
        fallBoxes();

        numbers=minusRightNumbers();
        boxes[numbers].isLive=false;
        cout<<numbers<<"\n";
        //test cout<<numbers<<"!!!!"<<"\n";
        minusBoxes(numbers);
        fallBoxes();
    }
}

void input(){
    for (int i=1; i<=n; i++)
        for (int j=1; j<=n; j++) curBoard[i][j]=0;

    cin>>n>>m;
    for(int i=1; i<=m; i++){

        int k,h,w,c;
        cin>>k>>h>>w>>c;
        boxes[k].isLive=true;
        boxes[k].cy=1;
        boxes[k].h=h;
        boxes[k].w=w;
        boxes[k].c=c;
        fallInitBoxes(k,h,w,c);
        curCountmax=max(curCountmax,k);
    }

}


int main() {
        input();
        game();
        return 0;
}

/*
 *
 *minus lfet,right, fallbox 다시보기

입력 : 택배 번호(k), 세로크기 (h), 가로크기 (w), 좌측 좌표 c

1. 택배 투입
- 왼쪽 열 위치, 가로크기, 세로 크기 기준 투입

board 맨아래부터 비교해서 가로크기 만큼 존재하지 않을 경우
그만큼의 가로, 세로크기만큼 board[i][j]= k 넣기


2. (택배하차)
왼쪽으로 뺄건데 막히지 않는 것들 빼기
만약 이것들이 많으면 k 넘버가 제일 낮은거 빼기

3. (택배하차)
왼쪽으로 뺄건데 막히지 않는 것들 빼기
만약 이것들이 많으면 k 넘버가 제일 낮은거 빼기

*/
