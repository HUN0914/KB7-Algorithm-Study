# [level 3] 불량 사용자 - 64064번

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/64064) 

### 구분

코딩테스트 연습 > 2019 카카오 개발자 겨울 인턴십

### 제출 일자

2026년 04월 20일 23:06:20

### 채점결과

<pre class="console-content"><div></div><div class="console-heading">채점을 시작합니다.</div><div class="console-message">정확성  테스트</div><table class="console-test-group" data-category="correctness"><tbody><tr data-testcase-id="68756"><td valign="top" class="td-label">테스트 1 <span>〉</span></td><td class="result passed">통과 (0.03ms, 9.2MB)</td></tr><tr data-testcase-id="68758"><td valign="top" class="td-label">테스트 2 <span>〉</span></td><td class="result passed">통과 (0.07ms, 9.18MB)</td></tr><tr data-testcase-id="68760"><td valign="top" class="td-label">테스트 3 <span>〉</span></td><td class="result passed">통과 (0.07ms, 9.27MB)</td></tr><tr data-testcase-id="68762"><td valign="top" class="td-label">테스트 4 <span>〉</span></td><td class="result passed">통과 (0.08ms, 9.3MB)</td></tr><tr data-testcase-id="68763"><td valign="top" class="td-label">테스트 5 <span>〉</span></td><td class="result passed">통과 (161.68ms, 9.23MB)</td></tr><tr data-testcase-id="68765"><td valign="top" class="td-label">테스트 6 <span>〉</span></td><td class="result passed">통과 (2.23ms, 9.2MB)</td></tr><tr data-testcase-id="68766"><td valign="top" class="td-label">테스트 7 <span>〉</span></td><td class="result passed">통과 (0.05ms, 9.31MB)</td></tr><tr data-testcase-id="68768"><td valign="top" class="td-label">테스트 8 <span>〉</span></td><td class="result passed">통과 (0.12ms, 9.11MB)</td></tr><tr data-testcase-id="68769"><td valign="top" class="td-label">테스트 9 <span>〉</span></td><td class="result passed">통과 (0.08ms, 9.2MB)</td></tr><tr data-testcase-id="68771"><td valign="top" class="td-label">테스트 10 <span>〉</span></td><td class="result passed">통과 (0.08ms, 9.26MB)</td></tr><tr data-testcase-id="68772"><td valign="top" class="td-label">테스트 11 <span>〉</span></td><td class="result passed">통과 (0.06ms, 9.33MB)</td></tr></tbody></table><div class="console-heading">채점 결과</div><div class="console-message">정확성: 100.0</div><div class="console-message">합계: 100.0 / 100.0</div></pre>

### 문제 설명
<div class="guide-section" style="width: calc(98.8669% - 12px);">
    <div class="tab-pane fade active show" id="tour2">
      <div class="guide-section-description">
        <h6 class="guide-section-title">문제 설명</h6>
        <div class="markdown solarized-dark"><p>개발팀 내에서 이벤트 개발을 담당하고 있는 "무지"는 최근 진행된 카카오이모티콘 이벤트에 비정상적인 방법으로 당첨을 시도한 응모자들을 발견하였습니다. 이런 응모자들을 따로 모아 <code>불량 사용자</code>라는 이름으로 목록을 만들어서 당첨 처리 시 제외하도록 이벤트 당첨자 담당자인 "프로도" 에게 전달하려고 합니다. 이 때 개인정보 보호을 위해 사용자 아이디 중 일부 문자를 '*' 문자로 가려서 전달했습니다. 가리고자 하는 문자 하나에 '*' 문자 하나를 사용하였고 아이디 당 최소 하나 이상의 '*' 문자를 사용하였습니다.<br>
"무지"와 "프로도"는 불량 사용자 목록에 매핑된 응모자 아이디를 <code>제재 아이디</code> 라고 부르기로 하였습니다.</p>

