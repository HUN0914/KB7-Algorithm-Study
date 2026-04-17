# [level 3] 여행 경로 - 43164번

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/43164) 


### 구분

코딩테스트 연습 > 깊이/너비 우선 탐색 (DFS/BFS)

### 채점결과

<pre class="console-content"><div></div><div class="console-heading">채점을 시작합니다.</div><div class="console-message">정확성  테스트</div><table class="console-test-group" data-category="correctness"><tbody><tr data-testcase-id="33381"><td valign="top" class="td-label">테스트 1 <span>〉</span></td><td class="result passed">통과 (0.04ms, 9.29MB)</td></tr><tr data-testcase-id="33382"><td valign="top" class="td-label">테스트 2 <span>〉</span></td><td class="result passed">통과 (0.01ms, 9.27MB)</td></tr><tr data-testcase-id="33383"><td valign="top" class="td-label">테스트 3 <span>〉</span></td><td class="result passed">통과 (0.01ms, 9.29MB)</td></tr><tr data-testcase-id="33384"><td valign="top" class="td-label">테스트 4 <span>〉</span></td><td class="result passed">통과 (0.01ms, 9.27MB)</td></tr></tbody></table><div class="console-heading">채점 결과</div><div class="console-message">정확성: 100.0</div><div class="console-message">합계: 100.0 / 100.0</div></pre>

### 제출 일자

2026년 04월 16일 10:02:18

### 문제 설명
<div class="guide-section-description">
        <h6 class="guide-section-title">문제 설명</h6>
        <div class="markdown solarized-dark"><p>주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 "ICN" 공항에서 출발합니다.</p>

<p>항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.</p>

<h5>제한사항</h5>

<ul>
<li>모든 공항은 알파벳 대문자 3글자로 이루어집니다.</li>
<li>주어진 공항 수는 3개 이상 10,000개 이하입니다.</li>
<li>tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.</li>
<li>주어진 항공권은 모두 사용해야 합니다.</li>
<li>만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.</li>
<li>모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>tickets</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]</td>
<td>["ICN", "JFK", "HND", "IAD"]</td>
</tr>
<tr>
<td>[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]</td>
<td>["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges

## 💡 풀이 핵심

그래프 문자열 순으로 정렬하고 DFS