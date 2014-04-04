#include <stdio.h>
#include <stdlib.h> 
#include <string.h>

int main(void)
{
    int loop;
    int i = 0;
    int sum = 0;
    int *count = (int*) malloc(200 *sizeof(int));
    char *name = (char*) malloc(200 *sizeof(char));
    scanf ("%d",&loop); 
    for (i = 0; i < loop; i++){
        scanf("%s",name);
        memset(count , 0, 200 *sizeof(count));
        printf("%d\n",charcount(name, count));
    }
return 0;
}


int charcount(char *p, int *q){
    int sum = 0;
    int j;
    int a = 0;
    int b = 0;
    for(j = 0 ; j < strlen(p); j++)
    {
        q[*(p+j)]++;
    }
    //printf("%s",p);
    for(j = 0; j < 200; j++)
    {
       a =  (*(q + j)) / 2;
       b =  (*(q + j)) % 2;
       //printf("%d %d\n",a,b);
       sum = sum + a + b;
    }
    return sum;
}
