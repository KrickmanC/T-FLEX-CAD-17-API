# TFlex.Model.Model3D.Geometry.SweepGenerator.Law.Discrete

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry.SweepGenerator.Law`

## Summary

Табличная функция : вершина траектории и значение закона в ней. Возможно перечисление значений с использованием конструкции foreach

## Remarks

Можно задавать любой набор пар вершина траектории / значение. То есть не обязательно задавать закон во всех точках. Порядок задания пар несущественен за исключением замкнутой траектории. В последнем случае первое вхождение в список вершины ассоциируется с начальным значением функции. Второй вхождение - с конечным значением функции. Существует два специальных варианта интерпретации закона : - Если в таблице только одна пара, то функция считается константной; - Если в таблице две пары, соответственно для начальной вершины и конечной вершины траектории, то используется линейная интерполяция.

## Methods

### `Add(TFlex.Model.Model3D.Geometry.SweepGenerator.Law.Discrete.Association)`

ID: `M:TFlex.Model.Model3D.Geometry.SweepGenerator.Law.Discrete.Add(TFlex.Model.Model3D.Geometry.SweepGenerator.Law.Discrete.Association)`

Добавить пару в конец списка

### `Delete(System.UInt32)`

ID: `M:TFlex.Model.Model3D.Geometry.SweepGenerator.Law.Discrete.Delete(System.UInt32)`

Удалить пару по номеру

Parameters:
- `index`: Номер пары

Remarks: Пары нумеруются от нуля. Если индекс отрицательный или превышает пар, то результат не определён

### `DeleteAll`

ID: `M:TFlex.Model.Model3D.Geometry.SweepGenerator.Law.Discrete.DeleteAll`

Удалить все пары

### `GetEnumerator`

ID: `M:TFlex.Model.Model3D.Geometry.SweepGenerator.Law.Discrete.GetEnumerator`

Получить перечислитель

### `Insert(System.UInt32,TFlex.Model.Model3D.Geometry.SweepGenerator.Law.Discrete.Association)`

ID: `M:TFlex.Model.Model3D.Geometry.SweepGenerator.Law.Discrete.Insert(System.UInt32,TFlex.Model.Model3D.Geometry.SweepGenerator.Law.Discrete.Association)`

Вставить пару перед номером

Parameters:
- `index`: Номер пары

Remarks: Пары нумеруются от нуля. Если индекс отрицательный или превышает количество пар, то результат не определён

### `MoveNext`

ID: `M:TFlex.Model.Model3D.Geometry.SweepGenerator.Law.Discrete.MoveNext`

Перейти к следующему элементу

### `Reset`

ID: `M:TFlex.Model.Model3D.Geometry.SweepGenerator.Law.Discrete.Reset`

Сбросить перечислитель

## Propertys

### `Current`

ID: `P:TFlex.Model.Model3D.Geometry.SweepGenerator.Law.Discrete.Current`

Получить текущий элемент

### `Length`

ID: `P:TFlex.Model.Model3D.Geometry.SweepGenerator.Law.Discrete.Length`

Количество пар

### `default(System.UInt32)`

ID: `P:TFlex.Model.Model3D.Geometry.SweepGenerator.Law.Discrete.default(System.UInt32)`

Пара по номеру

Parameters:
- `index`: Номер пары

Remarks: Пары нумеруются от нуля. Если индекс отрицательный или превышает количество пар, то результат не определён
