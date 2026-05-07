//DFS 형태
#include <stdio.h>

int ck(int y, int x, int N, int m[N][N]){
    int dy[] = {0,0,-1,1}, dx[] = {-1,1,0,0};
    int cnt = 0;

    for(int i = 0; i < 4; i++){
        int ny = y + dy[i];
        int nx = x + dx[i];
        if (0 <= ny && ny < N && 0 <= nx && nx < N){
            if(m[ny][nx] == 1){
               m[ny][nx] = 0;
               cnt++;
               cnt += ck(ny,nx,N,m); 
            }
        }
    }
    return cnt;
}

int main(){
    int N = 0;
    scanf("%d",&N);

    int m[N][N];
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            scanf("%1d", &m[i][j]);
        }
    }
    int b[100];
    int ans = 0;
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            if(m[i][j] == 1){
                m[i][j] = 0;
                int a = 0;
                b[ans] = 1 + ck(i,j,N,m);
                ans++;
            }
        }
    }

    for(int i = 0; i < ans - 1; i++){
        for(int j = 0; j < ans - 1 - i; j++){
            if(b[j] > b[j+1]){
                int temp = b[j];
                b[j] = b[j+1];
                b[j+1] = temp;
          }
        }
    }
    
    printf("%d\n",ans);

    for(int i = 0; i < ans; i++){
        printf("%d\n",b[i]);
    }
}

// BFS 형태
#include <stdio.h>

int N;
int m[25][25];
int b[1000];
int dy[] = {0,0,-1,1}, dx[] = {-1,1,0,0};

int q[1000];
int f = 0, r = 0;

void push(int data){
    q[r] = data;
    r++;
}

int pop(){
    int data = q[f];
    f++;
    return data;
}

int e(){
    if(f == r) return 1;
    return 0;
}

int main(){
    scanf("%d",&N);
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            scanf("%1d", &m[i][j]);
        }
    }

    int A = 0;

    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            if(m[i][j] == 1){
                A += 1;
                push(i);
                push(j);
                int ans = 1;
                m[i][j] = 0;
                while (!e()){
                    int y = pop();
                    int x = pop();
                    for(int dir = 0; dir < 4; dir++){
                        int ny = y + dy[dir];
                        int nx = x + dx[dir];
                        if (0 <= ny && ny < N && 0 <= nx && nx < N){
                            if(m[ny][nx]==1){
                                m[ny][nx] = 0;
                                ans += 1;
                                push(ny);
                                push(nx);
                            }
                        }
                    }
                }
                b[A] = ans;
            }
        }
    }

    for (int i = 0; i < A; i++){
        for (int j = 0; j < A - i; j++){
            if(b[j] > b[j+1]){
                int t = b[j];
                b[j] = b[j+1];
                b[j+1] = t;
            }
        }
    }

    printf("%d\n",A);
    for(int i = 1; i < A+1; i++){
        printf("%d\n",b[i]);
    }
}