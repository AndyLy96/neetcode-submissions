class Solution {
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> subset = new ArrayList<>();

        dfs(0, 0, target, subset, nums, res);
        return res;
    }

    public void dfs(int i, int curr, int target, List<Integer> subset, int[] nums, List<List<Integer>> res){
        if (curr == target){
            res.add(new ArrayList<>(subset));
            return;
        }

        if(curr > target || i >= nums.length){
            return;
        }

        subset.add(nums[i]);
        dfs(i, curr + nums[i], target, subset, nums,res);
        subset.remove(subset.size() -1);
        dfs(i+1, curr, target, subset, nums, res);
    }
}
