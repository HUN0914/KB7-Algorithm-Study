# [level 3] 미로 탈출 명령어 - 150365번

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/150365) 


### 구분

코딩테스트 연습 > 2023 KAKAO BLIND RECRUITMENT

### 채점결과

<pre class="console-content"><div></div><div class="console-heading">채점을 시작합니다.</div><div class="console-message">정확성  테스트</div><table class="console-test-group" data-category="correctness"><tbody><tr data-testcase-id="150047"><td valign="top" class="td-label">테스트 1 <span>〉</span></td><td class="result passed">통과 (0.13ms, 9.09MB)</td></tr><tr data-testcase-id="150048"><td valign="top" class="td-label">테스트 2 <span>〉</span></td><td class="result passed">통과 (0.14ms, 9.24MB)</td></tr><tr data-testcase-id="150049"><td valign="top" class="td-label">테스트 3 <span>〉</span></td><td class="result passed">통과 (0.00ms, 8.83MB)</td></tr><tr data-testcase-id="150050"><td valign="top" class="td-label">테스트 4 <span>〉</span></td><td class="result passed">통과 (0.02ms, 9.2MB)</td></tr><tr data-testcase-id="150051"><td valign="top" class="td-label">테스트 5 <span>〉</span></td><td class="result passed">통과 (0.02ms, 9.1MB)</td></tr><tr data-testcase-id="150052"><td valign="top" class="td-label">테스트 6 <span>〉</span></td><td class="result passed">통과 (0.01ms, 8.84MB)</td></tr><tr data-testcase-id="150053"><td valign="top" class="td-label">테스트 7 <span>〉</span></td><td class="result passed">통과 (0.01ms, 8.96MB)</td></tr><tr data-testcase-id="150054"><td valign="top" class="td-label">테스트 8 <span>〉</span></td><td class="result passed">통과 (0.02ms, 9.3MB)</td></tr><tr data-testcase-id="150055"><td valign="top" class="td-label">테스트 9 <span>〉</span></td><td class="result passed">통과 (2.89ms, 11.7MB)</td></tr><tr data-testcase-id="150056"><td valign="top" class="td-label">테스트 10 <span>〉</span></td><td class="result passed">통과 (3.44ms, 11.9MB)</td></tr><tr data-testcase-id="150057"><td valign="top" class="td-label">테스트 11 <span>〉</span></td><td class="result passed">통과 (3.63ms, 11.9MB)</td></tr><tr data-testcase-id="150058"><td valign="top" class="td-label">테스트 12 <span>〉</span></td><td class="result passed">통과 (3.77ms, 11.7MB)</td></tr><tr data-testcase-id="150059"><td valign="top" class="td-label">테스트 13 <span>〉</span></td><td class="result passed">통과 (2.50ms, 11.6MB)</td></tr><tr data-testcase-id="150060"><td valign="top" class="td-label">테스트 14 <span>〉</span></td><td class="result passed">통과 (2.56ms, 11.7MB)</td></tr><tr data-testcase-id="150061"><td valign="top" class="td-label">테스트 15 <span>〉</span></td><td class="result passed">통과 (2.63ms, 11.9MB)</td></tr><tr data-testcase-id="150062"><td valign="top" class="td-label">테스트 16 <span>〉</span></td><td class="result passed">통과 (3.93ms, 11.9MB)</td></tr><tr data-testcase-id="150063"><td valign="top" class="td-label">테스트 17 <span>〉</span></td><td class="result passed">통과 (2.74ms, 11.7MB)</td></tr><tr data-testcase-id="150064"><td valign="top" class="td-label">테스트 18 <span>〉</span></td><td class="result passed">통과 (3.74ms, 11.6MB)</td></tr><tr data-testcase-id="150065"><td valign="top" class="td-label">테스트 19 <span>〉</span></td><td class="result passed">통과 (3.71ms, 11.8MB)</td></tr><tr data-testcase-id="150066"><td valign="top" class="td-label">테스트 20 <span>〉</span></td><td class="result passed">통과 (2.62ms, 11.9MB)</td></tr><tr data-testcase-id="150067"><td valign="top" class="td-label">테스트 21 <span>〉</span></td><td class="result passed">통과 (2.62ms, 11.8MB)</td></tr><tr data-testcase-id="150068"><td valign="top" class="td-label">테스트 22 <span>〉</span></td><td class="result passed">통과 (2.64ms, 11.9MB)</td></tr><tr data-testcase-id="150069"><td valign="top" class="td-label">테스트 23 <span>〉</span></td><td class="result passed">통과 (2.64ms, 11.8MB)</td></tr><tr data-testcase-id="150070"><td valign="top" class="td-label">테스트 24 <span>〉</span></td><td class="result passed">통과 (2.54ms, 11.8MB)</td></tr><tr data-testcase-id="150071"><td valign="top" class="td-label">테스트 25 <span>〉</span></td><td class="result passed">통과 (3.74ms, 11.8MB)</td></tr><tr data-testcase-id="150072"><td valign="top" class="td-label">테스트 26 <span>〉</span></td><td class="result passed">통과 (2.54ms, 12MB)</td></tr><tr data-testcase-id="150073"><td valign="top" class="td-label">테스트 27 <span>〉</span></td><td class="result passed">통과 (2.65ms, 12MB)</td></tr><tr data-testcase-id="150074"><td valign="top" class="td-label">테스트 28 <span>〉</span></td><td class="result passed">통과 (2.68ms, 12MB)</td></tr><tr data-testcase-id="150075"><td valign="top" class="td-label">테스트 29 <span>〉</span></td><td class="result passed">통과 (2.52ms, 11.8MB)</td></tr><tr data-testcase-id="150076"><td valign="top" class="td-label">테스트 30 <span>〉</span></td><td class="result passed">통과 (3.15ms, 11.8MB)</td></tr><tr data-testcase-id="150077"><td valign="top" class="td-label">테스트 31 <span>〉</span></td><td class="result passed">통과 (0.00ms, 9.16MB)</td></tr></tbody></table><div class="console-heading">채점 결과</div><div class="console-message">정확성: 100.0</div><div class="console-message">합계: 100.0 / 100.0</div></pre>

