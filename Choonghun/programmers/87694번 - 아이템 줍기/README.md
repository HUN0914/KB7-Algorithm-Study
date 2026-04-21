# [level 3] 아이템 줍기 - 87694번

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/87694) 

### 구분

코딩테스트 연습 > 깊이/너비 우선 탐색(DFS/BFS)

### 제출 일자

2026년 04월 21일 15:37:39

### 채점결과

<pre class="console-content"><div></div><div class="console-heading">채점을 시작합니다.</div><div class="console-message">정확성  테스트</div><table class="console-test-group" data-category="correctness"><tbody><tr data-testcase-id="110311"><td valign="top" class="td-label">테스트 1 <span>〉</span></td><td class="result passed">통과 (0.15ms, 9.42MB)</td></tr><tr data-testcase-id="110312"><td valign="top" class="td-label">테스트 2 <span>〉</span></td><td class="result passed">통과 (0.08ms, 9.38MB)</td></tr><tr data-testcase-id="110313"><td valign="top" class="td-label">테스트 3 <span>〉</span></td><td class="result passed">통과 (0.14ms, 9.45MB)</td></tr><tr data-testcase-id="110314"><td valign="top" class="td-label">테스트 4 <span>〉</span></td><td class="result passed">통과 (0.10ms, 9.37MB)</td></tr><tr data-testcase-id="110315"><td valign="top" class="td-label">테스트 5 <span>〉</span></td><td class="result passed">통과 (0.11ms, 9.45MB)</td></tr><tr data-testcase-id="110316"><td valign="top" class="td-label">테스트 6 <span>〉</span></td><td class="result passed">통과 (0.15ms, 9.31MB)</td></tr><tr data-testcase-id="110317"><td valign="top" class="td-label">테스트 7 <span>〉</span></td><td class="result passed">통과 (0.16ms, 9.29MB)</td></tr><tr data-testcase-id="110318"><td valign="top" class="td-label">테스트 8 <span>〉</span></td><td class="result passed">통과 (0.18ms, 9.39MB)</td></tr><tr data-testcase-id="110319"><td valign="top" class="td-label">테스트 9 <span>〉</span></td><td class="result passed">통과 (0.56ms, 9.26MB)</td></tr><tr data-testcase-id="110320"><td valign="top" class="td-label">테스트 10 <span>〉</span></td><td class="result passed">통과 (0.43ms, 9.34MB)</td></tr><tr data-testcase-id="110321"><td valign="top" class="td-label">테스트 11 <span>〉</span></td><td class="result passed">통과 (0.59ms, 9.34MB)</td></tr><tr data-testcase-id="110322"><td valign="top" class="td-label">테스트 12 <span>〉</span></td><td class="result passed">통과 (0.54ms, 9.21MB)</td></tr><tr data-testcase-id="110323"><td valign="top" class="td-label">테스트 13 <span>〉</span></td><td class="result passed">통과 (0.91ms, 9.35MB)</td></tr><tr data-testcase-id="110324"><td valign="top" class="td-label">테스트 14 <span>〉</span></td><td class="result passed">통과 (0.38ms, 9.22MB)</td></tr><tr data-testcase-id="110325"><td valign="top" class="td-label">테스트 15 <span>〉</span></td><td class="result passed">통과 (0.20ms, 9.34MB)</td></tr><tr data-testcase-id="110326"><td valign="top" class="td-label">테스트 16 <span>〉</span></td><td class="result passed">통과 (1.12ms, 9.35MB)</td></tr><tr data-testcase-id="110327"><td valign="top" class="td-label">테스트 17 <span>〉</span></td><td class="result passed">통과 (1.32ms, 9.17MB)</td></tr><tr data-testcase-id="110328"><td valign="top" class="td-label">테스트 18 <span>〉</span></td><td class="result passed">통과 (0.96ms, 9.14MB)</td></tr><tr data-testcase-id="110329"><td valign="top" class="td-label">테스트 19 <span>〉</span></td><td class="result passed">통과 (1.35ms, 9.27MB)</td></tr><tr data-testcase-id="110330"><td valign="top" class="td-label">테스트 20 <span>〉</span></td><td class="result passed">통과 (1.38ms, 9.32MB)</td></tr><tr data-testcase-id="110331"><td valign="top" class="td-label">테스트 21 <span>〉</span></td><td class="result passed">통과 (1.54ms, 9.21MB)</td></tr><tr data-testcase-id="110332"><td valign="top" class="td-label">테스트 22 <span>〉</span></td><td class="result passed">통과 (0.90ms, 9.29MB)</td></tr><tr data-testcase-id="110333"><td valign="top" class="td-label">테스트 23 <span>〉</span></td><td class="result passed">통과 (1.29ms, 9.18MB)</td></tr><tr data-testcase-id="110334"><td valign="top" class="td-label">테스트 24 <span>〉</span></td><td class="result passed">통과 (1.30ms, 9.32MB)</td></tr><tr data-testcase-id="110335"><td valign="top" class="td-label">테스트 25 <span>〉</span></td><td class="result passed">통과 (0.42ms, 9.14MB)</td></tr><tr data-testcase-id="110336"><td valign="top" class="td-label">테스트 26 <span>〉</span></td><td class="result passed">통과 (0.75ms, 9.32MB)</td></tr><tr data-testcase-id="113734"><td valign="top" class="td-label">테스트 27 <span>〉</span></td><td class="result passed">통과 (0.66ms, 9.25MB)</td></tr><tr data-testcase-id="113735"><td valign="top" class="td-label">테스트 28 <span>〉</span></td><td class="result passed">통과 (0.74ms, 9.35MB)</td></tr><tr data-testcase-id="113736"><td valign="top" class="td-label">테스트 29 <span>〉</span></td><td class="result passed">통과 (0.68ms, 9.1MB)</td></tr><tr data-testcase-id="113737"><td valign="top" class="td-label">테스트 30 <span>〉</span></td><td class="result passed">통과 (0.52ms, 9.26MB)</td></tr></tbody></table><div class="console-heading">채점 결과</div><div class="console-message">정확성: 100.0</div><div class="console-message">합계: 100.0 / 100.0</div></pre>

