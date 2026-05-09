# [level 3] 외벽 점검 - 60062

## 문제 링크

https://school.programmers.co.kr/learn/courses/30/lessons/60062

## 문제 설명

레스토랑을 운영하고 있는 "스카피"는 레스토랑 내부가 너무 낡아 친구들과 함께 직접 리모델링 하기로 했습니다.

레스토랑의 구조는 완전히 동그란 모양이고 외벽의 총 둘레는 n미터이며, 외벽의 몇몇 지점은 취약 지점들입니다.

친구들은:

- 시계 방향 또는 반시계 방향 이동 가능

- 1시간 동안 일정 거리 이동 가능

모든 취약 지점을 점검하기 위한 최소 친구 수를 구하는 문제입니다.

불가능하면 `-1` 반환.

## 제한사항

- n은 1 이상 200 이하인 자연수

- weak 길이: 1 ~ 15

- dist 길이: 1 ~ 8

## 입출력 예

| n | weak | dist | result |

|---|---|---|---|

| 12 | [1, 5, 6, 10] | [1, 2, 3, 4] | 2 |

| 12 | [1, 3, 4, 9, 10] | [3, 5, 7] | 1 |

## ⏱ 성능

<pre class="console-content"><div></div><div class="console-message">정확성  테스트</div><table class="console-test-group" data-category="correctness"><tbody><tr data-testcase-id="54449"><td valign="top" class="td-label">테스트 1 <span>〉</span></td><td class="result passed">통과 (0.05ms, 9.27MB)</td></tr><tr data-testcase-id="54450"><td valign="top" class="td-label">테스트 2 <span>〉</span></td><td class="result passed">통과 (0.12ms, 9.2MB)</td></tr><tr data-testcase-id="54451"><td valign="top" class="td-label">테스트 3 <span>〉</span></td><td class="result passed">통과 (3328.42ms, 9.31MB)</td></tr><tr data-testcase-id="54452"><td valign="top" class="td-label">테스트 4 <span>〉</span></td><td class="result passed">통과 (3010.63ms, 9.31MB)</td></tr><tr data-testcase-id="54453"><td valign="top" class="td-label">테스트 5 <span>〉</span></td><td class="result passed">통과 (6.30ms, 9.17MB)</td></tr><tr data-testcase-id="54454"><td valign="top" class="td-label">테스트 6 <span>〉</span></td><td class="result passed">통과 (71.51ms, 9.27MB)</td></tr><tr data-testcase-id="54455"><td valign="top" class="td-label">테스트 7 <span>〉</span></td><td class="result passed">통과 (0.06ms, 9.28MB)</td></tr><tr data-testcase-id="54456"><td valign="top" class="td-label">테스트 8 <span>〉</span></td><td class="result passed">통과 (0.24ms, 9.23MB)</td></tr><tr data-testcase-id="54457"><td valign="top" class="td-label">테스트 9 <span>〉</span></td><td class="result passed">통과 (0.71ms, 9.32MB)</td></tr><tr data-testcase-id="54458"><td valign="top" class="td-label">테스트 10 <span>〉</span></td><td class="result passed">통과 (495.83ms, 9.23MB)</td></tr><tr data-testcase-id="54459"><td valign="top" class="td-label">테스트 11 <span>〉</span></td><td class="result passed">통과 (1483.01ms, 9.16MB)</td></tr><tr data-testcase-id="54460"><td valign="top" class="td-label">테스트 12 <span>〉</span></td><td class="result passed">통과 (535.41ms, 9.11MB)</td></tr><tr data-testcase-id="54461"><td valign="top" class="td-label">테스트 13 <span>〉</span></td><td class="result passed">통과 (5496.51ms, 9.32MB)</td></tr><tr data-testcase-id="54462"><td valign="top" class="td-label">테스트 14 <span>〉</span></td><td class="result passed">통과 (1416.51ms, 9.17MB)</td></tr><tr data-testcase-id="54463"><td valign="top" class="td-label">테스트 15 <span>〉</span></td><td class="result passed">통과 (507.58ms, 9.16MB)</td></tr><tr data-testcase-id="54464"><td valign="top" class="td-label">테스트 16 <span>〉</span></td><td class="result passed">통과 (5.89ms, 9.36MB)</td></tr><tr data-testcase-id="54465"><td valign="top" class="td-label">테스트 17 <span>〉</span></td><td class="result passed">통과 (150.75ms, 9.34MB)</td></tr><tr data-testcase-id="54466"><td valign="top" class="td-label">테스트 18 <span>〉</span></td><td class="result passed">통과 (36.37ms, 9.43MB)</td></tr><tr data-testcase-id="54467"><td valign="top" class="td-label">테스트 19 <span>〉</span></td><td class="result passed">통과 (1.71ms, 9.22MB)</td></tr><tr data-testcase-id="54468"><td valign="top" class="td-label">테스트 20 <span>〉</span></td><td class="result passed">통과 (8.04ms, 9.42MB)</td></tr><tr data-testcase-id="54469"><td valign="top" class="td-label">테스트 21 <span>〉</span></td><td class="result passed">통과 (0.96ms, 9.29MB)</td></tr><tr data-testcase-id="54470"><td valign="top" class="td-label">테스트 22 <span>〉</span></td><td class="result passed">통과 (1.28ms, 9.23MB)</td></tr><tr data-testcase-id="54471"><td valign="top" class="td-label">테스트 23 <span>〉</span></td><td class="result passed">통과 (1.99ms, 9.16MB)</td></tr><tr data-testcase-id="54472"><td valign="top" class="td-label">테스트 24 <span>〉</span></td><td class="result passed">통과 (2.07ms, 9.09MB)</td></tr><tr data-testcase-id="54635"><td valign="top" class="td-label">테스트 25 <span>〉</span></td><td class="result passed">통과 (141.20ms, 9.39MB)</td></tr></tbody></table><div class="console-heading">채점 결과</div><div class="console-message">정확성: 100.0</div><div class="console-message">합계: 100.0 / 100.0</div></pre>

