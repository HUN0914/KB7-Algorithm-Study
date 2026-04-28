# [level 4] 도둑질 - 42897번

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/42897) 


### 구분

코딩테스트 연습 > 동적계획법(Dynamic Programming)

### 채점결과

<pre class="console-content"><div></div><div class="console-heading">채점을 시작합니다.</div><div class="console-message">정확성  테스트</div><table class="console-test-group" data-category="correctness"><tbody><tr data-testcase-id="32749"><td valign="top" class="td-label">테스트 1 <span>〉</span></td><td class="result passed">통과 (0.30ms, 9.39MB)</td></tr><tr data-testcase-id="32750"><td valign="top" class="td-label">테스트 2 <span>〉</span></td><td class="result passed">통과 (0.90ms, 9.26MB)</td></tr><tr data-testcase-id="32751"><td valign="top" class="td-label">테스트 3 <span>〉</span></td><td class="result passed">통과 (1.00ms, 9.32MB)</td></tr><tr data-testcase-id="32752"><td valign="top" class="td-label">테스트 4 <span>〉</span></td><td class="result passed">통과 (0.05ms, 9.39MB)</td></tr><tr data-testcase-id="32753"><td valign="top" class="td-label">테스트 5 <span>〉</span></td><td class="result passed">통과 (0.23ms, 9.38MB)</td></tr><tr data-testcase-id="32754"><td valign="top" class="td-label">테스트 6 <span>〉</span></td><td class="result passed">통과 (0.55ms, 9.31MB)</td></tr><tr data-testcase-id="32755"><td valign="top" class="td-label">테스트 7 <span>〉</span></td><td class="result passed">통과 (0.36ms, 9.3MB)</td></tr><tr data-testcase-id="32756"><td valign="top" class="td-label">테스트 8 <span>〉</span></td><td class="result passed">통과 (0.26ms, 9.25MB)</td></tr><tr data-testcase-id="32757"><td valign="top" class="td-label">테스트 9 <span>〉</span></td><td class="result passed">통과 (0.91ms, 9.3MB)</td></tr><tr data-testcase-id="32758"><td valign="top" class="td-label">테스트 10 <span>〉</span></td><td class="result passed">통과 (0.17ms, 9.18MB)</td></tr></tbody></table><div class="console-message">효율성  테스트</div><table class="console-test-group" data-category="effectiveness"><tbody><tr data-testcase-id="32760"><td valign="top" class="td-label">테스트 1 <span>〉</span></td><td class="result passed">통과 (1108.93ms, 176MB)</td></tr><tr data-testcase-id="32761"><td valign="top" class="td-label">테스트 2 <span>〉</span></td><td class="result passed">통과 (971.73ms, 165MB)</td></tr><tr data-testcase-id="32762"><td valign="top" class="td-label">테스트 3 <span>〉</span></td><td class="result passed">통과 (1142.18ms, 172MB)</td></tr><tr data-testcase-id="32763"><td valign="top" class="td-label">테스트 4 <span>〉</span></td><td class="result passed">통과 (1022.40ms, 173MB)</td></tr><tr data-testcase-id="32764"><td valign="top" class="td-label">테스트 5 <span>〉</span></td><td class="result passed">통과 (900.06ms, 146MB)</td></tr><tr data-testcase-id="32765"><td valign="top" class="td-label">테스트 6 <span>〉</span></td><td class="result passed">통과 (974.92ms, 166MB)</td></tr><tr data-testcase-id="32766"><td valign="top" class="td-label">테스트 7 <span>〉</span></td><td class="result passed">통과 (549.89ms, 101MB)</td></tr><tr data-testcase-id="32767"><td valign="top" class="td-label">테스트 8 <span>〉</span></td><td class="result passed">통과 (644.61ms, 104MB)</td></tr><tr data-testcase-id="32768"><td valign="top" class="td-label">테스트 9 <span>〉</span></td><td class="result passed">통과 (668.97ms, 120MB)</td></tr><tr data-testcase-id="32769"><td valign="top" class="td-label">테스트 10 <span>〉</span></td><td class="result passed">통과 (967.56ms, 168MB)</td></tr></tbody></table><div class="console-heading">채점 결과</div><div class="console-message">정확성: 50.0</div><div class="console-message">효율성: 50.0</div><div class="console-message">합계: 100.0 / 100.0</div></pre>

### 제출 일자

2026년 04월 16일 13:02:08

### 문제 설명
<div class="guide-section" style="width: calc(72.0432% - 12px);">
    <div class="tab-pane fade active show" id="tour2">
      <div class="guide-section-description">
        <h6 class="guide-section-title">문제 설명</h6>
        <div class="markdown solarized-dark"><p>도둑이 어느 마을을 털 계획을 하고 있습니다. 이 마을의 모든 집들은 아래 그림과 같이 동그랗게 배치되어 있습니다. </p>

<p><img src="https://grepp-programmers.s3.amazonaws.com/files/ybm/e7dd4f51c3/a228c73d-1cbe-4d59-bb5d-833fd18d3382.png" title="" alt="image.png"></p>

<p>각 집들은 서로 인접한 집들과 방범장치가 연결되어 있기 때문에 인접한 두 집을 털면 경보가 울립니다.</p>

<p>각 집에 있는 돈이 담긴 배열 money가 주어질 때, 도둑이 훔칠 수 있는 돈의 최댓값을 return 하도록 solution 함수를 작성하세요.</p>

<h5>제한사항</h5>

<ul>
<li>이 마을에 있는 집은 3개 이상 1,000,000개 이하입니다.</li>
<li>money 배열의 각 원소는 0 이상 1,000 이하인 정수입니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>money</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>[1, 2, 3, 1]</td>
<td>4</td>
</tr>
</tbody>
      </table></div>
      </div>
    </div>


<div class="submission-history-list-section tab-pane fade" id="submissionHistory">
<div class="submission-history-wrapper">


  
  <script src="https://hera-client.grepp.co/269c0e1cc4ea037ef673.js" defer="defer"></script>
</div>

</div>
</div>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges

## 💡 풀이 핵심

순환하고 인접한 집은 방문하면 안되므로<br/>
핵심은 0번 집을 포함하느냐 하지 않느냐 문제이다<br/>
DP로 접근하면 풀이 자체는 간단하지만<br/>
최댓값을 가져올때 엣지 케이스를 생각해주어야 한다.<br/>