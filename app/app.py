from collections import defaultdict
from typing import List 

def dedupe_header(columns: List[str]) -> List[str]: 
    """ 
    通过为重复项添加数字后缀，使标题列名唯一。
    规则：
    - 名称的首次出现保持原样。
    - 同一名称的第2次、3次……出现时，分别添加“.1”、“.2”……（与pandas消除重复列标签逻辑一致）。
    - 完全保留输入列表的原始顺序。
    - 输入输出均为字符串列表，且长度相同。
    示例：["id", "name", "id", "name", "name"] -> ["id", "name", "id.1", "name.1", "name.2"]
    """
    seen_counts = defaultdict(int)  # 记录每个列名的出现次数
    result: List[str] = []          # 存储最终结果的列表
    for col in columns:
        count = seen_counts[col]    # 获取当前列名已出现的次数
        if count == 0:
            # 首次出现，直接添加列名
            result.append(col)
        else:
            # 重复出现，添加带数字后缀的列名
            result.append(f"{col}.{count}")
        # 更新当前列名的出现次数（每次循环后+1）
        seen_counts[col] += 1
    return result