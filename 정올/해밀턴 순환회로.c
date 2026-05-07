#include <stdio.h>

int N;
int A = 1e9;
int m[13][13];
int v[13];


void dfs(int n, int c, int r){

    if (r >= A){
        return;
    }
    
    if ( n == N - 1){
        if (m[c][0] != 0){
            if (r + m[c][0] < A){
                A = r + m[c][0];
            }
        }
        return;
    }

    for (int i = 1; i < N; i++){
        if (m[c][i] != 0 && v[i] == 0){
            v[i] = 1;
            dfs(n + 1, i, r + m[c][i]);
            v[i] = 0;
        }
    }
}

int main(){
    scanf("%d",&N);
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            scanf("%d",&m[i][j]);
        }
    }

    v[0] = 1;
    dfs(0,0,0);
    printf("%d\n",A);
}