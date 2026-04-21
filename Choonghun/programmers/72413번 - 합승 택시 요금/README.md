# [level 3] 합승 택시 요금 - 72413번

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/72413) 

### 구분

코딩테스트 연습 > 2021 KAKAO BLIND RECRUITMENT

### 제출 일자

2026년 04월 19일 18:33:08

### 채점결과

<div id="output-wrapper"><pre class="console-content"><div></div><div class="console-heading">채점을 시작합니다.</div><div class="console-message">정확성  테스트</div><table class="console-test-group" data-category="correctness"><tbody><tr data-testcase-id="88189"><td valign="top" class="td-label">테스트 1 <span>〉</span></td><td class="result passed">통과 (0.06ms, 9.2MB)</td></tr><tr data-testcase-id="88190"><td valign="top" class="td-label">테스트 2 <span>〉</span></td><td class="result passed">통과 (0.09ms, 9.31MB)</td></tr><tr data-testcase-id="88191"><td valign="top" class="td-label">테스트 3 <span>〉</span></td><td class="result passed">통과 (0.11ms, 9.43MB)</td></tr><tr data-testcase-id="88192"><td valign="top" class="td-label">테스트 4 <span>〉</span></td><td class="result passed">통과 (0.31ms, 9.34MB)</td></tr><tr data-testcase-id="88193"><td valign="top" class="td-label">테스트 5 <span>〉</span></td><td class="result passed">통과 (0.33ms, 9.21MB)</td></tr><tr data-testcase-id="88194"><td valign="top" class="td-label">테스트 6 <span>〉</span></td><td class="result passed">통과 (0.50ms, 9.22MB)</td></tr><tr data-testcase-id="88195"><td valign="top" class="td-label">테스트 7 <span>〉</span></td><td class="result passed">통과 (0.67ms, 9.13MB)</td></tr><tr data-testcase-id="88196"><td valign="top" class="td-label">테스트 8 <span>〉</span></td><td class="result passed">통과 (0.82ms, 9.43MB)</td></tr><tr data-testcase-id="88197"><td valign="top" class="td-label">테스트 9 <span>〉</span></td><td class="result passed">통과 (1.13ms, 9.28MB)</td></tr><tr data-testcase-id="88198"><td valign="top" class="td-label">테스트 10 <span>〉</span></td><td class="result passed">통과 (1.45ms, 9.27MB)</td></tr></tbody></table><div class="console-message">효율성  테스트</div><table class="console-test-group" data-category="effectiveness"><tbody><tr data-testcase-id="88199"><td valign="top" class="td-label">테스트 1 <span>〉</span></td><td class="result passed">통과 (205.19ms, 9.57MB)</td></tr><tr data-testcase-id="88200"><td valign="top" class="td-label">테스트 2 <span>〉</span></td><td class="result passed">통과 (485.24ms, 10.2MB)</td></tr><tr data-testcase-id="88201"><td valign="top" class="td-label">테스트 3 <span>〉</span></td><td class="result passed">통과 (1133.28ms, 10.5MB)</td></tr><tr data-testcase-id="88202"><td valign="top" class="td-label">테스트 4 <span>〉</span></td><td class="result passed">통과 (1113.22ms, 10.6MB)</td></tr><tr data-testcase-id="88203"><td valign="top" class="td-label">테스트 5 <span>〉</span></td><td class="result passed">통과 (1125.17ms, 10.5MB)</td></tr><tr data-testcase-id="88204"><td valign="top" class="td-label">테스트 6 <span>〉</span></td><td class="result passed">통과 (1164.70ms, 10.6MB)</td></tr><tr data-testcase-id="88205"><td valign="top" class="td-label">테스트 7 <span>〉</span></td><td class="result passed">통과 (1621.68ms, 12.9MB)</td></tr><tr data-testcase-id="88206"><td valign="top" class="td-label">테스트 8 <span>〉</span></td><td class="result passed">통과 (1182.18ms, 13.2MB)</td></tr><tr data-testcase-id="88207"><td valign="top" class="td-label">테스트 9 <span>〉</span></td><td class="result passed">통과 (1251.73ms, 12.1MB)</td></tr><tr data-testcase-id="88208"><td valign="top" class="td-label">테스트 10 <span>〉</span></td><td class="result passed">통과 (1612.06ms, 12MB)</td></tr><tr data-testcase-id="88209"><td valign="top" class="td-label">테스트 11 <span>〉</span></td><td class="result passed">통과 (1190.65ms, 11.9MB)</td></tr><tr data-testcase-id="88210"><td valign="top" class="td-label">테스트 12 <span>〉</span></td><td class="result passed">통과 (1298.50ms, 11.9MB)</td></tr><tr data-testcase-id="88211"><td valign="top" class="td-label">테스트 13 <span>〉</span></td><td class="result passed">통과 (1176.80ms, 11.8MB)</td></tr><tr data-testcase-id="88212"><td valign="top" class="td-label">테스트 14 <span>〉</span></td><td class="result passed">통과 (1299.50ms, 11.9MB)</td></tr><tr data-testcase-id="88213"><td valign="top" class="td-label">테스트 15 <span>〉</span></td><td class="result passed">통과 (1180.62ms, 11.9MB)</td></tr><tr data-testcase-id="88214"><td valign="top" class="td-label">테스트 16 <span>〉</span></td><td class="result passed">통과 (1130.74ms, 10.6MB)</td></tr><tr data-testcase-id="88215"><td valign="top" class="td-label">테스트 17 <span>〉</span></td><td class="result passed">통과 (1131.79ms, 10.5MB)</td></tr><tr data-testcase-id="88216"><td valign="top" class="td-label">테스트 18 <span>〉</span></td><td class="result passed">통과 (1153.73ms, 10.3MB)</td></tr><tr data-testcase-id="88217"><td valign="top" class="td-label">테스트 19 <span>〉</span></td><td class="result passed">통과 (1141.88ms, 10.7MB)</td></tr><tr data-testcase-id="88218"><td valign="top" class="td-label">테스트 20 <span>〉</span></td><td class="result passed">통과 (1142.50ms, 10.9MB)</td></tr><tr data-testcase-id="88219"><td valign="top" class="td-label">테스트 21 <span>〉</span></td><td class="result passed">통과 (1140.63ms, 10.9MB)</td></tr><tr data-testcase-id="88220"><td valign="top" class="td-label">테스트 22 <span>〉</span></td><td class="result passed">통과 (1167.09ms, 11.9MB)</td></tr><tr data-testcase-id="88221"><td valign="top" class="td-label">테스트 23 <span>〉</span></td><td class="result passed">통과 (1186.75ms, 11.9MB)</td></tr><tr data-testcase-id="88222"><td valign="top" class="td-label">테스트 24 <span>〉</span></td><td class="result passed">통과 (1193.19ms, 11.8MB)</td></tr><tr data-testcase-id="88223"><td valign="top" class="td-label">테스트 25 <span>〉</span></td><td class="result passed">통과 (1266.56ms, 10.3MB)</td></tr><tr data-testcase-id="88224"><td valign="top" class="td-label">테스트 26 <span>〉</span></td><td class="result passed">통과 (1097.25ms, 10.3MB)</td></tr><tr data-testcase-id="88225"><td valign="top" class="td-label">테스트 27 <span>〉</span></td><td class="result passed">통과 (1052.01ms, 9.73MB)</td></tr><tr data-testcase-id="88226"><td valign="top" class="td-label">테스트 28 <span>〉</span></td><td class="result passed">통과 (1509.90ms, 9.65MB)</td></tr><tr data-testcase-id="88227"><td valign="top" class="td-label">테스트 29 <span>〉</span></td><td class="result passed">통과 (143.43ms, 9.45MB)</td></tr><tr data-testcase-id="88228"><td valign="top" class="td-label">테스트 30 <span>〉</span></td><td class="result passed">통과 (144.37ms, 9.6MB)</td></tr></tbody></table><div class="console-heading">채점 결과</div><div class="console-message">정확성: 50.0</div><div class="console-message">효율성: 50.0</div><div class="console-message">합계: 100.0 / 100.0</div></pre></div>

