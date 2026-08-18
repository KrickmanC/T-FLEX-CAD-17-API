# TFlex.Model.Model2D.ProjectionNode

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Узел полученный проецированием

## Constructors

### `ProjectionNode(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.ProjectionNode.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию. Координаты установлены в значение 0,0

Parameters:
- `document`: Документ объекта

### `ProjectionNode(TFlex.Model.Document,TFlex.Model.ModelObject,TFlex.Model.ModelObject)`

ID: `M:TFlex.Model.Model2D.ProjectionNode.#ctor(TFlex.Model.Document,TFlex.Model.ModelObject,TFlex.Model.ModelObject)`

Конструктор, задающий 3d объекты

Parameters:
- `document`: Документ объекта
- `workplane`: Рабочая плоскость
- `projectedObject`: Проецируемый объект (вершина или 3d узел)

## Methods

### `ProjectionNode(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.ProjectionNode.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию. Координаты установлены в значение 0,0

Parameters:
- `document`: Документ объекта

### `ProjectionNode(TFlex.Model.Document,TFlex.Model.ModelObject,TFlex.Model.ModelObject)`

ID: `M:TFlex.Model.Model2D.ProjectionNode.#ctor(TFlex.Model.Document,TFlex.Model.ModelObject,TFlex.Model.ModelObject)`

Конструктор, задающий 3d объекты

Parameters:
- `document`: Документ объекта
- `workplane`: Рабочая плоскость
- `projectedObject`: Проецируемый объект (вершина или 3d узел)

## Propertys

### `ProjectedObject`

ID: `P:TFlex.Model.Model2D.ProjectionNode.ProjectedObject`

проецируемый объект

### `SubType`

ID: `P:TFlex.Model.Model2D.ProjectionNode.SubType`

Тип узла

### `Workplane`

ID: `P:TFlex.Model.Model2D.ProjectionNode.Workplane`

Рабочая плоскость
