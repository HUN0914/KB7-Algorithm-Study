# 🧩 Maximum Depth of Binary Tree

## 📌 문제 정보

| 항목 | 내용 |
| --- | --- |
| 플랫폼 | NeetCode |
| 문제 번호 | 104 |
| 난이도 | Easy |
| 분류 | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| 언어 | Java |
| 제출 일자 | 2026년 05월 19일 09:28:59 |
| 문제 링크 | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) |
| 원본 경로 | `Data Structures & Algorithms/depth-of-binary-tree/submission-0.java` |
<!-- AI_ANALYSIS: version=v1 model=gemini-3.1-flash-lite hash=005c4d213df65433 -->

## 📝 문제 설명

Given the `root` of a binary tree, return its **depth**.

The **depth** of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.

**Example 1:**

```text
Input: root = [1,2,3,null,null,4]

Output: 3
```

**Example 2:**

```text
Input: root = []

Output: 0
```

**Constraints:**

- `0 <= The number of nodes in the tree <= 100`.

- `-100 <= Node.val <= 100`

## 📥 입력

```text
root = [1,2,3,null,null,4]
```

## 📤 출력

```text
3
```

## 💡 핵심 아이디어

- 이진 트리의 최대 깊이는 루트 노드에서 가장 먼 리프 노드까지의 경로에 있는 노드 수로 정의된다.
- 재귀적 구조를 활용하여 왼쪽 서브트리의 최대 깊이와 오른쪽 서브트리의 최대 깊이를 각각 구한다.
- 현재 노드를 포함한 전체 트리의 깊이는 양쪽 서브트리 깊이 중 큰 값에 1을 더한 값이다.

## 🧮 정답 계산식

maxDepth(node) = (node == null) ? 0 : 1 + max(maxDepth(node.left), maxDepth(node.right))

## 🔍 구현 흐름

1. 루트 노드가 null인 경우 트리가 비어있으므로 0을 반환한다.
2. 재귀 함수를 호출하여 왼쪽 자식 노드의 최대 깊이를 계산한다.
3. 재귀 함수를 호출하여 오른쪽 자식 노드의 최대 깊이를 계산한다.
4. 두 값 중 더 큰 값을 선택하고 현재 노드 층을 의미하는 1을 더하여 반환한다.

## ⚠️ 주의할 점

- 루트 노드가 null인 경우를 반드시 기저 조건으로 처리해야 런타임 에러를 방지할 수 있다.

## 📁 제출 코드

- 풀이 파일: [solution.java](./solution.java)
- 수집 위치: `Data Structures & Algorithms/depth-of-binary-tree/submission-0.java`

## ⏱️ 복잡도 분석

- 시간 복잡도: O(N)
- 공간 복잡도: O(H)

## ✅ 한 줄 요약

재귀적인 DFS 방식을 사용하여 각 서브트리의 최대 깊이를 비교하며 전체 트리의 높이를 계산하는 문제이다.
