# TFlex.Drawing.AffineMap

Assembly: `TFlexAPI`
Namespace: `TFlex.Drawing`

## Summary

Класс двухмерного афинного преобразования

## Constructors

### `AffineMap`

ID: `M:TFlex.Drawing.AffineMap.#ctor`

Конструктор

### `AffineMap(System.Double,System.Double,System.Double)`

ID: `M:TFlex.Drawing.AffineMap.#ctor(System.Double,System.Double,System.Double)`

Конструктор

Parameters:
- `offsetX`: Отступ по X
- `offsetY`: Отступ по Y
- `angle`: Угол поворота

### `AffineMap(System.Double,System.Double,System.Double,System.Double,System.Double,System.Double)`

ID: `M:TFlex.Drawing.AffineMap.#ctor(System.Double,System.Double,System.Double,System.Double,System.Double,System.Double)`

Конструктор

Parameters:
- `scale`: Масштаб
- `angle`: Угол поворота
- `originX`: Цент вращения X
- `originY`: Цент вращения Y
- `offsetX`: Отступ по X
- `offsetY`: Отступ по Y

### `AffineMap(TFlex.Drawing.AffineMap)`

ID: `M:TFlex.Drawing.AffineMap.#ctor(TFlex.Drawing.AffineMap)`

Конструктор

## Methods

### `AffineMap`

ID: `M:TFlex.Drawing.AffineMap.#ctor`

Конструктор

### `AffineMap(System.Double,System.Double,System.Double)`

ID: `M:TFlex.Drawing.AffineMap.#ctor(System.Double,System.Double,System.Double)`

Конструктор

Parameters:
- `offsetX`: Отступ по X
- `offsetY`: Отступ по Y
- `angle`: Угол поворота

### `AffineMap(System.Double,System.Double,System.Double,System.Double,System.Double,System.Double)`

ID: `M:TFlex.Drawing.AffineMap.#ctor(System.Double,System.Double,System.Double,System.Double,System.Double,System.Double)`

Конструктор

Parameters:
- `scale`: Масштаб
- `angle`: Угол поворота
- `originX`: Цент вращения X
- `originY`: Цент вращения Y
- `offsetX`: Отступ по X
- `offsetY`: Отступ по Y

### `AffineMap(TFlex.Drawing.AffineMap)`

ID: `M:TFlex.Drawing.AffineMap.#ctor(TFlex.Drawing.AffineMap)`

Конструктор

### `ApplyToAngle(System.Doubleref )`

ID: `M:TFlex.Drawing.AffineMap.ApplyToAngle(System.Double@)`

Применить афинное преобразование к углу

Parameters:
- `angle`: Значение угола в исходной системе координат

Remarks: На выходе метода получаем значение угла в преобразованной системе координат

### `Dispose`

ID: `M:TFlex.Drawing.AffineMap.Dispose`

Выполняет определяемые приложением задачи, связанные с удалением, высвобождением или сбросом неуправляемых ресурсов

### `Finalize`

ID: `M:TFlex.Drawing.AffineMap.Finalize`

Финализатор. Выполняет определяемые приложением задачи, связанные с удалением, высвобождением или сбросом неуправляемых ресурсов

### `Multiply(TFlex.Drawing.AffineMap)`

ID: `M:TFlex.Drawing.AffineMap.Multiply(TFlex.Drawing.AffineMap)`

Умножить карту преобразования на другую карту

Parameters:
- `other`: Карта, на которую умножаем

### `ToLCS(System.Doubleref ,System.Doubleref )`

ID: `M:TFlex.Drawing.AffineMap.ToLCS(System.Double@,System.Double@)`

Отменить афинное преобразование

Parameters:
- `x`: Координата x точки в системе координат после преобразования
- `y`: Координата y точки в системе координат после преобразования

Remarks: Входные значения координат x и y передаются по ссылке, на выходе метода получаем значения x и y в исходной системе координат

### `ToWCS(System.Doubleref ,System.Doubleref )`

ID: `M:TFlex.Drawing.AffineMap.ToWCS(System.Double@,System.Double@)`

Применить афинное преобразование

Parameters:
- `x`: Координата x точки в исходной системе координат
- `y`: Координата y точки в исходной системе координат

Remarks: Входные значения координат x и y передаются по ссылке, на выходе метода получаем значения x и y в преобразованной системе координат

## Propertys

### `Angle`

ID: `P:TFlex.Drawing.AffineMap.Angle`

Угол афинного преобразования

### `Scale`

ID: `P:TFlex.Drawing.AffineMap.Scale`

Масштаб афинного преобразования
