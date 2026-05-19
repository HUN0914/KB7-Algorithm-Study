# 🧩 Lowest Common Ancestor of a Binary Tree

## 📌 문제 정보

| 항목 | 내용 |
| --- | --- |
| 플랫폼 | NeetCode |
| 문제 번호 | 236 |
| 난이도 | Medium |
| 분류 | Tree, Depth-First Search, Binary Tree |
| 언어 | Java |
| 제출 일자 | 2026년 05월 19일 10:50:40 |
| 문제 링크 | [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) |
| 원본 경로 | `Data Structures & Algorithms/lowest-common-ancestor-of-a-binary-tree/submission-0.java` |
<!-- AI_ANALYSIS: version=v1 model=gemini-3.1-flash-lite hash=cedd7a09e7ea65e2 -->

## 📝 문제 설명

You are given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the **[definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor)**: “The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow a **node to be a descendant of itself**).”

In this context, "lowest" means the deepest node in the tree, not the node with the smallest value.

**Example 1:**

```text
Input: root = [5,3,4,2,1], p = 1, q = 2

Output: 3
```

**Example 2:**

```text
Input: root = [5,3,4,2,1,null,9,null,11,10,12], p = 3, q = 12

Output: 3
```

**Constraints:**

- `2 <= The number of nodes in the tree <= 100,000`.

- `-1,000,000,000 <= Node.val <= 1,000,000,000`

- All `Node.val` are **unique**.

- `p != q`

- `p` and `q` will both exist in the tree.

## 📥 입력

```text
root = [5,3,4,2,1], p = 1, q = 2
```

## 📤 출력

```text
3
```

## 💡 핵심 아이디어

- 재귀를 사용하여 트리를 후위 순회하며 p와 q를 찾는다.
- 현재 노드가 p 또는 q와 일치하거나 null이면 해당 노드를 반환한다.
- 왼쪽과 오른쪽 서브트리에서 각각 반환된 값이 모두 존재하면 현재 노드가 LCA이다.
- 한쪽 서브트리에서만 값이 반환되면 해당 값을 상위 노드로 전달한다.

## 🧮 정답 계산식

현재 노드가 p 또는 q이거나, 왼쪽과 오른쪽 서브트리에서 각각 p와 q가 하나씩 발견되는 지점이 LCA이다.

## 🔍 구현 흐름

1. 기저 조건으로 root가 null이거나 p 또는 q와 일치하는지 확인한다.
2. 왼쪽 자식 노드에 대해 재귀 호출을 수행한다.
3. 오른쪽 자식 노드에 대해 재귀 호출을 수행한다.
4. 왼쪽과 오른쪽 결과가 모두 null이 아니면 현재 노드를 반환한다.
5. 둘 중 하나만 null이 아니면 null이 아닌 쪽을 반환하고, 둘 다 null이면 null을 반환한다.

## ⚠️ 주의할 점

- p와 q가 반드시 트리에 존재한다는 조건이 있으므로, 탐색 실패 케이스를 별도로 처리할 필요가 없다.
- 재귀 호출 시 트리의 깊이가 매우 깊을 경우 스택 오버플로우가 발생할 가능성을 고려해야 한다.

## 📁 제출 코드

- 풀이 파일: [solution.java](./solution.java)
- 수집 위치: `Data Structures & Algorithms/lowest-common-ancestor-of-a-binary-tree/submission-0.java`

## ⏱️ 복잡도 분석

- 시간 복잡도: O(N)
- 공간 복잡도: O(H)

## ✅ 한 줄 요약

재귀적 후위 순회를 통해 p와 q를 포함하는 가장 깊은 공통 조상 노드를 탐색하는 알고리즘입니다.
