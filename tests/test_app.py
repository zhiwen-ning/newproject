# 新增：将仓库根目录（app/与tests/的父目录）加入Python模块搜索路径
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

# 原有导入语句（此时可正常从app模块的app.py中导入dedupe_header）
from app import dedupe_header
def test_unique_columns():
    assert dedupe_header(["id", "name", "age"]) == ["id", "name", "age"]

def test_duplicate_columns():
    assert dedupe_header(["id", "id", "id"]) == ["id", "id.1", "id.2"]
def test_mixed_columns():
    cols = ["id", "name", "id", "name", "name"]
    expected = ["id", "name", "id.1", "name.1", "name.2"]
    assert dedupe_header(cols) == expected