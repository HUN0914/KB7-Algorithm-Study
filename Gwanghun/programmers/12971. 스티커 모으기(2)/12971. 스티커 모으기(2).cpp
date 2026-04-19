#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

/*
스티커의 길이는 100,000까지 됨 (2중 반복문 X)
그리디? 
현재는 10,6,11,9 = 16 + 20 = 36이 최대임
이거 그냥 무조건 +2칸씩 띄우고 max 구하는 식으로?
이렇게 풀어도 전체 케이스에 대한 브포는 한번 해야함
-> 맨 마지막에서 시작하는 case 1, 맨 처음에서 시작한 case 1
두개에 대해서만 max 구해주면 될 듯?
근데 우연히 제일 큰 값이 이 두 케이스에 대해 걸릴수 있나? 
제일 큰 값 찾고, boolean 처리하고 (이건 2중 반복문)
dp? -> 
그리디같은데...
10으로
dp해서 14로 시작한거면 5에서 시작한것과 같음 
14에서 시작한 dp[1] 값 넣어두고 
만약 11에서 시작한걸 dp[4]라고하면 max (arr[2]+dp, arr[1]+ dp) 대충 요런식으로 푸는거같긴한데

초깃값 세팅을 어떻게 ??

처음 3개 이하면 걍 14+5 나 2중 하나 고르라 하고
dp[0]=14;
dp[1]=6;
dp[2]=5+14;

3부터
dp[i]= arr[i]+ max(dp[i-1],dp[i-2]);
이렇게하면 격자 스티커 처리 못함
*/

int zerodp[100001];
int onedp[100001];

int cal(vector<int> sticker){
    
    if(sticker.size()==1) return sticker[0];
    else if(sticker.size()==2){
        if(sticker[0]>sticker[1]) return sticker[0];
        return sticker[1];
    }
    
    zerodp[0]=sticker[0];
    zerodp[1]=sticker[0];
    
    onedp[0]=0;
    onedp[1]=sticker[1];

    for(int i=2; i<sticker.size()-1; i++){
        zerodp[i]=max(zerodp[i-1],zerodp[i-2]+sticker[i]);
    }
    
    for(int i=2; i<sticker.size(); i++){
        onedp[i]=max(onedp[i-1],onedp[i-2]+sticker[i]);
        //점화식에서 바로 첫번째 onedp[0]=0이니까 첫번째 스티커 안 골랐을 경우로 측정 가능
    }
    
    int maximum=max(onedp[sticker.size()-1],zerodp[sticker.size()-2]);
    
    return maximum;
}


int solution(vector<int> sticker)
{
    int answer = cal(sticker);
    return answer;
}
