#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/*
순열 쭉 돌려서 그때그떄마다 카운트? 근데 이러면 시간초과 날텐데
DP로 값 저장 하는 방식은 어떻게?
그리디?
A순서 안다는건 그냥 이놈도 다 정렬처리해도 상관없다는 의미
A sort, B sort 후 가장 인접 케이스로 가져가기

1,3,5,7
2,2,6,8 
근데 
1,3,5,7
1,2,3,4 로 두면 케이스가 이긴 값이 0인데 실제로는 
승점 2점을 가져갈 수 있는 상황이 되는것임

둘다 sort를 하고 만약 a가 b 이겼을 시 a++, b++ 졌을 시 b++만해서 b의 크기까지 갔을 때 break
*/

int cal(vector<int>A, vector<int>B){
    int total=0;
    sort(A.begin(), A.end());
    sort(B.begin(), B.end());
    
    int Bsize=0;
    int Asize=0;
    while(Bsize<=B.size()){
        if(A[Asize]<B[Bsize]){
            Asize++;
            Bsize++;
            total++;
        }else{
            Bsize++;
        }
    }
    
    return total;
}


int solution(vector<int> A, vector<int> B) {
    int answer = -1;
    answer=cal(A,B);
    return answer;
}
