# [level 3] 선입 선출 스케줄링 - 12920번

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12920) 


### 구분

코딩테스트 연습 > 연습문제

### 채점결과

<div id="output" class="console-output tab-pane fade in active show banner">
              <div id="output-wrapper"><pre class="console-content"><div></div><div class="console-heading">채점을 시작합니다.</div><div class="console-message">정확성  테스트</div><table class="console-test-group" data-category="correctness"><tbody><tr data-testcase-id="18649"><td valign="top" class="td-label">테스트 1 <span>〉</span></td><td class="result passed">통과 (0.51ms, 11.6MB)</td></tr><tr data-testcase-id="18650"><td valign="top" class="td-label">테스트 2 <span>〉</span></td><td class="result passed">통과 (1.16ms, 11.3MB)</td></tr><tr data-testcase-id="18651"><td valign="top" class="td-label">테스트 3 <span>〉</span></td><td class="result passed">통과 (0.44ms, 11.3MB)</td></tr><tr data-testcase-id="18652"><td valign="top" class="td-label">테스트 4 <span>〉</span></td><td class="result passed">통과 (1.00ms, 11.4MB)</td></tr><tr data-testcase-id="18653"><td valign="top" class="td-label">테스트 5 <span>〉</span></td><td class="result passed">통과 (5.54ms, 11.4MB)</td></tr><tr data-testcase-id="18654"><td valign="top" class="td-label">테스트 6 <span>〉</span></td><td class="result passed">통과 (1.43ms, 11.6MB)</td></tr><tr data-testcase-id="18655"><td valign="top" class="td-label">테스트 7 <span>〉</span></td><td class="result passed">통과 (1.06ms, 11.3MB)</td></tr><tr data-testcase-id="18656"><td valign="top" class="td-label">테스트 8 <span>〉</span></td><td class="result passed">통과 (3.88ms, 11.6MB)</td></tr><tr data-testcase-id="18657"><td valign="top" class="td-label">테스트 9 <span>〉</span></td><td class="result passed">통과 (0.23ms, 11.5MB)</td></tr><tr data-testcase-id="18658"><td valign="top" class="td-label">테스트 10 <span>〉</span></td><td class="result passed">통과 (0.02ms, 11.4MB)</td></tr><tr data-testcase-id="18659"><td valign="top" class="td-label">테스트 11 <span>〉</span></td><td class="result passed">통과 (0.02ms, 11.5MB)</td></tr><tr data-testcase-id="18660"><td valign="top" class="td-label">테스트 12 <span>〉</span></td><td class="result passed">통과 (8.82ms, 11.5MB)</td></tr><tr data-testcase-id="18661"><td valign="top" class="td-label">테스트 13 <span>〉</span></td><td class="result passed">통과 (1.11ms, 11.6MB)</td></tr><tr data-testcase-id="18662"><td valign="top" class="td-label">테스트 14 <span>〉</span></td><td class="result passed">통과 (0.46ms, 11.5MB)</td></tr></tbody></table><div class="console-message">효율성  테스트</div><table class="console-test-group" data-category="effectiveness"><tbody><tr data-testcase-id="18665"><td valign="top" class="td-label">테스트 1 <span>〉</span></td><td class="result passed">통과 (21.74ms, 11.6MB)</td></tr><tr data-testcase-id="18666"><td valign="top" class="td-label">테스트 2 <span>〉</span></td><td class="result passed">통과 (10.30ms, 11.2MB)</td></tr><tr data-testcase-id="18667"><td valign="top" class="td-label">테스트 3 <span>〉</span></td><td class="result passed">통과 (13.52ms, 11.3MB)</td></tr><tr data-testcase-id="18668"><td valign="top" class="td-label">테스트 4 <span>〉</span></td><td class="result passed">통과 (16.18ms, 11.6MB)</td></tr><tr data-testcase-id="18669"><td valign="top" class="td-label">테스트 5 <span>〉</span></td><td class="result passed">통과 (4.06ms, 11MB)</td></tr><tr data-testcase-id="18670"><td valign="top" class="td-label">테스트 6 <span>〉</span></td><td class="result passed">통과 (8.07ms, 11.2MB)</td></tr></tbody></table><div class="console-heading">채점 결과</div><div class="console-message">정확성: 70.0</div><div class="console-message">효율성: 30.0</div><div class="console-message">합계: 100.0 / 100.0</div></pre></div>
            
</div>

### 문제 설명

<div class="guide-section" style="width: calc(93.7067% - 12px);">
      <div class="tab-pane fade active show" id="tour2">
        <div class="guide-section-description">
          <div class="markdown solarized-dark"><p>처리해야 할 동일한 작업이 n 개가 있고, 이를 처리하기 위한 CPU가 있습니다.</p>

<p>이 CPU는 다음과 같은 특징이 있습니다.</p>

<ul>
<li>CPU에는 여러 개의 코어가 있고, 코어별로 한 작업을 처리하는 시간이 다릅니다.</li>
<li>한 코어에서 작업이 끝나면 작업이 없는 코어가 바로 다음 작업을 수행합니다.</li>
<li>2개 이상의 코어가 남을 경우 앞의 코어부터 작업을 처리 합니다.</li>
</ul>

<p>처리해야 될 작업의 개수 n과, 각 코어의 처리시간이 담긴 배열 cores 가 매개변수로 주어질 때, 마지막 작업을 처리하는 코어의 번호를  return 하는 solution 함수를 완성해주세요.</p>

<h5>제한 사항</h5>

<ul>
<li>코어의 수는 10,000 이하 2이상 입니다.</li>
<li>코어당 작업을 처리하는 시간은 10,000이하 입니다.</li>
<li>처리해야 하는 일의 개수는 50,000개를 넘기지 않습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>n</th>
<th>cores</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>6</td>
<td>[1,2,3]</td>
<td>2</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>입출력 예 #1<br>
처음 3개의 작업은 각각 1,2,3번에 들어가고, 1시간 뒤 1번 코어에 4번째 작업,다시 1시간 뒤 1,2번 코어에 5,6번째 작업이 들어가므로 2를 반환해주면 됩니다.</p>
</div>
</div>
</div>


## 💡 풀이 핵심

이분 탐색을 이용하여 모든 일을 코어에 배정을 마치는데 걸리는 시간을 구한다</br>
이후 해당 시간 직전까지 처리된 일 개수만큼 처음 일에서 뺀 다음</br>
남은 일을 배정 받을 수 있는 모든 코어에 순서대로 배정을 하여 모든 일이 배정되었을 때의 코어의 번호를 반환한다.</br>