### 문제 설명

<div class="guide-section" style="width: calc(98.8789% - 12px);">
    <div class="tab-pane fade active show" id="tour2">
      <div class="guide-section-description">
        <h6 class="guide-section-title">문제 설명</h6>
        <div class="markdown solarized-dark"><p>다음과 같은 다각형 모양 지형에서 캐릭터가 아이템을 줍기 위해 이동하려 합니다.</p>

<p><img src="https://asset.programmers.co.kr/files/production/9b96b07f-72db-4b1c-bd7a-6a9c9b8d0dc6/rect_1.png" title="" alt="rect_1.png"></p>

<p>지형은 각 변이 x축, y축과 평행한 직사각형이 겹쳐진 형태로 표현하며, 캐릭터는 이 다각형의 둘레(굵은 선)를 따라서 이동합니다. </p>

<p>만약 직사각형을 겹친 후 다음과 같이 중앙에 빈 공간이 생기는 경우, 다각형의 가장 바깥쪽 테두리가 캐릭터의 이동 경로가 됩니다.</p>

<p><img src="https://asset.programmers.co.kr/files/production/38b0739b-8dd8-40d8-ac44-c71678d28d07/rect_2.png" title="" alt="rect_2.png"></p>

<p>단, 서로 다른 두 직사각형의 x축 좌표 또는 y축 좌표가 같은 경우는 없습니다.</p>

<p><img src="https://asset.programmers.co.kr/files/production/ec976181-987e-494e-bb2d-0615ce16252f/rect_4.png" title="" alt="rect_4.png"></p>

