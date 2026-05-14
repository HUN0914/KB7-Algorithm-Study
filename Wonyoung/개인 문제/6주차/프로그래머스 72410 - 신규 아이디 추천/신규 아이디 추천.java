import java.util.*;

class Solution {
    public String solution(String new_id) {
        String answer = "";
        StringBuilder sb = new StringBuilder();
        
        // 1단계: 대문자 -> 소문자
        for(char c: new_id.toCharArray()){
            if('A' <= c && c <= 'Z'){
                sb.append(Character.toLowerCase(c));
            } else {
                sb.append(c);
            }
        }
        
        answer = sb.toString();
        sb = new StringBuilder();
        
        // 2단계: 알파벳 소문자, 숫자, 빼기, 밑줄, 마침표를 제외한 모든 문자를 제외
        for(char c: answer.toCharArray()){
            if(('a' <= c && c <= 'z') || ('0' <= c && c <= '9') || c == '-' || c == '_' || c == '.' ){
                sb.append(c);
            }
        }
        
        answer = sb.toString();
        sb = new StringBuilder();

        // 3단계: 마침표가 2개 이상 연속되면 하나로 치환
        for(char c: answer.toCharArray()){
            if(sb.length() > 0 && sb.charAt(sb.length()-1) == '.' && c == '.') continue;
            sb.append(c);
        }

        answer = sb.toString();
        sb = new StringBuilder();

        // 4단계: 마침표 처음/끝 -> 제거
        if(answer.length() > 0 && answer.charAt(0) == '.') answer = answer.substring(1, answer.length());
        if(answer.length() > 0 && answer.charAt(answer.length()-1) == '.') answer = answer.substring(0, answer.length() - 1);

        // 5단계: 빈 문자열이면 a를 대입
        if(answer.equals("")) answer += "a";

        // 6단계: 16자 이상 -> 15자
        if(answer.length() >= 16) answer = answer.substring(0, 15);

        // 7단계: 2자 이하 -> 3자 이상이 될때까지 마지막 문자 삽입
        if(answer.length() <= 2){
            int n = 3 - answer.length();
            while(n--> 0) answer += answer.charAt(answer.length()-1);
        }
        
        // 최종: 마침표 처음/끝 -> 제거
        if(answer.length() > 0 && answer.charAt(0) == '.') answer = answer.substring(1, answer.length());
        if(answer.length() > 0 && answer.charAt(answer.length()-1) == '.') answer = answer.substring(0, answer.length() - 1);
        
        return answer;
    }
}