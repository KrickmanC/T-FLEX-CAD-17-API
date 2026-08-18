# TFlex.Model.Model2D.ObjectNode

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Класс узла, принадлежащего объекту

## Constructors

### `ObjectNode(TFlex.Model.Document,System.UInt32,TFlex.Model.ModelObject)`

ID: `M:TFlex.Model.Model2D.ObjectNode.#ctor(TFlex.Model.Document,System.UInt32,TFlex.Model.ModelObject)`

Конструктор, задающий родительский 3D объект и идентификатор узла

Parameters:
- `document`: Документ объекта
- `parentObject`: Родительский 3D объект
- `index`: Идентификатор

### `ObjectNode(TFlex.Model.Document,TFlex.Model.Model2D.Object2D,System.UInt32)`

ID: `M:TFlex.Model.Model2D.ObjectNode.#ctor(TFlex.Model.Document,TFlex.Model.Model2D.Object2D,System.UInt32)`

Конструктор, задающий родительский 2D объект и идентификатор узла

Parameters:
- `document`: Документ объекта
- `parentObject`: Родительский 2D объект
- `index`: Идентификатор

## Methods

### `ObjectNode(TFlex.Model.Document,System.UInt32,TFlex.Model.ModelObject)`

ID: `M:TFlex.Model.Model2D.ObjectNode.#ctor(TFlex.Model.Document,System.UInt32,TFlex.Model.ModelObject)`

Конструктор, задающий родительский 3D объект и идентификатор узла

Parameters:
- `document`: Документ объекта
- `parentObject`: Родительский 3D объект
- `index`: Идентификатор

### `ObjectNode(TFlex.Model.Document,TFlex.Model.Model2D.Object2D,System.UInt32)`

ID: `M:TFlex.Model.Model2D.ObjectNode.#ctor(TFlex.Model.Document,TFlex.Model.Model2D.Object2D,System.UInt32)`

Конструктор, задающий родительский 2D объект и идентификатор узла

Parameters:
- `document`: Документ объекта
- `parentObject`: Родительский 2D объект
- `index`: Идентификатор

## Propertys

### `Index`

ID: `P:TFlex.Model.Model2D.ObjectNode.Index`

Идентификатор узла для определения номера его точки привязки к объекту

### `ParentObject`

ID: `P:TFlex.Model.Model2D.ObjectNode.ParentObject`

Объект, которому принадлежит узел

### `SubType`

ID: `P:TFlex.Model.Model2D.ObjectNode.SubType`

Подтип способа построения узла
