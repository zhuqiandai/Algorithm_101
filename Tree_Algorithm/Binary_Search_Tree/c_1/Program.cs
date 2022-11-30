//

namespace c_1
{
    class BSTree
    {
        public TreeNode? root { get; set; }

        public TreeNode? search(TreeNode? start, int target)
        {
            if (start == null || target == start.value)
                return root;

            if (start.value < target)
                return search(start.right, target);

            return search(start.left, target);
        }

        public TreeNode? search_iter(TreeNode? start, int target)
        {
            while (start != null && target != start.value)
            {
                if (target < start.value)
                {
                    start = start.left;
                }
                else
                {
                    start = start.right;
                }
            }

            return start;
        }

        public void insert(TreeNode node)
        {
            TreeNode? pointer = null;

            TreeNode? root = this.root;

            while (root != null)
            {
                pointer = root;

                if (root.value > node.value)
                {
                    this.root = root.left;
                }
                else
                {
                    this.root = root.right;
                }
            }

            node.parent = pointer;

            if (pointer == null)
            {
                this.root = node;
            }
            else if (node.value < pointer.value)
            {
                pointer.left = node;
            }
            else
            {
                pointer.right = node;
            }
        }

        public void inorder(TreeNode? start)
        {
            if (start != null)
            {
                inorder(start.left);
                System.Console.WriteLine(start.value);
                inorder(start.right);
            }
        }

        public void transplant(TreeNode u, TreeNode? v)
        {
            if (u.parent == null)
            {
                root = v;
            }
            else if (u == u.parent.left)
            {
                u.parent.left = v;
            }
            else
            {
                u.parent.right = v;
            }

            // if v is not null, set v's parent
            if (v != null)
            {
                v.parent = u.parent;
            }
        }

        public void delete(TreeNode node)
        {
            if (node.left == null)
            {
                transplant(node, node.right);
            }
            else if (node.right == null)
            {
                transplant(node, node.left);
            }
            else { }
        }

        public TreeNode maximum(TreeNode start)
        {
            while (start.right != null)
            {
                start = start.right;
            }

            return start;
        }

        public TreeNode minimum(TreeNode start)
        {
            while (start.left != null)
            {
                start = start.left;
            }

            return start;
        }
    }

    class TreeNode
    {
        public int value { get; }

        public TreeNode? left { get; set; }
        public TreeNode? right { get; set; }
        public TreeNode? parent { get; set; }

        public TreeNode(int value)
        {
            this.value = value;
        }
    }

    class Program
    {
        int[] values = new int[10] { 2, 3, 4, 5, 6, 7, 8, 9, 1, 10 };
    }
}
