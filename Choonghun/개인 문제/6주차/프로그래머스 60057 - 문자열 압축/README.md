b# [level 2] 문자열 압축 - 60057번

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/60057) 


### 구분

코딩테스트 연습 > 2020 KAKAO BLIND RECRUITMENT

### 채점결과

<pre class="console-content"><div></div><div class="console-heading">채점을 시작합니다.</div><div class="console-message">정확성  테스트</div><table class="console-test-group" data-category="correctness"><tbody><tr data-testcase-id="55087"><td valign="top" class="td-label">테스트 1 <span>〉</span></td><td class="result passed">통과 (0.03ms, 9.17MB)</td></tr><tr data-testcase-id="55088"><td valign="top" class="td-label">테스트 2 <span>〉</span></td><td class="result passed">통과 (0.35ms, 9.06MB)</td></tr><tr data-testcase-id="55089"><td valign="top" class="td-label">테스트 3 <span>〉</span></td><td class="result passed">통과 (0.29ms, 9.16MB)</td></tr><tr data-testcase-id="55090"><td valign="top" class="td-label">테스트 4 <span>〉</span></td><td class="result passed">통과 (0.03ms, 8.94MB)</td></tr><tr data-testcase-id="55091"><td valign="top" class="td-label">테스트 5 <span>〉</span></td><td class="result passed">통과 (0.00ms, 9.33MB)</td></tr><tr data-testcase-id="55092"><td valign="top" class="td-label">테스트 6 <span>〉</span></td><td class="result passed">통과 (0.06ms, 9.26MB)</td></tr><tr data-testcase-id="55093"><td valign="top" class="td-label">테스트 7 <span>〉</span></td><td class="result passed">통과 (0.45ms, 9.06MB)</td></tr><tr data-testcase-id="55094"><td valign="top" class="td-label">테스트 8 <span>〉</span></td><td class="result passed">통과 (0.43ms, 9.1MB)</td></tr><tr data-testcase-id="55095"><td valign="top" class="td-label">테스트 9 <span>〉</span></td><td class="result passed">통과 (0.62ms, 9.05MB)</td></tr><tr data-testcase-id="55096"><td valign="top" class="td-label">테스트 10 <span>〉</span></td><td class="result passed">통과 (3.90ms, 9.03MB)</td></tr><tr data-testcase-id="55097"><td valign="top" class="td-label">테스트 11 <span>〉</span></td><td class="result passed">통과 (0.10ms, 9.18MB)</td></tr><tr data-testcase-id="55098"><td valign="top" class="td-label">테스트 12 <span>〉</span></td><td class="result passed">통과 (0.09ms, 9.17MB)</td></tr><tr data-testcase-id="55099"><td valign="top" class="td-label">테스트 13 <span>〉</span></td><td class="result passed">통과 (0.10ms, 9.24MB)</td></tr><tr data-testcase-id="55100"><td valign="top" class="td-label">테스트 14 <span>〉</span></td><td class="result passed">통과 (0.98ms, 9.23MB)</td></tr><tr data-testcase-id="55101"><td valign="top" class="td-label">테스트 15 <span>〉</span></td><td class="result passed">통과 (0.11ms, 9.16MB)</td></tr><tr data-testcase-id="55102"><td valign="top" class="td-label">테스트 16 <span>〉</span></td><td class="result passed">통과 (0.01ms, 9.04MB)</td></tr><tr data-testcase-id="55103"><td valign="top" class="td-label">테스트 17 <span>〉</span></td><td class="result passed">통과 (1.13ms, 9.16MB)</td></tr><tr data-testcase-id="55104"><td valign="top" class="td-label">테스트 18 <span>〉</span></td><td class="result passed">통과 (1.06ms, 9.11MB)</td></tr><tr data-testcase-id="55105"><td valign="top" class="td-label">테스트 19 <span>〉</span></td><td class="result passed">통과 (1.13ms, 9.16MB)</td></tr><tr data-testcase-id="55106"><td valign="top" class="td-label">테스트 20 <span>〉</span></td><td class="result passed">통과 (2.54ms, 9.21MB)</td></tr><tr data-testcase-id="55107"><td valign="top" class="td-label">테스트 21 <span>〉</span></td><td class="result passed">통과 (4.14ms, 9.16MB)</td></tr><tr data-testcase-id="55108"><td valign="top" class="td-label">테스트 22 <span>〉</span></td><td class="result passed">통과 (2.69ms, 9.03MB)</td></tr><tr data-testcase-id="55109"><td valign="top" class="td-label">테스트 23 <span>〉</span></td><td class="result passed">통과 (2.43ms, 9.04MB)</td></tr><tr data-testcase-id="55110"><td valign="top" class="td-label">테스트 24 <span>〉</span></td><td class="result passed">통과 (2.36ms, 9.21MB)</td></tr><tr data-testcase-id="55111"><td valign="top" class="td-label">테스트 25 <span>〉</span></td><td class="result passed">통과 (3.23ms, 9.11MB)</td></tr><tr data-testcase-id="55112"><td valign="top" class="td-label">테스트 26 <span>〉</span></td><td class="result passed">통과 (2.64ms, 9.14MB)</td></tr><tr data-testcase-id="55113"><td valign="top" class="td-label">테스트 27 <span>〉</span></td><td class="result passed">통과 (2.59ms, 9.2MB)</td></tr><tr data-testcase-id="55114"><td valign="top" class="td-label">테스트 28 <span>〉</span></td><td class="result passed">통과 (0.02ms, 9.04MB)</td></tr><tr data-testcase-id="242557"><td valign="top" class="td-label">테스트 29 <span>〉</span></td><td class="result passed">통과 (0.04ms, 9.09MB)</td></tr><tr data-testcase-id="242558"><td valign="top" class="td-label">테스트 30 <span>〉</span></td><td class="result passed">통과 (0.18ms, 9.3MB)</td></tr><tr data-testcase-id="242559"><td valign="top" class="td-label">테스트 31 <span>〉</span></td><td class="result passed">통과 (1.59ms, 9.03MB)</td></tr></tbody></table><div class="console-heading">채점 결과</div><div class="console-message">정확성: 100.0</div><div class="console-message">합계: 100.0 / 100.0</div></pre>

