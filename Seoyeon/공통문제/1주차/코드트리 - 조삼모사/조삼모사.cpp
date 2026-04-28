#include <bits/stdc++.h>
using namespace std;

int n;
int P[21][21];
bool visited[21];
int ans = INT_MAX;
void calc(){
    int morning = 0;
    int evening = 0;

    for(int i = 0; i < n; i++){
        for(int j = i + 1; j < n; j++){
            if(visited[i] && visited[j]){
                morning += P[i][j] + P[j][i];
            }
            else if(!visited[i] && !visited[j]){
                evening += P[i][j] + P[j][i];
            }
        }
    }

    ans = min(ans, abs(morning - evening));
}

// 조합 생성
void dfs(int idx, int cnt){
    // n/2명 뽑았으면 계산
    if(cnt == n/2){
        calc();
        return;
    }

    for(int i = idx; i< n; i++){ // idx : 다음에 어디부터 볼지  , cnt : 지금까지 몇 개 뽑았는지
        visited[i] = true;
        dfs(i+1, cnt+1);
        visited[i] = false; // 백트래킹
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n;

    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cin >> P[i][j];
        }
    }

    // 중복 제거 
    visited[0] = true; // 0번은 무조건 아침팀
    dfs(1, 1);

    cout << ans;


    
    return 0;
}
