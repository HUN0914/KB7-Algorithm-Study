# [level 3] 보물 지도 - 12690번

[문제 링크](https://school.programmers.co.kr/learn/courses/15009/lessons/121690) 


### 구분

프로그래밍 강의 > PCCP 모의고사 2회

### 채점결과

<pre class="console-content"><div></div><div class="console-failed">같은 코드로 채점한 결과가 있습니다.</div><div class="console-message">정확성  테스트</div><table class="console-test-group" data-category="correctness"><tbody><tr data-testcase-id="140015"><td valign="top" class="td-label">테스트 1 <span>〉</span></td><td class="result passed">통과 (0.01ms, 9.45MB)</td></tr><tr data-testcase-id="140016"><td valign="top" class="td-label">테스트 2 <span>〉</span></td><td class="result passed">통과 (1505.89ms, 69.7MB)</td></tr><tr data-testcase-id="140017"><td valign="top" class="td-label">테스트 3 <span>〉</span></td><td class="result passed">통과 (68.66ms, 14.4MB)</td></tr><tr data-testcase-id="140018"><td valign="top" class="td-label">테스트 4 <span>〉</span></td><td class="result passed">통과 (29.57ms, 13MB)</td></tr><tr data-testcase-id="140019"><td valign="top" class="td-label">테스트 5 <span>〉</span></td><td class="result passed">통과 (17.04ms, 10.1MB)</td></tr><tr data-testcase-id="140020"><td valign="top" class="td-label">테스트 6 <span>〉</span></td><td class="result passed">통과 (773.54ms, 50.9MB)</td></tr><tr data-testcase-id="140021"><td valign="top" class="td-label">테스트 7 <span>〉</span></td><td class="result passed">통과 (35.72ms, 10.6MB)</td></tr><tr data-testcase-id="140022"><td valign="top" class="td-label">테스트 8 <span>〉</span></td><td class="result passed">통과 (268.53ms, 27.1MB)</td></tr><tr data-testcase-id="140023"><td valign="top" class="td-label">테스트 9 <span>〉</span></td><td class="result passed">통과 (129.18ms, 28.7MB)</td></tr><tr data-testcase-id="140024"><td valign="top" class="td-label">테스트 10 <span>〉</span></td><td class="result passed">통과 (216.03ms, 22.7MB)</td></tr><tr data-testcase-id="140025"><td valign="top" class="td-label">테스트 11 <span>〉</span></td><td class="result passed">통과 (1318.87ms, 77.9MB)</td></tr><tr data-testcase-id="140026"><td valign="top" class="td-label">테스트 12 <span>〉</span></td><td class="result passed">통과 (410.12ms, 225MB)</td></tr><tr data-testcase-id="140027"><td valign="top" class="td-label">테스트 13 <span>〉</span></td><td class="result passed">통과 (1162.37ms, 154MB)</td></tr><tr data-testcase-id="140028"><td valign="top" class="td-label">테스트 14 <span>〉</span></td><td class="result passed">통과 (379.12ms, 201MB)</td></tr><tr data-testcase-id="140029"><td valign="top" class="td-label">테스트 15 <span>〉</span></td><td class="result passed">통과 (1909.91ms, 151MB)</td></tr><tr data-testcase-id="140030"><td valign="top" class="td-label">테스트 16 <span>〉</span></td><td class="result passed">통과 (840.32ms, 154MB)</td></tr><tr data-testcase-id="140031"><td valign="top" class="td-label">테스트 17 <span>〉</span></td><td class="result passed">통과 (0.02ms, 9.36MB)</td></tr><tr data-testcase-id="140032"><td valign="top" class="td-label">테스트 18 <span>〉</span></td><td class="result passed">통과 (0.02ms, 9.27MB)</td></tr><tr data-testcase-id="140033"><td valign="top" class="td-label">테스트 19 <span>〉</span></td><td class="result passed">통과 (0.02ms, 9.28MB)</td></tr></tbody></table><div class="console-heading">채점 결과</div><div class="console-message">정확성: 100.0</div><div class="console-message">합계: 100.0 / 100.0</div></pre>

<div class="false" id="tour2">
      <div class="guide-section-description">
        <h6 class="guide-section-title">문제 설명</h6>
        <div class="markdown solarized-dark"><p>진수는 보물이 묻힌 장소와 함정이 표시된 보물 지도를 이용해 보물을 찾으려 합니다. 보물지도는 가로 길이가 <code>n</code>, 세로 길이가 <code>m</code>인 직사각형 모양입니다.</p>

<p>맨 왼쪽 아래 칸의 좌표를 (1, 1)으로, 맨 오른쪽 위 칸의 좌표를 (n, m)으로 나타냈을 때, 보물은 (n, m) 좌표에 묻혀있습니다. 또한, 일부 칸에는 함정이 있으며, 해당 칸으로는 지나갈 수 없습니다.</p>

<p>진수는 처음에 (1, 1) 좌표에서 출발해 보물이 있는 칸으로 이동하려 합니다. 이동할 때는 [상,하,좌,우]로 인접한 네 칸 중 한 칸으로 걸어서 이동합니다. 한 칸을 걸어서 이동하는 데 걸리는 시간은 1입니다.</p>

<p>진수는 보물이 위치한 칸으로 수월하게 이동하기 위해 신비로운 신발을 하나 준비했습니다. 이 신발을 신고 뛰면 한 번에 두 칸을 이동할 수 있으며, 함정이 있는 칸도 넘을 수 있습니다. 하지만, 이 신발은 한 번밖에 사용할 수 없습니다. 신비로운 신발을 사용하여 뛰어서 두 칸을 이동하는 시간도 1입니다.</p>

<p>이때 진수가 출발점에서 보물이 위치한 칸으로 이동하는데 필요한 최소 시간을 구해야 합니다.</p>

<p>예를 들어, 진수의 보물지도가 아래 그림과 같을 때, 진수가 걸어서 오른쪽으로 3칸, 걸어서 위쪽으로 3칸 이동하면 6의 시간에 보물이 위치한 칸으로 이동할 수 있습니다. 만약, 오른쪽으로 걸어서 1칸, 위쪽으로 걸어서 1칸, 신비로운 신발을 사용하여 위로 뛰어 2칸, 오른쪽으로 걸어서 2칸 이동한다면 총 5의 시간에 보물이 위치한 칸으로 이동할 수 있으며, 이보다 빠른 시간 내에 보물이 있는 위치에 도착할 수 없습니다.</p>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/bd10a026-21f5-4e5a-8c26-635d6b81d108/%EC%A7%80%EB%8F%84%201.png" title="" alt="지도 1.png"></p>

<p>진수의 보물지도가 표현하는 지역의 가로 길이를 나타내는 정수 <code>n</code>, 세로 길이를 나타내는 정수 <code>m</code>, 함정의 위치를 나타내는 2차원 정수 배열 <code>hole</code>이 주어졌을 때, 진수가 보물이 있는 칸으로 이동하는데 필요한 최소 시간을 return 하는 solution 함수를 완성해주세요. <strong>단, 보물이 있는 칸으로 이동할 수 없다면, -1을 return 해야 합니다.</strong></p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>n</code>, <code>m</code> ≤ 1,000

<ul>
<li>단, <code>n</code> * <code>m</code>이 3 이상인 경우만 입력으로 주어집니다.</li>
</ul></li>
<li>1 ≤ <code>hole</code>의 길이 ≤ <code>n</code> * <code>m</code> - 2

<ul>
<li><code>hole[i]</code>는 [a, b]의 형태이며, (a, b) 칸에 함정이 존재한다는 의미이며, 1 ≤ a ≤ <code>n</code>, 1 ≤ b ≤ <code>m</code>을 만족합니다.</li>
<li>같은 함정에 대한 정보가 중복해서 들어있지 않습니다.</li>
</ul></li>
<li>(1, 1) 칸과 (n, m) 칸은 항상 함정이 없습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>n</th>
<th>m</th>
<th>hole</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>4</td>
<td>4</td>
<td>[[2, 3], [3, 3]]</td>
<td>5</td>
</tr>
<tr>
<td>5</td>
<td>4</td>
<td>[[1, 4], [2, 1], [2, 2], [2, 3], [2, 4], [3, 3], [4, 1], [4, 3], [5, 3]]</td>
<td>-1</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p><strong>입출력 예 #1</strong></p>

<ul>
<li>본문의 예시와 같습니다.</li>
</ul>

<p><strong>입출력 예 #2</strong></p>

<ul>
<li>보물지도를 그림으로 나타내면 아래와 같으며, 보물이 위치한 칸으로 이동할 수 없습니다. 따라서, -1을 return 해야 합니다.</li>
</ul>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/43c3e7a9-3eea-4899-a805-ee52b4b7a65a/%EC%A7%80%EB%8F%84%202.png" title="" alt="지도 2.png"></p>
</div>
</div>
</div>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges

## 💡 풀이 핵심

신발을 사용 한 경우 / 하지 않은 경우를 나눠서 BFS 진행