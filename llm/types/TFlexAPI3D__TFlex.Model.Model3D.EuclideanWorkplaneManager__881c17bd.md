# TFlex.Model.Model3D.EuclideanWorkplaneManager

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Функции управления несколькими рабочими плоскостями

## Methods

### `MakeArray(TFlex.Model.Model3D.Workplane,TFlex.Model.Model3D.Workplane,System.Int32,System.Boolean,System.Double,System.Double,System.Double)`

ID: `M:TFlex.Model.Model3D.EuclideanWorkplaneManager.MakeArray(TFlex.Model.Model3D.Workplane,TFlex.Model.Model3D.Workplane,System.Int32,System.Boolean,System.Double,System.Double,System.Double)`

Создать группу рабочих плоскостей

Parameters:
- `plane1`: Первая плоскость
- `plane2`: Вторая плоскость
- `nCount`: 
- `fUseStep`: true - использовать значение шага step, иначе - определять шаг по расстоянию между данными плоскостями и количеству nCount
- `step`: 
- `beginOffset`: Начальное смещение
- `endOffset`: Конечное смещение

### `MakeUniform(TFlex.Model.Model3D.Workplane[],System.Double,System.Double)`

ID: `M:TFlex.Model.Model3D.EuclideanWorkplaneManager.MakeUniform(TFlex.Model.Model3D.Workplane[],System.Double,System.Double)`

Установить рабочие плоскости равномерно

Parameters:
- `planes`: Набор плоскостей
- `beginOffset`: Начальное смещение
- `endOffset`: Конечное смещение

### `MovePlane(TFlex.Model.Model3D.Workplane,System.Double)`

ID: `M:TFlex.Model.Model3D.EuclideanWorkplaneManager.MovePlane(TFlex.Model.Model3D.Workplane,System.Double)`

Переместить рабочую плоскость по нормали к плоскости на заданное значение

Parameters:
- `plane`: Перемещаемая плоскость
- `offset`: Величина, на которую выполняется перемещение

### `SetDistance(TFlex.Model.Model3D.Workplane,TFlex.Model.Model3D.Workplane,System.Double)`

ID: `M:TFlex.Model.Model3D.EuclideanWorkplaneManager.SetDistance(TFlex.Model.Model3D.Workplane,TFlex.Model.Model3D.Workplane,System.Double)`

Задать расстояние между рабочими плоскостями

Parameters:
- `basePlane`: Базовая плоскость
- `moveablePlane`: Перемещаемая плоскость
- `dDistance`: Расстояние
