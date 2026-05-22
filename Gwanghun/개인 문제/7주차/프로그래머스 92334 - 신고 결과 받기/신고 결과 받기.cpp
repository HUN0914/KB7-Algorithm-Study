#include <string>
#include <vector>
#include <map>
#include <set>

using namespace std;

vector<int> cal(vector<string> id_list, vector<string> report, int k) {
    
    vector<int> result;
    
    set<pair<string,string>> s;
    map<string,int> ma; //신고 카운트 체크용 
    vector<string> who;
    
        
    for(int i=0; i<report.size(); i++){
        
        string firstName="";
        string lastName="";
        bool visited=false;
        
        for(int j=0; j<report[i].size(); j++){
            if(report[i][j]==' '){
                visited=true;
                continue;
            }
            if(visited) lastName+=report[i][j];
            else firstName+=report[i][j];
        }
        s.insert({firstName, lastName});
    }
    
    for(auto & val : s){
        ma[val.second]++;
    }
    
    for(auto& val : ma){
        if(val.second>=k) who.push_back(val.first);
    }
    
    //id_list에 저장되어있는 순서에 따라 
    
    for(auto &val: id_list){
        int cnt=0;
        for(auto &val2: s){
            
            if(val2.first==val){
                
                for(auto& cur: who){
                    
                    if(cur==val2.second){
                        
                        cnt++;
                    }
                }
            }
        }
        result.push_back(cnt);
    }
    
    
    return result;
}

vector<int> solution(vector<string> id_list, vector<string> report, int k) {
    vector<int> answer = cal(id_list, report, k);
    return answer;
}