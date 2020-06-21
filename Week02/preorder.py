class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        stack = [root]
        out = []
        while len(stack):
            temp = stack.pop()
            out.append(temp.val)
            stack.extend(reversed(temp.children))
        return out

# 递归
def recursive(self, root):
    	def rec(root):
		if root:
			out.append(root.val)
			for i in root.children:
				rec(i)

	out = []
	rec(root)
	return out