# TFlex.Model.Model3D.BasePipe

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Базовая операция трубопровода

## Methods

### `AddCuttingItem(TFlex.Model.Model3D.Operation)`

ID: `M:TFlex.Model.Model3D.BasePipe.AddCuttingItem(TFlex.Model.Model3D.Operation)`

Добавляет операцию для создание "врезки"

### `GetBeginPartVariables`

ID: `M:TFlex.Model.Model3D.BasePipe.GetBeginPartVariables`

Получить переменные начала трубы

Returns: Переменные "начала" трубы

### `GetCuttingItem(System.Int32)`

ID: `M:TFlex.Model.Model3D.BasePipe.GetCuttingItem(System.Int32)`

Возвращает операцию "врезки" по индексу

### `GetEndPartVariables`

ID: `M:TFlex.Model.Model3D.BasePipe.GetEndPartVariables`

Получить переменные конца трубы

Returns: Переменные "конца" трубы

### `GetMidPartVariables`

ID: `M:TFlex.Model.Model3D.BasePipe.GetMidPartVariables`

Получить переменные середины трубы

Returns: Переменные "середины" трубы

### `RemoveAllCuttingItem`

ID: `M:TFlex.Model.Model3D.BasePipe.RemoveAllCuttingItem`

Удаляет все операции "врезки"

### `RemoveCuttingItem(System.Int32)`

ID: `M:TFlex.Model.Model3D.BasePipe.RemoveCuttingItem(System.Int32)`

Удаляет операцию "врезки" по индексу

### `RemoveCuttingItem(TFlex.Model.Model3D.Operation)`

ID: `M:TFlex.Model.Model3D.BasePipe.RemoveCuttingItem(TFlex.Model.Model3D.Operation)`

Удаляет операцию "врезки"

### `TryCopyPipeStandardFrom(TFlex.Model.Model3D.BasePipe)`

ID: `M:TFlex.Model.Model3D.BasePipe.TryCopyPipeStandardFrom(TFlex.Model.Model3D.BasePipe)`

Попробовать скопировать стандарт из другой трубы

## Propertys

### `Accuracy`

ID: `P:TFlex.Model.Model3D.BasePipe.Accuracy`

Точность геометрии

### `BeginBorder`

ID: `P:TFlex.Model.Model3D.BasePipe.BeginBorder`

Начальная граница трубопровода

### `BeginPart`

ID: `P:TFlex.Model.Model3D.BasePipe.BeginPart`

Специальное "окончание" трубы

### `CountCuttingItem`

ID: `P:TFlex.Model.Model3D.BasePipe.CountCuttingItem`

Количество операций "врезки"

### `EndBorder`

ID: `P:TFlex.Model.Model3D.BasePipe.EndBorder`

Конечная граница трубопровода

### `EndPart`

ID: `P:TFlex.Model.Model3D.BasePipe.EndPart`

Специальное "окончание" трубы

### `IsRevers`

ID: `P:TFlex.Model.Model3D.BasePipe.IsRevers`

Возвращает true, если направление трубы (от начальной к конечной границе) не совпадает с направлением пути

### `IsSetBeginPart`

ID: `P:TFlex.Model.Model3D.BasePipe.IsSetBeginPart`

Наличие специального "окончания" трубы, как фрагмента

### `IsSetEndPart`

ID: `P:TFlex.Model.Model3D.BasePipe.IsSetEndPart`

Наличие специального "окончания" трубы, как фрагмента

### `IsSetMidPart`

ID: `P:TFlex.Model.Model3D.BasePipe.IsSetMidPart`

Наличие специальной "середины" трубы, как адаптивный фрагмент

### `MidPart`

ID: `P:TFlex.Model.Model3D.BasePipe.MidPart`

Специальная "середина" трубы

### `NotCreateSolids`

ID: `P:TFlex.Model.Model3D.BasePipe.NotCreateSolids`

Не создавать твёрдотельную геометрию

### `Path`

ID: `P:TFlex.Model.Model3D.BasePipe.Path`

Путь, используется вместо Wires

### `PipeSegments`

ID: `P:TFlex.Model.Model3D.BasePipe.PipeSegments`

Возвращает информацию об участках трубопровода

### `Simplify`

ID: `P:TFlex.Model.Model3D.BasePipe.Simplify`

Параметр упрощения геометрии

### `Wires`

ID: `P:TFlex.Model.Model3D.BasePipe.Wires`

Путь трубопровода
