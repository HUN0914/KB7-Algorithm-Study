# [level 3] 야근 지수 - 12927번

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12927) 


### 구분

코딩테스트 연습 > 연습 문제

### 채점결과

<div id="output-wrapper"><pre class="console-content"><div></div><div class="console-heading">채점을 시작합니다.</div><div class="console-message">정확성  테스트</div><table class="console-test-group" data-category="correctness"><tbody><tr data-testcase-id="23406"><td valign="top" class="td-label">테스트 1 <span>〉</span></td><td class="result passed">통과 (45.87ms, 16.8MB)</td></tr><tr data-testcase-id="23407"><td valign="top" class="td-label">테스트 2 <span>〉</span></td><td class="result passed">통과 (35.11ms, 16.7MB)</td></tr><tr data-testcase-id="23408"><td valign="top" class="td-label">테스트 3 <span>〉</span></td><td class="result passed">통과 (54.36ms, 16.7MB)</td></tr><tr data-testcase-id="23409"><td valign="top" class="td-label">테스트 4 <span>〉</span></td><td class="result passed">통과 (51.99ms, 16.6MB)</td></tr><tr data-testcase-id="23410"><td valign="top" class="td-label">테스트 5 <span>〉</span></td><td class="result passed">통과 (49.49ms, 16.8MB)</td></tr><tr data-testcase-id="23411"><td valign="top" class="td-label">테스트 6 <span>〉</span></td><td class="result passed">통과 (41.99ms, 16.6MB)</td></tr><tr data-testcase-id="23412"><td valign="top" class="td-label">테스트 7 <span>〉</span></td><td class="result passed">통과 (39.22ms, 16.7MB)</td></tr><tr data-testcase-id="23413"><td valign="top" class="td-label">테스트 8 <span>〉</span></td><td class="result passed">통과 (47.63ms, 16.8MB)</td></tr><tr data-testcase-id="23414"><td valign="top" class="td-label">테스트 9 <span>〉</span></td><td class="result passed">통과 (52.07ms, 17.1MB)</td></tr><tr data-testcase-id="23415"><td valign="top" class="td-label">테스트 10 <span>〉</span></td><td class="result passed">통과 (32.63ms, 16.6MB)</td></tr><tr data-testcase-id="23416"><td valign="top" class="td-label">테스트 11 <span>〉</span></td><td class="result passed">통과 (38.57ms, 16.6MB)</td></tr><tr data-testcase-id="23417"><td valign="top" class="td-label">테스트 12 <span>〉</span></td><td class="result passed">통과 (33.98ms, 16.8MB)</td></tr><tr data-testcase-id="23418"><td valign="top" class="td-label">테스트 13 <span>〉</span></td><td class="result passed">통과 (32.09ms, 16.7MB)</td></tr></tbody></table><div class="console-message">효율성  테스트</div><table class="console-test-group" data-category="effectiveness"><tbody><tr data-testcase-id="23419"><td valign="top" class="td-label">테스트 1 <span>〉</span></td><td class="result passed">통과 (29.14ms, 16.9MB)</td></tr><tr data-testcase-id="23420"><td valign="top" class="td-label">테스트 2 <span>〉</span></td><td class="result passed">통과 (39.81ms, 16.9MB)</td></tr></tbody></table><div class="console-heading">채점 결과</div><div class="console-message">정확성: 86.7</div><div class="console-message">효율성: 13.3</div><div class="console-message">합계: 100.0 / 100.0</div></pre></div>

<div class="guide-section" style="width: calc(78.3616% - 12px);">
    <div class="tab-pane fade active show" id="tour2">
      <div class="guide-section-description">
        <h6 class="guide-section-title">문제 설명</h6>
        <div class="markdown solarized-dark"><p>회사원 Demi는 가끔은 야근을 하는데요, 야근을 하면 야근 피로도가 쌓입니다. 야근 피로도는 야근을 시작한 시점에서 남은 일의 작업량을 제곱하여 더한 값입니다. Demi는 N시간 동안 야근 피로도를 최소화하도록 일할 겁니다.Demi가 1시간 동안 작업량 1만큼을 처리할 수 있다고 할 때,  퇴근까지 남은 N 시간과 각 일에 대한 작업량 works에 대해 야근 피로도를 최소화한 값을 리턴하는 함수 solution을 완성해주세요.</p>

