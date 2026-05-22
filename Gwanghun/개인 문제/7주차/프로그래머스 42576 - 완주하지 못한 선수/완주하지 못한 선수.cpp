#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    
    unordered_map<string,int> ma;
    string answer="";
    
    for(const auto& val: participant) ma[val]++;
    
    for(const auto& val: completion) ma[val]--;
    
    for(const auto& val: ma){
        if(val.second>0){
            return val.first;
        }
    }

    return answer;
}