class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Memoization dictionary to store the number of paths from each cell
        memo = {}

        def dfs(i, j):
            # If out of bounds, return 0 (invalid path)
            if i >= m or j >= n:
                return 0
            # If we reach the bottom-right corner, there's one valid path
            if i == m - 1 and j == n - 1:
                return 1
            # Check if the result is already memoized
            if (i, j) in memo:
                return memo[(i, j)]

            # Explore the two possible moves: right and down
            right_paths = dfs(i, j + 1)
            down_paths = dfs(i + 1, j)

            # Store the result in memo and return it
            memo[(i, j)] = right_paths + down_paths
            return memo[(i, j)]

        # Start DFS from the top-left corner
        return dfs(0, 0)
        
            
        