<p>예를 들어, 이벤트에 응모한 전체 사용자 아이디 목록이 다음과 같다면</p>
<table class="table">
        <thead><tr>
<th>응모자 아이디</th>
</tr>
</thead>
        <tbody><tr>
<td>frodo</td>
</tr>
<tr>
<td>fradi</td>
</tr>
<tr>
<td>crodo</td>
</tr>
<tr>
<td>abc123</td>
</tr>
<tr>
<td>frodoc</td>
</tr>
</tbody>
      </table>
<p>다음과 같이 불량 사용자 아이디 목록이 전달된 경우,</p>
<table class="table">
        <thead><tr>
<th>불량 사용자</th>
</tr>
</thead>
        <tbody><tr>
<td>fr*d*</td>
</tr>
<tr>
<td>abc1**</td>
</tr>
</tbody>
      </table>
<p>불량 사용자에 매핑되어 당첨에서 제외되어야 야 할 제재 아이디 목록은 다음과 같이 두 가지 경우가 있을 수 있습니다.</p>
<table class="table">
        <thead><tr>
<th>제재 아이디</th>
</tr>
</thead>
        <tbody><tr>
<td>frodo</td>
</tr>
<tr>
<td>abc123</td>
</tr>
</tbody>
      </table><table class="table">
        <thead><tr>
<th>제재 아이디</th>
</tr>
</thead>
        <tbody><tr>
<td>fradi</td>
</tr>
<tr>
<td>abc123</td>
</tr>
</tbody>
      </table>
<p>이벤트 응모자 아이디 목록이 담긴 배열 user_id와 불량 사용자 아이디 목록이 담긴 배열 banned_id가 매개변수로 주어질 때, 당첨에서 제외되어야 할 제재 아이디 목록은 몇가지 경우의 수가 가능한 지 return 하도록 solution 함수를 완성해주세요.</p>

<h4><strong>[제한사항]</strong></h4>

<ul>
<li>user_id 배열의 크기는 1 이상 8 이하입니다.</li>
<li>user_id 배열 각 원소들의 값은 길이가 1 이상 8 이하인 문자열입니다.

<ul>
<li>응모한 사용자 아이디들은 서로 중복되지 않습니다.</li>
<li>응모한 사용자 아이디는 알파벳 소문자와 숫자로만으로 구성되어 있습니다.</li>
</ul></li>
<li>banned_id 배열의 크기는 1 이상 user_id 배열의 크기 이하입니다.</li>
<li>banned_id 배열 각 원소들의 값은 길이가 1 이상 8 이하인 문자열입니다.

<ul>
<li>불량 사용자 아이디는 알파벳 소문자와 숫자, 가리기 위한 문자 '*' 로만 이루어져 있습니다.</li>
<li>불량 사용자 아이디는 '*' 문자를 하나 이상 포함하고 있습니다.</li>
<li>불량 사용자 아이디 하나는 응모자 아이디 중 하나에 해당하고 같은 응모자 아이디가 중복해서 제재 아이디 목록에 들어가는 경우는 없습니다.</li>
</ul></li>
<li>제재 아이디 목록들을 구했을 때 아이디들이 나열된 순서와 관계없이 아이디 목록의 내용이 동일하다면 같은 것으로 처리하여 하나로 세면 됩니다.</li>
</ul>

<hr>

<h5><strong>[입출력 예]</strong></h5>
<table class="table">
        <thead><tr>
<th>user_id</th>
<th>banned_id</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td><code>["frodo", "fradi", "crodo", "abc123", "frodoc"]</code></td>
<td><code>["fr*d*", "abc1**"]</code></td>
<td>2</td>
</tr>
<tr>
<td><code>["frodo", "fradi", "crodo", "abc123", "frodoc"]</code></td>
<td><code>["*rodo", "*rodo", "******"]</code></td>
<td>2</td>
</tr>
<tr>
<td><code>["frodo", "fradi", "crodo", "abc123", "frodoc"]</code></td>
<td><code>["fr*d*", "*rodo", "******", "******"]</code></td>
<td>3</td>
</tr>
</tbody>
      </table>
