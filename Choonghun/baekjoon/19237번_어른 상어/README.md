# 19237번: 어른 상어 - <img src="https://static.solved.ac/tier_small/15.svg" style="height:20px" /> Gold I

<!-- performance -->

<!-- 문제 제출 후 깃허브에 푸시를 했을 때 제출한 코드의 성능이 입력될 공간입니다.-->

<!-- end -->

## 📌 문제 정보
- 플랫폼: Baekjoon
- 유형: BFS
- 정답률: 40.519%
- 총 제출: 18,892회

## 🔗 문제 링크
[문제 링크](https://www.acmicpc.net/problem/19237)

---

## 📝 문제 설명

<section id="description" class="problem-section">
				<div class="headline">
				<h2>문제</h2>
				</div>
				<div id="problem_description" class="problem-text">
				<p><a href="/problem/19236">청소년 상어</a>는 더욱 자라 어른 상어가 되었다. 상어가 사는 공간에 더 이상 물고기는 오지 않고&nbsp;다른 상어들만이 남아있다. 상어에는&nbsp;1 이상 M 이하의 자연수 번호가 붙어 있고, 모든 번호는 서로 다르다. 상어들은 영역을 사수하기 위해 다른 상어들을 쫓아내려고 하는데, 1의 번호를 가진&nbsp;어른 상어는 가장 강력해서 나머지 모두를 쫓아낼 수 있다.</p>

<p>N×N 크기의 격자 중 M개의 칸에&nbsp;상어가 한 마리씩 들어 있다. 맨 처음에는 모든 상어가 자신의 위치에 자신의 냄새를 뿌린다. 그 후 1초마다 모든 상어가 동시에&nbsp;상하좌우로 인접한 칸 중 하나로 이동하고, 자신의 냄새를 그 칸에 뿌린다. 냄새는 상어가 k번 이동하고 나면 사라진다.</p>

<p>각 상어가 이동 방향을 결정할 때는, 먼저 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다. 그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다.&nbsp;이때 가능한 칸이 여러 개일 수 있는데, 그 경우에는 특정한 우선순위를 따른다. 우선순위는 상어마다 다를 수 있고, 같은 상어라도 현재 상어가 보고 있는 방향에 따라 또 다를 수 있다. 상어가 맨 처음에 보고 있는 방향은 입력으로 주어지고, 그 후에는 방금 이동한 방향이 보고 있는 방향이 된다.</p>

<p>모든 상어가 이동한 후 한 칸에 여러 마리의 상어가 남아 있으면, 가장 작은 번호를 가진 상어를 제외하고 모두 격자 밖으로 쫓겨난다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/149aa507-f474-43cb-9071-1959bb83d59a/-/preview/" style="width: 353px; height: 352px;"></p>

<p style="text-align: center;">&lt;그림 1&gt;</p>

<table class="table table-border table table-bordered" style="width: 100%;">
	<thead>
		<tr>
			<th colspan="8" style="text-align: center;">우선 순위</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th colspan="2" style="text-align: center;">상어 1</th>
			<th colspan="2" style="text-align: center;">상어 2</th>
			<th colspan="2" style="text-align: center;">상어 3</th>
			<th colspan="2" style="text-align: center;">상어 4</th>
		</tr>
		<tr>
			<th style="text-align: center;">↑</th>
			<td style="text-align: center;">↓ ← ↑ →</td>
			<th style="text-align: center;">↑</th>
			<td style="text-align: center;">↓ → ← ↑</td>
			<th style="text-align: center;">↑</th>
			<td style="text-align: center;">→ ← ↓ ↑</td>
			<th style="text-align: center;">↑</th>
			<td style="text-align: center;">← → ↑ ↓</td>
		</tr>
		<tr>
			<th style="text-align: center;">↓</th>
			<td style="text-align: center;">→ ↑ ↓ ←</td>
			<th style="text-align: center;">↓</th>
			<td style="text-align: center;">↓ ↑ ← →</td>
			<th style="text-align: center;">↓</th>
			<td style="text-align: center;">↑ → ← ↓</td>
			<th style="text-align: center;">↓</th>
			<td style="text-align: center;">← ↓ → ↑</td>
		</tr>
		<tr>
			<th style="text-align: center;">←</th>
			<td style="text-align: center;">← → ↓ ↑</td>
			<th style="text-align: center;">←</th>
			<td style="text-align: center;">← → ↑ ↓</td>
			<th style="text-align: center;">←</th>
			<td style="text-align: center;">↑ ← ↓ →</td>
			<th style="text-align: center;">←</th>
			<td style="text-align: center;">↑ → ↓ ←</td>
		</tr>
		<tr>
			<th style="text-align: center;">→</th>
			<td style="text-align: center;">→ ← ↑ ↓</td>
			<th style="text-align: center;">→</th>
			<td style="text-align: center;">→ ↑ ↓ ←</td>
			<th style="text-align: center;">→</th>
			<td style="text-align: center;">← ↓ ↑ →</td>
			<th style="text-align: center;">→</th>
			<td style="text-align: center;">↑ → ↓ ←</td>
		</tr>
	</tbody>
</table>

<p style="text-align: center;">&lt;표 1&gt;</p>

<p>&lt;그림 1&gt;은 맨 처음에 모든 상어가 자신의 냄새를 뿌린 상태를 나타내며, &lt;표 1&gt;에는 각 상어 및 현재 방향에 따른 우선순위가 표시되어 있다. 이 예제에서는 k = 4이다. 왼쪽 하단에 적힌 정수는&nbsp;냄새를 의미하고, 그 값은 사라지기까지 남은 시간이다. 좌측 상단에 적힌 정수는 상어의 번호 또는 냄새를 뿌린 상어의 번호를 의미한다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/b2d80580-57ba-419b-9d16-bc7fbe49512b/-/preview/" style="width: 900px; height: 352px;"></p>

<p style="text-align: center;">&lt;그림 2&gt;</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/52324aeb-3f7d-49b0-8128-560eb3742aa3/-/preview/" style="width: 901px; height: 358px;"></p>

<p style="text-align: center;">&lt;그림 3&gt;</p>

<p>&lt;그림 2&gt;는 모든 상어가 한 칸 이동하고 자신의 냄새를 뿌린 상태이고, &lt;그림 3&gt;은 &lt;그림 2&gt;의 상태에서 한 칸 더 이동한 것이다. (2, 4)에는 상어 2과 4가 같이 도달했기 때문에, 상어 4는 격자 밖으로 쫓겨났다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/86821cd6-b638-43a1-8abb-99c917d6d324/-/preview/" style="width: 901px; height: 355px;"></p>

<p style="text-align: center;">&lt;그림 4&gt;</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/76e735b6-44e1-437c-9b69-b7f55ea29d02/-/preview/" style="width: 902px; height: 357px;"></p>

<p style="text-align: center;">&lt;그림 5&gt;</p>

<p>&lt;그림 4&gt;은 격자에 남아있는 모든 상어가 한 칸 이동하고 자신의 냄새를 뿌린 상태, &lt;그림 5&gt;는 &lt;그림 4&gt;에서 한 칸 더 이동한 상태를&nbsp;나타낸다. 상어 2는 인접한 칸 중에 아무 냄새도 없는 칸이 없으므로&nbsp;자신의 냄새가 들어있는 (2, 4)으로 이동했다. 상어가 이동한 후에, 맨 처음에 각 상어가 뿌린 냄새는 사라졌다.</p>

<p>이 과정을 반복할 때, 1번 상어만 격자에 남게 되기까지 몇 초가 걸리는지를 구하는 프로그램을 작성하시오.</p>

</div>
</section>


## 입력

<div id="problem_input" class="problem-text">
					<p>첫 줄에는 N, M, k가&nbsp;주어진다. (2&nbsp;≤ N&nbsp;≤ 20, 2&nbsp;≤ M&nbsp;≤ N<sup>2</sup>, 1&nbsp;≤ k&nbsp;≤ 1,000)</p>

<p>그 다음 줄부터 N개의 줄에 걸쳐 격자의 모습이 주어진다. 0은 빈칸이고, 0이 아닌 수 x는 x번 상어가 들어있는 칸을 의미한다.</p>

<p>그 다음 줄에는 각 상어의 방향이 차례대로 주어진다.&nbsp;1, 2, 3, 4는 각각 위, 아래, 왼쪽, 오른쪽을 의미한다.</p>

<p>그 다음 줄부터 각 상어의 방향 우선순위가 상어 당 4줄씩 차례대로 주어진다. 각 줄은 4개의 수로 이루어져 있다. 하나의 상어를 나타내는 네 줄 중 첫 번째 줄은 해당 상어가 위를 향할 때의 방향 우선순위, 두 번째 줄은 아래를 향할 때의 우선순위, 세 번째 줄은 왼쪽을 향할 때의 우선순위, 네 번째 줄은 오른쪽을 향할 때의 우선순위이다. 각 우선순위에는 1부터 4까지의 자연수가 한 번씩 나타난다. 가장 먼저 나오는 방향이 최우선이다. 예를 들어, 우선순위가 1 3 2 4라면, 방향의 순서는 위, 왼쪽, 아래, 오른쪽이다.</p>


<p>맨 처음에는 각 상어마다 인접한 빈 칸이 존재한다. 따라서 처음부터 이동을 못 하는 경우는 없다.</p>

</div>

## 출력

<p>1번 상어만 격자에 남게 되기까지 걸리는 시간을 출력한다. 단, 1,000초가 넘어도 다른 상어가 격자에 남아 있으면 -1을 출력한다.</p>

## ⏱ 성능
- 시간: 364ms
- 메모리: 35140KB 
---

## 💡 풀이 핵심

상어 위치 파악 -> 모든 상어들에 대해 이동 가능한 곳 체크 후 이동 -> 모든 상어들의 냄새 관리 -> 시간 및 종료 여부 체크

냄새는 상어가 사라진다고 없어지지 않으며
이미 같은 위치의 냄새가 중복되어 큐에 들어가지 않도록 체크를 잘해주어야 한다.
그리고 현재 상어의 위치와 냄새의 위치를 구분해주기 위해
실제 상어가 있다면 음수, 냄새만 있다면 양수로 구분하였다.