# 14890번: 경사로 - <img src="https://static.solved.ac/tier_small/13.svg" style="height:20px" /> Gold III

## 📌 문제 정보
- 플랫폼: Baekjoon
- 유형: 구현
- 정답률: 58.476%
- 총 제출: 37,246회

## 🔗 문제 링크
[문제 링크](https://www.acmicpc.net/problem/14890)

---

<div id="problem_description" class="problem-text">
				<p>크기가 N×N인 지도가 있다. 지도의 각 칸에는 그 곳의 높이가 적혀져 있다. </p>

<p>오늘은 이 지도에서 지나갈 수 있는 길이 몇 개 있는지 알아보려고 한다. 길이란 한 행 또는 한 열 전부를 나타내며, 한쪽 끝에서 다른쪽 끝까지 지나가는 것이다. </p>

<p>다음과 같은 N=6인 경우 지도를 살펴보자.</p>

<p style="text-align:center"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/14890/1.png" style="height:250px; width:250px"></p>

<p>이때, 길은 총 2N개가 있으며, 아래와 같다.</p>

<p style="text-align:center"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/14890/2.png" style="height:290px; width:290px"></p>

<p>길을 지나갈 수 있으려면 길에 속한 모든 칸의 높이가 모두 같아야 한다. 또는, 경사로를 놓아서 지나갈 수 있는 길을 만들 수 있다. 경사로는 높이가 항상 1이며, 길이는 L이다. 또, 개수는 매우 많아 부족할 일이 없다. 경사로는 낮은 칸과 높은 칸을 연결하며, 아래와 같은 조건을 만족해야한다.</p>

<ul>
	<li>경사로는 낮은 칸에 놓으며, L개의 연속된 칸에 경사로의 바닥이 모두 접해야 한다.</li>
	<li>낮은 칸과 높은 칸의 높이 차이는 1이어야 한다.</li>
	<li>경사로를 놓을 낮은 칸의 높이는 모두 같아야 하고, L개의 칸이 연속되어 있어야 한다.</li>
</ul>

<p>아래와 같은 경우에는 경사로를 놓을 수 없다.</p>

<ul>
	<li>경사로를 놓은 곳에 또 경사로를 놓는 경우</li>
	<li>낮은 칸과 높은 칸의 높이 차이가 1이 아닌 경우</li>
	<li>낮은 지점의 칸의 높이가 모두 같지 않거나, L개가 연속되지 않은 경우</li>
	<li>경사로를 놓다가 범위를 벗어나는 경우</li>
</ul>

<p>L = 2인 경우에 경사로를 놓을 수 있는 경우를 그림으로 나타내면 아래와 같다.</p>

<p style="text-align:center"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/14890/3.png" style="height:107px; width:687px"></p>

<p>경사로를 놓을 수 없는 경우는 아래와 같다.</p>

<p style="text-align:center"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/14890/4.png" style="height:158px; width:1023px"></p>

<p>위의 그림의 가장 왼쪽부터 1번, 2번, 3번, 4번 예제라고 했을 때, 1번은 높이 차이가 1이 아니라서, 2번은 경사로를 바닥과 접하게 놓지 않아서, 3번은 겹쳐서 놓아서, 4번은 기울이게 놓아서 불가능한 경우이다.</p>

<p>가장 위에 주어진 그림 예의 경우에 지나갈 수 있는 길은 파란색으로, 지나갈 수 없는 길은 빨간색으로 표시되어 있으며, 아래와 같다. 경사로의 길이 L = 2이다.</p>

<p style="text-align:center"><img alt="" src="https://upload.acmicpc.net/255e47cf-0988-4b7f-b81c-2742f010a4c5/-/preview/" style="width: 338px; height: 338px;"></p>

<p>지도가 주어졌을 때, 지나갈 수 있는 길의 개수를 구하는 프로그램을 작성하시오.</p>

## 입력

<p>첫째 줄에 N (2 ≤ N ≤ 100)과 L (1 ≤ L ≤ N)이 주어진다. 둘째 줄부터 N개의 줄에 지도가 주어진다. 각 칸의 높이는 10보다 작거나 같은 자연수이다.</p>

## 출력

<p>첫째 줄에 지나갈 수 있는 길의 개수를 출력한다.</p>

## ⏱ 성능
- 시간: 36ms
- 메모리: 33412KB
---

## 💡 풀이 핵심

오르막 경사로와 내리막 경사로를 구분하고
오르막의 경우에는 이전부터 지금까지 l 이상의 여유 공간이 있어야 하고
내리막의 경우에는 지금부터 앞으로 l 이상의 여유 공간이 있어야 한다.
따라서 여유 공간을 체크하기 위한 변수나 자료구조를 선언 (아마 스택, 본인은 변수(temp) 사용했음)
높이가 달라질때마다 오르막을 설치해야 하는지 내리막을 설치해야 하는지 구분하고
설치 여부를 잘 판단하면 풀리는 문제