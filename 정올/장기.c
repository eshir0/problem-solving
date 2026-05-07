#include <stdio.h>

int N,M;
int m[105][105];
int dy[] = {-2,-2,-1,-1,1,1,2,2};
int dx[] = {-1,1,-2,2,-2,2,-1,1};
int ay,ax;


void dfs(int y, int x, int cnt){
    if (cnt >= m[y][x]){
        return;
    }
    m[y][x] = cnt;

    if (y == ay && x == ax){
        return;
    }

    for(int i = 0; i < 8; i++){
        int ny = y + dy[i];
        int nx = x + dx[i];
        if (ny >= 1 && ny <= N && nx >= 1 && nx <= M){
            dfs(ny,nx,cnt +1);
        }
    }

}

int main(){
    scanf("%d %d",&N,&M);

    for(int i = 0; i <= N; i++){
        for(int j = 0; j <= M; j++){
            m[i][j] = 1e9;
        }
    }

    int y,x;
    scanf("%d %d %d %d",&y,&x,&ay,&ax);
    dfs(y,x,0);
    printf("%d\n",m[ay][ax]);
}