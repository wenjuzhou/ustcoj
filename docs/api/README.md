# USTCOJ 接口设计规范

## 普遍规范

### 时间表示

遵守 ISO 8601 规范，如下：

```
YYYY-MM-DDTHH:MM:SSZ
```

### 简略信息

当只需要列表的时候，使用简略信息，提供的属性是详细信息的子集。

提供属性具体有哪些根据属性的不同而定，一般的，需要大量计算的信息不提供。

### 详细信息

获取单个资源的详细信息，包含该资源的所有属性。

这里的所有属性会因为认证权限的不同而不同。

## 认证

使用 session 记录认证信息。

## 分页

如果一个资源列表需要分页，使用以下参数：

`page`：代表第几页，从 1 开始编号，默认值为 1；

`per_page`：代表每页数量；

## 错误

| 错误名称         | 含义                                                         |
| ---------------- | ------------------------------------------------------------ |
| `missing`        | This means a resource does not exist.                        |
| `missing_field`  | This means a required field on a resource has not been set.  |
| `invalid`        | This means the formatting of a field is invalid. The documentation for that resource should be able to give you more specific information. |
| `already_exists` | This means another resource has the same value as this field. This can happen in resources that must have some unique key (such as Label names). |

## 链接

尽量避免拼接接口地址，接口提供的地址默认有以下含义：

| 参数    | 含义     |
| ------- | -------- |
| `next`  | 下一个   |
| `last`  | 最后一个 |
| `first` | 第一个   |
| `prev`  | 上一个   |