<div class="guide-section" style="width: calc(85.0964% - 12px);">
    <div class="tab-pane fade active show" id="tour2">
      <div class="guide-section-description">
        <h6 class="guide-section-title">문제 설명</h6>
        <div class="markdown solarized-dark"><p><code>n</code> x <code>m</code> 격자 미로가 주어집니다. 당신은 미로의 (x, y)에서 출발해 (r, c)로 이동해서 탈출해야 합니다.</p>

<p>단, 미로를 탈출하는 조건이 세 가지 있습니다.</p>

<ol>
<li>격자의 바깥으로는 나갈 수 없습니다.</li>
<li>(x, y)에서 (r, c)까지 이동하는 거리가 총 <code>k</code>여야 합니다. <strong>이때, (x, y)와 (r, c)격자를 포함해, 같은 격자를 두 번 이상 방문해도 됩니다.</strong></li>
<li>미로에서 탈출한 경로를 문자열로 나타냈을 때, 문자열이 사전 순으로 가장 빠른 경로로 탈출해야 합니다.</li>
</ol>

<p>이동 경로는 다음과 같이 문자열로 바꿀 수 있습니다.</p>

<ul>
<li>l: 왼쪽으로 한 칸 이동</li>
<li>r: 오른쪽으로 한 칸 이동</li>
<li>u: 위쪽으로 한 칸 이동</li>
<li>d: 아래쪽으로 한 칸 이동</li>
</ul>

<p>예를 들어, 왼쪽으로 한 칸, 위로 한 칸, 왼쪽으로 한 칸 움직였다면, 문자열 <code>"lul"</code>로 나타낼 수 있습니다.</p>

<p>미로에서는 인접한 상, 하, 좌, 우 격자로 한 칸씩 이동할 수 있습니다.</p>

<p>예를 들어 다음과 같이 3 x 4 격자가 있다고 가정해 보겠습니다.</p>
<div class="highlight"><pre class="codehilite"><code>....
..S.
E...
</code></pre></div>
<p>미로의 좌측 상단은 (1, 1)이고 우측 하단은 (3, 4)입니다. <code>.</code>은 빈 공간, <code>S</code>는 출발 지점, <code>E</code>는 탈출 지점입니다.</p>

<p>탈출까지 이동해야 하는 거리 <code>k</code>가 5라면 다음과 같은 경로로 탈출할 수 있습니다.</p>

<ol>
<li>lldud</li>
<li>ulldd</li>
<li>rdlll</li>
<li>dllrl</li>
<li>dllud</li>
<li>...</li>
</ol>

<p>이때 dllrl보다 사전 순으로 빠른 경로로 탈출할 수는 없습니다.</p>

