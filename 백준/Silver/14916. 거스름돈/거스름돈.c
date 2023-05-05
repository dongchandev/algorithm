#include <stdio.h>

int main(){
    long long int n;
    int cnt=0;
    scanf("%lld",&n);
    while(n%5){
        n-=2;
        cnt++;
    }
    if(n<0)
        printf("%d",-1);
    else
        printf("%lld",cnt+n/5);
}