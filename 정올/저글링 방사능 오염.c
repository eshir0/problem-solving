#include <stdio.h>

int n,N;
int m[100][100];

int dy[] = {0,0,-1,1}, dx[] = {-1,1,0,0};

int q[1000];
int r=0,f=0;

void push(int data){
    q[r] = data;
    r++;
}

int pop(){
    int data = q[f];
    f++;
    return data;
}

int max(int m[100][100]){
    int b = 0;
    for(int i = 0; i < N; i++){
        for (int j = 0; j < n; j++){
            if (b < m[i][j]){
                b = m[i][j];
            }
        }
    }
    return b;
}


int main(){
    scanf("%d %d", &n, &N);
    for(int i=0; i < N; i++){
        for(int j=0; j < n; j++){
            scanf("%1d", &m[i][j]);
        }
    }
    int y,x;
    scanf("%d %d",&x,&y);
    x = x - 1;
    y = y - 1;
    m[y][x] = 3;
    push(y);
    push(x);
    while (r!=f){
        y = pop();
        x = pop();
        for(int i = 0; i < 4; i++){
            int ny = y + dy[i];
            int nx = x + dx[i];
            if (0 <= ny && ny < N && 0 <= nx && nx < n){
                if(m[ny][nx] == 1){
                    m[ny][nx] = m[y][x] + 1;
                    push(ny);
                    push(nx);
                }
            }
        }
    }
    int a=0;
    for (int i = 0; i < N; i++){
        for (int j = 0; j < n; j++){
            if (m[i][j]==1){
                a++;
            }
        }
    }
    printf("%d\n",max(m));
    printf("%d\n",a);
}