#include <string>
#include <vector>

using namespace std;

int diff[1001][1001];
//이를 통해 skill 사이즈만큼의 시간복잡도를 개선

int cal(vector<vector<int>> board, vector<vector<int>> skill) {
    
    int n = board.size();
    int m= board[0].size();
    
    for(auto s : skill){
        
        int type=s[0];
        
        int r1=s[1];
        int c1=s[2];
        int r2=s[3];
        int c2=s[4];
        
        int degree=s[5];
        
        int value=0;
        
        if(type==1) value = -degree;
        else value = degree;
        
        diff[r1][c1]+=value;
        diff[r1][c2+1]-=value;
        diff[r2+1][c1]-=value;
        diff[r2+1][c2+1]+=value;
        
    }
    
    for(int i=0; i<=n; i++){
        for(int j=1; j<=m; j++){
            diff[i][j]+=diff[i][j-1];
        }
    }
    
    for(int i=0; i<=m; i++){
        for(int j=1; j<=n; j++){
            diff[j][i]+=diff[j-1][i];
        }
    }
    
    int answer=0;
    
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            long long total = board[i][j]+diff[i][j];
            
            if(total>0) answer++;
        }
    }
    
    return answer;
}

int solution(vector<vector<int>> board, vector<vector<int>> skill) {
    int answer = cal(board,skill);
        
    return answer;
}
