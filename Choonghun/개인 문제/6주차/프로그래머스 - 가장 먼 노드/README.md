# [level 3] 가장 먼 노드 - 42586번

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/42586) 


### 구분

코딩테스트 연습 > 그래프(Graph)

### 채점결과

<pre class="console-content"><div></div><div class="console-heading">채점을 시작합니다.</div><div class="console-message">정확성  테스트</div><table class="console-test-group" data-category="correctness"><tbody><tr data-testcase-id="32686"><td valign="top" class="td-label">테스트 1 <span>〉</span></td><td class="result passed">통과 (0.01ms, 9.05MB)</td></tr><tr data-testcase-id="32687"><td valign="top" class="td-label">테스트 2 <span>〉</span></td><td class="result passed">통과 (0.03ms, 9.28MB)</td></tr><tr data-testcase-id="33176"><td valign="top" class="td-label">테스트 3 <span>〉</span></td><td class="result passed">통과 (0.02ms, 9.28MB)</td></tr><tr data-testcase-id="33177"><td valign="top" class="td-label">테스트 4 <span>〉</span></td><td class="result passed">통과 (0.02ms, 9.12MB)</td></tr><tr data-testcase-id="33178"><td valign="top" class="td-label">테스트 5 <span>〉</span></td><td class="result passed">통과 (0.01ms, 9.09MB)</td></tr><tr data-testcase-id="33179"><td valign="top" class="td-label">테스트 6 <span>〉</span></td><td class="result passed">통과 (0.01ms, 9.23MB)</td></tr><tr data-testcase-id="33180"><td valign="top" class="td-label">테스트 7 <span>〉</span></td><td class="result passed">통과 (0.04ms, 9.07MB)</td></tr><tr data-testcase-id="33181"><td valign="top" class="td-label">테스트 8 <span>〉</span></td><td class="result passed">통과 (0.01ms, 9.08MB)</td></tr><tr data-testcase-id="33182"><td valign="top" class="td-label">테스트 9 <span>〉</span></td><td class="result passed">통과 (0.02ms, 8.97MB)</td></tr><tr data-testcase-id="33183"><td valign="top" class="td-label">테스트 10 <span>〉</span></td><td class="result passed">통과 (0.02ms, 9.11MB)</td></tr><tr data-testcase-id="77620"><td valign="top" class="td-label">테스트 11 <span>〉</span></td><td class="result passed">통과 (0.01ms, 9.2MB)</td></tr></tbody></table><div class="console-heading">채점 결과</div><div class="console-message">정확성: 100.0</div><div class="console-message">합계: 100.0 / 100.0</div></pre>

<div class="tab-pane fade active show" id="tour2">
      <div class="guide-section-description">
        <h6 class="guide-section-title">문제 설명</h6>
        <div class="markdown solarized-dark"><p>n개의 노드가 있는 그래프가 있습니다. 각 노드는 1부터 n까지 번호가 적혀있습니다. 1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 합니다. 가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미합니다.</p>

<p>노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때, 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 하도록 solution 함수를 작성해주세요.</p>

<h5>제한사항</h5>

<ul>
<li>노드의 개수 n은 2 이상 20,000 이하입니다.</li>
<li>간선은 양방향이며 총 1개 이상 50,000개 이하의 간선이 있습니다.</li>
<li>vertex 배열 각 행 [a, b]는 a번 노드와 b번 노드 사이에 간선이 있다는 의미입니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>n</th>
<th>vertex</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>6</td>
<td>[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]</td>
<td>3</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>예제의 그래프를 표현하면 아래 그림과 같고, 1번 노드에서 가장 멀리 떨어진 노드는 4,5,6번 노드입니다.</p>

<p><img src="https://asset.programmers.co.kr/files/ybm/fadbae38bb/dec85ab5-0273-47b3-ba73-fc0b5f6be28a.png" title="" alt="image.png"></p>
</div>
      </div>
    </div>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges

## 💡 풀이 핵심

다익스트라 딸깍