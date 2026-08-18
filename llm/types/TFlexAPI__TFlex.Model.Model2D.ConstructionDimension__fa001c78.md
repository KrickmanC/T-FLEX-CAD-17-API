# TFlex.Model.Model2D.ConstructionDimension

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Класс строительного размера

## Constructors

### `ConstructionDimension(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.ConstructionDimension.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию

Parameters:
- `Doc`: Документ

## Methods

### `ConstructionDimension(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.ConstructionDimension.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию

Parameters:
- `Doc`: Документ

### `SetConstruction(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Node)`

ID: `M:TFlex.Model.Model2D.ConstructionDimension.SetConstruction(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Node)`

Прикрепление размера к линии построения

Parameters:
- `horizontalLine`: Линия построения, к которой прикрепляется размер
- `node`: Узел, до которого рисуется выносная линия размера

### `SetNode(TFlex.Model.Model2D.Node)`

ID: `M:TFlex.Model.Model2D.ConstructionDimension.SetNode(TFlex.Model.Model2D.Node)`

Прикрепление размера к узлу

Parameters:
- `node`: Узел, к которому прикрепляется размер

### `SetOffsets(TFlex.Model.Model2D.Node,System.Double,TFlex.Model.Model2D.Node,System.Double)`

ID: `M:TFlex.Model.Model2D.ConstructionDimension.SetOffsets(TFlex.Model.Model2D.Node,System.Double,TFlex.Model.Model2D.Node,System.Double)`

Установка привязок размера к узлам, либо по относительным смещениям

Parameters:
- `fixNodeX`: Первый узел привязки, смещение размера от точки привязки по горизонтали
- `offsetX`: Смещение размера от точки привязки по горизонтали (используется, если fixNodeX не задан)
- `fixNodeY`: Второй узел привязки, смещение размера от точки привязки по вертикали
- `offsetY`: Смещение размера от точки привязки по вертикали (используется, если fixNodeY не задан)

### `SetOutline(TFlex.Model.Model2D.Outline,System.Boolean)`

ID: `M:TFlex.Model.Model2D.ConstructionDimension.SetOutline(TFlex.Model.Model2D.Outline,System.Boolean)`

Прикрепление размера к линии изображения

Parameters:
- `horizontalLine`: Линия изображения, к которой прикрепляется размер
- `isOnEnd1`: Параметр рисования выносной линии до конечной точки линии изображения (иначе - рисуется до начальной)

## Propertys

### `Accuracy`

ID: `P:TFlex.Model.Model2D.ConstructionDimension.Accuracy`

Точность

### `AltScaleFactor`

ID: `P:TFlex.Model.Model2D.ConstructionDimension.AltScaleFactor`

Величина дополнительного масштабирования альтернативного размера

### `AltScaleFactorType`

ID: `P:TFlex.Model.Model2D.ConstructionDimension.AltScaleFactorType`

Тип дополнительного масштабирования альтернативного размера

### `ArrowSize`

ID: `P:TFlex.Model.Model2D.ConstructionDimension.ArrowSize`

Размер стрелки

### `ConstructionDimType`

ID: `P:TFlex.Model.Model2D.ConstructionDimension.ConstructionDimType`

Тип привязки размера

### `DrawLeaderLine`

ID: `P:TFlex.Model.Model2D.ConstructionDimension.DrawLeaderLine`

Параметр рисования выносной линии

### `DrawPlus`

ID: `P:TFlex.Model.Model2D.ConstructionDimension.DrawPlus`

Флага рисования знака "+" у положительных значений размера

### `Dual`

ID: `P:TFlex.Model.Model2D.ConstructionDimension.Dual`

Режим отображения двойного размера

### `MinDigits`

ID: `P:TFlex.Model.Model2D.ConstructionDimension.MinDigits`

Минимальное число знаков после запятой

### `ParentDimension`

ID: `P:TFlex.Model.Model2D.ConstructionDimension.ParentDimension`

Родительский размер

Remarks: В зависимости от положения родительского размера будет вычисляться значение текущего размера. Установленный родительский размер не должен иметь других родительских размеров

### `ScaleFactor`

ID: `P:TFlex.Model.Model2D.ConstructionDimension.ScaleFactor`

Величина дополнительного масштабирования размера

### `ScaleFactorType`

ID: `P:TFlex.Model.Model2D.ConstructionDimension.ScaleFactorType`

Тип дополнительного масштабирования размера

### `Standard`

ID: `P:TFlex.Model.Model2D.ConstructionDimension.Standard`

Тип стандарта размера

### `StringsOffset`

ID: `P:TFlex.Model.Model2D.ConstructionDimension.StringsOffset`

Величина смещения строк от размерной линии

### `SubType`

ID: `P:TFlex.Model.Model2D.ConstructionDimension.SubType`

Подтип размера

### `Units`

ID: `P:TFlex.Model.Model2D.ConstructionDimension.Units`

Тип единиц измерения
