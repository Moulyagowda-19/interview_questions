#include<stdio.h>

void b_sort(int arr[],int len){
    for(int i=0;i<len-1;i++){
        for(int j=0;j<len-1;j++){
            if(arr[j]>arr[j+1]){
                int temp =arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=temp;
            }
        }
    }
}
int main(){
    int arr[]={2,1,4,6,5};
    int len = sizeof(arr)/sizeof(arr[0]);
        
    b_sort(arr,len);
    printf("sorted arr :\n");
    for(int i=0;i<len;i++){
        printf("%d ",arr[i]);
    }
}
