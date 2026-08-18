# TFlex.Model.Model3D.DynamicStudy

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Задача динамического анализа

## Methods

### `GetRestraint(System.Int32)`

ID: `M:TFlex.Model.Model3D.DynamicStudy.GetRestraint(System.Int32)`

Получить нагружение по номеру

Parameters:
- `index`: Номер нагружения

Remarks: Элементы нумеруются от нуля. Если индекс отрицательный или превышает количество элементов, то результат не определён

### `GetSensor(System.Int32)`

ID: `M:TFlex.Model.Model3D.DynamicStudy.GetSensor(System.Int32)`

Получить датчик по номеру

Parameters:
- `index`: Номер датчика

Remarks: Элементы нумеруются от нуля. Если индекс отрицательный или превышает количество элементов, то результат неопределён

### `Solve`

ID: `M:TFlex.Model.Model3D.DynamicStudy.Solve`

Рассчитать задачу

### `Solve(TFlex.Model.Model3D.DynamicStudy.SolveCallback)`

ID: `M:TFlex.Model.Model3D.DynamicStudy.Solve(TFlex.Model.Model3D.DynamicStudy.SolveCallback)`

Рассчитать задачу с возможностью досрочной остановки расчёта

Parameters:
- `callback`: Функция, вызываемая в конце каждого шага симуляции. Возврат значения false сигнализирует о необходимости прервать расчёт

Remarks: Функция, переданная в параметре callback, не должна каким-либо образом изменять состояние относящихся к задаче объектов, так как это может привести к нежелательным последствиям

## Propertys

### `Frame`

ID: `P:TFlex.Model.Model3D.DynamicStudy.Frame`

Текущий кадр моделирования

### `RestraintCount`

ID: `P:TFlex.Model.Model3D.DynamicStudy.RestraintCount`

Количество нагружений

### `SensorCount`

ID: `P:TFlex.Model.Model3D.DynamicStudy.SensorCount`

Количество датчиков

### `Time`

ID: `P:TFlex.Model.Model3D.DynamicStudy.Time`

Текущее время моделирования
