# TFlex.Model.Model3D.Swept

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Операция по траектории

## Constructors

### `Swept(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Swept.#ctor(TFlex.Model.Document)`

Конструктор для создания операции по траектории

Parameters:
- `Doc`: Документ, в котором создаётся новый объект

## Methods

### `Swept(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Swept.#ctor(TFlex.Model.Document)`

Конструктор для создания операции по траектории

Parameters:
- `Doc`: Документ, в котором создаётся новый объект

### `CancelBinding`

ID: `M:TFlex.Model.Model3D.Swept.CancelBinding`

Отмена привязки контура к пути по точкам

## Propertys

### `Accuracy`

ID: `P:TFlex.Model.Model3D.Swept.Accuracy`

Точность геометрии

### `GuidePath`

ID: `P:TFlex.Model.Model3D.Swept.GuidePath`

Составной путь, задающий движение

### `Orientation`

ID: `P:TFlex.Model.Model3D.Swept.Orientation`

Ориентация контура

### `ReferencePoint`

ID: `P:TFlex.Model.Model3D.Swept.ReferencePoint`

Точка для задания поворота контура

Remarks: Точка для задания поворота контура задаётся одновременно со второй точкой привязки

### `ScaleLaw`

ID: `P:TFlex.Model.Model3D.Swept.ScaleLaw`

Табличная функция, задающая зависимость масштаба от положения на пути в процентах

### `ScaleLawType`

ID: `P:TFlex.Model.Model3D.Swept.ScaleLawType`

Способ определения направления при задании закона масштабирования составным путём

### `ScalePath`

ID: `P:TFlex.Model.Model3D.Swept.ScalePath`

Составной путь, задающий закон масштабирования

Remarks: Закон масштабирования может задаваться двумя взаимоисключающими способами : - Составным путём; - Табличной функцией, задающей зависимость масштаба от положения на пути в процентах.

### `ScalePoint`

ID: `P:TFlex.Model.Model3D.Swept.ScalePoint`

Точка масштабирования

Remarks: Точка масштабирования используется, если есть путь, задающий закон масштабирования

### `Scaling`

ID: `P:TFlex.Model.Model3D.Swept.Scaling`

Тип масштабирования

### `SecondPoint`

ID: `P:TFlex.Model.Model3D.Swept.SecondPoint`

Вторая точка для привязки контура

Remarks: Вторая точка привязки задаётся одновременно с точкой для задания поворота контура

### `Simplify`

ID: `P:TFlex.Model.Model3D.Swept.Simplify`

Параметр упрощения геометрии

### `StartPoint`

ID: `P:TFlex.Model.Model3D.Swept.StartPoint`

Точка для размещения контура в начало траектории

Remarks: Если точка не задана, то начальное положение контура не изменяется

### `Synchronize`

ID: `P:TFlex.Model.Model3D.Swept.Synchronize`

Синхронизация начала пути с положением контура

Remarks: Это свойство актуально для замкнутых путей, когда стартовая точка актуальна для получения правильного пути

### `TwistLaw`

ID: `P:TFlex.Model.Model3D.Swept.TwistLaw`

Табличная функция, задающая зависимость угла кручения от положения на пути в процентах

### `TwistLawType`

ID: `P:TFlex.Model.Model3D.Swept.TwistLawType`

Способ определения направления при задании закона кручения составным путём

### `TwistPath`

ID: `P:TFlex.Model.Model3D.Swept.TwistPath`

Составной путь, задающий закон кручения

Remarks: Закон кручения может задаваться тремя взаимоисключающими способами : - Составным путём; - Табличной функцией, задающей зависимость угла кручения от положения на пути в процентах; - Составным листом, задающим закон кручения.

### `TwistSheet`

ID: `P:TFlex.Model.Model3D.Swept.TwistSheet`

Составной лист, задающий закон вращения

Remarks: Закон кручения может задаваться тремя взаимоисключающими способами : - Составным путём; - Табличной функцией, задающей зависимость угла кручения от положения на пути в процентах; - Составным листом, задающим закон кручения.
