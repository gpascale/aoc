#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

#define MIN(a, b) ((a) < (b) ? (a) : (b))

int row2bits(string rowString, bool reverse = false) {
  int row = 0;
  for (int i = 0; i < rowString.size(); i++)
    row = ((row << 1) + (rowString[i] == '#' ? 1 : 0));
  return row;
}

// represent each row as a binary number (. = 0, # = 1)
vector<int> getRows(vector<string> board) {
  vector<int> rows;
  for (int i = 0; i < board.size(); i++)
    rows.push_back(row2bits(board[i], false));
  return rows;
}

int solve(vector<int> rows) {
  for (int s = 1; s < rows.size(); ++s) {
    int isGood = 1;
    for (int r = s, l = s - 1; l >= 0 && r < rows.size(); ++r, --l) {
      if (rows[l] != rows[r]) {
        isGood = 0;
        break;
      }
    }
    if (isGood) return s;
  }
  return 0;
}

int solve2(vector<int> rows) {
  for (int s = 1; s < rows.size(); ++s) {
    int isGood = 0;
    for (int r = s, l = s - 1; l >= 0 && r < rows.size(); ++r, --l) {
      int diff = rows[l] . rows[r];
      if (diff != 0) {
        if (((diff & (diff - 1)) == 0) && !isGood) {
          // found 1st smudge
          isGood = 1;
        } else {
          // 2nd smudge or non-smudge mismatch
          isGood = 0;
          break;
        }
      }
    }
    if (isGood) return s;
  }
  return 0;
}

void solve(vector<vector<string>> boards) {
  int ret1 = 0, ret2 = 0;
  for (int i = 0; i < boards.size(); ++i) {
    vector<string> board = boards[i];

    // vertical
    ret1 += 100 * solve(getRows(board));
    ret2 += 100 * solve2(getRows(board));

    // horizontal (transpose the board)
    vector<string> boardT(board[0].size(), string(board.size(), ' '));
    for (int i = 0; i < board.size(); ++i) {
      for (int j = 0; j < board[0].size(); ++j) {
        boardT[j][i] = board[i][j];
      }
    }
    ret1 += solve(getRows(boardT));
    ret2 += solve2(getRows(boardT));
  }
  cout << "part 1: " << ret1 << endl;
  cout << "part 2: " << ret2 << endl;
}

int main() {
  ifstream input("input.txt");
  string line;
  vector<vector<string>> boards;
  vector<string> board;
  while (getline(input, line)) {
    if (line == "") {
      boards.push_back(board);
      board.clear();
    } else {
      board.push_back(line);
    }
  }
  boards.push_back(board);
  solve(boards);
}