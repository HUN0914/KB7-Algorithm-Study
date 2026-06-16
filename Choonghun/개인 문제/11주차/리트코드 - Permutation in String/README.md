# [Midium] Permutation in String

[문제 링크](https://leetcode.com/problems/permutation-in-string/?envType=problem-list-v2&envId=sliding-window) 


### 구분

리트코드

### 채점결과

147ms / 19.39MB

### 문제 설명
<div class="flex flex-col" style="position: relative;"><div class="HTMLContent_html__0OZLp" data-track-load="description_content"><p>Given two strings <code>s1</code> and <code>s2</code>, return <code>true</code> if <code>s2</code> contains a <span data-keyword="permutation-string" class=" cursor-pointer relative text-dark-blue-s text-sm"><button type="button" aria-haspopup="dialog" aria-expanded="false" aria-controls="radix-_r_1h_" data-state="closed" class="">permutation</button></span> of <code>s1</code>, or <code>false</code> otherwise.</p>

<p>In other words, return <code>true</code> if one of <code>s1</code>'s permutations is the substring of <code>s2</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> s1 = "ab", s2 = "eidbaooo"
<strong>Output:</strong> true
<strong>Explanation:</strong> s2 contains one permutation of s1 ("ba").
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s1 = "ab", s2 = "eidboaoo"
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s1.length, s2.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s1</code> and <code>s2</code> consist of lowercase English letters.</li>
</ul>

## 💡 풀이 핵심

윈도우를 구성하는 순열과 s1의 구성을 지속적으로 비교하기
