# [Medium] Surrounded Regions

[문제 링크](https://leetcode.com/problems/surrounded-regions//) 


### 구분

리트코드

### 채점결과

0ms / 22.31MB

### 문제 설명

<p>You are given an <code>m x n</code> matrix <code>board</code> containing <strong>letters</strong> <code>'X'</code> and <code>'O'</code>, <strong>capture regions</strong> that are <strong>surrounded</strong>:</p>

<ul>
	<li><strong>Connect</strong>: A cell is connected to adjacent cells horizontally or vertically.</li>
	<li><strong>Region</strong>: To form a region <strong>connect every</strong> <code>'O'</code> cell.</li>
	<li><strong>Surround</strong>: A region is surrounded if none of the <code>'O'</code> cells in that region are on the edge of the board. Such regions are <strong>completely enclosed </strong>by <code>'X'</code> cells.</li>
</ul>

<p>To capture a <strong>surrounded region</strong>, replace all <code>'O'</code>s with <code>'X'</code>s <strong>in-place</strong> within the original board. You do not need to return anything.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]</span></p>

<p><strong>Explanation:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/xogrid.jpg" style="width: 367px; height: 158px;">
<p>In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">board = [["X"]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[["X"]]</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == board.length</code></li>
	<li><code>n == board[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 200</code></li>
	<li><code>board[i][j]</code> is <code>'X'</code> or <code>'O'</code>.</li>
</ul>

## 💡 풀이 핵심

최외곽 노드만 순회하며 방문하지 않은 O에 대해 BFS를 시작한다.</br>
X로 둘러싸이지 않은 O를 체크하기 위한 용도이다.<br/>
나머지 노드는 모두 X로 바꾸면 끝