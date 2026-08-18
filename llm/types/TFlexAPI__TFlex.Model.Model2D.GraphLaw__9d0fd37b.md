# TFlex.Model.Model2D.GraphLaw

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Зависимость F(x), заданная графиком

## Methods

### `GetNode(System.UInt32)`

ID: `M:TFlex.Model.Model2D.GraphLaw.GetNode(System.UInt32)`

Получение узла по номеру

### `GetRepeatCount(System.UInt32*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.UInt32*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:TFlex.Model.Model2D.GraphLaw.GetRepeatCount(System.UInt32*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.UInt32*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Количество повторений графика в положительном и отрицательном направлениях

### `GetValue(System.Double)`

ID: `M:TFlex.Model.Model2D.GraphLaw.GetValue(System.Double)`

Получение значения по аргументу

### `InsertNode(TFlex.Drawing.Point)`

ID: `M:TFlex.Model.Model2D.GraphLaw.InsertNode(TFlex.Drawing.Point)`

Вставка узла в соответствии со значением аргумента

### `Load(System.String,TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.GraphLaw.Load(System.String,TFlex.Model.Document)`

Создание графика из файла *.tflaw

### `RemoveAllNodes`

ID: `M:TFlex.Model.Model2D.GraphLaw.RemoveAllNodes`

Удаление всех узлов

### `RemoveNode(System.UInt32)`

ID: `M:TFlex.Model.Model2D.GraphLaw.RemoveNode(System.UInt32)`

Удаление узла

### `Save(System.String)`

ID: `M:TFlex.Model.Model2D.GraphLaw.Save(System.String)`

Сохранение в отдельный файл *.tflaw

### `SetNode(System.UInt32,TFlex.Drawing.Point)`

ID: `M:TFlex.Model.Model2D.GraphLaw.SetNode(System.UInt32,TFlex.Drawing.Point)`

Установка узла по номеру

Remarks: Узел изменяется только в том случае, если заданное значение аргумента соответствует порядку значений аргументов остальных узлов (по возрастанию)

## Propertys

### `ArgumentName`

ID: `P:TFlex.Model.Model2D.GraphLaw.ArgumentName`

Название аргумента (x) в форме: [имя], [буквы_обозначения], [единицы]

### `ArgumentToValueVisualRatio`

ID: `P:TFlex.Model.Model2D.GraphLaw.ArgumentToValueVisualRatio`

Визуальное соотношение единиц аргумента и функции (для отображения в диалоге)

### `ArgumentTolerance`

ID: `P:TFlex.Model.Model2D.GraphLaw.ArgumentTolerance`

Наименьшее допустимое расстояние между соседними узлами по значению аргумента

### `Color`

ID: `P:TFlex.Model.Model2D.GraphLaw.Color`

Цвет (для отображения в диалоге)

Examples:
- `public static void SetColor(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа ob.Color = 40;//установка цвета document.EndChanges();//Закрытие блока изменений документа }`

### `GroupType`

ID: `P:TFlex.Model.Model2D.GraphLaw.GroupType`

Тип объекта

### `IsSmooth`

ID: `P:TFlex.Model.Model2D.GraphLaw.IsSmooth`

График является сглаженным

### `NodeCount`

ID: `P:TFlex.Model.Model2D.GraphLaw.NodeCount`

Количество точек графика

### `Nodes`

ID: `P:TFlex.Model.Model2D.GraphLaw.Nodes`

Точки графика

### `NodesBounds`

ID: `P:TFlex.Model.Model2D.GraphLaw.NodesBounds`

Ограничивающий прямоугольник узлов

### `SpecialName`

ID: `P:TFlex.Model.Model2D.GraphLaw.SpecialName`

Специальное имя

### `UseLogarArgScale`

ID: `P:TFlex.Model.Model2D.GraphLaw.UseLogarArgScale`

Использование логарифмической шкалы аргумента

### `UseWorkingArea`

ID: `P:TFlex.Model.Model2D.GraphLaw.UseWorkingArea`

Использование области допустимых значений

### `ValueName`

ID: `P:TFlex.Model.Model2D.GraphLaw.ValueName`

Название функции (F) в форме: [имя], [буквы_обозначения], [единицы]

### `ViewOnly`

ID: `P:TFlex.Model.Model2D.GraphLaw.ViewOnly`

Редактирование в диалоге запрещено

### `WorkingArea`

ID: `P:TFlex.Model.Model2D.GraphLaw.WorkingArea`

Область допустимых значений
