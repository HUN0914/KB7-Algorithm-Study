bbbbrb# [level 3] 기지국 설치 - 12979번

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12979) 


### 구분

코딩테스트 연습 > Summer/Winter Coding(~2018)

### 채점결과

<pre class="console-content"><div></div><div class="console-heading">채점을 시작합니다.</div><div class="console-message">정확성  테스트</div><table class="console-test-group" data-category="correctness"><tbody><tr data-testcase-id="10356"><td valign="top" class="td-label">테스트 1 <span>〉</span></td><td class="result passed">통과 (0.00ms, 9.11MB)</td></tr><tr data-testcase-id="10357"><td valign="top" class="td-label">테스트 2 <span>〉</span></td><td class="result passed">통과 (0.00ms, 9.11MB)</td></tr><tr data-testcase-id="10358"><td valign="top" class="td-label">테스트 3 <span>〉</span></td><td class="result passed">통과 (0.00ms, 9.08MB)</td></tr><tr data-testcase-id="10359"><td valign="top" class="td-label">테스트 4 <span>〉</span></td><td class="result passed">통과 (0.00ms, 9.02MB)</td></tr><tr data-testcase-id="10360"><td valign="top" class="td-label">테스트 5 <span>〉</span></td><td class="result passed">통과 (0.00ms, 9.04MB)</td></tr><tr data-testcase-id="10362"><td valign="top" class="td-label">테스트 6 <span>〉</span></td><td class="result passed">통과 (0.00ms, 9.33MB)</td></tr><tr data-testcase-id="10363"><td valign="top" class="td-label">테스트 7 <span>〉</span></td><td class="result passed">통과 (0.00ms, 9.05MB)</td></tr><tr data-testcase-id="10365"><td valign="top" class="td-label">테스트 8 <span>〉</span></td><td class="result passed">통과 (0.00ms, 9.16MB)</td></tr><tr data-testcase-id="10366"><td valign="top" class="td-label">테스트 9 <span>〉</span></td><td class="result passed">통과 (0.00ms, 9.11MB)</td></tr><tr data-testcase-id="10367"><td valign="top" class="td-label">테스트 10 <span>〉</span></td><td class="result passed">통과 (0.00ms, 9.25MB)</td></tr><tr data-testcase-id="10368"><td valign="top" class="td-label">테스트 11 <span>〉</span></td><td class="result passed">통과 (0.00ms, 9.16MB)</td></tr><tr data-testcase-id="10370"><td valign="top" class="td-label">테스트 12 <span>〉</span></td><td class="result passed">통과 (0.00ms, 9.22MB)</td></tr><tr data-testcase-id="10371"><td valign="top" class="td-label">테스트 13 <span>〉</span></td><td class="result passed">통과 (0.01ms, 9.01MB)</td></tr><tr data-testcase-id="10372"><td valign="top" class="td-label">테스트 14 <span>〉</span></td><td class="result passed">통과 (0.00ms, 9.17MB)</td></tr><tr data-testcase-id="10374"><td valign="top" class="td-label">테스트 15 <span>〉</span></td><td class="result passed">통과 (0.00ms, 9.2MB)</td></tr><tr data-testcase-id="10389"><td valign="top" class="td-label">테스트 16 <span>〉</span></td><td class="result passed">통과 (0.01ms, 9.09MB)</td></tr><tr data-testcase-id="10390"><td valign="top" class="td-label">테스트 17 <span>〉</span></td><td class="result passed">통과 (0.01ms, 9.16MB)</td></tr><tr data-testcase-id="10391"><td valign="top" class="td-label">테스트 18 <span>〉</span></td><td class="result passed">통과 (0.01ms, 9.18MB)</td></tr><tr data-testcase-id="10392"><td valign="top" class="td-label">테스트 19 <span>〉</span></td><td class="result passed">통과 (0.01ms, 9.26MB)</td></tr><tr data-testcase-id="10393"><td valign="top" class="td-label">테스트 20 <span>〉</span></td><td class="result passed">통과 (0.00ms, 9.19MB)</td></tr><tr data-testcase-id="10394"><td valign="top" class="td-label">테스트 21 <span>〉</span></td><td class="result passed">통과 (0.01ms, 9.17MB)</td></tr></tbody></table><div class="console-message">효율성  테스트</div><table class="console-test-group" data-category="effectiveness"><tbody><tr data-testcase-id="10548"><td valign="top" class="td-label">테스트 1 <span>〉</span></td><td class="result passed">통과 (2.60ms, 10.7MB)</td></tr><tr data-testcase-id="10549"><td valign="top" class="td-label">테스트 2 <span>〉</span></td><td class="result passed">통과 (4.16ms, 10.9MB)</td></tr><tr data-testcase-id="10550"><td valign="top" class="td-label">테스트 3 <span>〉</span></td><td class="result passed">통과 (2.76ms, 11MB)</td></tr><tr data-testcase-id="10551"><td valign="top" class="td-label">테스트 4 <span>〉</span></td><td class="result passed">통과 (2.79ms, 10.8MB)</td></tr></tbody></table><div class="console-heading">채점 결과</div><div class="console-message">정확성: 70.5</div><div class="console-message">효율성: 29.5</div><div class="console-message">합계: 100.0 / 100.0</div></pre>

<div class="tab-pane fade active show" id="tour2">
        <div class="guide-section-description">
          <h6 class="guide-section-title">
            문제 설명
          </h6>
          <div class="markdown solarized-dark"><p>N개의 아파트가 일렬로 쭉 늘어서 있습니다. 이 중에서 일부 아파트 옥상에는 4g 기지국이 설치되어 있습니다. 기술이 발전해 5g 수요가 높아져 4g 기지국을 5g 기지국으로 바꾸려 합니다. 그런데 5g 기지국은 4g 기지국보다 전달 범위가 좁아, 4g 기지국을 5g 기지국으로 바꾸면 어떤 아파트에는 전파가 도달하지 않습니다.</p>

