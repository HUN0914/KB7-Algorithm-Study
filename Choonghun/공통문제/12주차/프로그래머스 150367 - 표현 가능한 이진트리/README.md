# [level 3] 표현 가능한 이진트리 - 150367번

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/150367) 


### 구분

코딩테스트 연습 > 2023 KAKAO BLIND RECRUITMENT

### 채점결과

<pre class="console-content"><div></div><div class="console-heading">채점을 시작합니다.</div><div class="console-message">정확성  테스트</div><table class="console-test-group" data-category="correctness"><tbody><tr data-testcase-id="150498"><td valign="top" class="td-label">테스트 1 <span>〉</span></td><td class="result passed">통과 (0.04ms, 11.5MB)</td></tr><tr data-testcase-id="150499"><td valign="top" class="td-label">테스트 2 <span>〉</span></td><td class="result passed">통과 (0.06ms, 11.5MB)</td></tr><tr data-testcase-id="150500"><td valign="top" class="td-label">테스트 3 <span>〉</span></td><td class="result passed">통과 (0.08ms, 11.6MB)</td></tr><tr data-testcase-id="150501"><td valign="top" class="td-label">테스트 4 <span>〉</span></td><td class="result passed">통과 (0.28ms, 11.7MB)</td></tr><tr data-testcase-id="150502"><td valign="top" class="td-label">테스트 5 <span>〉</span></td><td class="result passed">통과 (0.51ms, 11.7MB)</td></tr><tr data-testcase-id="150503"><td valign="top" class="td-label">테스트 6 <span>〉</span></td><td class="result passed">통과 (0.94ms, 11.6MB)</td></tr><tr data-testcase-id="150504"><td valign="top" class="td-label">테스트 7 <span>〉</span></td><td class="result passed">통과 (1.42ms, 11.5MB)</td></tr><tr data-testcase-id="150505"><td valign="top" class="td-label">테스트 8 <span>〉</span></td><td class="result passed">통과 (0.70ms, 11.6MB)</td></tr><tr data-testcase-id="150506"><td valign="top" class="td-label">테스트 9 <span>〉</span></td><td class="result passed">통과 (9.35ms, 11.7MB)</td></tr><tr data-testcase-id="150507"><td valign="top" class="td-label">테스트 10 <span>〉</span></td><td class="result passed">통과 (52.31ms, 14.4MB)</td></tr><tr data-testcase-id="150508"><td valign="top" class="td-label">테스트 11 <span>〉</span></td><td class="result passed">통과 (57.07ms, 14.8MB)</td></tr><tr data-testcase-id="150509"><td valign="top" class="td-label">테스트 12 <span>〉</span></td><td class="result passed">통과 (56.08ms, 14.8MB)</td></tr><tr data-testcase-id="150510"><td valign="top" class="td-label">테스트 13 <span>〉</span></td><td class="result passed">통과 (47.27ms, 14.5MB)</td></tr><tr data-testcase-id="150511"><td valign="top" class="td-label">테스트 14 <span>〉</span></td><td class="result passed">통과 (45.65ms, 14.2MB)</td></tr><tr data-testcase-id="150512"><td valign="top" class="td-label">테스트 15 <span>〉</span></td><td class="result passed">통과 (34.86ms, 13.5MB)</td></tr><tr data-testcase-id="150513"><td valign="top" class="td-label">테스트 16 <span>〉</span></td><td class="result passed">통과 (88.61ms, 16.9MB)</td></tr><tr data-testcase-id="150514"><td valign="top" class="td-label">테스트 17 <span>〉</span></td><td class="result passed">통과 (85.38ms, 16.7MB)</td></tr><tr data-testcase-id="150515"><td valign="top" class="td-label">테스트 18 <span>〉</span></td><td class="result passed">통과 (79.77ms, 16.2MB)</td></tr><tr data-testcase-id="150516"><td valign="top" class="td-label">테스트 19 <span>〉</span></td><td class="result passed">통과 (70.21ms, 15.8MB)</td></tr><tr data-testcase-id="150517"><td valign="top" class="td-label">테스트 20 <span>〉</span></td><td class="result passed">통과 (43.84ms, 14.1MB)</td></tr></tbody></table><div class="console-heading">채점 결과</div><div class="console-message">정확성: 100.0</div><div class="console-message">합계: 100.0 / 100.0</div></pre>

