# TFlex.Model.ModelObject.Reference

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.ModelObject`

## Summary

Класс для передачи ссылки на другой объект модели

## Constructors

### `Reference(System.UInt32)`

ID: `M:TFlex.Model.ModelObject.Reference.#ctor(System.UInt32)`

Конструктор пустой ссылки по ключу с передаваемым набором флажков

Parameters:
- `states`: Набор флажков

### `Reference(TFlex.Model.ModelObject)`

ID: `M:TFlex.Model.ModelObject.Reference.#ctor(TFlex.Model.ModelObject)`

Конструктор ссылки по ключу

Parameters:
- `object`: Родительский объект

### `Reference(TFlex.Model.ModelObject,System.UInt32)`

ID: `M:TFlex.Model.ModelObject.Reference.#ctor(TFlex.Model.ModelObject,System.UInt32)`

Конструктор ссылки по ключу с передаваемым набором флажков

Parameters:
- `object`: Родительский объект
- `states`: Набор флажков

## Methods

### `Reference(System.UInt32)`

ID: `M:TFlex.Model.ModelObject.Reference.#ctor(System.UInt32)`

Конструктор пустой ссылки по ключу с передаваемым набором флажков

Parameters:
- `states`: Набор флажков

### `Reference(TFlex.Model.ModelObject)`

ID: `M:TFlex.Model.ModelObject.Reference.#ctor(TFlex.Model.ModelObject)`

Конструктор ссылки по ключу

Parameters:
- `object`: Родительский объект

### `Reference(TFlex.Model.ModelObject,System.UInt32)`

ID: `M:TFlex.Model.ModelObject.Reference.#ctor(TFlex.Model.ModelObject,System.UInt32)`

Конструктор ссылки по ключу с передаваемым набором флажков

Parameters:
- `object`: Родительский объект
- `states`: Набор флажков

## Propertys

### `AllowDelete`

ID: `P:TFlex.Model.ModelObject.Reference.AllowDelete`

Не удалять объект при удалении родителя (удалять только ссылку)

### `DeleteParentObjects`

ID: `P:TFlex.Model.ModelObject.Reference.DeleteParentObjects`

Удалять родительские объекты

### `IgnoreAllowDeteteForOneChild`

ID: `P:TFlex.Model.ModelObject.Reference.IgnoreAllowDeteteForOneChild`

Игнорировать флаг AllowDelete в случае удаления родителя с одним зависимым потомком

### `Object`

ID: `P:TFlex.Model.ModelObject.Reference.Object`

Родительский объект

### `States`

ID: `P:TFlex.Model.ModelObject.Reference.States`

Получить набор флагов
