#include <string>
#include <vector>
#include <map>

using namespace std;

/*
판매원 : 자신 판매에 의해 발생하는 이익 10% 추천인에게 주고 90% 가짐
판매원 : 자신이 조직에 추천하여 가입시킨 이득의 10%도 자기 바로 윗대가리한테 줘야함 
10% 절사 했을 때 금액이 1원 미만일 경우 주지 않고 자신이 다 가짐
백트래킹 같긴함
그 처음에 수익이 발생했을 때 자기 위에 depth가 얼마만큼 있는지를 먼저 알아서 수익 발생 위치로부터 depth
측정 후 그만큼 지급해야되는 구조?같음

여기서 edword를 참여시킨 사람은 mary와 같음 
일단 graph를 먼저 만들어야 할 필요가 있어보임 
*/

vector<int> cal(vector<string> enroll, vector<string> referral, vector<string> seller, vector<int> amount) {
    vector<int> answer;
    
    map<string, string> parent;
    
    map<string, int> res;
    
    for(int i=0; i<referral.size(); i++){
        parent[enroll[i]]=referral[i];
    }
    
    for(int i=0; i<seller.size(); i++){
        int point=amount[i]*100;
        
        string me= seller[i];
        
        res[me]+=point;
        
        while(me!="-" && point>9){
            point /=10;
            res[parent[me]] +=point;
            res[me]-=point;
            me=parent[me];
        }
    }
    
    for(int i=0; i<enroll.size(); i++){
        answer.push_back(res[enroll[i]]);
    }
    
    return answer;
}

vector<int> solution(vector<string> enroll, vector<string> referral, vector<string> seller, vector<int> amount) {
    
    vector<int> answer;
    
    answer=cal(enroll,referral,seller,amount);
    return answer;
}
