#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric> // accumulate関数のために必要
using namespace std;

int inp_i() {
    int x;
    cin >> x;
    return x;
}

vector<int> inp_li() {
    int n;
    cin >> n;
    vector<int> lst(n);
    for (int i = 0; i < n; ++i)
        cin >> lst[i];
    return lst;
}

string inp_s() {
    string s;
    cin >> s;
    return s;
}

vector<string> inp_ls() {
    int n;
    cin >> n;
    vector<string> lst(n);
    for (int i = 0; i < n; ++i)
        cin >> lst[i];
    return lst;
}

int main() {
    int M = inp_i(), N = inp_i();
    int K = inp_i();
    vector<string> Area(M);
    for (int i = 0; i < M; ++i)
        Area[i] = inp_s();
    
    vector<vector<int>> J(M, vector<int>(N + 1, 0));
    vector<vector<int>> O(M, vector<int>(N + 1, 0));
    for (int i = 0; i < M; ++i) {
        for (int j = 0; j < N; ++j) {
            if (Area[i][j] == 'J')
                J[i][j + 1] = J[i][j] + 1;
            else
                J[i][j + 1] = J[i][j];
            
            if (Area[i][j] == 'O')
                O[i][j + 1] = O[i][j] + 1;
            else
                O[i][j + 1] = O[i][j];
        }
    }

    for (int k = 0; k < K; ++k) {
        int ans1 = 0, ans2 = 0;
        int a, b, c, d;
        cin >> a >> b >> c >> d;
        for (int m = a - 1; m < c; ++m) {
            ans1 += J[m][d] - J[m][b - 1];
            ans2 += O[m][d] - O[m][b - 1];
        }
        cout << ans1 << " " << ans2 << " " << (c - a + 1) * (d - b + 1) - ans1 - ans2 << endl;
    }

    return 0;
}