### 문제 설명

<div class="guide-section" style="width: calc(100%);">
      <div class="tab-pane fade active show" id="tour2">
        <div class="guide-section-description">
          <h6 class="guide-section-title">
            문제 설명
          </h6>
          <div class="markdown solarized-dark"><p>당신은 이진트리를 수로 표현하는 것을 좋아합니다.</p>

<p>이진트리를 수로 표현하는 방법은 다음과 같습니다.</p>

<ol>
<li>이진수를 저장할 빈 문자열을 생성합니다.</li>
<li>주어진 이진트리에 더미 노드를 추가하여 포화 이진트리로 만듭니다. <strong>루트 노드는 그대로 유지합니다.</strong></li>
<li>만들어진 포화 이진트리의 노드들을 가장 왼쪽 노드부터 가장 오른쪽 노드까지, 왼쪽에 있는 순서대로 살펴봅니다. <strong>노드의 높이는 살펴보는 순서에 영향을 끼치지 않습니다.</strong></li>
<li>살펴본 노드가 더미 노드라면, 문자열 뒤에 0을 추가합니다. 살펴본 노드가 더미 노드가 아니라면, 문자열 뒤에 1을 추가합니다.</li>
<li>문자열에 저장된 이진수를 십진수로 변환합니다.</li>
</ol>

<p><strong>이진트리에서 리프 노드가 아닌 노드는 자신의 왼쪽 자식이 루트인 서브트리의 노드들보다 오른쪽에 있으며, 자신의 오른쪽 자식이 루트인 서브트리의 노드들보다 왼쪽에 있다고 가정합니다.</strong></p>

<p>다음은 이진트리를 수로 표현하는 예시입니다.</p>

<p>주어진 이진트리는 다음과 같습니다.<br>
<img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/c3331b5f-2151-4ebd-a20e-8df122709d3e/%E1%84%8C%E1%85%A6%E1%84%86%E1%85%A9%E1%86%A8%20%E1%84%8B%E1%85%A5%E1%86%B9%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%83%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%8B%E1%85%A5%E1%84%80%E1%85%B3%E1%84%85%E1%85%A2%E1%86%B7.drawio%20%284%29.png" title="" alt="제목 없는 다이어그램.drawio \(4\).png"></p>

<p>주어진 이진트리에 더미노드를 추가하여 포화 이진트리로 만들면 다음과 같습니다. <strong>더미 노드는 점선으로 표시하였고, 노드 안의 수는 살펴보는 순서를 의미합니다.</strong><br>
<img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/0eb238be-9bfe-479a-bed8-84e1abe63097/%E1%84%8C%E1%85%A6%E1%84%86%E1%85%A9%E1%86%A8%20%E1%84%8B%E1%85%A5%E1%86%B9%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%83%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%8B%E1%85%A5%E1%84%80%E1%85%B3%E1%84%85%E1%85%A2%E1%86%B7.drawio%20%285%29.png" title="" alt="제목 없는 다이어그램.drawio \(5\).png"></p>

<p>노드들을 왼쪽에 있는 순서대로 살펴보며 0과 1을 생성한 문자열에 추가하면 <code>"0111010"</code>이 됩니다. 이 이진수를 십진수로 변환하면 58입니다. </p>

<p>당신은 수가 주어졌을때, 하나의 이진트리로 해당 수를 표현할 수 있는지 알고 싶습니다.</p>

<p>이진트리로 만들고 싶은 수를 담은 1차원 정수 배열 <code>numbers</code>가 주어집니다. <code>numbers</code>에 주어진 순서대로 하나의 이진트리로 해당 수를 표현할 수 있다면 1을, 표현할 수 없다면 0을 1차원 정수 배열에 담아 return 하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>numbers</code>의 길이 ≤ 10,000