<h5><strong>입출력 예에 대한 설명</strong></h5>

<h5><strong>입출력 예 #1</strong></h5>

<p>문제 설명과 같습니다.</p>

<h5><strong>입출력 예 #2</strong></h5>

<p>다음과 같이 두 가지 경우가 있습니다.</p>
<table class="table">
        <thead><tr>
<th>제재 아이디</th>
</tr>
</thead>
        <tbody><tr>
<td>frodo</td>
</tr>
<tr>
<td>crodo</td>
</tr>
<tr>
<td>abc123</td>
</tr>
</tbody>
      </table><table class="table">
        <thead><tr>
<th>제재 아이디</th>
</tr>
</thead>
        <tbody><tr>
<td>frodo</td>
</tr>
<tr>
<td>crodo</td>
</tr>
<tr>
<td>frodoc</td>
</tr>
</tbody>
      </table>
<h5><strong>입출력 예 #3</strong></h5>

<p>다음과 같이 세 가지 경우가 있습니다.</p>
<table class="table">
        <thead><tr>
<th>제재 아이디</th>
</tr>
</thead>
        <tbody><tr>
<td>frodo</td>
</tr>
<tr>
<td>crodo</td>
</tr>
<tr>
<td>abc123</td>
</tr>
<tr>
<td>frodoc</td>
</tr>
</tbody>
      </table><table class="table">
        <thead><tr>
<th>제재 아이디</th>
</tr>
</thead>
        <tbody><tr>
<td>fradi</td>
</tr>
<tr>
<td>crodo</td>
</tr>
<tr>
<td>abc123</td>
</tr>
<tr>
<td>frodoc</td>
</tr>
</tbody>
      </table><table class="table">
        <thead><tr>
<th>제재 아이디</th>
</tr>
</thead>
        <tbody><tr>
<td>fradi</td>
</tr>
<tr>
<td>frodo</td>
</tr>
<tr>
<td>abc123</td>
</tr>
<tr>
<td>frodoc</td>
</tr>
</tbody>
</table></div>
</div>
</div>

 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges

## 💡 풀이 핵심

구현 문제... 이긴 한데 아이디어 떠올리는게 좀 힘들었다.<br/>
일단 각 banned_id에서 각 패턴에 부합하는 id를 고르는것은 맞다고 생각했는데<br/>
패턴의 교집합과 합집합을 통해서 모두 부합하는 패턴을 재도출한 다음 답을 구하는 줄 알았다가</br>
문제를 다시 읽고 그것이 아님을 깨달았다.<br/>
input 데이터가 작은편이기도 하고, 각 id가 ban에 포함되느냐 아니냐의 문제이므로<br/>
백트래킹이 떠올랐고, 중복을 피해야 했기에 user_id 배열을 인덱스만 취급하여<br/>
0과 1, 즉 포함되지 않느냐, 포함되느냐만 따져서 이를 10진수로 변환함으로써<br/>
최종적으로 answer를 구하기 위한 check 배열에 체크를 하는 방식으로 문제를 해결했다.<br/>

### 로직
1. banned_id 배열의 길이만큼의 2차원 배열 banned_case를 선언하고, 각 user_id에 대해 모든 패턴과 비교하여 user_id의 인덱스를 부합하는 모든 case의 배열에 삽입한다.
2. 백트래킹용 check 배열을 선언하고 각 case를 처음부터 끝까지 백트래킹을 진행하며 모든 경우의 수에 대해 체크한다.
3. 하나의 경우의 수가 나왔을때 백트래킹용 check 배열을 10진수로 변환하여 answer을 도출하기 위한 check 배열에 도출한 10진수의 인덱스에 해당하는 값을 1로 바꿔준다.
4. 모든 경우의 수를 탐색한 뒤 check에 존재하는 1의 개수가 곧 answer이다.
