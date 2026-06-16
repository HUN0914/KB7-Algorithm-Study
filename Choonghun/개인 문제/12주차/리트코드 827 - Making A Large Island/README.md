# [Hard] Making A Large Island

[문제 링크](https://leetcode.com/problems/making-a-large-island/description/?envType=problem-list-v2&envId=breadth-first-search) 


### 구분

리트코드

### 채점결과

1097ms / 50.76MB

### 문제 설명

<div class="HTMLContent_html__0OZLp" data-track-load="description_content"><p>You are given an <code>n x n</code> binary matrix <code>grid</code>. You are allowed to change <strong>at most one</strong> <code>0</code> to be <code>1</code>.</p>

<p>Return <em>the size of the largest <strong>island</strong> in</em> <code>grid</code> <em>after applying this operation</em>.</p>

<p>An <strong>island</strong> is a 4-directionally connected group of <code>1</code>s.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> grid = [[1,0],[0,1]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> grid = [[1,1],[1,0]]
<strong>Output:</strong> 4
<strong>Explanation: </strong>Change the 0 to 1 and make the island bigger, only one island with area = 4.</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> grid = [[1,1],[1,1]]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Can't change any 0 to 1, only one island with area = 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= n &lt;= 500</code></li>
	<li><code>grid[i][j]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>

## 💡 풀이 핵심

BFS + DFS를 활용하여 각 섬의 넓이를 구하고</br>
각 섬을 연결할 수 있는 경우을 모두 따져서 넓이를 합산한다</br>
연결할 수 있는 경우가 없다면 주변에 남는 공간이 있는지를 고려하여 최대 넓이를 반환한다.</br>
