# [Hard] Expression Add Operators

[문제 링크](https://leetcode.com/problems/expression-add-operators/submissions/2035830310/?envType=problem-list-v2&envId=backtracking) 


### 구분

리트코드

### 채점결과

3106ms / 19.62MB

### 문제 설명

<div class="flex w-full flex-1 flex-col gap-4 overflow-y-auto px-4 py-5"><div class="flex items-start justify-between gap-4"><div class="flex items-start gap-2"></div>Hint</div></div><div><div class="flex flex-col" style="position: relative;"><div class="HTMLContent_html__0OZLp" data-track-load="description_content"><p>Given a string <code>num</code> that contains only digits and an integer <code>target</code>, return <em><strong>all possibilities</strong> to insert the binary operators </em><code>'+'</code><em>, </em><code>'-'</code><em>, and/or </em><code>'*'</code><em> between the digits of </em><code>num</code><em> so that the resultant expression evaluates to the </em><code>target</code><em> value</em>.</p>

<p>Note that operands in the returned expressions <strong>should not</strong> contain leading zeros.</p>

<p><strong>Note</strong> that a number can contain multiple digits.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> num = "123", target = 6
<strong>Output:</strong> ["1*2*3","1+2+3"]
<strong>Explanation:</strong> Both "1*2*3" and "1+2+3" evaluate to 6.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> num = "232", target = 8
<strong>Output:</strong> ["2*3+2","2+3*2"]
<strong>Explanation:</strong> Both "2*3+2" and "2+3*2" evaluate to 8.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> num = "3456237490", target = 9191
<strong>Output:</strong> []
<strong>Explanation:</strong> There are no expressions that can be created from "3456237490" to evaluate to 9191.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num.length &lt;= 10</code></li>
	<li><code>num</code> consists of only digits.</li>
	<li><code>-2<sup>31</sup> &lt;= target &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

## 💡 풀이 핵심

백트래킹을 하여 모든 경우의 수를 고려한다</br>
공식의 결과를 구할 때 하나의 식이 모두 완성된 다음에 곱셈 > 덧/뺄셈 </br>
순서에 맞게 결과값을 구하여 target과 비교후 정답에 추가한다.
