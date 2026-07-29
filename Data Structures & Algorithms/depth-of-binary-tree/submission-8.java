/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null){
            return 0;
        }

        return helps(root, 1);
    }

    public int helps(TreeNode node, int depth) {
        if (node == null){
            return depth;
        }

        if(node.left == null && node.right == null){
            return depth;
        }

        int left = helps(node.left, depth + 1);
        int right = helps(node.right, depth + 1);

        return Math.max(left,right);
    }
}
