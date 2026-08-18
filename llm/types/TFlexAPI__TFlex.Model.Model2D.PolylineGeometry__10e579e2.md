# TFlex.Model.Model2D.PolylineGeometry

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Класс 2D геометрии - полилиния

## Constructors

### `PolylineGeometry(System.Collections.Generic.IEnumerable`1{TFlex.Drawing.Point})`

ID: `M:TFlex.Model.Model2D.PolylineGeometry.#ctor(System.Collections.Generic.IEnumerable`1{TFlex.Drawing.Point})`

Конструктор, инициализирующий параметры геометрии

Parameters:
- `points`: Точки полилинии

## Methods

### `PolylineGeometry(System.Collections.Generic.IEnumerable`1{TFlex.Drawing.Point})`

ID: `M:TFlex.Model.Model2D.PolylineGeometry.#ctor(System.Collections.Generic.IEnumerable`1{TFlex.Drawing.Point})`

Конструктор, инициализирующий параметры геометрии

Parameters:
- `points`: Точки полилинии

### `GetCircleArcApproximation(System.Double)`

ID: `M:TFlex.Model.Model2D.PolylineGeometry.GetCircleArcApproximation(System.Double)`

Аппроксимация дугами окружности.

### `GetCircleArcApproximation(System.Double[],System.Double[],System.Double)`

ID: `M:TFlex.Model.Model2D.PolylineGeometry.GetCircleArcApproximation(System.Double[],System.Double[],System.Double)`

Аппроксимация дугами окружности.

### `GetCircleArcApproximationByArray(System.Double[],System.Double[],System.Double)`

ID: `M:TFlex.Model.Model2D.PolylineGeometry.GetCircleArcApproximationByArray(System.Double[],System.Double[],System.Double)`

Аппроксимация дугами окружности.

Remarks: Каждые шесть элементов (xb, yb, xm, ym, xe, ye) задают дугу.

### `GetX(System.Int32)`

ID: `M:TFlex.Model.Model2D.PolylineGeometry.GetX(System.Int32)`

X-координата точки полилинии с указанным индексом

Remarks: Индекс может принимать значения от 0 до Count-1

### `GetY(System.Int32)`

ID: `M:TFlex.Model.Model2D.PolylineGeometry.GetY(System.Int32)`

Y-координата точки полилинии с указанным индексом

Remarks: Индекс может принимать значения от 0 до Count-1

## Propertys

### `Count`

ID: `P:TFlex.Model.Model2D.PolylineGeometry.Count`

Количество точек полилинии

### `Type`

ID: `P:TFlex.Model.Model2D.PolylineGeometry.Type`

Тип геометрии