### 문제 설명
<div class="guide-section-description">
<div class="markdown solarized-dark"><p><strong>[본 문제는 정확성과 효율성 테스트 각각 점수가 있는 문제입니다.]</strong></p>

<p>밤늦게 귀가할 때 안전을 위해 항상 택시를 이용하던 <code>무지</code>는 최근 야근이 잦아져 택시를 더 많이 이용하게 되어 택시비를 아낄 수 있는 방법을 고민하고 있습니다. "무지"는 자신이 택시를 이용할 때 동료인 <code>어피치</code> 역시 자신과 비슷한 방향으로 가는 택시를 종종 이용하는 것을 알게 되었습니다. "무지"는 "어피치"와 귀가 방향이 비슷하여 택시 합승을 적절히 이용하면 택시요금을 얼마나 아낄 수 있을 지 계산해 보고 "어피치"에게 합승을 제안해 보려고 합니다.</p>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/715ff493-d1a0-44d8-9273-a785280b3f1e/2021_kakao_taxi_01.png" title="" alt="2021_kakao_taxi_01.png"></p>

<p>위 예시 그림은 택시가 이동 가능한 반경에 있는 6개 지점 사이의 이동 가능한 택시노선과 예상요금을 보여주고 있습니다.<br>
그림에서 <code>A</code>와 <code>B</code> 두 사람은 출발지점인 4번 지점에서 출발해서 택시를 타고 귀가하려고 합니다. <code>A</code>의 집은 6번 지점에 있으며 <code>B</code>의 집은 2번 지점에 있고 두 사람이 모두 귀가하는 데 소요되는 예상 최저 택시요금이 얼마인 지 계산하려고 합니다.</p>

