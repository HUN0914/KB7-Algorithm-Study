#include <string>
#include <vector>
#include <cctype>

using namespace std;

string cal(string new_id){
    
    //1단계
    for(int i=0; i<new_id.size(); i++) new_id[i]=tolower(new_id[i]);
    
    //2단계
    string newTwo="";
    for(int i=0; i<new_id.size(); i++){
  if(

        (new_id[i]>='a' && new_id[i]<='z') ||

        (new_id[i]>='0' && new_id[i]<='9') ||

        new_id[i]=='-' ||

        new_id[i]=='_' ||

        new_id[i]=='.'

    ) newTwo += new_id[i];
        
    }
    new_id=newTwo;
    
    //3단계
    string newThree="";
    for(int i=0; i<new_id.size(); i++){
        
        newThree+=new_id[i];
        
        if(new_id[i]=='.'){
            for(int j=i; j<new_id.size(); j++){
                if(new_id[j]!='.'){
                    newThree+=new_id[j];
                    i=j;
                    break;
                }
                i=j;
            }
            
        }
    }
    new_id=newThree;
    
    //4단계
    string newFour="";
    for(int i=0; i<new_id.size(); i++){
        if(i==0){
            if(new_id[0]=='.') continue;
        }
        if(i==new_id.size()-1){
            if(new_id[new_id.size()-1]=='.') continue;
        }
        newFour+=new_id[i];
    }
    new_id=newFour;
    
    //5단계
    if(new_id.size()==0) new_id="a";
    
    //6단계
    string newSix="";
    if(new_id.size()>=16) {
        for(int i=0; i<15; i++){
            if(i==14){
                if(new_id[i]=='.') break;
            }
            newSix+=new_id[i];
        }
        new_id=newSix;
    }
    
    //7단계
    if(new_id.size()==1){
        new_id+=new_id[0];
        new_id+=new_id[0];
    }else if (new_id.size()==2){
        new_id+=new_id[1];
    }
    
    return new_id;
}

string solution(string new_id) {
    string answer = cal(new_id);
    return answer;
}