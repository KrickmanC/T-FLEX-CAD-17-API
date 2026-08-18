# TFlex.Model.Model3D.TableFunction

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Табличная функция

## Remarks

Возможно перечисление точек с использованием конструкции foreach

## Methods

### `Add(TFlex.Model.Model3D.TableFunction.Dependence)`

ID: `M:TFlex.Model.Model3D.TableFunction.Add(TFlex.Model.Model3D.TableFunction.Dependence)`

Добавить точку в конец списка

Parameters:
- `pair`: Пара независимого и зависимого параметра

### `Delete(System.Int32)`

ID: `M:TFlex.Model.Model3D.TableFunction.Delete(System.Int32)`

Удалить точку по номеру

Parameters:
- `index`: Номер точки

Remarks: Точки нумеруются от нуля. Если индекс отрицательный или превышает количество точек, то результат не определён

### `DeleteAll`

ID: `M:TFlex.Model.Model3D.TableFunction.DeleteAll`

Удалить все точки

### `GetEnumerator`

ID: `M:TFlex.Model.Model3D.TableFunction.GetEnumerator`

Получить перечислитель

### `Insert(System.Int32,TFlex.Model.Model3D.TableFunction.Dependence)`

ID: `M:TFlex.Model.Model3D.TableFunction.Insert(System.Int32,TFlex.Model.Model3D.TableFunction.Dependence)`

Вставить точку перед номером

Parameters:
- `index`: Номер точки
- `pair`: Пара независимого и зависимого параметра

Remarks: Точки нумеруются от нуля. Если индекс отрицательный или превышает количество точек, то результат не определён

### `MoveNext`

ID: `M:TFlex.Model.Model3D.TableFunction.MoveNext`

Перейти к следующему элементу

### `Reset`

ID: `M:TFlex.Model.Model3D.TableFunction.Reset`

Сбросить перечислитель

## Propertys

### `Current`

ID: `P:TFlex.Model.Model3D.TableFunction.Current`

Получить текущий элемент

### `Length`

ID: `P:TFlex.Model.Model3D.TableFunction.Length`

Количество элементов

### `default(System.Int32)`

ID: `P:TFlex.Model.Model3D.TableFunction.default(System.Int32)`

Элемент по номеру

Parameters:
- `index`: Номер элемента

Remarks: Элементы нумеруются от нуля. Если индекс отрицательный или превышает количество точек, то результат не определён
