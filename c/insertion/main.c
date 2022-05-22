#include <stdio.h>
#include <stdlib.h>

int main() {

    int arr[] = {3, 1, 8, 6, 10};
    int temp;

    for (int i = 0; i < 5; i++){
        printf("%d ", arr[i]);
    }
    printf("\n");
    for (int i = 0; i < 5; i++){
        for (int j = i+1; j < 5; j++){
            if (arr[j] < arr[j-1]){
                temp = arr[j];
                arr[j] = arr[j-1];
                arr[j-1] = temp;
            }
        }
    }

    for (int i = 0; i < 5; i++){
        printf("%d ", arr[i]);
    }
	
}