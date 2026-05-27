#include <string>
#include <vector>
#include <queue>
#include <map>

using namespace std;

vector<int> cal(vector<string> operations) {
    
    priority_queue<int> UpPq;
    priority_queue<int, vector<int>, greater<int>> DownPq;
    map<int,int> m;
    
     for(int i=0; i<operations.size(); i++){
         if(operations[i][0]== 'I'){
             string val="";
             for(int j=2; j<operations[i].size(); j++){
                 val+=operations[i][j];
             }
             int value=stoi(val);
             UpPq.push(value);
             DownPq.push(value);
             m[value]++;
         }else{
             if(operations[i][2]== '-'){
                 while(!DownPq.empty()&&m[DownPq.top()]==0){
                     DownPq.pop();
                 }
                 if(!DownPq.empty()){
                     m[DownPq.top()]--;
                     DownPq.pop();
                 }
             }
             else{
                 while(!UpPq.empty() && m[UpPq.top()]==0){
                     UpPq.pop();
                 }
                 if(!UpPq.empty()){ 
                     m[UpPq.top()]--;
                     UpPq.pop();
                 }
             }
         }
     }
    
    while(!UpPq.empty()&&m[UpPq.top()]==0){
        UpPq.pop();
    }

    while(!DownPq.empty()&&m[DownPq.top()]==0){
        DownPq.pop();
    }
    
    if(DownPq.empty()||UpPq.empty()){
        vector<int> answer;
        answer.push_back(0);
        answer.push_back(0);
        return answer;
    }
    
    else {
        vector<int> answer;
        answer.push_back(UpPq.top());
        answer.push_back(DownPq.top());     
        return answer;
    }
}

vector<int> solution(vector<string> operations) {
    vector<int> answer = cal(operations);
    return answer;
}
