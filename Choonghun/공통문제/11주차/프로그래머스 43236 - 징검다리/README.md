# [level 4] 징검다리 - 43236번

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/43236) 


### 구분

코딩테스트 연습 > 이분탐색

### 채점결과

<pre class="console-content"><div></div><div class="console-heading">채점을 시작합니다.</div><div class="console-message">정확성  테스트</div><table class="console-test-group" data-category="correctness"><tbody><tr data-testcase-id="33119"><td valign="top" class="td-label">테스트 1 <span>〉</span></td><td class="result passed">통과 (0.10ms, 11.4MB)</td></tr><tr data-testcase-id="33120"><td valign="top" class="td-label">테스트 2 <span>〉</span></td><td class="result passed">통과 (0.10ms, 11.3MB)</td></tr><tr data-testcase-id="33121"><td valign="top" class="td-label">테스트 3 <span>〉</span></td><td class="result passed">통과 (0.15ms, 11.4MB)</td></tr><tr data-testcase-id="33122"><td valign="top" class="td-label">테스트 4 <span>〉</span></td><td class="result passed">통과 (5.17ms, 11.5MB)</td></tr><tr data-testcase-id="33123"><td valign="top" class="td-label">테스트 5 <span>〉</span></td><td class="result passed">통과 (4.71ms, 11.5MB)</td></tr><tr data-testcase-id="33124"><td valign="top" class="td-label">테스트 6 <span>〉</span></td><td class="result passed">통과 (50.63ms, 13.5MB)</td></tr><tr data-testcase-id="33125"><td valign="top" class="td-label">테스트 7 <span>〉</span></td><td class="result passed">통과 (77.09ms, 13.5MB)</td></tr><tr data-testcase-id="33126"><td valign="top" class="td-label">테스트 8 <span>〉</span></td><td class="result passed">통과 (67.52ms, 13.6MB)</td></tr><tr data-testcase-id="64834"><td valign="top" class="td-label">테스트 9 <span>〉</span></td><td class="result passed">통과 (0.01ms, 11.2MB)</td></tr><tr data-testcase-id="208764"><td valign="top" class="td-label">테스트 10 <span>〉</span></td><td class="result passed">통과 (0.03ms, 11.3MB)</td></tr><tr data-testcase-id="208765"><td valign="top" class="td-label">테스트 11 <span>〉</span></td><td class="result passed">통과 (0.02ms, 11.3MB)</td></tr><tr data-testcase-id="208766"><td valign="top" class="td-label">테스트 12 <span>〉</span></td><td class="result passed">통과 (0.02ms, 11.7MB)</td></tr><tr data-testcase-id="208767"><td valign="top" class="td-label">테스트 13 <span>〉</span></td><td class="result passed">통과 (0.01ms, 11.3MB)</td></tr><tr data-testcase-id="208768"><td valign="top" class="td-label">테스트 14 <span>〉</span></td><td class="result passed">통과 (0.04ms, 11.6MB)</td></tr><tr data-testcase-id="208769"><td valign="top" class="td-label">테스트 15 <span>〉</span></td><td class="result passed">통과 (0.01ms, 11.4MB)</td></tr><tr data-testcase-id="208770"><td valign="top" class="td-label">테스트 16 <span>〉</span></td><td class="result passed">통과 (0.02ms, 11.6MB)</td></tr><tr data-testcase-id="208771"><td valign="top" class="td-label">테스트 17 <span>〉</span></td><td class="result passed">통과 (0.07ms, 11.3MB)</td></tr><tr data-testcase-id="208772"><td valign="top" class="td-label">테스트 18 <span>〉</span></td><td class="result passed">통과 (0.01ms, 11.4MB)</td></tr><tr data-testcase-id="208773"><td valign="top" class="td-label">테스트 19 <span>〉</span></td><td class="result passed">통과 (0.02ms, 11.2MB)</td></tr><tr data-testcase-id="208774"><td valign="top" class="td-label">테스트 20 <span>〉</span></td><td class="result passed">통과 (44.13ms, 13.1MB)</td></tr><tr data-testcase-id="208775"><td valign="top" class="td-label">테스트 21 <span>〉</span></td><td class="result passed">통과 (4.86ms, 11.6MB)</td></tr><tr data-testcase-id="208776"><td valign="top" class="td-label">테스트 22 <span>〉</span></td><td class="result passed">통과 (38.26ms, 12.8MB)</td></tr><tr data-testcase-id="208777"><td valign="top" class="td-label">테스트 23 <span>〉</span></td><td class="result passed">통과 (33.95ms, 12.5MB)</td></tr><tr data-testcase-id="208778"><td valign="top" class="td-label">테스트 24 <span>〉</span></td><td class="result passed">통과 (58.61ms, 13.4MB)</td></tr><tr data-testcase-id="208779"><td valign="top" class="td-label">테스트 25 <span>〉</span></td><td class="result passed">통과 (3.98ms, 11.4MB)</td></tr><tr data-testcase-id="208780"><td valign="top" class="td-label">테스트 26 <span>〉</span></td><td class="result passed">통과 (17.67ms, 12MB)</td></tr><tr data-testcase-id="208781"><td valign="top" class="td-label">테스트 27 <span>〉</span></td><td class="result passed">통과 (27.37ms, 12.6MB)</td></tr><tr data-testcase-id="208782"><td valign="top" class="td-label">테스트 28 <span>〉</span></td><td class="result passed">통과 (2.73ms, 11.4MB)</td></tr><tr data-testcase-id="208783"><td valign="top" class="td-label">테스트 29 <span>〉</span></td><td class="result passed">통과 (9.67ms, 12MB)</td></tr><tr data-testcase-id="208784"><td valign="top" class="td-label">테스트 30 <span>〉</span></td><td class="result passed">통과 (31.46ms, 12.2MB)</td></tr><tr data-testcase-id="208785"><td valign="top" class="td-label">테스트 31 <span>〉</span></td><td class="result passed">통과 (52.36ms, 13MB)</td></tr><tr data-testcase-id="208786"><td valign="top" class="td-label">테스트 32 <span>〉</span></td><td class="result passed">통과 (2.79ms, 11.4MB)</td></tr><tr data-testcase-id="208787"><td valign="top" class="td-label">테스트 33 <span>〉</span></td><td class="result passed">통과 (46.17ms, 12.4MB)</td></tr><tr data-testcase-id="208788"><td valign="top" class="td-label">테스트 34 <span>〉</span></td><td class="result passed">통과 (78.89ms, 13.6MB)</td></tr><tr data-testcase-id="208789"><td valign="top" class="td-label">테스트 35 <span>〉</span></td><td class="result passed">통과 (3.50ms, 11.6MB)</td></tr><tr data-testcase-id="208790"><td valign="top" class="td-label">테스트 36 <span>〉</span></td><td class="result passed">통과 (23.73ms, 12.1MB)</td></tr><tr data-testcase-id="208791"><td valign="top" class="td-label">테스트 37 <span>〉</span></td><td class="result passed">통과 (1.10ms, 11.4MB)</td></tr><tr data-testcase-id="208792"><td valign="top" class="td-label">테스트 38 <span>〉</span></td><td class="result passed">통과 (2.78ms, 11.5MB)</td></tr><tr data-testcase-id="208793"><td valign="top" class="td-label">테스트 39 <span>〉</span></td><td class="result passed">통과 (44.07ms, 13.2MB)</td></tr></tbody></table><div class="console-heading">채점 결과</div><div class="console-message">정확성: 100.0</div><div class="console-message">합계: 100.0 / 100.0</div></pre>

