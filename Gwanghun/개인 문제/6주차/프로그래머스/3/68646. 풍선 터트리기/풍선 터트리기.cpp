#include <string>
#include <vector>

using namespace std;

        /*
        두 풍선 중 번호가 더 작은 풍선 터트리는건 단 한번만 가능
        나머지는 더 큰 풍선을 터트려야함 (음,양수 주의)
        주어진 풍선 list 중에서 각자 풍선이 최후까지 남을 수 있는지 확인하기 (count)        
        근데 언제 터뜨리냐에 따라서 케이스가 너무 많이 나오지않나 ?
        기본 defalut: cnt가 2개이상일 때 (앞, 뒤 번호 작은 풍선 터뜨려야하는데 이 경우가 2번 이상 나타날 때)           기준점 +-1 기준으로
        그냥 왼 오른쪽 Max만 쭉 남기는 기준으로해서 작은값 2개이상이면 안되게?
        */

int arr[1000001];
int rightArr[1000001];

int cal(vector<int> a){
    int cnt=2;
    
    for(int i=0; i<a.size(); i++){
        arr[i]=2e9;
        rightArr[i]=2e9;
    }
    
    arr[0]=a[0];
    for(int i=1; i< a.size(); i++) arr[i]=min(arr[i-1],a[i]);
    
    rightArr[a.size()-1]=a[a.size()-1];
    for(int i=a.size()-2; i>=0; i--) rightArr[i]=min(rightArr[i+1],a[i]);

    for(int i=1; i<a.size()-1; i++){
        int val=0;
        if(arr[i-1]<a[i]) val++;
        if(rightArr[i+1]<a[i]) val++;
        
        if(val<2) cnt++;
    }
    
    return cnt;
}

int solution(vector<int> a) {
    int answer = cal(a);
    return answer;
}
