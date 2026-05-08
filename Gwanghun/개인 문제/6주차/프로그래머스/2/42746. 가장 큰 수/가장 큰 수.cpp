#include <string>
#include <vector>
#include <algorithm>

using namespace std;
vector<string> val;
bool compare(string str1, string str2){
    return str1+str2>str2+str1;
}

string solution(vector<int> numbers) {
    string answer = "";
    
    for(int i=0; i<numbers.size(); i++){
        val.push_back(to_string(numbers[i]));
    }
    sort(val.begin(),val.end(), compare);
    
    if(val[0] == "0") return "0";
    
    for(int i=0; i<val.size(); i++) answer+=val[i];
       
    return answer;
}
