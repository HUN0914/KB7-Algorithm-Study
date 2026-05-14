# [Medium] Mine Sweeper

[문제 링크](https://leetcode.com/problems/minesweeper/) 


### 구분

리트코드

### 채점결과

7ms / 19.71MB

### 문제 설명

<div class="HTMLContent_html__0OZLp" data-track-load="description_content"><p>Let's play the minesweeper game (<a href="https://en.wikipedia.org/wiki/Minesweeper_(video_game)" target="_blank">Wikipedia</a>, <a href="http://minesweeperonline.com" target="_blank">online game</a>)!</p>

<p>You are given an <code>m x n</code> char matrix <code>board</code> representing the game board where:</p>

<ul>
	<li><code>'M'</code> represents an unrevealed mine,</li>
	<li><code>'E'</code> represents an unrevealed empty square,</li>
	<li><code>'B'</code> represents a revealed blank square that has no adjacent mines (i.e., above, below, left, right, and all 4 diagonals),</li>
	<li>digit (<code>'1'</code> to <code>'8'</code>) represents how many mines are adjacent to this revealed square, and</li>
	<li><code>'X'</code> represents a revealed mine.</li>
</ul>

<p>You are also given an integer array <code>click</code> where <code>click = [click<sub>r</sub>, click<sub>c</sub>]</code> represents the next click position among all the unrevealed squares (<code>'M'</code> or <code>'E'</code>).</p>

<p>Return <em>the board after revealing this position according to the following rules</em>:</p>

<ol>
	<li>If a mine <code>'M'</code> is revealed, then the game is over. You should change it to <code>'X'</code>.</li>
	<li>If an empty square <code>'E'</code> with no adjacent mines is revealed, then change it to a revealed blank <code>'B'</code> and all of its adjacent unrevealed squares should be revealed recursively.</li>
	<li>If an empty square <code>'E'</code> with at least one adjacent mine is revealed, then change it to a digit (<code>'1'</code> to <code>'8'</code>) representing the number of adjacent mines.</li>
	<li>Return the board when no more squares will be revealed.</li>
</ol>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img src="https://assets.leetcode.com/uploads/2023/08/09/untitled.jpeg" style="width: 500px; max-width: 400px; height: 269px;">
<pre><strong>Input:</strong> board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], click = [3,0]
<strong>Output:</strong> [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img src="https://assets.leetcode.com/uploads/2023/08/09/untitled-2.jpeg" style="width: 489px; max-width: 400px; height: 269px;">
<pre><strong>Input:</strong> board = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]], click = [1,2]
<strong>Output:</strong> [["B","1","E","1","B"],["B","1","X","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == board.length</code></li>
	<li><code>n == board[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 50</code></li>
	<li><code>board[i][j]</code> is either <code>'M'</code>, <code>'E'</code>, <code>'B'</code>, or a digit from <code>'1'</code> to <code>'8'</code>.</li>
	<li><code>click.length == 2</code></li>
	<li><code>0 &lt;= click<sub>r</sub> &lt; m</code></li>
	<li><code>0 &lt;= click<sub>c</sub> &lt; n</code></li>
	<li><code>board[click<sub>r</sub>][click<sub>c</sub>]</code> is either <code>'M'</code> or <code>'E'</code>.</li>
</ul>
</div>

## 💡 풀이 핵심

8방향에 대해 탐색하며, 근처에 지뢰가 있으면 방문처리를 하지 않고, 현재 노드에 카운트한 지뢰 개수를 입력한다.</br>
지뢰가 없으면 방문처리를 하여 큐에 삽입하고 현재 노드는 'B'를 입력한다.</br>