<ul>
<li>1 ≤ <code>numbers</code>의 원소 ≤ 10<sup>15</sup></li>
</ul></li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th><code>numbers</code></th>
<th><code>result</code></th>
</tr>
</thead>
        <tbody><tr>
<td>[7, 42, 5]</td>
<td>[1, 1, 0]</td>
</tr>
<tr>
<td>[63, 111, 95]</td>
<td>[1, 1, 0]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p><strong>입출력 예 #1</strong></p>

<p>7은 다음과 같은 이진트리로 표현할 수 있습니다.<br>
<img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/f7e1fdb9-3344-420d-9238-e033a24e83ba/%E1%84%8C%E1%85%A6%E1%84%86%E1%85%A9%E1%86%A8%20%E1%84%8B%E1%85%A5%E1%86%B9%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%83%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%8B%E1%85%A5%E1%84%80%E1%85%B3%E1%84%85%E1%85%A2%E1%86%B7.drawio%20%287%29.png" title="" alt="제목 없는 다이어그램.drawio \(7\).png"></p>

<p>42는 다음과 같은 이진트리로 표현할 수 있습니다.<br>
<img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/f7e1fdb9-3344-420d-9238-e033a24e83ba/%E1%84%8C%E1%85%A6%E1%84%86%E1%85%A9%E1%86%A8%20%E1%84%8B%E1%85%A5%E1%86%B9%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%83%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%8B%E1%85%A5%E1%84%80%E1%85%B3%E1%84%85%E1%85%A2%E1%86%B7.drawio%20%287%29.png" title="" alt="제목 없는 다이어그램.drawio \(7\).png"></p>

<p>5는 이진트리로 표현할 수 없습니다.</p>

<p>따라서, [1, 0]을 return 하면 됩니다.</p>

<p><strong>입출력 예 #2</strong></p>

<p>63은 다음과 같은 이진트리로 표현할 수 있습니다.<br>
<img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/ae334397-6cf6-4cb7-a76e-f760c080def3/%E1%84%8C%E1%85%A6%E1%84%86%E1%85%A9%E1%86%A8%20%E1%84%8B%E1%85%A5%E1%86%B9%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%83%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%8B%E1%85%A5%E1%84%80%E1%85%B3%E1%84%85%E1%85%A2%E1%86%B7.drawio%20%288%29.png" title="" alt="제목 없는 다이어그램.drawio \(8\).png"></p>

<p>111은 다음과 같은 이진트리로 표현할 수 있습니다.<br>
<img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/b6873b5d-421c-433e-a739-97f9ab1b62b8/%E1%84%8C%E1%85%A6%E1%84%86%E1%85%A9%E1%86%A8%20%E1%84%8B%E1%85%A5%E1%86%B9%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%83%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%8B%E1%85%A5%E1%84%80%E1%85%B3%E1%84%85%E1%85%A2%E1%86%B7.drawio%20%2810%29.png" title="" alt="제목 없는 다이어그램.drawio \(10\).png"></p>

<p>95는 이진트리로 표현할 수 없습니다.</p>

<p>따라서, [1, 1, 0]을 return 하면 됩니다.</p>
</div>
        </div>
      </div>

</div>
</div>

## 💡 풀이 핵심

알고리즘보다는 규칙성을 찾는 것이 중점인 문제이다.</br>
포화이진트리의 노드 개수는 1, 3, 7, 15 ... 이며</br>
root는 결국 포화이진트리의 정가운데에 위치한 노드이고</br>
자식노드는 현재 노드의 번호에서 2^(트리의 높이 - 현재 노드의 높이 - 1)을 빼고, 더한 값이 자식의 번호이다.</br>
이진트리로 표현할 수 없는 수는 리프를 제외한 노드가 자식이 있음에도 불구하고 0인 경우이다.<br/>
이를 이용하여 DFS를 진행해주면 해당 수를 이진트리로 표현할 수 있는지 체크할 수 있다.