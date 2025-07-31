class Solution {
    public int[] runningSum(int[] nums) {
        int n = nums.length;
        int counter = 0;
        int[] runningSum = new int[n];
        for(int i = 0;i < n;i++){
            if(i==0){
                counter = nums[i];
                runningSum[i]=nums[i];
            }
            else{
                counter = counter + nums[i];
                runningSum[i]= counter;
            }
        }
        return runningSum;
    }
}