<pre class="console-content"><div></div><div class="console-heading">채점을 시작합니다.</div><div class="console-message">정확성  테스트</div><table class="console-test-group" data-category="correctness"><tbody><tr data-testcase-id="54449"><td valign="top" class="td-label">테스트 1 <span>〉</span></td><td class="result passed">통과 (0.13ms, 9.21MB)</td></tr><tr data-testcase-id="54450"><td valign="top" class="td-label">테스트 2 <span>〉</span></td><td class="result passed">통과 (0.23ms, 9.16MB)</td></tr><tr data-testcase-id="54451"><td valign="top" class="td-label">테스트 3 <span>〉</span></td><td class="result passed">통과 (1375.48ms, 9.19MB)</td></tr><tr data-testcase-id="54452"><td valign="top" class="td-label">테스트 4 <span>〉</span></td><td class="result passed">통과 (1276.44ms, 9.22MB)</td></tr><tr data-testcase-id="54453"><td valign="top" class="td-label">테스트 5 <span>〉</span></td><td class="result passed">통과 (5.44ms, 9.39MB)</td></tr><tr data-testcase-id="54454"><td valign="top" class="td-label">테스트 6 <span>〉</span></td><td class="result passed">통과 (226.84ms, 9.21MB)</td></tr><tr data-testcase-id="54455"><td valign="top" class="td-label">테스트 7 <span>〉</span></td><td class="result passed">통과 (0.08ms, 9.22MB)</td></tr><tr data-testcase-id="54456"><td valign="top" class="td-label">테스트 8 <span>〉</span></td><td class="result passed">통과 (0.49ms, 9.16MB)</td></tr><tr data-testcase-id="54457"><td valign="top" class="td-label">테스트 9 <span>〉</span></td><td class="result passed">통과 (0.92ms, 9.21MB)</td></tr><tr data-testcase-id="54458"><td valign="top" class="td-label">테스트 10 <span>〉</span></td><td class="result passed">통과 (1003.75ms, 9.19MB)</td></tr><tr data-testcase-id="54459"><td valign="top" class="td-label">테스트 11 <span>〉</span></td><td class="result passed">통과 (2085.88ms, 9.27MB)</td></tr><tr data-testcase-id="54460"><td valign="top" class="td-label">테스트 12 <span>〉</span></td><td class="result passed">통과 (1448.52ms, 9.27MB)</td></tr><tr data-testcase-id="54461"><td valign="top" class="td-label">테스트 13 <span>〉</span></td><td class="result passed">통과 (2303.00ms, 9.24MB)</td></tr><tr data-testcase-id="54462"><td valign="top" class="td-label">테스트 14 <span>〉</span></td><td class="result passed">통과 (1769.97ms, 9.2MB)</td></tr><tr data-testcase-id="54463"><td valign="top" class="td-label">테스트 15 <span>〉</span></td><td class="result passed">통과 (1025.96ms, 9.08MB)</td></tr><tr data-testcase-id="54464"><td valign="top" class="td-label">테스트 16 <span>〉</span></td><td class="result passed">통과 (23.08ms, 9.23MB)</td></tr><tr data-testcase-id="54465"><td valign="top" class="td-label">테스트 17 <span>〉</span></td><td class="result passed">통과 (297.70ms, 9.26MB)</td></tr><tr data-testcase-id="54466"><td valign="top" class="td-label">테스트 18 <span>〉</span></td><td class="result passed">통과 (98.27ms, 9.23MB)</td></tr><tr data-testcase-id="54467"><td valign="top" class="td-label">테스트 19 <span>〉</span></td><td class="result passed">통과 (7.87ms, 9.21MB)</td></tr><tr data-testcase-id="54468"><td valign="top" class="td-label">테스트 20 <span>〉</span></td><td class="result passed">통과 (27.83ms, 9.36MB)</td></tr><tr data-testcase-id="54469"><td valign="top" class="td-label">테스트 21 <span>〉</span></td><td class="result passed">통과 (6.75ms, 9.21MB)</td></tr><tr data-testcase-id="54470"><td valign="top" class="td-label">테스트 22 <span>〉</span></td><td class="result passed">통과 (1.02ms, 9.26MB)</td></tr><tr data-testcase-id="54471"><td valign="top" class="td-label">테스트 23 <span>〉</span></td><td class="result passed">통과 (0.89ms, 9.32MB)</td></tr><tr data-testcase-id="54472"><td valign="top" class="td-label">테스트 24 <span>〉</span></td><td class="result passed">통과 (0.99ms, 9.19MB)</td></tr><tr data-testcase-id="54635"><td valign="top" class="td-label">테스트 25 <span>〉</span></td><td class="result passed">통과 (95.37ms, 9.27MB)</td></tr></tbody></table><div class="console-heading">채점 결과</div><div class="console-message">정확성: 100.0</div><div class="console-message">합계: 100.0 / 100.0</div></pre>
---

## 💡 풀이 핵심

이렇게 풀면 안될거 같긴 한데... </br>
일단 무작정 백트래킹 브루트 포스로 조져본 결과 통과에 성공했음 </br>
분기는 인원 조합과 각 인원이 담당하는 범위에 대한 조합을 모두 트라이하는 것으로 </br>
1명부터 시작해서 dist.length 명까지 각 인원 조합에 대해 담당 범위를 산정했을때 </br>
flag를 통해 성공한 경우를 찾았다면 해당 인원수를 그대로 반환한다.</br>