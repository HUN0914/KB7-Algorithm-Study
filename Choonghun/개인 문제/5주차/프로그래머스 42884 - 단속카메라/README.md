# [level 3] 단속카메라 - 42884번

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/42884) 


### 구분

코딩테스트 연습 > 탐욕법 (Greedy)

### 채점결과

<pre class="console-content"><div></div><div class="console-heading">채점을 시작합니다.</div><div class="console-message">정확성  테스트</div><table class="console-test-group" data-category="correctness"><tbody><tr data-testcase-id="33465"><td valign="top" class="td-label">테스트 1 <span>〉</span></td><td class="result passed">통과 (0.02ms, 9.12MB)</td></tr><tr data-testcase-id="33466"><td valign="top" class="td-label">테스트 2 <span>〉</span></td><td class="result passed">통과 (0.03ms, 9.25MB)</td></tr><tr data-testcase-id="33467"><td valign="top" class="td-label">테스트 3 <span>〉</span></td><td class="result passed">통과 (0.06ms, 9.25MB)</td></tr><tr data-testcase-id="33468"><td valign="top" class="td-label">테스트 4 <span>〉</span></td><td class="result passed">통과 (0.04ms, 9.1MB)</td></tr><tr data-testcase-id="33469"><td valign="top" class="td-label">테스트 5 <span>〉</span></td><td class="result passed">통과 (0.04ms, 9.22MB)</td></tr></tbody></table><div class="console-message">효율성  테스트</div><table class="console-test-group" data-category="effectiveness"><tbody><tr data-testcase-id="33459"><td valign="top" class="td-label">테스트 1 <span>〉</span></td><td class="result passed">통과 (1.16ms, 9.41MB)</td></tr><tr data-testcase-id="33460"><td valign="top" class="td-label">테스트 2 <span>〉</span></td><td class="result passed">통과 (0.67ms, 9.34MB)</td></tr><tr data-testcase-id="33461"><td valign="top" class="td-label">테스트 3 <span>〉</span></td><td class="result passed">통과 (2.04ms, 9.65MB)</td></tr><tr data-testcase-id="33462"><td valign="top" class="td-label">테스트 4 <span>〉</span></td><td class="result passed">통과 (0.15ms, 9.11MB)</td></tr><tr data-testcase-id="33463"><td valign="top" class="td-label">테스트 5 <span>〉</span></td><td class="result passed">통과 (2.57ms, 9.69MB)</td></tr></tbody></table><div class="console-heading">채점 결과</div><div class="console-message">정확성: 50.0</div><div class="console-message">효율성: 50.0</div><div class="console-message">합계: 100.0 / 100.0</div></pre>

<div class="guide-section-description">
        <h6 class="guide-section-title">문제 설명</h6>
        <div class="markdown solarized-dark"><p>고속도로를 이동하는 모든 차량이 고속도로를 이용하면서 단속용 카메라를 한 번은 만나도록 카메라를 설치하려고 합니다.</p>

<p>고속도로를 이동하는 차량의 경로 routes가 매개변수로 주어질 때, 모든 차량이 한 번은 단속용 카메라를 만나도록 하려면 최소 몇 대의 카메라를 설치해야 하는지를 return 하도록 solution 함수를 완성하세요.</p>

<p><strong>제한사항</strong></p>

<ul>
<li>차량의 대수는 1대 이상 10,000대 이하입니다.</li>
<li>routes에는 차량의 이동 경로가 포함되어 있으며 routes[i][0]에는 i번째 차량이 고속도로에 진입한 지점, routes[i][1]에는 i번째 차량이 고속도로에서 나간 지점이 적혀 있습니다.</li>
<li>차량의 진입/진출 지점에 카메라가 설치되어 있어도 카메라를 만난것으로 간주합니다.</li>
<li>차량의 진입 지점, 진출 지점은 -30,000 이상 30,000 이하입니다.</li>
</ul>

<p><strong>입출력 예</strong></p>
<table class="table">
        <thead><tr>
<th>routes</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>[[-20,-15], [-14,-5], [-18,-13], [-5,-3]]</td>
<td>2</td>
</tr>
</tbody>
      </table>
<p><strong>입출력 예 설명</strong></p>

<p>-5 지점에 카메라를 설치하면 두 번째, 네 번째 차량이 카메라를 만납니다.</p>

<p>-15 지점에 카메라를 설치하면 첫 번째, 세 번째 차량이 카메라를 만납니다.</p>
</div>
      </div>



> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges

## 💡 풀이 핵심

투 포인터