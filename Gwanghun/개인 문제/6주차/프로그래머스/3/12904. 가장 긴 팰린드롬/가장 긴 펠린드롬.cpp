#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

bool dp[2501][2501];

// i부터 j까지
int dynamic(string s){
    
    int answer=1;
    
    for(int i=0; i<s.size(); i++) dp[i][i]=true;
    
    for(int i=0; i<s.size()-1; i++){
        if(s[i]==s[i+1]) {
            dp[i][i+1]=true;
            answer=2;
        }
    }
    
    for(int len=3; len<=s.size(); len++){
        for(int i=0; i+len-1<s.size(); i++){
            int j = i+len-1;
            
            if(s[i]==s[j]&&dp[i+1][j-1]) {
                dp[i][j]=true;
                answer=max(len,answer);
            }
        }
    }

    return answer;
}

int solution(string s)
{
    int answer=dynamic(s);

    return answer;
}
