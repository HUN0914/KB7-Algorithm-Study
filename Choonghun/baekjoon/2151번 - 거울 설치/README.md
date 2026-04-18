# 2151번 - 거울 설치 <img src="https://static.solved.ac/tier_small/13.svg" style="height:20px" /> Gold III

<!-- performance -->

<!-- 문제 제출 후 깃허브에 푸시를 했을 때 제출한 코드의 성능이 입력될 공간입니다.-->

<!-- end -->

## 📌 문제 정보
- 플랫폼: Baekjoon
- 유형: BFS / 다익스트라
- 정답률: 27.125%
- 총 제출: 13,042회

## 🔗 문제 링크
[문제 링크](https://boj.kr/2151)

---

<div id="problem-body" class="">
			<div class="col-md-12">
				<section id="description" class="problem-section">
				<div class="headline">
				<h2>문제</h2>
				</div>
				<div id="problem_description" class="problem-text">
				<p>채영이는 거울을 들여다보는 것을 참 좋아한다. 그래서 집 곳곳에 거울을 설치해두고 집 안을 돌아다닐 때마다 거울을 보곤 한다.</p>

<p>채영이는 새 해를 맞이하여 이사를 하게 되었는데, 거울을 좋아하는 그녀의 성격 때문에 새 집에도 거울을 매달만한 위치가 여러 곳 있다. 또한 채영이네 새 집에는 문이 두 개 있는데, 채영이는 거울을 잘 설치하여 장난을 치고 싶어졌다. 즉, 한 쪽 문에서 다른 쪽 문을 볼 수 있도록 거울을 설치하고 싶어졌다.</p>

<p>채영이네 집에 대한 정보가 주어졌을 때, 한 쪽 문에서 다른 쪽 문을 볼 수 있도록 하기 위해 설치해야 하는 거울의 최소 개수를 구하는 프로그램을 작성하시오.</p>

<p>거울을 설치할 때에는 45도 기울어진 대각선 방향으로 설치해야 한다. 또한 모든 거울은 양면 거울이기 때문에 양 쪽 모두에서 반사가 일어날 수 있다. 채영이는 거울을 매우 많이 가지고 있어서 거울이 부족한 경우는 없다고 하자.</p>

<p>거울을 어떻게 설치해도 한 쪽 문에서 다른 쪽 문을 볼 수 없는 경우는 주어지지 않는다.</p>

</div>
</section>
</div>
                        <div class="col-md-12">
    <section id="input" class="problem-section">
    <div class="headline">
    <h2>입력</h2>
    </div>
    <div id="problem_input" class="problem-text">
    <p>첫째 줄에 집의 크기 N (2 ≤ N ≤ 50)이 주어진다. 다음 N개의 줄에는 N개의 문자로 집에 대한 정보가 주어진다. ‘#’는 문이 설치된 곳으로 항상 두 곳이며, ‘.’은 아무 것도 없는 것으로 빛은 이 곳을 통과한다. ‘!’은 거울을 설치할 수 있는 위치를 나타내고, ‘*’은 빛이 통과할 수 없는 벽을 나타낸다.</p>

</div>
</section>
</div>

<div class="col-md-12">
    <section id="output" class="problem-section">
    <div class="headline">
    <h2>출력</h2>
    </div>
    <div id="problem_output" class="problem-text">
    <p>첫째 줄에 설치해야 할 거울의 최소 개수를 출력한다.</p>

</div>
</section>
</div>
        <div class="col-md-12">
<section id="limit" style="display:none;" class="problem-section">
<div class="headline">
<h2>제한</h2>
</div>
<div id="problem_limit" class="problem-text">
        </div>
</section>
</div>
                                                    <div class="col-md-12">
<div class="row">
    <div class="col-md-6">
        <section id="sampleinput1">
        <div class="headline">
        <h2>예제 입력 1
            <button type="button" class="btn btn-link copy-button" style="padding: 0px;" data-clipboard-target="#sample-input-1">복사</button>
        </h2>
        </div>
        <pre class="sampledata" id="sample-input-1">5
***#*
*.!.*
*!.!*
*.!.*
*#***
</pre>
						</section>
					</div>
					<div class="col-md-6">
						<section id="sampleoutput1">
						<div class="headline">
						<h2>예제 출력 1
							<button type="button" class="btn btn-link copy-button" style="padding: 0px;" data-clipboard-target="#sample-output-1">복사</button>
						</h2>
						</div>
						<pre class="sampledata" id="sample-output-1">2</pre>
						</section>
					</div>
									</div>
				</div>
										<div class="col-md-12">
				<section id="hint" style="display: none;" class="problem-section">
				<div class="headline">
				<h2>힌트</h2>
				</div>
				<div id="problem_hint" class="problem-text">
				
</div>
</section>
</div>
</div>

## ⏱ 성능
- 시간: 204ms
- 메모리: 83536KB

---

## 💡 풀이 핵심

우선순위 큐를 활용하여 거울을 적게 사용한 경우를 우선적으로 다뤄서 
반대편 문으로 도착하는 경우를 찾도록 구현하면 된다.

따라서 다익스트라를 활용한다.

문제 예시에는 문이 반드시 벽에 있는 것처럼 되어 있는데
문은 어디든지 있을 수 있다. 벽도 꼭 가장자리에 있는 것이 아니므로
조건처리에 유의해야 한다.