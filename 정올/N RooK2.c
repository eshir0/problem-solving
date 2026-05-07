#include <stdio.h>

int N;
char m[9][9];
int v[9];
int a;

void dfs(int n){
    if (n == N){
        a++;
        return;
    }

    for(int i = 0; i < N; i++){
        if (m[n][i] == '.' && v[i] == 0){
            v[i] = 1;
            dfs(n+1);
            v[i] = 0;
        }
    }
}

int main(){
    scanf("%d",&N);
    for(int i = 0; i < N; i++){
        scanf("%s",m[i]);
    }

    dfs(0);
    printf("%d\n",a);
}