<p>즉, 위 그림처럼 서로 다른 두 직사각형이 꼭짓점에서 만나거나, 변이 겹치는 경우 등은 없습니다.</p>

<p>다음 그림과 같이 지형이 2개 이상으로 분리된 경우도 없습니다.</p>

<p><img src="https://asset.programmers.co.kr/files/production/7eda8d92-ebe0-4b5f-bd15-0c9dc7af3a3e/rect_3.png" title="" alt="rect_3.png"></p>

<p>한 직사각형이 다른 직사각형 안에 완전히 포함되는 경우 또한 없습니다.</p>

<p><img src="https://asset.programmers.co.kr/files/production/1e178b0d-6580-4981-aae3-dd82a1b95362/rect_7.png" title="" alt="rect_7.png"></p>

<p>지형을 나타내는 직사각형이 담긴 2차원 배열 rectangle, 초기 캐릭터의 위치 characterX, characterY, 아이템의 위치 itemX, itemY가 solution 함수의 매개변수로 주어질 때, 캐릭터가 아이템을 줍기 위해 이동해야 하는 가장 짧은 거리를 return 하도록 solution 함수를 완성해주세요.</p>

<h5>제한사항</h5>

<ul>
<li>rectangle의 세로(행) 길이는 1 이상 4 이하입니다.</li>
<li>rectangle의 원소는 각 직사각형의 [좌측 하단 x, 좌측 하단 y, 우측 상단 x, 우측 상단 y] 좌표 형태입니다.

<ul>
<li>직사각형을 나타내는 모든 좌표값은 1 이상 50 이하인 자연수입니다.</li>
<li>서로 다른 두 직사각형의 x축 좌표, 혹은 y축 좌표가 같은 경우는 없습니다.</li>
<li>문제에 주어진 조건에 맞는 직사각형만 입력으로 주어집니다.</li>
</ul></li>
<li>charcterX, charcterY는 1 이상 50 이하인 자연수입니다.

<ul>
<li>지형을 나타내는 다각형 테두리 위의 한 점이 주어집니다.</li>
</ul></li>
<li>itemX, itemY는 1 이상 50 이하인 자연수입니다.

<ul>
<li>지형을 나타내는 다각형 테두리 위의 한 점이 주어집니다.</li>
</ul></li>
<li>캐릭터와 아이템의 처음 위치가 같은 경우는 없습니다.</li>
</ul>

<hr>

<ul>
<li>전체 배점의 50%는 직사각형이 1개인 경우입니다.<br></li>
<li>전체 배점의 25%는 직사각형이 2개인 경우입니다.<br></li>
<li>전체 배점의 25%는 직사각형이 3개 또는 4개인 경우입니다.<br></li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>rectangle</th>
<th>characterX</th>
<th>characterY</th>
<th>itemX</th>
<th>itemY</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]</td>
<td>1</td>
<td>3</td>
<td>7</td>
<td>8</td>
<td>17</td>
</tr>
<tr>
<td>[[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]]</td>
<td>9</td>
<td>7</td>
<td>6</td>
<td>1</td>
<td>11</td>
</tr>
<tr>
<td>[[1,1,5,7]]</td>
<td>1</td>
<td>1</td>
<td>4</td>
<td>7</td>
<td>9</td>
</tr>
<tr>
<td>[[2,1,7,5],[6,4,10,10]]</td>
<td>3</td>
<td>1</td>
<td>7</td>
<td>10</td>
<td>15</td>
</tr>
<tr>
<td>[[2,2,5,5],[1,3,6,4],[3,1,4,6]]</td>
<td>1</td>
<td>4</td>
<td>6</td>
<td>3</td>
<td>10</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<p><img src="https://asset.programmers.co.kr/files/production/7b89552b-f7b6-47e7-8bbd-deaf01907f70/rect_5.png" title="" alt="rect_5.png"></p>

