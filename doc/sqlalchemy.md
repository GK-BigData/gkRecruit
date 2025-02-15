

# Flask SQLAlchemy 使用

## 一些前提

> SQLAlchemy 将代码转换为sql语句,with_entities类似sql中的select,选出需要的字段
>
> Model.query 是一个BaseQuery类
>
> 在调用.all(),.first(),.first_or_404() 这些函数之前，都可以通过print,将BaseQuery作为SQL语句输出
>
> 函数对应的参数都是列对象,列对象可以通过其他函数的返回值或者column函数将字符串转换为对应的列对象,Model.属性，也可以直接使用



## 常见操作

### 1. 使用sql函数

```python
from sqlalchemy.sql.expression import *

```

还有下面这个导入，每个都有各自的函数

```python
import sqlalchemy.sql.functions as func
```

### 2. 修改列名

调用avg之类的函数处理字段后,想修改字段名的话，在mysql里是as xx，这里是**调用列对象(column)的label方法**，如`xx.label(列名)`



## db.session

可用方法

['__call__', '__class__', '__contains__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'add', 'add_all', 'autocommit', 'autoflush', 'begin', 'begin_nested', 'bind', 'bulk_insert_mappings', 'bulk_save_objects', 'bulk_update_mappings', 'close', 'close_all', 'commit', 'configure', 'connection', 'delete', 'deleted', 'dirty', 'execute', 'expire', 'expire_all', 'expunge', 'expunge_all', 'flush', 'get_bind', 'identity_key', 'identity_map', 'info', 'is_active', 'is_modified', 'merge', 'new', 'no_autoflush', 'object_session', 'query', 'query_property', 'refresh', 'registry', 'remove', 'rollback', 'scalar', 'session_factory']

1. add

2. delete

   删除数据

3. 

## Model

> 定义数据库模型
>
> Flask里的Modal定义直接继承Modal类即可,Model类自db对象,db
>
> 通过db = SQLAlchemy()来创建
>
> 



model里的方法

['_Query__all_equivs', '__class__', '__clause_element__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_adapt_all_clauses', '_adapt_clause', '_adapt_col_list', '_adapt_polymorphic_element', '_adjust_for_single_inheritance', '_attributes', '_autoflush', '_bind_mapper', '_clone', '_compile_context', '_compound_eager_statement', '_conditional_options', '_connection_from_session', '_correlate', '_criterion', '_current_path', '_distinct', '_enable_assertions', '_enable_eagerloads', '_enable_single_crit', '_entities', '_entity_zero', '_execute_and_instances', '_execute_crud', '_execution_options', '_filter_aliases', '_for_update_arg', '_from_obj', '_from_obj_alias', '_from_selectable', '_get_bind_args', '_get_condition', '_get_existing_condition', '_get_impl', '_get_options', '_group_by', '_has_mapper_entities', '_having', '_identity_lookup', '_invoke_all_eagers', '_join', '_join_check_and_adapt_right_side', '_join_determine_implicit_left_side', '_join_entities', '_join_left_to_right', '_join_place_explicit_left_side', '_joinpath', '_joinpoint', '_joinpoint_zero', '_limit', '_mapper_adapter_map', '_mapper_entities', '_mapper_loads_polymorphically_with', '_mapper_zero', '_no_clauseelement_condition', '_no_criterion_assertion', '_no_criterion_condition', '_no_limit_offset', '_no_statement_condition', '_no_yield_per', '_offset', '_only_entity_zero', '_only_full_mapper_zero', '_only_load_props', '_only_return_tuples', '_options', '_order_by', '_orm_only_adapt', '_orm_only_from_obj_alias', '_params', '_polymorphic_adapters', '_populate_existing', '_prefixes', '_primary_entity', '_query_entity_zero', '_refresh_identity_token', '_refresh_state', '_reset_joinpoint', '_reset_polymorphic_adapter', '_select_args', '_select_from_entity', '_set_enable_single_crit', '_set_entities', '_set_entity_selectables', '_set_lazyload_from', '_set_op', '_set_select_from', '_should_log_debug', '_should_log_info', '_should_nest_selectable', '_simple_statement', '_statement', '_suffixes', '_update_joinpoint', '_values', '_version_check', '_with_current_path', '_with_hints', '_with_invoke_all_eagers', '_with_labels', '_with_options', '_yield_per', 'add_column', 'add_columns', 'add_entity', 'all', 'as_scalar', 'autoflush', 'column_descriptions', 'correlate', 'count', 'cte', 'delete', 'dispatch', 'distinct', 'enable_assertions', 'enable_eagerloads', 'except_', 'except_all', 'execution_options', 'exists', 'filter', 'filter_by', 'first', 'first_or_404', 'from_self', 'from_statement', 'get', 'get_execution_options', 'get_or_404', 'group_by', 'having', 'instances', 'intersect', 'intersect_all', 'join', 'label', 'lazy_loaded_from', 'limit', 'logger', 'merge_result', 'offset', 'one', 'one_or_none', 'only_return_tuples', 'options', 'order_by', 'outerjoin', 'paginate', 'params', 'populate_existing', 'prefix_with', 'reset_joinpoint', 'scalar', 'select_entity_from', 'select_from', 'selectable', 'session', 'slice', 'statement', 'subquery', 'suffix_with', 'union', 'union_all', 'update', 'value', 'values', 'whereclause', 'with_entities', 'with_for_update', 'with_hint', 'with_labels', 'with_lockmode', 'with_parent', 'with_polymorphic', 'with_session', 'with_statement_hint', 'with_transformation', 'yield_per']



update 

查询完后update更新

delete
删除所有数据
 zss = zs.query.delete()







字符串转列名

column函数

需要导入

```python
from sqlalchemy.sql.expression import *
```

修改列名

xx.label(列名)

排序

order_by

- contains

  最后转换为like函数..

  ```mysql
   SELECT sex_name, count(student_name) AS count_student_name 
  FROM zs 
  WHERE zs.recordid = %(recordid_1)s AND (source_provinces LIKE concat(concat('%%', %(source_provinces_1)s), '%%')) GROUP BY sex_name
  
  ```

  