#include <string>
#include <vector>

using namespace std; 

int dp[100001];

int dynamic(int n, vector<int> money){
    dp[0]=1;
    
    for(int i=0; i<money.size(); i++){
        for(int j=money[i]; j<=n; j++){
            dp[j]+=dp[j-money[i]];
            dp[j] %= 1000000007;
        }
    }
    return dp[n];
}

int solution(int n, vector<int> money) {
    int answer = dynamic(n,money);
    return answer;
}
