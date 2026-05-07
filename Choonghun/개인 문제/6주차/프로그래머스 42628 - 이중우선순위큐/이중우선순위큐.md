b# [level 3] 야근 지수 - 42627번

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/42627) 


### 구분

코딩테스트 연습 > 힙(Heap)

### 채점결과

<pre class="console-content"><div></div><div class="console-heading">채점을 시작합니다.</div><div class="console-message">정확성  테스트</div><table class="console-test-group" data-category="correctness"><tbody><tr data-testcase-id="32913"><td valign="top" class="td-label">테스트 1 <span>〉</span></td><td class="result passed">통과 (0.02ms, 8.94MB)</td></tr><tr data-testcase-id="32914"><td valign="top" class="td-label">테스트 2 <span>〉</span></td><td class="result passed">통과 (0.02ms, 9.13MB)</td></tr><tr data-testcase-id="32915"><td valign="top" class="td-label">테스트 3 <span>〉</span></td><td class="result passed">통과 (0.05ms, 9.04MB)</td></tr><tr data-testcase-id="32916"><td valign="top" class="td-label">테스트 4 <span>〉</span></td><td class="result passed">통과 (0.02ms, 8.9MB)</td></tr><tr data-testcase-id="32917"><td valign="top" class="td-label">테스트 5 <span>〉</span></td><td class="result passed">통과 (0.02ms, 9.02MB)</td></tr><tr data-testcase-id="32918"><td valign="top" class="td-label">테스트 6 <span>〉</span></td><td class="result passed">통과 (0.03ms, 9.11MB)</td></tr><tr data-testcase-id="243224"><td valign="top" class="td-label">테스트 7 <span>〉</span></td><td class="result passed">통과 (1099.99ms, 15.4MB)</td></tr><tr data-testcase-id="243367"><td valign="top" class="td-label">테스트 8 <span>〉</span></td><td class="result passed">통과 (0.02ms, 9.07MB)</td></tr><tr data-testcase-id="243368"><td valign="top" class="td-label">테스트 9 <span>〉</span></td><td class="result passed">통과 (0.02ms, 9.19MB)</td></tr><tr data-testcase-id="243369"><td valign="top" class="td-label">테스트 10 <span>〉</span></td><td class="result passed">통과 (0.02ms, 9.05MB)</td></tr></tbody></table><div class="console-heading">채점 결과</div><div class="console-message">정확성: 100.0</div><div class="console-message">합계: 100.0 / 100.0</div></pre>

<div class="tab-pane fade active show" id="tour2">
      <div class="guide-section-description">
        <h6 class="guide-section-title">문제 설명</h6>
        <div class="markdown solarized-dark"><p>이중 우선순위 큐는 다음 연산을 할 수 있는 자료구조를 말합니다.</p>
<table class="table">
        <thead><tr>
<th>명령어</th>
<th>수신 탑(높이)</th>
</tr>
</thead>
        <tbody><tr>
<td>I 숫자</td>
<td>큐에 주어진 숫자를 삽입합니다.</td>
</tr>
<tr>
<td>D 1</td>
<td>큐에서 최댓값을 삭제합니다.</td>
</tr>
<tr>
<td>D -1</td>
<td>큐에서 최솟값을 삭제합니다.</td>
</tr>
</tbody>
      </table>
<p>이중 우선순위 큐가 할 연산 operations가 매개변수로 주어질 때, 모든 연산을 처리한 후 큐가 비어있으면 [0,0] 비어있지 않으면 [최댓값, 최솟값]을 return 하도록 solution 함수를 구현해주세요.</p>

<h5>제한사항</h5>

<ul>
<li>operations는 길이가 1 이상 1,000,000 이하인 문자열 배열입니다.</li>
<li>operations의 원소는 큐가 수행할 연산을 나타냅니다.

<ul>
<li>원소는 “명령어 데이터” 형식으로 주어집니다.- 최댓값/최솟값을 삭제하는 연산에서 최댓값/최솟값이 둘 이상인 경우, 하나만 삭제합니다.</li>
</ul></li>
<li>빈 큐에 데이터를 삭제하라는 연산이 주어질 경우, 해당 연산은 무시합니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>operations</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]</td>
<td>[0,0]</td>
</tr>
<tr>
<td>["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]</td>
<td>[333, -45]</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>16과 -5643을 삽입합니다.</li>
<li>최솟값을 삭제합니다. -5643이 삭제되고 16이 남아있습니다.</li>
<li>최댓값을 삭제합니다. 16이 삭제되고 이중 우선순위 큐는 비어있습니다.</li>
<li>우선순위 큐가 비어있으므로 최댓값 삭제 연산이 무시됩니다.</li>
<li>123을 삽입합니다.</li>
<li>최솟값을 삭제합니다. 123이 삭제되고 이중 우선순위 큐는 비어있습니다.</li>
</ul>

<p>따라서 [0, 0]을 반환합니다.</p>

<p>입출력 예 #2</p>

<ul>
<li>-45와 653을 삽입후 최댓값(653)을 삭제합니다. -45가 남아있습니다.</li>
<li>-642, 45, 97을 삽입 후 최댓값(97), 최솟값(-642)을 삭제합니다. -45와 45가 남아있습니다.</li>
<li>333을 삽입합니다.</li>
</ul>

<p>이중 우선순위 큐에 -45, 45, 333이 남아있으므로, [333, -45]를 반환합니다.</p>

<hr>

<p>※ 공지 - 2024년 7월 22일 테스트케이스가 추가되었습니다. 기존에 제출한 코드가 통과하지 못할 수도 있습니다.</p>
</div>
      </div>
    </div>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges

## 💡 풀이 핵심

이게 시간 초과 없이 왜 되지....</br>
정렬만 잘 해주면 된다