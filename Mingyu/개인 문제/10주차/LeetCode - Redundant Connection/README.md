# 🧩 Redundant Connection

## 📌 문제 정보

| 항목 | 내용 |
| --- | --- |
| 플랫폼 | NeetCode |
| 문제 번호 | 684 |
| 난이도 | Medium |
| 분류 | Depth-First Search, Breadth-First Search, Union-Find, Graph Theory |
| 언어 | Java |
| 제출 일자 | 2026년 06월 10일 10:57:13 |
| 문제 링크 | [Redundant Connection](https://leetcode.com/problems/redundant-connection/) |
| 원본 경로 | `Data Structures & Algorithms/redundant-connection/submission-0.java` |
<!-- AI_ANALYSIS: version=v1 model=gemini-3.1-flash-lite hash=889dfbd94c62e33f -->

## 📝 문제 설명

You are given a connected **undirected graph** with `n` nodes labeled from `1` to `n`. Initially, it contained no cycles and consisted of `n-1` edges.

We have now added one additional edge to the graph. The edge has two **different** vertices chosen from `1` to `n`, and was not an edge that previously existed in the graph.

The graph is represented as an array `edges` of length `n` where `edges[i] = [ai, bi]` represents an edge between nodes `ai` and `bi` in the graph.

Return an edge that can be removed so that the graph is still a connected non-cyclical graph. If there are multiple answers, return the edge that appears last in the input `edges`.

**Example 1:**

```text
Input: edges = [[1,2],[1,3],[3,4],[2,4]]

Output: [2,4]
```

**Example 2:**

```text
Input: edges = [[1,2],[1,3],[1,4],[3,4],[4,5]]

Output: [3,4]
```

**Constraints:**

- `n == edges.length`

- `3 <= n <= 100`

- `1 <= edges[i][0] < edges[i][1] <= edges.length`

- There are no repeated edges and no self-loops in the input.

## 📥 입력

```text
edges = [[1,2],[1,3],[3,4],[2,4]]
```

## 📤 출력

```text
[2,4]
```

## 💡 핵심 아이디어

- 그래프 내에 사이클을 형성하는 마지막 간선을 찾는 문제로 Union-Find 알고리즘을 활용한다.
- 각 노드를 독립적인 집합으로 초기화한 뒤 간선을 하나씩 추가하며 연결 상태를 확인한다.
- 두 노드의 루트가 이미 동일하다면 해당 간선이 사이클을 만드는 중복 간선임을 판별한다.

## 🧮 정답 계산식

find(u) == find(v)인 경우 해당 간선 [u, v]는 사이클을 형성하는 중복 간선이다.

## 🔍 구현 흐름

1. 노드 개수만큼 부모 배열과 랭크 배열을 초기화한다.
2. 입력받은 간선 리스트를 순차적으로 순회한다.
3. 각 간선의 두 노드에 대해 find 연산을 수행하여 루트를 찾는다.
4. 루트가 같다면 사이클이 발생한 것이므로 즉시 해당 간선을 반환한다.
5. 루트가 다르다면 union 연산을 통해 두 집합을 병합한다.

## ⚠️ 주의할 점

- 문제에서 요구하는 마지막에 등장하는 간선을 반환하기 위해 순차적으로 탐색하며 가장 먼저 사이클을 만드는 간선을 찾는 로직이 중요하다.
- 경로 압축(Path Compression)과 랭크 기반 병합(Union by Rank)을 사용하여 연산 효율을 최적화해야 한다.

## 📁 제출 코드

- 풀이 파일: [solution.java](./solution.java)
- 수집 위치: `Data Structures & Algorithms/redundant-connection/submission-0.java`

## ⏱️ 복잡도 분석

- 시간 복잡도: O(N * α(N))
- 공간 복잡도: O(N)

## ✅ 한 줄 요약

Union-Find 자료구조를 사용하여 그래프 내에서 사이클을 형성하는 마지막 간선을 효율적으로 찾아내는 문제이다.