### 문제 설명

<div class="guide-section" style="width: calc(69.5254% - 12px);">
      <div class="tab-pane fade active show" id="tour2">
        <div class="guide-section-description">
          <h6 class="guide-section-title">
            문제 설명
          </h6>
          <div class="markdown solarized-dark"><p>출발지점부터 distance만큼 떨어진 곳에 도착지점이 있습니다. 그리고 그사이에는 바위들이 놓여있습니다. 바위 중 몇 개를 제거하려고 합니다.<br>
예를 들어, 도착지점이 25만큼 떨어져 있고, 바위가 [2, 14, 11, 21, 17] 지점에 놓여있을 때 바위 2개를 제거하면 출발지점, 도착지점, 바위 간의 거리가 아래와 같습니다.</p>
<table class="table">
        <thead><tr>
<th>제거한 바위의 위치</th>
<th>각 바위 사이의 거리</th>
<th>거리의 최솟값</th>
</tr>
</thead>
        <tbody><tr>
<td>[21, 17]</td>
<td>[2, 9, 3, 11]</td>
<td>2</td>
</tr>
<tr>
<td>[2, 21]</td>
<td>[11, 3, 3, 8]</td>
<td>3</td>
</tr>
<tr>
<td>[2, 11]</td>
<td>[14, 3, 4, 4]</td>
<td>3</td>
</tr>
<tr>
<td>[11, 21]</td>
<td>[2, 12, 3, 8]</td>
<td>2</td>
</tr>
<tr>
<td>[2, 14]</td>
<td>[11, 6, 4, 4]</td>
<td>4</td>
</tr>
</tbody>
      </table>
