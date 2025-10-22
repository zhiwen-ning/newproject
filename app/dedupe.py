from collections import defaultdict
from typing import List, Optional

def dedupe_header(columns: List[str], case_format: Optional[str] = None) -> List[str]: 
    """ 
    通过为重复项添加数字后缀，使标题列名唯一；可选统一列名大小写格式。
    规则：
    1. 去重规则：
       - 名称的首次出现保持处理后格式（或原始格式）。
       - 同一名称的第2次、3次……出现时，分别添加“.1”、“.2”……（与pandas消除重复列标签逻辑一致）。
       - 完全保留输入列表的原始顺序，输入输出长度相同。
    2. 格式标准化规则（case_format 可选值）：
       - "upper"：全大写（如 "user_id" → "USER_ID"）
       - "lower"：全小写（如 "UserName" → "username"）
       - "title"：首字母大写（如 "product_name" → "Product_Name"）
       - None（默认）：不修改原始格式
    示例：
    - 输入：["id", "name", "Id", "NAME", "name"], case_format="lower"
    - 输出：["id", "name", "id.1", "name.1", "name.2"]
    - 输入：["user_id", "UserID", "user_id"], case_format="title"
    - 输出：["User_Id", "Userid", "User_Id.1"]
    """
    # 步骤1：处理列名格式（若指定格式）
    def format_column(col: str) -> str:
        if case_format == "upper":
            return col.upper()
        elif case_format == "lower":
            return col.lower()
        elif case_format == "title":
            # 处理下划线分隔的单词，确保每个单词首字母大写（如 "user_id" → "User_Id"）
            return "_".join(word.capitalize() for word in col.split("_"))
        else:
            return col  # 默认返回原始格式
    
    seen_counts = defaultdict(int)  # 记录处理后列名的出现次数
    result: List[str] = []          # 存储最终结果的列表
    for col in columns:
        # 步骤2：先对当前列名进行格式标准化
        formatted_col = format_column(col)
        # 步骤3：基于处理后的列名判断是否重复，执行去重逻辑
        count = seen_counts[formatted_col]
        if count == 0:
            result.append(formatted_col)
        else:
            result.append(f"{formatted_col}.{count}")
        # 步骤4：更新处理后列名的出现次数
        seen_counts[formatted_col] += 1
    return result