<h5>제한 사항</h5>

<ul>
<li><code>works</code>는 길이 1 이상, 20,000 이하인 배열입니다.</li>
<li><code>works</code>의 원소는 50000 이하인 자연수입니다.</li>
<li><code>n</code>은 1,000,000 이하인 자연수입니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>works</th>
<th>n</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[4, 3, 3]</td>
<td>4</td>
<td>12</td>
</tr>
<tr>
<td>[2, 1, 2]</td>
<td>1</td>
<td>6</td>
</tr>
<tr>
<td>[1,1]</td>
<td>3</td>
<td>0</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>입출력 예 #1<br>
n=4 일 때, 남은 일의 작업량이 [4, 3, 3] 이라면 야근 지수를 최소화하기 위해 4시간동안 일을 한 결과는 [2, 2, 2]입니다. 이 때 야근 지수는 2<sup>2</sup> + 2<sup>2</sup> + 2<sup>2</sup> = 12 입니다.</p>

<p>입출력 예 #2<br>
n=1일 때, 남은 일의 작업량이 [2,1,2]라면 야근 지수를 최소화하기 위해 1시간동안 일을 한 결과는 [1,1,2]입니다. 야근지수는 1<sup>2</sup> + 1<sup>2</sup> + 2<sup>2</sup> = 6입니다.</p>

<p>입출력 예 #3</p>

<p>남은 작업량이 없으므로 피로도는 0입니다.</p>
</div>
      </div>
    </div>


      <div class="submission-history-list-section tab-pane fade" id="submissionHistory">
        <div class="submission-history-wrapper">


  <div data-challengeable-submission-history-component="submission-history" data-user-id="915387" data-lesson-id="12927" data-current-theme="dark" data-webapp="true" style="width: 100%; height: 100%;"><div class="SubmissionHistorystyle__Container-sc-topbuc-0 cBfbrE theme-dark"><div class="SubmissionHistorystyle__ListLayout-sc-topbuc-1 kUgbnd"><div class="Headerstyle__Container-sc-xey78k-0 jXBvhh"><div class="Headerstyle__TotalSubmissionCount-sc-xey78k-1 jXcjGi">0개의 제출</div><div class="Headerstyle__RefreshButton-sc-xey78k-4 bxRQzJ theme-dark" data-hackle-value="{&quot;key&quot;:&quot;open_challenge_lesson_submission_history_refresh_clicked&quot;,&quot;properties&quot;:{&quot;total_entries&quot;:0,&quot;lesson_id&quot;:12927}}"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="Headerstyle__RefreshIcon-sc-xey78k-2 bxmpYS"><path fill-rule="evenodd" clip-rule="evenodd" d="M19 8L15 12H18C18 15.31 15.31 18 12 18C10.99 18 10.03 17.75 9.2 17.3L7.74 18.76C8.97 19.54 10.43 20 12 20C16.42 20 20 16.42 20 12H23L19 8ZM6 12C6 8.69 8.69 6 12 6C13.01 6 13.97 6.25 14.8 6.7L16.26 5.24C15.03 4.46 13.57 4 12 4C7.58 4 4 7.58 4 12H1L5 16L9 12H6Z" fill="black"></path></svg><span class="Headerstyle__RefreshText-sc-xey78k-3 kkDrMQ">새로고침</span></div></div><div class="SubmissionListstyle__CenterLayout-sc-dysuo0-0 dJaWUi"><div class="SubmissionListstyle__NoSubmissionText-sc-dysuo0-1 jXZSoA">제출 내역이 없습니다</div></div></div></div></div>
  <script src="https://hera-client.grepp.co/269c0e1cc4ea037ef673.js" defer="defer"></script>
</div>

</div>
</div>



> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges

## 💡 풀이 핵심

정렬해서 해도 되긴 할거 같은데 시간대별로 나눠서 개수로만 연산하는게 나을거 같아서</br>
별도의 배열 선언후 카운팅해서 진행