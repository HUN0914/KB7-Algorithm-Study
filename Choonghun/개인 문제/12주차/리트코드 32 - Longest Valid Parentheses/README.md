# [Hard] Longest Valid Parentheses

[문제 링크](https://leetcode.com/problems/longest-valid-parentheses/description/) 


### 구분

리트코드

### 채점결과

7ms / 20.68MB

### 문제 설명
<div><div class="flex flex-col" style="position: relative;"><div class="HTMLContent_html__0OZLp" data-track-load="description_content"><p>Given a string containing just the characters <code>'('</code> and <code>')'</code>, return <em>the length of the longest valid (well-formed) parentheses </em><span data-keyword="substring-nonempty" class=" cursor-pointer relative text-dark-blue-s text-sm"><button type="button" aria-haspopup="dialog" aria-expanded="false" aria-controls="radix-_r_1h_" data-state="closed" class=""><em>substring</em></button></span>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> s = "(()"
<strong>Output:</strong> 2
<strong>Explanation:</strong> The longest valid parentheses substring is "()".
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s = ")()())"
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest valid parentheses substring is "()()".
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> s = ""
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>s[i]</code> is <code>'('</code>, or <code>')'</code>.</li>
</ul>

## 💡 풀이 핵심

괄호가 닫히는 구간을 모두 배열에 저장한 뒤</br>
정렬하여 투 포인터를 사용하여 최대 길이를 구한다.