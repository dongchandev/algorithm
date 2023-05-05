#include <stdio.h>

int main(){
    int n;
    scanf("%d",&n);
    int triangleNum[46];
    for (int i = 1; i < 45; i++) {
        triangleNum[i-1] = (i*i + i) / 2;
    }
    for(int i=0;i<n;i++){
        int t=0;
        int flag=0;
        scanf("%d",&t);
        for (int a = 0; a < 44; a++) {
            for (int b = 0; b < 44; b++) {
                for (int c = 0; c < 44; c++) {
                    if (triangleNum[a] + triangleNum[b] + triangleNum[c] == t) {
                        flag=1;
                    }
                }
            }
        }
        if(flag==1)
            printf("%d\n",1);
        else
            printf("%d\n",0);
    }
}