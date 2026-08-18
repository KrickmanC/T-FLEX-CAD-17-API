# TFlex.Model.Model3D.Loft.AutomaticXyzPoint

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Loft`

## Summary

Класс автоматической точки соответствия

## Constructors

### `AutomaticXyzPoint(System.Double,System.Double,System.Double)`

ID: `M:TFlex.Model.Model3D.Loft.AutomaticXyzPoint.#ctor(System.Double,System.Double,System.Double)`

Конструктор для создания точки по абсолютным координатам

Parameters:
- `x`: Координата X
- `y`: Координата Y
- `z`: Координата Z

Remarks: Расстояние между координатами точки и контуром должно быть меньше значения Tolerance. Созданная точка в классе Loft сохраняется с типом PointVertex если расстояние между координатами точки и ближайшей вершиной контура меньше значения Tolerance или в тип PointEdge в противном случае

## Methods

### `AutomaticXyzPoint(System.Double,System.Double,System.Double)`

ID: `M:TFlex.Model.Model3D.Loft.AutomaticXyzPoint.#ctor(System.Double,System.Double,System.Double)`

Конструктор для создания точки по абсолютным координатам

Parameters:
- `x`: Координата X
- `y`: Координата Y
- `z`: Координата Z

Remarks: Расстояние между координатами точки и контуром должно быть меньше значения Tolerance. Созданная точка в классе Loft сохраняется с типом PointVertex если расстояние между координатами точки и ближайшей вершиной контура меньше значения Tolerance или в тип PointEdge в противном случае

## Propertys

### `Type`

ID: `P:TFlex.Model.Model3D.Loft.AutomaticXyzPoint.Type`

Получить тип точки

### `X`

ID: `P:TFlex.Model.Model3D.Loft.AutomaticXyzPoint.X`

Возвращает координату X точки

### `Y`

ID: `P:TFlex.Model.Model3D.Loft.AutomaticXyzPoint.Y`

Возвращает координату Y точки

### `Z`

ID: `P:TFlex.Model.Model3D.Loft.AutomaticXyzPoint.Z`

Возвращает координату Z точки
