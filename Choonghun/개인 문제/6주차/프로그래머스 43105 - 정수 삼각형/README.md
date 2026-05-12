# [level 3] 정수 삼각형 - 43105번

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/43105) 


### 구분

코딩테스트 연습 > 동적계획법(Dynamic Programming)

### 채점결과

<pre class="console-content"><div></div><div class="console-heading">채점을 시작합니다.</div><div class="console-message">정확성  테스트</div><table class="console-test-group" data-category="correctness"><tbody><tr data-testcase-id="30294"><td valign="top" class="td-label">테스트 1 <span>〉</span></td><td class="result passed">통과 (0.01ms, 9.04MB)</td></tr><tr data-testcase-id="30295"><td valign="top" class="td-label">테스트 2 <span>〉</span></td><td class="result passed">통과 (0.01ms, 9.26MB)</td></tr><tr data-testcase-id="30296"><td valign="top" class="td-label">테스트 3 <span>〉</span></td><td class="result passed">통과 (0.03ms, 9.25MB)</td></tr><tr data-testcase-id="30297"><td valign="top" class="td-label">테스트 4 <span>〉</span></td><td class="result passed">통과 (0.06ms, 9.03MB)</td></tr><tr data-testcase-id="33493"><td valign="top" class="td-label">테스트 5 <span>〉</span></td><td class="result passed">통과 (0.46ms, 9.2MB)</td></tr><tr data-testcase-id="33494"><td valign="top" class="td-label">테스트 6 <span>〉</span></td><td class="result passed">통과 (0.13ms, 9.24MB)</td></tr><tr data-testcase-id="33495"><td valign="top" class="td-label">테스트 7 <span>〉</span></td><td class="result passed">통과 (0.46ms, 9.27MB)</td></tr><tr data-testcase-id="33496"><td valign="top" class="td-label">테스트 8 <span>〉</span></td><td class="result passed">통과 (0.10ms, 9.08MB)</td></tr><tr data-testcase-id="33497"><td valign="top" class="td-label">테스트 9 <span>〉</span></td><td class="result passed">통과 (0.01ms, 9.07MB)</td></tr><tr data-testcase-id="33498"><td valign="top" class="td-label">테스트 10 <span>〉</span></td><td class="result passed">통과 (0.06ms, 9.16MB)</td></tr></tbody></table><div class="console-message">효율성  테스트</div><table class="console-test-group" data-category="effectiveness"><tbody><tr data-testcase-id="33483"><td valign="top" class="td-label">테스트 1 <span>〉</span></td><td class="result passed">통과 (15.21ms, 13MB)</td></tr><tr data-testcase-id="33484"><td valign="top" class="td-label">테스트 2 <span>〉</span></td><td class="result passed">통과 (11.58ms, 12.3MB)</td></tr><tr data-testcase-id="33485"><td valign="top" class="td-label">테스트 3 <span>〉</span></td><td class="result passed">통과 (17.24ms, 13.6MB)</td></tr><tr data-testcase-id="33486"><td valign="top" class="td-label">테스트 4 <span>〉</span></td><td class="result passed">통과 (15.70ms, 13MB)</td></tr><tr data-testcase-id="33487"><td valign="top" class="td-label">테스트 5 <span>〉</span></td><td class="result passed">통과 (18.46ms, 12.9MB)</td></tr><tr data-testcase-id="33488"><td valign="top" class="td-label">테스트 6 <span>〉</span></td><td class="result passed">통과 (18.05ms, 13.8MB)</td></tr><tr data-testcase-id="33489"><td valign="top" class="td-label">테스트 7 <span>〉</span></td><td class="result passed">통과 (16.88ms, 13.3MB)</td></tr><tr data-testcase-id="33490"><td valign="top" class="td-label">테스트 8 <span>〉</span></td><td class="result passed">통과 (13.92ms, 12.6MB)</td></tr><tr data-testcase-id="33491"><td valign="top" class="td-label">테스트 9 <span>〉</span></td><td class="result passed">통과 (17.09ms, 12.8MB)</td></tr><tr data-testcase-id="33492"><td valign="top" class="td-label">테스트 10 <span>〉</span></td><td class="result passed">통과 (18.31ms, 13.3MB)</td></tr></tbody></table><div class="console-heading">채점 결과</div><div class="console-message">정확성: 64.3</div><div class="console-message">효율성: 35.7</div><div class="console-message">합계: 100.0 / 100.0</div></pre>

<div class="guide-section" style="width: calc(98.6957% - 12px);">
    <div class="tab-pane fade active show" id="tour2">
      <div class="guide-section-description">
        <h6 class="guide-section-title">문제 설명</h6>
        <div class="markdown solarized-dark"><p><img src="https://asset.programmers.co.kr/files/production/97ec02cc39/296a0863-a418-431d-9e8c-e57f7a9722ac.png" title="" alt="스크린샷 2018-09-14 오후 5.44.19.png"></p>

<p>위와 같은 삼각형의 꼭대기에서 바닥까지 이어지는 경로 중, 거쳐간 숫자의 합이 가장 큰 경우를 찾아보려고 합니다. 아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능합니다. 예를 들어 3에서는 그 아래칸의 8 또는 1로만 이동이 가능합니다.</p>

<p>삼각형의 정보가 담긴 배열 triangle이 매개변수로 주어질 때, 거쳐간 숫자의 최댓값을 return 하도록 solution 함수를 완성하세요.</p>

<h5>제한사항</h5>

<ul>
<li>삼각형의 높이는 1 이상 500 이하입니다.</li>
<li>삼각형을 이루고 있는 숫자는 0 이상 9,999 이하의 정수입니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>triangle</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]</td>
<td>30</td>
</tr>
</tbody>
      </table></div>
      </div>
    </div>


</div>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges

## 💡 풀이 핵심

정답률이 높아서 방심한 문제</br>
DP 배열 따로 만들면 안 되고</br>
주어진 triangle 배열 그대로 역순으로 dp 진행하는 문제</br>