#include <stdio.h>

struct Rect{
    int r,c,area;
};

int main(){
    int T;
    scanf("%d", &T);
    for(int _ = 1; _ <= T; _++){
        int N;
        int m[100][100];
        struct Rect ans[10000];
        int t = 0;

        scanf("%d",&N);
        for (int i = 0; i < N; i++){
            for (int j = 0; j < N; j++){
                scanf("%d", &m[i][j]);
            }
        }

        for (int i = 0; i < N; i++){
            for (int j = 0; j < N; j++){
                if(m[i][j] != 0){
                    int r = 0, c = 0;
                    while(j+c<N && m[i][j+c] != 0) c++;
                    while(i+r<N && m[i+r][j] != 0) r++;
                    
                    for(int y = i; y < i+r; y++){
                        for(int x = j; x < j+c; x++){
                            m[y][x] = 0;
                        }
                    }
                    ans[t].r = r;
                    ans[t].c = c;
                    ans[t].area = r * c;
                    t++;
                }
            }
        }
        
        for(int i = 0; i < t - 1; i++){
            for(int j = 0; j < t - 1 - i; j++){
                if(ans[j].area > ans[j+1].area || (ans[j].area == ans[j+1].area && ans[j].r > ans[j + 1].r)){
                    struct Rect temp = ans[j];
                    ans[j] = ans[j + 1];
                    ans[j + 1] = temp;
                }
            }
        }

        printf("#%d %d",_,t);
        for (int i = 0; i < t; i++){
            printf(" %d %d", ans[i].r, ans[i].c);
        }
        printf("\n");
    }
}