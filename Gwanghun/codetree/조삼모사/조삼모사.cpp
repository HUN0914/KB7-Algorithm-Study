#include <iostream>
#include <vector>

using namespace std;

int board[21][21];
bool isNumber[21];
bool isVisited[21];

vector<int> noon;
vector<int> night;

int n;

int minimum=1e9;

int cal(vector<int>v) {

    int result=0;
    for (int i=0; i<v.size(); i++) {
        for (int j=i+1; j<v.size(); j++) {
            if (v[i]==v[j]) continue;
            result+=board[v[i]][v[j]];
            result+=board[v[j]][v[i]];
        }
    }
    return result;
}

void dfs(int cnt) {
    if (noon.size()==n/2) {
        night.clear();
       for (int j=1; j<=n; j++) {
           if (!isNumber[j]) night.push_back(j);
       }

        //memset(isVisited,false,sizeof(isVisited));
        int noonVal=cal(noon);
        //memset(isVisited,false,sizeof(isVisited));
        cal(night);
        int nightVal=cal(night);

        minimum=min(abs(noonVal-nightVal),minimum);
    }

    for (int i=cnt; i<=n; i++) {
        if (isNumber[i]) continue;
        isNumber[i]=true;
        noon.push_back(i);
        dfs(i+1);
        isNumber[i]=false;
        noon.pop_back();
    }

}

void input() {
    cin>>n;
    for (int i=1; i<=n; i++)
        for (int j=1; j<=n; j++) cin>>board[i][j];
}

int main() {

    input();
    dfs(1);
    cout<<minimum;

    return 0;
}

/*
 순열마냥 반반씩 뽑고 min 계산
 vector 2개로 값 담아서 계산하는데, 이것도 백트래킹
 백트 2번
 */
