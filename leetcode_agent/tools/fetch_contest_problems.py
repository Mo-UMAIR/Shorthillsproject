def fetch_contest_problems(contest_name: str) -> list:
    """
    Returns a mock list of problems for a given contest.
    (Basic version: static data for reliability)
    """
    return [
        {
            "title": "Minimum Operations to Make Array Increasing",
            "url": "https://leetcode.com/problems/minimum-operations-to-make-array-increasing/",
        },
        {
            "title": "Count Good Nodes in Binary Tree",
            "url": "https://leetcode.com/problems/count-good-nodes-in-binary-tree/",
        },
        {
            "title": "Shortest Path in Grid with Obstacles",
            "url": "https://leetcode.com/problems/shortest-path-in-grid-with-obstacles-elimination/",
        },
    ]