<p>위에서 구한 거리의 최솟값 중에 가장 큰 값은 4입니다.</p>

<p>출발지점부터 도착지점까지의 거리 distance, 바위들이 있는 위치를 담은 배열 rocks, 제거할 바위의 수 n이 매개변수로 주어질 때, 바위를 n개 제거한 뒤 각 지점 사이의 거리의 최솟값 중에 가장 큰 값을 return 하도록 solution 함수를 작성해주세요.</p>

<h5>제한사항</h5>

<ul>
<li>도착지점까지의 거리 distance는 1 이상 1,000,000,000 이하입니다.</li>
<li>바위는 1개 이상 50,000개 이하가 있습니다.</li>
<li>n 은 1 이상 <code>바위의 개수</code> 이하입니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>distance</th>
<th>rocks</th>
<th>n</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>25</td>
<td>[2, 14, 11, 21, 17]</td>
<td>2</td>
<td>4</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>문제에 나온 예와 같습니다.</p>

<p><a href="http://contest.usaco.org/DEC06.htm" target="_blank" rel="noopener">출처</a></p>

<p>※ 공지 - 2020년 2월 17일 테스트케이스가 추가되었습니다.<br>
※ 공지 - 2023년 5월 15일 테스트케이스가 추가되었습니다. 기존에 제출한 코드가 통과하지 못할 수도 있습니다.</p>
</div>
        </div>
      </div>

## 💡 풀이 핵심

결과값을 이분탐색을 통해 찾는다.</br>
n개의 바위를 제거하여 구할 수 있는 최소 간격 중 최댓값을 구하는데</br>
구간 1 ~ distance 범위 내에서 이분탐색을 진행한다.</br>
Left와 Right의 중앙값(mid)을 최소 간격이라고 상정하고</br>
모든 바위를 순회하며 해당 간격보다 작은 간격을 가진 바위를 발견하면 제거하는 방식이다.</br></br>
최소 간격을 만족시키는데 제거해야 하는 바위의 개수를 구하여<br/>
제거된 바위의 개수가 n보다 크면 간격을 더 줄이기 위해 r을 mid-1로 갱신하고<br/>
n과 같거나 작다면 정답을 m으로 갱신하되 최댓값을 구해야하므로 l을 mid+1로 갱신하여<br/>
정답이 가능한 한 더 큰 값을 찾을 수 있도록 한다.