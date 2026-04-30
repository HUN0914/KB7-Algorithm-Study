# [level 3] 섬 연결하기 - 42861번

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/42861) 


### 구분

코딩테스트 연습 > 탐욕법 (Greedy)

### 채점결과

<div id="output-wrapper"><pre class="console-content"><div></div><div class="console-heading">채점을 시작합니다.</div><div class="console-message">정확성  테스트</div><table class="console-test-group" data-category="correctness"><tbody><tr data-testcase-id="32093"><td valign="top" class="td-label">테스트 1 <span>〉</span></td><td class="result passed">통과 (0.01ms, 9.29MB)</td></tr><tr data-testcase-id="32094"><td valign="top" class="td-label">테스트 2 <span>〉</span></td><td class="result passed">통과 (0.01ms, 9.29MB)</td></tr><tr data-testcase-id="32095"><td valign="top" class="td-label">테스트 3 <span>〉</span></td><td class="result passed">통과 (0.04ms, 9.19MB)</td></tr><tr data-testcase-id="32096"><td valign="top" class="td-label">테스트 4 <span>〉</span></td><td class="result passed">통과 (0.06ms, 9.31MB)</td></tr><tr data-testcase-id="32097"><td valign="top" class="td-label">테스트 5 <span>〉</span></td><td class="result passed">통과 (0.04ms, 9.34MB)</td></tr><tr data-testcase-id="32098"><td valign="top" class="td-label">테스트 6 <span>〉</span></td><td class="result passed">통과 (0.08ms, 9.2MB)</td></tr><tr data-testcase-id="32099"><td valign="top" class="td-label">테스트 7 <span>〉</span></td><td class="result passed">통과 (0.07ms, 9.34MB)</td></tr><tr data-testcase-id="32100"><td valign="top" class="td-label">테스트 8 <span>〉</span></td><td class="result passed">통과 (0.03ms, 9.21MB)</td></tr></tbody></table><div class="console-heading">채점 결과</div><div class="console-message">정확성: 100.0</div><div class="console-message">합계: 100.0 / 100.0</div></pre></div>

<div class="guide-section" style="width: calc(93.9454% - 12px);">
    <div class="tab-pane fade active show" id="tour2">
      <div class="guide-section-description">
        <h6 class="guide-section-title">문제 설명</h6>
        <div class="markdown solarized-dark"><p>n개의 섬 사이에 다리를 건설하는 비용(costs)이 주어질 때, 최소의 비용으로 모든 섬이 서로 통행 가능하도록 만들 때 필요한 최소 비용을 return 하도록 solution을 완성하세요.</p>

<p>다리를 여러 번 건너더라도, 도달할 수만 있으면 통행 가능하다고 봅니다. 예를 들어 A 섬과 B 섬 사이에 다리가 있고, B 섬과 C 섬 사이에 다리가 있으면 A 섬과 C 섬은 서로 통행 가능합니다.</p>

<p><strong>제한사항</strong></p>

<ul>
<li>섬의 개수 n은 1 이상 100 이하입니다.</li>
<li>costs의 길이는 <code>((n-1) * n) / 2</code>이하입니다.</li>
<li>임의의 i에 대해, costs[i][0] 와 costs[i] [1]에는 다리가 연결되는 두 섬의 번호가 들어있고, costs[i] [2]에는 이 두 섬을 연결하는 다리를 건설할 때 드는 비용입니다.</li>
<li>같은 연결은 두 번 주어지지 않습니다. 또한 순서가 바뀌더라도 같은 연결로 봅니다. 즉 0과 1 사이를 연결하는 비용이 주어졌을 때, 1과 0의 비용이 주어지지 않습니다.</li>
<li>모든 섬 사이의 다리 건설 비용이 주어지지 않습니다. 이 경우, 두 섬 사이의 건설이 불가능한 것으로 봅니다.</li>
<li>연결할 수 없는 섬은 주어지지 않습니다.</li>
</ul>

<p><strong>입출력 예</strong></p>
<table class="table">
        <thead><tr>
<th>n</th>
<th>costs</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>4</td>
<td>[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]</td>
<td>4</td>
</tr>
</tbody>
      </table>
<p><strong>입출력 예 설명</strong></p>

<p>costs를 그림으로 표현하면 다음과 같으며, 이때 초록색 경로로 연결하는 것이 가장 적은 비용으로 모두를 통행할 수 있도록 만드는 방법입니다.</p>

<p><img src="https://grepp-programmers.s3.amazonaws.com/files/production/13e2952057/f2746a8c-527c-4451-9a73-42129911fe17.png" title="" alt="image.png"></p>
</div>
</div>
</div>



> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges

## 💡 풀이 핵심

대놓고 최소 간선 비용 구하라는 문제</br>
[프림](https://8iggy.tistory.com/159)이나 [크루스칼](https://velog.io/@sy508011/%EA%B7%B8%EB%9E%98%ED%94%84-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%ED%81%AC%EB%A3%A8%EC%8A%A4%EC%B9%BC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Kruskal-Algorithm) 둘 중 하나 골라서 쓰면 되는데</br>
크루스칼 까먹어서 인터넷에서 찾음...</br>