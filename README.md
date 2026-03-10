# hw01
八皇后问题工程化实践作业
# hw01 八皇后问题工程化实践
## 实现思路
使用回溯法逐行放置皇后，保证不同行、不同列、不同对角线；递归枚举所有合法解。
## 运行方式
python tests/test_queens.py
## 测试方式
pytest tests/ -v