<div class="guide-section" style="width: calc(93.8636% - 12px);">
    <div class="tab-pane fade active show" id="tour2">
      <div class="guide-section-description">
        <h6 class="guide-section-title">문제 설명</h6>
        <div class="markdown solarized-dark"><p>데이터 처리 전문가가 되고 싶은 <strong>"어피치"</strong>는 문자열을 압축하는 방법에 대해 공부를 하고 있습니다. 최근에 대량의 데이터 처리를 위한 간단한 비손실 압축 방법에 대해 공부를 하고 있는데, 문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현하여 더 짧은 문자열로 줄여서 표현하는 알고리즘을 공부하고 있습니다.<br>
간단한 예로 "aabbaccc"의 경우 "2a2ba3c"(문자가 반복되지 않아 한번만 나타난 경우 1은 생략함)와 같이 표현할 수 있는데, 이러한 방식은 반복되는 문자가 적은 경우 압축률이 낮다는 단점이 있습니다. 예를 들면, "abcabcdede"와 같은 문자열은 전혀 압축되지 않습니다. "어피치"는 이러한 단점을 해결하기 위해 문자열을 1개 이상의 단위로 잘라서 압축하여 더 짧은 문자열로 표현할 수 있는지 방법을 찾아보려고 합니다.</p>

<p>예를 들어, "ababcdcdababcdcd"의 경우 문자를 1개 단위로 자르면 전혀 압축되지 않지만, 2개 단위로 잘라서 압축한다면 "2ab2cd2ab2cd"로 표현할 수 있습니다. 다른 방법으로 8개 단위로 잘라서 압축한다면 "2ababcdcd"로 표현할 수 있으며, 이때가 가장 짧게 압축하여 표현할 수 있는 방법입니다.</p>

<p>다른 예로, "abcabcdede"와 같은 경우, 문자를 2개 단위로 잘라서 압축하면 "abcabc2de"가 되지만, 3개 단위로 자른다면 "2abcdede"가 되어 3개 단위가 가장 짧은 압축 방법이 됩니다. 이때 3개 단위로 자르고 마지막에 남는 문자열은 그대로 붙여주면 됩니다.</p>

<p>압축할 문자열 s가 매개변수로 주어질 때, 위에 설명한 방법으로 1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return 하도록 solution 함수를 완성해주세요.</p>

<h3>제한사항</h3>

<ul>
<li>s의 길이는 1 이상 1,000 이하입니다.</li>
<li>s는 알파벳 소문자로만 이루어져 있습니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>s</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td><code>"aabbaccc"</code></td>
<td>7</td>
</tr>
<tr>
<td><code>"ababcdcdababcdcd"</code></td>
<td>9</td>
</tr>
<tr>
<td><code>"abcabcdede"</code></td>
<td>8</td>
</tr>
<tr>
<td><code>"abcabcabcabcdededededede"</code></td>
<td>14</td>
</tr>
<tr>
<td><code>"xababcdcdababcdcd"</code></td>
<td>17</td>
</tr>
</tbody>
      </table>
<h3>입출력 예에 대한 설명</h3>

<p><strong>입출력 예 #1</strong></p>

<p>문자열을 1개 단위로 잘라 압축했을 때 가장 짧습니다.</p>

<p><strong>입출력 예 #2</strong></p>

<p>문자열을 8개 단위로 잘라 압축했을 때 가장 짧습니다.</p>

<p><strong>입출력 예 #3</strong></p>

<p>문자열을 3개 단위로 잘라 압축했을 때 가장 짧습니다.</p>

<p><strong>입출력 예 #4</strong></p>

<p>문자열을 2개 단위로 자르면 "abcabcabcabc6de" 가 됩니다.<br>
문자열을 3개 단위로 자르면 "4abcdededededede" 가 됩니다.<br>
문자열을 4개 단위로 자르면 "abcabcabcabc3dede" 가 됩니다.<br>
문자열을 6개 단위로 자를 경우 "2abcabc2dedede"가 되며, 이때의 길이가 14로 가장 짧습니다.</p>

<p><strong>입출력 예 #5</strong></p>

<p>문자열은 제일 앞부터 정해진 길이만큼 잘라야 합니다.<br>
따라서 주어진 문자열을 x / ababcdcd  /  ababcdcd 로 자르는 것은 불가능 합니다.<br>
이 경우 어떻게 문자열을 잘라도 압축되지 않으므로 가장 짧은 길이는 17이 됩니다. </p>

<hr>

<p>※ 공지 - 2024년 7월 8일 테스트케이스가 추가되었습니다. 기존에 제출한 코드가 통과하지 못할 수도 있습니다.</p>
</div>
</div>
</div>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges

## 💡 풀이 핵심

문자열 슬라이싱 + 스택 사용