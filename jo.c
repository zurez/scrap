#include <stdio.h>
#include <stdbool.h>
//Check for existense of a value in an array. Will be used below :D
bool check(int val, int *arr, int size){
	int i;
    for (i=0; i < size; i++) {
        if (arr[i] == val)
            return true;
    }
    return false;
}
// Ties

void ties(int numbers[], int array_size) {
  int temp[];
  for (int i = 0; i < array_size; ++i)
  {
  	if (check(numbers[i],temp,array_size))
  	{
  		
  	}
  }
   
   }
// 
int main(){
	int a[4]={1,2,2,3};
	int size = 4;
	bubbleSort(a,size);
	return 0 ;
}