<ul>
<li>그림의 원은 지점을 나타내며 원 안의 숫자는 지점 번호를 나타냅니다.

<ul>
<li>지점이 n개일 때, 지점 번호는 1부터 n까지 사용됩니다.</li>
</ul></li>
<li>지점 간에 택시가 이동할 수 있는 경로를 간선이라 하며, 간선에 표시된 숫자는 두 지점 사이의 예상 택시요금을 나타냅니다.

<ul>
<li>간선은 편의 상 직선으로 표시되어 있습니다.</li>
<li>위 그림 예시에서, 4번 지점에서 1번 지점으로(4→1) 가거나, 1번 지점에서 4번 지점으로(1→4) 갈 때 예상 택시요금은 <code>10</code>원으로 동일하며 이동 방향에 따라 달라지지 않습니다.</li>
</ul></li>
<li>예상되는 최저 택시요금은 다음과 같이 계산됩니다.

<ul>
<li>4→1→5 : <code>A</code>, <code>B</code>가 합승하여 택시를 이용합니다. 예상 택시요금은 <code>10 + 24 = 34</code>원 입니다.</li>
<li>5→6 : <code>A</code>가 혼자 택시를 이용합니다. 예상 택시요금은 <code>2</code>원 입니다.</li>
<li>5→3→2 : <code>B</code>가 혼자 택시를 이용합니다. 예상 택시요금은 <code>24 + 22 = 46</code>원 입니다.</li>
<li><code>A</code>, <code>B</code> 모두 귀가 완료까지 예상되는 최저 택시요금은 <code>34 + 2 + 46 = 82</code>원 입니다.</li>
</ul></li>
</ul>

<hr>

<h4><strong>[문제]</strong></h4>

<p>지점의 개수 n, 출발지점을 나타내는 s, <code>A</code>의 도착지점을 나타내는 a, <code>B</code>의 도착지점을 나타내는 b, 지점 사이의 예상 택시요금을 나타내는 fares가 매개변수로 주어집니다. 이때, <code>A</code>, <code>B</code> 두 사람이 s에서 출발해서 각각의 도착 지점까지 택시를 타고 간다고 가정할 때, 최저 예상 택시요금을 계산해서 return 하도록 solution 함수를 완성해 주세요.<br>
만약, 아예 합승을 하지 않고 각자 이동하는 경우의 예상 택시요금이 더 낮다면, 합승을 하지 않아도 됩니다.</p>

<h4><strong>[제한사항]</strong></h4>

<ul>
<li>지점갯수 n은 3 이상 200 이하인 자연수입니다.</li>
<li>지점 s, a, b는 1 이상 n 이하인 자연수이며, 각기 서로 다른 값입니다.