<p>격자의 크기를 뜻하는 정수 <code>n</code>, <code>m</code>, 출발 위치를 뜻하는 정수 <code>x</code>, <code>y</code>, 탈출 지점을 뜻하는 정수 <code>r</code>, <code>c</code>, 탈출까지 이동해야 하는 거리를 뜻하는 정수 <code>k</code>가 매개변수로 주어집니다. 이때, 미로를 탈출하기 위한 경로를 return 하도록 solution 함수를 완성해주세요. <strong>단, 위 조건대로 미로를 탈출할 수 없는 경우 <code>"impossible"</code>을 return 해야 합니다.</strong></p>

<hr>

<h5>제한사항</h5>

<ul>
<li>2 ≤ <code>n</code> (= 미로의 세로 길이) ≤ 50</li>
<li>2 ≤ <code>m</code> (= 미로의 가로 길이) ≤ 50</li>
<li>1 ≤ <code>x</code> ≤ <code>n</code></li>
<li>1 ≤ <code>y</code> ≤ <code>m</code></li>
<li>1 ≤ <code>r</code> ≤ <code>n</code></li>
<li>1 ≤ <code>c</code> ≤ <code>m</code></li>
<li>(<code>x</code>, <code>y</code>) ≠ (<code>r</code>, <code>c</code>)</li>
<li>1 ≤ <code>k</code> ≤ 2,500</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>n</th>
<th>m</th>
<th>x</th>
<th>y</th>
<th>r</th>
<th>c</th>
<th>k</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>3</td>
<td>4</td>
<td>2</td>
<td>3</td>
<td>3</td>
<td>1</td>
<td>5</td>
<td><code>"dllrl"</code></td>
</tr>
<tr>
<td>2</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td><code>"dr"</code></td>
</tr>
<tr>
<td>3</td>
<td>3</td>
<td>1</td>
<td>2</td>
<td>3</td>
<td>3</td>
<td>4</td>
<td><code>"impossible"</code></td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p><strong>입출력 예 #1</strong></p>

<p>문제 예시와 동일합니다.</p>

<p><strong>입출력 예 #2</strong></p>

<p>미로의 크기는 2 x 2입니다. 출발 지점은 (1, 1)이고, 탈출 지점은 (2, 2)입니다.</p>

<p>빈 공간은 <code>.</code>, 출발 지점을 <code>S</code>, 탈출 지점을 <code>E</code>로 나타내면 다음과 같습니다.</p>
<div class="highlight"><pre class="codehilite"><code>S.
.E
</code></pre></div>
<p>미로의 좌측 상단은 (1, 1)이고 우측 하단은 (2, 2)입니다.</p>

<p>탈출까지 이동해야 하는 거리 <code>k</code>가 2이므로 다음과 같은 경로로 탈출할 수 있습니다.</p>

<ol>
<li>rd</li>
<li>dr</li>
</ol>

<p><code>"dr"</code>이 사전 순으로 가장 빠른 경로입니다. 따라서 <code>"dr"</code>을 return 해야 합니다.</p>

<p><strong>입출력 예 #3</strong></p>

<p>미로의 크기는 3 x 3입니다. 출발 지점은 (1, 2)이고, 탈출 지점은 (3, 3)입니다.</p>

<p>빈 공간은 <code>.</code>, 출발 지점을 <code>S</code>, 탈출 지점을 <code>E</code>로 나타내면 다음과 같습니다.</p>
<div class="highlight"><pre class="codehilite"><code>.S.
...
..E
</code></pre></div>
<p>미로의 좌측 상단은 (1, 1)이고 우측 하단은 (3, 3)입니다.</p>

<p>탈출까지 이동해야 하는 거리 <code>k</code>가 4입니다. 이때, 이동 거리가 4이면서, <code>S</code>에서 <code>E</code>까지 이동할 수 있는 경로는 존재하지 않습니다.</p>

<p>따라서 <code>"impossible"</code>을 return 해야 합니다.</p>
</div>
</div>
</div>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges

## 💡 풀이 핵심

백트랙으로 해야할 것은 알았으나</br>
탐색 조건을 파악하지 못해 많이 헤맨 문제이다.</br>
잉여 이동 횟수가 남은 거리를 충족할 수 없거나</br>
왔다갔다 하여 남은 잉여 이동 횟수를 소비하는 경우를 따져야 했다.</br>