<p>캐릭터 위치는 (1, 3)이며, 아이템 위치는 (7, 8)입니다. 위 그림과 같이 굵은 선을 따라 이동하는 경로가 가장 짧습니다.</p>

<p>입출력 예 #2</p>

<p><img src="https://asset.programmers.co.kr/files/production/ac6911d0-e386-472b-a109-2542214c8d6b/rect_6.png" title="" alt="rect_6.png"></p>

<p>캐릭터 위치는 (9, 7)이며, 아이템 위치는 (6, 1)입니다. 위 그림과 같이 굵은 선을 따라 이동하는 경로가 가장 짧습니다.</p>

<p>입출력 예 #3</p>

<p><img src="https://asset.programmers.co.kr/files/production/9c47ca5c-df4b-4b2e-8c5b-faf0815de665/rect_8.png" title="" alt="rect_8.png"></p>

<p>캐릭터 위치는 (1, 1)이며, 아이템 위치는 (4, 7)입니다. 위 그림과 같이 굵은 선을 따라 이동하는 경로가 가장 짧습니다.</p>

<p>입출력 예 #4, #5</p>

<p>설명 생략</p>
</div>
      </div>
    </div>


<div class="submission-history-list-section tab-pane fade" id="submissionHistory">
<div class="submission-history-wrapper">


  <div data-challengeable-submission-history-component="submission-history" data-user-id="915387" data-lesson-id="87694" data-current-theme="light" data-webapp="true" style="width: 100%; height: 100%;"><div class="SubmissionHistorystyle__Container-sc-topbuc-0 cBfbrE theme-light"><div class="SubmissionHistorystyle__ListLayout-sc-topbuc-1 kUgbnd"><div class="Headerstyle__Container-sc-xey78k-0 jXBvhh"><div class="Headerstyle__TotalSubmissionCount-sc-xey78k-1 jXcjGi">5개의 제출</div><div class="Headerstyle__RefreshButton-sc-xey78k-4 bxRQzJ theme-light" data-hackle-value="{&quot;key&quot;:&quot;open_challenge_lesson_submission_history_refresh_clicked&quot;,&quot;properties&quot;:{&quot;total_entries&quot;:5,&quot;lesson_id&quot;:87694}}"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="Headerstyle__RefreshIcon-sc-xey78k-2 bxmpYS"><path fill-rule="evenodd" clip-rule="evenodd" d="M19 8L15 12H18C18 15.31 15.31 18 12 18C10.99 18 10.03 17.75 9.2 17.3L7.74 18.76C8.97 19.54 10.43 20 12 20C16.42 20 20 16.42 20 12H23L19 8ZM6 12C6 8.69 8.69 6 12 6C13.01 6 13.97 6.25 14.8 6.7L16.26 5.24C15.03 4.46 13.57 4 12 4C7.58 4 4 7.58 4 12H1L5 16L9 12H6Z" fill="black"></path></svg><span class="Headerstyle__RefreshText-sc-xey78k-3 kkDrMQ">새로고침</span></div></div><div class="SubmissionListstyle__ListLayout-sc-dysuo0-2 ejcbyi"><div class="SubmissionListstyle__ListHeader-sc-dysuo0-9 hpvOiX theme-light"><div class="SubmissionListstyle__ListRow-sc-dysuo0-8 ihamDy"><div class="SubmissionListstyle__ListItemColumnWrapper-sc-dysuo0-5 hyzPgq"><div class="SubmissionListstyle__ListColumn-sc-dysuo0-7 cnDSVL"></div><div class="SubmissionListstyle__ListColumn-sc-dysuo0-7 cnDSVL">제출일시</div><div class="SubmissionListstyle__ListColumn-sc-dysuo0-7 cnDSVL">언어</div><div class="SubmissionListstyle__ListColumn-sc-dysuo0-7 cnDSVL">채점 내역</div></div></div></div><div class="SubmissionListstyle__ListBody-sc-dysuo0-10 ftaYLJ theme-light"><div data-hackle-value="{&quot;key&quot;:&quot;open_challenge_lesson_submission_history_list_item_toggle_clicked&quot;,&quot;properties&quot;:{&quot;lesson_id&quot;:87694,&quot;created_at&quot;:&quot;2026-04-21T15:37:39.025+09:00&quot;,&quot;language&quot;:&quot;python&quot;,&quot;score&quot;:100,&quot;is_perfect_score&quot;:true}}" class="SubmissionListstyle__ListRow-sc-dysuo0-8 ihamDy"><div class="SubmissionListstyle__ListItemColumnWrapper-sc-dysuo0-5 hyzPgq theme-light"><div class="SubmissionListstyle__ListColumn-sc-dysuo0-7 cnDSVL"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="SubmissionListstyle__ToggleIcon-sc-dysuo0-4 lgYMPL"><path d="M20.735 11.1653C21.334 11.5606 21.334 12.4394 20.735 12.8347L7.80074 21.3691C7.13589 21.8078 6.25 21.3309 6.25 20.5344L6.25 3.4656C6.25 2.66905 7.13589 2.19223 7.80074 2.63092L20.735 11.1653Z" fill="black"></path></svg></div><div class="SubmissionListstyle__ListColumn-sc-dysuo0-7 cnDSVL"><span class="SubmissionListstyle__WhiteText-sc-dysuo0-3 lbcwAz theme-light">2026-04-21 15:37:39</span></div><div class="SubmissionListstyle__ListColumn-sc-dysuo0-7 cnDSVL"><span class="SubmissionListstyle__WhiteText-sc-dysuo0-3 lbcwAz theme-light">Python3</span></div><div class="SubmissionListstyle__ListColumn-sc-dysuo0-7 cnDSVL"><div class="SubmissionListstyle__ScoreInfo-sc-dysuo0-14 bGHFVK theme-light"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" class="SubmissionListstyle__CorrectIcon-sc-dysuo0-12 kPjulc"><g clip-path="url(#clip0_697_1368)"><path d="M8 0C3.6 0 0 3.6 0 8C0 12.4 3.6 16 8 16C12.4 16 16 12.4 16 8C16 3.6 12.4 0 8 0ZM6.3 12L3 8.7L4.4 7.3L6.3 9.2L11.6 3.9L13 5.3L6.3 12Z" fill="black"></path></g><defs><clipPath id="clip0_697_1368"><rect width="16" height="16" fill="white"></rect></clipPath></defs></svg><span class="SubmissionListstyle__ScoreText-sc-dysuo0-11 dGfPnt correct">정답</span></div><div class="SubmissionListstyle__ScoreNumber-sc-dysuo0-15 jRtHnV theme-light">100 / 100</div></div></div></div><div data-hackle-value="{&quot;key&quot;:&quot;open_challenge_lesson_submission_history_list_item_toggle_clicked&quot;,&quot;properties&quot;:{&quot;lesson_id&quot;:87694,&quot;created_at&quot;:&quot;2026-04-21T15:18:26.842+09:00&quot;,&quot;language&quot;:&quot;python&quot;,&quot;score&quot;:76.42857142857143,&quot;is_perfect_score&quot;:false}}" class="SubmissionListstyle__ListRow-sc-dysuo0-8 ihamDy"><div class="SubmissionListstyle__ListItemColumnWrapper-sc-dysuo0-5 hyzPgq theme-light"><div class="SubmissionListstyle__ListColumn-sc-dysuo0-7 cnDSVL"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="SubmissionListstyle__ToggleIcon-sc-dysuo0-4 lgYMPL"><path d="M20.735 11.1653C21.334 11.5606 21.334 12.4394 20.735 12.8347L7.80074 21.3691C7.13589 21.8078 6.25 21.3309 6.25 20.5344L6.25 3.4656C6.25 2.66905 7.13589 2.19223 7.80074 2.63092L20.735 11.1653Z" fill="black"></path></svg></div><div class="SubmissionListstyle__ListColumn-sc-dysuo0-7 cnDSVL"><span class="SubmissionListstyle__WhiteText-sc-dysuo0-3 lbcwAz theme-light">2026-04-21 15:18:26</span></div><div class="SubmissionListstyle__ListColumn-sc-dysuo0-7 cnDSVL"><span class="SubmissionListstyle__WhiteText-sc-dysuo0-3 lbcwAz theme-light">Python3</span></div><div class="SubmissionListstyle__ListColumn-sc-dysuo0-7 cnDSVL"><div class="SubmissionListstyle__ScoreInfo-sc-dysuo0-14 bGHFVK theme-light"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg" class="SubmissionListstyle__InCorrectIcon-sc-dysuo0-13 gCJeoj"><g clip-path="url(#clip0_697_1060)"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 0C3.129 0 0 3.129 0 7C0 10.871 3.129 14 7 14C10.871 14 14 10.871 14 7C14 3.129 10.871 0 7 0ZM10.5 9.231L9.231 10.5L7 8.269L4.769 10.5L3.5 9.231L5.731 7L3.5 4.769L4.769 3.5L7 5.731L9.231 3.5L10.5 4.769L8.269 7L10.5 9.231Z" fill="black"></path></g><defs><clipPath id="clip0_697_1060"><rect width="14" height="14" fill="white"></rect></clipPath></defs></svg><span class="SubmissionListstyle__ScoreText-sc-dysuo0-11 dGfPnt incorrect">오답</span></div><div class="SubmissionListstyle__ScoreNumber-sc-dysuo0-15 jRtHnV theme-light">76.4 / 100</div></div></div></div><div data-hackle-value="{&quot;key&quot;:&quot;open_challenge_lesson_submission_history_list_item_toggle_clicked&quot;,&quot;properties&quot;:{&quot;lesson_id&quot;:87694,&quot;created_at&quot;:&quot;2026-04-21T15:13:06.400+09:00&quot;,&quot;language&quot;:&quot;python&quot;,&quot;score&quot;:76.42857142857143,&quot;is_perfect_score&quot;:false}}" class="SubmissionListstyle__ListRow-sc-dysuo0-8 ihamDy"><div class="SubmissionListstyle__ListItemColumnWrapper-sc-dysuo0-5 hyzPgq theme-light"><div class="SubmissionListstyle__ListColumn-sc-dysuo0-7 cnDSVL"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="SubmissionListstyle__ToggleIcon-sc-dysuo0-4 lgYMPL"><path d="M20.735 11.1653C21.334 11.5606 21.334 12.4394 20.735 12.8347L7.80074 21.3691C7.13589 21.8078 6.25 21.3309 6.25 20.5344L6.25 3.4656C6.25 2.66905 7.13589 2.19223 7.80074 2.63092L20.735 11.1653Z" fill="black"></path></svg></div><div class="SubmissionListstyle__ListColumn-sc-dysuo0-7 cnDSVL"><span class="SubmissionListstyle__WhiteText-sc-dysuo0-3 lbcwAz theme-light">2026-04-21 15:13:06</span></div><div class="SubmissionListstyle__ListColumn-sc-dysuo0-7 cnDSVL"><span class="SubmissionListstyle__WhiteText-sc-dysuo0-3 lbcwAz theme-light">Python3</span></div><div class="SubmissionListstyle__ListColumn-sc-dysuo0-7 cnDSVL"><div class="SubmissionListstyle__ScoreInfo-sc-dysuo0-14 bGHFVK theme-light"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg" class="SubmissionListstyle__InCorrectIcon-sc-dysuo0-13 gCJeoj"><g clip-path="url(#clip0_697_1060)"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 0C3.129 0 0 3.129 0 7C0 10.871 3.129 14 7 14C10.871 14 14 10.871 14 7C14 3.129 10.871 0 7 0ZM10.5 9.231L9.231 10.5L7 8.269L4.769 10.5L3.5 9.231L5.731 7L3.5 4.769L4.769 3.5L7 5.731L9.231 3.5L10.5 4.769L8.269 7L10.5 9.231Z" fill="black"></path></g><defs><clipPath id="clip0_697_1060"><rect width="14" height="14" fill="white"></rect></clipPath></defs></svg><span class="SubmissionListstyle__ScoreText-sc-dysuo0-11 dGfPnt incorrect">오답</span></div><div class="SubmissionListstyle__ScoreNumber-sc-dysuo0-15 jRtHnV theme-light">76.4 / 100</div></div></div></div><div data-hackle-value="{&quot;key&quot;:&quot;open_challenge_lesson_submission_history_list_item_toggle_clicked&quot;,&quot;properties&quot;:{&quot;lesson_id&quot;:87694,&quot;created_at&quot;:&quot;2026-04-21T14:19:13.347+09:00&quot;,&quot;language&quot;:&quot;python&quot;,&quot;score&quot;:76.42857142857143,&quot;is_perfect_score&quot;:false}}" class="SubmissionListstyle__ListRow-sc-dysuo0-8 ihamDy"><div class="SubmissionListstyle__ListItemColumnWrapper-sc-dysuo0-5 hyzPgq theme-light"><div class="SubmissionListstyle__ListColumn-sc-dysuo0-7 cnDSVL"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="SubmissionListstyle__ToggleIcon-sc-dysuo0-4 lgYMPL"><path d="M20.735 11.1653C21.334 11.5606 21.334 12.4394 20.735 12.8347L7.80074 21.3691C7.13589 21.8078 6.25 21.3309 6.25 20.5344L6.25 3.4656C6.25 2.66905 7.13589 2.19223 7.80074 2.63092L20.735 11.1653Z" fill="black"></path></svg></div><div class="SubmissionListstyle__ListColumn-sc-dysuo0-7 cnDSVL"><span class="SubmissionListstyle__WhiteText-sc-dysuo0-3 lbcwAz theme-light">2026-04-21 14:19:13</span></div><div class="SubmissionListstyle__ListColumn-sc-dysuo0-7 cnDSVL"><span class="SubmissionListstyle__WhiteText-sc-dysuo0-3 lbcwAz theme-light">Python3</span></div><div class="SubmissionListstyle__ListColumn-sc-dysuo0-7 cnDSVL"><div class="SubmissionListstyle__ScoreInfo-sc-dysuo0-14 bGHFVK theme-light"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg" class="SubmissionListstyle__InCorrectIcon-sc-dysuo0-13 gCJeoj"><g clip-path="url(#clip0_697_1060)"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 0C3.129 0 0 3.129 0 7C0 10.871 3.129 14 7 14C10.871 14 14 10.871 14 7C14 3.129 10.871 0 7 0ZM10.5 9.231L9.231 10.5L7 8.269L4.769 10.5L3.5 9.231L5.731 7L3.5 4.769L4.769 3.5L7 5.731L9.231 3.5L10.5 4.769L8.269 7L10.5 9.231Z" fill="black"></path></g><defs><clipPath id="clip0_697_1060"><rect width="14" height="14" fill="white"></rect></clipPath></defs></svg><span class="SubmissionListstyle__ScoreText-sc-dysuo0-11 dGfPnt incorrect">오답</span></div><div class="SubmissionListstyle__ScoreNumber-sc-dysuo0-15 jRtHnV theme-light">76.4 / 100</div></div></div></div><div data-hackle-value="{&quot;key&quot;:&quot;open_challenge_lesson_submission_history_list_item_toggle_clicked&quot;,&quot;properties&quot;:{&quot;lesson_id&quot;:87694,&quot;created_at&quot;:&quot;2026-04-21T14:17:25.124+09:00&quot;,&quot;language&quot;:&quot;python&quot;,&quot;score&quot;:55,&quot;is_perfect_score&quot;:false}}" class="SubmissionListstyle__ListRow-sc-dysuo0-8 ihamDy"><div class="SubmissionListstyle__ListItemColumnWrapper-sc-dysuo0-5 hyzPgq theme-light"><div class="SubmissionListstyle__ListColumn-sc-dysuo0-7 cnDSVL"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="SubmissionListstyle__ToggleIcon-sc-dysuo0-4 lgYMPL"><path d="M20.735 11.1653C21.334 11.5606 21.334 12.4394 20.735 12.8347L7.80074 21.3691C7.13589 21.8078 6.25 21.3309 6.25 20.5344L6.25 3.4656C6.25 2.66905 7.13589 2.19223 7.80074 2.63092L20.735 11.1653Z" fill="black"></path></svg></div><div class="SubmissionListstyle__ListColumn-sc-dysuo0-7 cnDSVL"><span class="SubmissionListstyle__WhiteText-sc-dysuo0-3 lbcwAz theme-light">2026-04-21 14:17:25</span></div><div class="SubmissionListstyle__ListColumn-sc-dysuo0-7 cnDSVL"><span class="SubmissionListstyle__WhiteText-sc-dysuo0-3 lbcwAz theme-light">Python3</span></div><div class="SubmissionListstyle__ListColumn-sc-dysuo0-7 cnDSVL"><div class="SubmissionListstyle__ScoreInfo-sc-dysuo0-14 bGHFVK theme-light"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg" class="SubmissionListstyle__InCorrectIcon-sc-dysuo0-13 gCJeoj"><g clip-path="url(#clip0_697_1060)"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 0C3.129 0 0 3.129 0 7C0 10.871 3.129 14 7 14C10.871 14 14 10.871 14 7C14 3.129 10.871 0 7 0ZM10.5 9.231L9.231 10.5L7 8.269L4.769 10.5L3.5 9.231L5.731 7L3.5 4.769L4.769 3.5L7 5.731L9.231 3.5L10.5 4.769L8.269 7L10.5 9.231Z" fill="black"></path></g><defs><clipPath id="clip0_697_1060"><rect width="14" height="14" fill="white"></rect></clipPath></defs></svg><span class="SubmissionListstyle__ScoreText-sc-dysuo0-11 dGfPnt incorrect">오답</span></div><div class="SubmissionListstyle__ScoreNumber-sc-dysuo0-15 jRtHnV theme-light">55 / 100</div></div></div></div></div><div class="PaginationNavstyle__Buttons-sc-isexrc-0 cRzBTt"><button class="PaginationNavstyle__ArrowEnd-sc-isexrc-2 wQYXn start" aria-label="처음 페이지" disabled=""></button><button class="PaginationNavstyle__Arrow-sc-isexrc-3 gRPoLu prev" aria-label="이전 페이지" disabled=""></button><span class="PaginationNavstyle__PageButtonContainer-sc-isexrc-1 dZUlmd"><button data-testid="page-active" class="PaginationNavstyle__PageButton-sc-isexrc-4 kUFtZp">1</button></span><button class="PaginationNavstyle__Arrow-sc-isexrc-3 gRPoLu next" aria-label="다음 페이지" disabled=""></button><button class="PaginationNavstyle__ArrowEnd-sc-isexrc-2 wQYXn last" aria-label="마지막 페이지" disabled=""></button></div></div></div></div></div>
  <script src="https://hera-client.grepp.co/269c0e1cc4ea037ef673.js" defer="defer"></script>
</div>

</div>
</div>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges

## 💡 풀이 핵심

시작 점부터 인근 점을 잇는 선분이 모든 영역에 대하여 하나의 영역에만 유일하게 소속된
부분 선분인 경우에만 해당 점으로 이동하는 조건 처리가 좀 까다로웠다...<br/>

이거만 해결하면 무난한 BFS/DFS 문제이다.