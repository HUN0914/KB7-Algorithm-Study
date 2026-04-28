#include <map>
#include <vector>
#include <iostream>

using namespace std;

/*
1. 박스 하나 넣기
2. 밑으로 떨어뜨리기 (중력)
3. 반복:
   - 왼쪽으로 빠지는 박스 하나 제거
   - 중력
   - 오른쪽으로 빠지는 박스 하나 제거
   - 중력
*/

const int MAX = 55;

int N, M, maxBoxNum; // 현재 존재하는 박스 번호의 최대값

int MAP[MAX][MAX];

struct Box {
	int k, h, w, r, c;
	bool drop;
};

vector<Box> box(110); // 택배 박스

void init() {
	maxBoxNum = 0;

	cin >> N >> M;

	for (int i = 0; i < 110; i++) {
		box[i] = { 0, 0, 0, 0, 0, false };
	}

	// 범위 체크 안하기 위해 벽처럼 설정
	for (int r = 0; r <= N + 1; r++) {
		for (int c = 0; c <= N + 1; c++) {
			MAP[r][c] = -1;
		}
	}

	for (int r = 1; r <= N; r++) {
		for (int c = 1; c <= N; c++) {
			MAP[r][c] = 0;
		}
	}
}

void setBox(int idx) { // idx는 k를 뜻함
	auto& b = box[idx];
	for (int r = b.r; r < b.r + b.h; r++) {
		for (int c = b.c; c < b.c + b.w; c++) {
			MAP[r][c] = idx;
		}
	}
}

void deleteBox(int idx) {
	auto& b = box[idx];
	for (int r = b.r; r < b.r + b.h; r++) {
		for (int c = b.c; c < b.c + b.w; c++) {
			MAP[r][c] = 0;
		}
	}
}

bool canDown(int idx) {
	auto& b = box[idx];
	for (int c = b.c; c < b.c + b.w; c++) {
		if (MAP[b.r + b.h][c] != 0) { // r = b.r + b.h(박스 바로 아래칸)
			return false;
		}
	}
	return true;
}

void moveDown(int idx) {
	deleteBox(idx);

	while (canDown(idx)) {
		box[idx].r++;
	}

	setBox(idx);
}

/*
drop = true → 이미 밖으로 나간 택배
drop = false → 아직 창고에 있는 택배
*/
void moveDownAll() {
	while (true) {
		bool moved = false;

		for (int i = 1; i <= maxBoxNum; i++) {
			if (box[i].drop || box[i].k == 0) continue;
			if (!canDown(i)) continue;

			moveDown(i);
			moved = true;
		}

		if (!moved) break;

	}
}

bool canLeft(int idx) {
	auto& b = box[idx];

	for (int r = b.r; r < b.r + b.h; r++) { // 박스가 차지하는 모든 행 검사
		for (int c = 1; c < b.c; c++) { // 박스 왼쪽 열 검사
			if (MAP[r][c] != 0) return false;
		}
	}
	return true;
}

void moveLeft() {
	for (int i = 1; i <= maxBoxNum; i++) {
		if (box[i].drop || box[i].k == 0) continue;

		if (canLeft(i)) {
			box[i].drop = true;
			deleteBox(i);
			cout << i << "\n";
			return;
		}
	}
}

bool canRight(int idx) {
	auto& b = box[idx];

	for (int r = b.r; r < b.r + b.h; r++) {
		for (int c = b.c + b.w; c <= N; c++) {
			if (MAP[r][c] != 0) return false;
		}
	}
	return true;
}

void moveRight() {
	for (int i = 1; i <= maxBoxNum; i++) {
		if (box[i].drop || box[i].k == 0) continue;

		if (canRight(i)) {
			box[i].drop = true;
			deleteBox(i);
			cout << i << "\n";
			return;
		}
	}
}

void simulate() {
	// 1. 택배 투입
	for (int i = 0; i < M; i++) {
		int k, h, w, c;
		cin >> k >> h >> w >> c;

		box[k] = { k, h, w, 1, c, false };

		maxBoxNum = max(maxBoxNum, k);

		setBox(k);
		moveDown(k);
	}

	// 2. 시뮬레이션
	for (int i = 0; i < M; i += 2) { // 한 번 돌 때 박스 2개씩 제거하므로 += 2
		moveLeft();
		moveDownAll();

		moveRight();
		moveDownAll();
	}

}

int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	init();
	simulate();

	return 0;
}
