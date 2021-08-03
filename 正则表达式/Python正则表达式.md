# 基本用法

```python
import re
pattern = re.compile("[a-z]+")
string =  "abc123def456ghi789"
print(pattern.match(string))
print(pattern.search(string))
print(pattern.findall(string))
print(pattern.finditer(string))
```

# 匹配字符

大多数字母和字符只会匹配自己。例如，正则表达式 `test`将完全匹配字符串 `test`：

```python
import re

pattern = re.compile("test")

string = "This is a test string for testing re."

print(re.findall(pattern, string))
```

另一些字符比较特殊，不匹配自己，这些字符匹配一些与众不同的东西，这些字符称为元字符。

一共有14个元字符：`. ^ $ * + ? { } [ ] \\ | ( )`

# 断言