<ul>
<li>즉, 출발지점, <code>A</code>의 도착지점, <code>B</code>의 도착지점은 서로 겹치지 않습니다.</li>
</ul></li>
<li>fares는 2차원 정수 배열입니다.</li>
<li>fares 배열의 크기는 2 이상 <code>n x (n-1) / 2</code> 이하입니다.

<ul>
<li>예를들어, n = 6이라면 fares 배열의 크기는 2 이상 15 이하입니다. (<code>6 x 5 / 2 = 15</code>)</li>
<li>fares 배열의 각 행은 [c, d, f] 형태입니다.</li>
<li>c지점과 d지점 사이의 예상 택시요금이 <code>f</code>원이라는 뜻입니다.</li>
<li>지점 c, d는 1 이상 n 이하인 자연수이며, 각기 서로 다른 값입니다.</li>
<li>요금 f는 1 이상 100,000 이하인 자연수입니다.</li>
<li>fares 배열에 두 지점 간 예상 택시요금은 1개만 주어집니다. 즉, [c, d, f]가 있다면 [d, c, f]는 주어지지 않습니다.</li>
</ul></li>
<li>출발지점 s에서 도착지점 a와 b로 가는 경로가 존재하는 경우만 입력으로 주어집니다.</li>
</ul>

<hr>

<h5><strong>[입출력 예]</strong></h5>
<table class="table">
        <thead><tr>
<th>n</th>
<th>s</th>
<th>a</th>
<th>b</th>
<th>fares</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>6</td>
<td>4</td>
<td>6</td>
<td>2</td>
<td>[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]</td>
<td>82</td>
</tr>
<tr>
<td>7</td>
<td>3</td>
<td>4</td>
<td>1</td>
<td>[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]</td>
<td>14</td>
</tr>
<tr>
<td>6</td>
<td>4</td>
<td>5</td>
<td>6</td>
<td>[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]</td>
<td>18</td>
</tr>
</tbody>
      </table>
<h5><strong>입출력 예에 대한 설명</strong></h5>

<hr>

<p><strong>입출력 예 #1</strong><br>
문제 예시와 같습니다.</p>

<p><strong>입출력 예 #2</strong><br>
<img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/934fcb5a-f844-4b02-b7fa-46198123be05/2021_kakao_taxi_02.png" title="" alt="2021_kakao_taxi_02.png"></p>

<ul>
<li>합승을 하지 않고, <code>B</code>는 <code>3→2→1</code>, <code>A</code>는 <code>3→6→4</code> 경로로 각자 택시를 타고 가는 것이 최저 예상 택시요금입니다.</li>
<li>따라서 최저 예상 택시요금은 <code>(3 + 6) + (1 + 4) = 14</code>원 입니다.</li>
</ul>

<p><strong>입출력 예 #3</strong><br>
<img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/179cc8ad-73d2-46c9-95e9-2363f3cb345d/2021_kakao_taxi_03.png" title="" alt="2021_kakao_taxi_03.png"></p>

<ul>
<li><code>A</code>와 <code>B</code>가 <code>4→6</code> 구간을 합승하고 <code>B</code>가 6번 지점에서 내린 후, <code>A가</code>6→5` 구간을 혼자 타고 가는 것이 최저 예상 택시요금입니다.</li>
<li>따라서 최저 예상 택시요금은 <code>7 + 11 = 18</code>원 입니다.</li>
</ul>
</div>
</div>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges

## 💡 풀이 핵심

합승이라고 하길래... 아예 처음부터 따로 가거나
한 명 내릴때까지는 계속 같이 타고 가는 줄 알고
다익스트라로 풀었으나 

다시 보니 어느 한 곳에서 같이 내려서 각자 타고
가도 되는 문제였다...

따라서 <strong>플로이드 워셜 알고리즘</strong>으로 

1. 각 노드에서 다른 노드로 가는 최소 요금을 구한 다음
2. 시작 지점에서 각 노드(i) 마다<br/>
    2-1. a로 가는데 최소 요금</br>
    2-2. b로 가는데 최소 요금
3. 즉 정답은 <br>st에서 i와의 최소 요금 + 
<br>i에서 a로의 최소 요금 + 
<br>i에서 b로의 최소 요금
<br>의 최솟값이다.