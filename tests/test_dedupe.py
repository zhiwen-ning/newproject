from app import dedupe_header

def test_dedupe_with_lower_format():
    """测试全小写格式标准化 + 去重（忽略原始大小写差异）"""
    input_cols = ["id", "Name", "ID", "NAME", "id"]
    expected = ["id", "name", "id.1", "name.1", "id.2"]
    assert dedupe_header(input_cols, case_format="lower") == expected

def test_dedupe_with_upper_format():
    """测试全大写格式标准化 + 去重（统一转为大写后判断重复）"""
    input_cols = ["user", "User", "USER", "user", "User"]
    expected = ["USER", "USER.1", "USER.2", "USER.3", "USER.4"]
    assert dedupe_header(input_cols, case_format="upper") == expected

def test_dedupe_with_title_format():
    """测试首字母大写格式标准化 + 去重（处理下划线分隔列名）"""
    input_cols = ["user_id", "productName", "user_id", "Product_Name", "order_id"]
    expected = ["User_Id", "Productname", "User_Id.1", "Product_Name.1", "Order_Id"]
    assert dedupe_header(input_cols, case_format="title") == expected

def test_dedupe_with_invalid_format():
    """测试非法格式参数（按默认逻辑处理，不进行格式标准化）"""
    input_cols = ["Id", "ID", "id", "Id"]
    # 非法格式参数→不标准化，仅按原始字符串去重（4个值均为不同原始字符串，无重复）
    expected = ["Id", "ID", "id", "Id.1"]
    assert dedupe_header(input_cols, case_format="invalid") == expected

def test_dedupe_empty_columns_with_format():
    """测试空列表输入 + 格式参数（边界场景，确保无报错且返回空列表）"""
    assert dedupe_header([], case_format="lower") == []

def test_dedupe_single_column_with_format():
    """测试单个列名输入 + 格式参数（无重复，仅验证格式转换）"""
    input_cols = ["product_price"]
    # 首字母大写格式："product_price" → "Product_Price"
    assert dedupe_header(input_cols, case_format="title") == ["Product_Price"]
    # 全大写格式："product_price" → "PRODUCT_PRICE"
    assert dedupe_header(input_cols, case_format="upper") == ["PRODUCT_PRICE"]