<p>예를 들어 11개의 아파트가 쭉 늘어서 있고, [4, 11] 번째 아파트 옥상에는 4g 기지국이 설치되어 있습니다. 만약 이 4g 기지국이 전파 도달 거리가 1인 5g 기지국으로 바뀔 경우 모든 아파트에 전파를 전달할 수 없습니다. (전파의 도달 거리가 W일 땐, 기지국이 설치된 아파트를 기준으로 전파를 양쪽으로 W만큼 전달할 수 있습니다.)</p>

<ul>
<li>초기에, 1, 2, 6, 7, 8, 9번째 아파트에는 전파가 전달되지 않습니다.</li>
</ul>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/fcb45e06-ebb2-4d93-98cc-b6203185e933/%E1%84%80%E1%85%B5%E1%84%8C%E1%85%B5%E1%84%80%E1%85%AE%E1%86%A8%E1%84%89%E1%85%A5%E1%86%AF%E1%84%8E%E1%85%B51_pvskxt.png" title="" alt="기지국설치1_pvskxt.png"></p>

<ul>
<li>1, 7, 9번째 아파트 옥상에 기지국을 설치할 경우, 모든 아파트에 전파를 전달할 수 있습니다.</li>
</ul>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/dd31ddb8-f50d-404c-a6f5-8d6a1d88f620/%E1%84%80%E1%85%B5%E1%84%8C%E1%85%B5%E1%84%80%E1%85%AE%E1%86%A8%E1%84%89%E1%85%A5%E1%86%AF%E1%84%8E%E1%85%B52_kml0pb.png" title="" alt="기지국설치2_kml0pb.png"></p>

<ul>
<li>더 많은 아파트 옥상에 기지국을 설치하면 모든 아파트에 전파를 전달할 수 있습니다.</li>
</ul>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/f5801b12-f683-422d-b26f-5e23e72915dc/%E1%84%80%E1%85%B5%E1%84%8C%E1%85%B5%E1%84%80%E1%85%AE%E1%86%A8%E1%84%89%E1%85%A5%E1%86%AF%E1%84%8E%E1%85%B53_xhv7r3.png" title="" alt="기지국설치3_xhv7r3.png"></p>

<p>이때, 우리는 5g 기지국을 <strong>최소로 설치</strong>하면서 모든 아파트에 전파를 전달하려고 합니다. 위의 예시에선 최소 3개의 아파트 옥상에 기지국을 설치해야 모든 아파트에 전파를 전달할 수 있습니다.</p>

<p>아파트의 개수 N, 현재 기지국이 설치된 아파트의 번호가 담긴 1차원 배열 stations, 전파의 도달 거리 W가 매개변수로 주어질 때, 모든 아파트에 전파를 전달하기 위해 증설해야 할 기지국 개수의 최솟값을 리턴하는 solution 함수를 완성해주세요</p>

<h5>제한사항</h5>

<ul>
<li>N: 200,000,000 이하의 자연수</li>
<li>stations의 크기: 10,000 이하의 자연수</li>
<li>stations는 오름차순으로 정렬되어 있고, 배열에 담긴 수는 N보다 같거나 작은 자연수입니다.</li>
<li>W: 10,000 이하의 자연수</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>N</th>
<th>stations</th>
<th>W</th>
<th>answer</th>
</tr>
</thead>
        <tbody><tr>
<td>11</td>
<td>[4, 11]</td>
<td>1</td>
<td>3</td>
</tr>
<tr>
<td>16</td>
<td>[9]</td>
<td>2</td>
<td>3</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>입출력 예 #1<br>
문제의 예시와 같습니다</p>

<p>입출력 예 #2</p>

<ul>
<li>초기에, 1~6, 12~16번째 아파트에는 전파가 전달되지 않습니다.</li>
</ul>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/1d766102-f684-4643-bea2-02daea82e710/%E1%84%80%E1%85%B5%E1%84%8C%E1%85%B5%E1%84%80%E1%85%AE%E1%86%A8%E1%84%89%E1%85%A5%E1%86%AF%E1%84%8E%E1%85%B54_nqfrmm.png" title="" alt="기지국설치4_nqfrmm.png"></p>

<ul>
<li>3, 6, 14번째 아파트 옥상에 기지국을 설치할 경우 모든 아파트에 전파를 전달할 수 있습니다.</li>
</ul>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/bc7d4fdb-cb48-4f45-b2eb-977cfb2c54dd/%E1%84%80%E1%85%B5%E1%84%8C%E1%85%B5%E1%84%80%E1%85%AE%E1%86%A8%E1%84%89%E1%85%A5%E1%86%AF%E1%84%8E%E1%85%B55_zh4ebk.png" title="" alt="기지국설치5_zh4ebk.png"></p>
</div>
        </div>
      </div>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges

## 💡 풀이 핵심

투포인터를 활용하여 left와 right를 0부터 출발</br>
stations를 범위 양 끝(x,y)으로 치환하여 다시 저장하고</br>
right가 x 이상이면 right를 y로 갱신,</br>
right가 x 보다 작으면 right와 x의 간격을 기지국으로 채운다.</br>
간격에서 기지국의 범위 길이를 나누고,</br>
이때 나머지가 있다면 몫 + 1 없다면 몫 만큼 answer에 더해준다.</br>
모든 stations를 순회하고 최종적으로 남은 right와 맨 끝(n) 간의 간격도 나누어</br>
위와 똑같이 연산하고 answer을 반환해주면 종료된다.