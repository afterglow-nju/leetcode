class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        max_diameter = [0]  # Using a list to hold the max_diameter to make it mutable in nested functions
        E1, E2 = defaultdict(list), defaultdict(list)

        def dfs(node, parent, edge):
            max_depth_1, max_depth_2 = 0, 0

            for neighbor in edge[node]:
                if neighbor == parent:
                    continue

                depth = dfs(neighbor, node, edge)

                if depth > max_depth_1:
                    max_depth_2 = max_depth_1
                    max_depth_1 = depth
                elif depth > max_depth_2:
                    max_depth_2 = depth

            max_diameter[0] = max(max_diameter[0], max_depth_1 + max_depth_2)

            return max_depth_1 + 1

        # Build the first tree
        for x, y in edges1:
            E1[x].append(y)
            E1[y].append(x)

        # Build the second tree
        for x, y in edges2:
            E2[x].append(y)
            E2[y].append(x)

        # Calculate diameter for first tree
        dfs(0, -1, E1)
        d1 = max_diameter[0]

        # Reset for the second tree
        max_diameter[0] = 0

        # Calculate diameter for second tree
        dfs(0, -1, E2)
        d2 = max_diameter[0]
        #print(d1,d2)
        return min(d1+d2+1,max(d1,d2,math.ceil(d1/2)+math.ceil(d2/2)+1))