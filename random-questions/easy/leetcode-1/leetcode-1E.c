#include <stdlib.h>
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    
    int *rarr = malloc(2*sizeof(int));
    rarr[0] = 1;
    rarr[1] = 1;
    for (int i=0;i<numsSize;i++){
        for (int j=i+1;j<numsSize;j++){
            if(nums[i]+nums[j]==target){
                *returnSize = 2;
                rarr[0]=i;
                rarr[1]=j;
                return rarr;
            }
        }
    }
    *returnSize = 0;
    return 0;
}

int main(){
    int arr[] = {2,7,11,15};
    int target = 18;
    int ans[] = twoSum(arr, sizeof(arr), target, 2);
    printf(ans[0], ans[1]);
    return 0;
}
