# TFlex.Model.Model2D.Outline

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Базовый класс линии изображения

## Methods

### `EvaluatePoint(System.Double,TFlex.Drawing.Pointref )`

ID: `M:TFlex.Model.Model2D.Outline.EvaluatePoint(System.Double,TFlex.Drawing.Point@)`

Получить точку на кривой по параметру iU

Parameters:
- `iU`: Параметр на кривой, в котором вычисляется точка
- `oPoint`: Вычисленная точка

Returns: true - в случае успеха

### `GetDashStyle`

ID: `M:TFlex.Model.Model2D.Outline.GetDashStyle`

Получение штрихов

### `SetDashStyle(System.Collections.Generic.List`1{TFlex.Model.Model2D.OutlineDashStyleItem})`

ID: `M:TFlex.Model.Model2D.Outline.SetDashStyle(System.Collections.Generic.List`1{TFlex.Model.Model2D.OutlineDashStyleItem})`

Установка штрихов

### `SetDefaults`

ID: `M:TFlex.Model.Model2D.Outline.SetDefaults`

Установка параметров линий изображения в соответствии с параметрами по умолчанию

## Propertys

### `Color`

ID: `P:TFlex.Model.Model2D.Outline.Color`

Цвет линии изображения

Examples:
- `public static void SetColor(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа ob.Color = 40;//установка цвета document.EndChanges();//Закрытие блока изменений документа }`

### `EndArrowSize`

ID: `P:TFlex.Model.Model2D.Outline.EndArrowSize`

Размер конечной стрелки линии изображения

### `EndArrowType`

ID: `P:TFlex.Model.Model2D.Outline.EndArrowType`

Тип конечной стрелки линии изображения

### `Geometry`

ID: `P:TFlex.Model.Model2D.Outline.Geometry`

Получение геометрии линии изображения с учётом масштаба

### `GeometryAsPolyline`

ID: `P:TFlex.Model.Model2D.Outline.GeometryAsPolyline`

Получение геометрии в виде полилинии независимо от типа

### `GeometryType`

ID: `P:TFlex.Model.Model2D.Outline.GeometryType`

Тип геометрии линии изображения

### `GroupType`

ID: `P:TFlex.Model.Model2D.Outline.GroupType`

Тип объекта "Линия изображения"

### `IsService`

ID: `P:TFlex.Model.Model2D.Outline.IsService`

Вспомогательная линия

### `Layer`

ID: `P:TFlex.Model.Model2D.Outline.Layer`

Слой линии изображения

Examples:
- `public static void SetLayer(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Layer l = new Layer(document); l.Monochrome = true;//Параметр слоя "одноцветный" l.Color = 12;//цвет ob.Layer = l;//установка слоя document.EndChanges();//Закрытие блока изменений документа }`

### `Level`

ID: `P:TFlex.Model.Model2D.Outline.Level`

Уровень линии

Examples:
- `public static void SetLevel(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("Установка уровня");//Открытие блока изменений документа ob.Level = 3;//установка уровня document.EndChanges();//Закрытие блока изменений документа }`

### `LineWidth`

ID: `P:TFlex.Model.Model2D.Outline.LineWidth`

Толщина линии изображения

Examples:
- `public static void SetLineWidth(ModelObject ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("Установка толщины линии");//Открытие блока изменений документа ob.LineWidth = 3; document.EndChanges();//Закрытие блока изменений документа }`

### `ModelGeometry`

ID: `P:TFlex.Model.Model2D.Outline.ModelGeometry`

Получение геометрии линии изображения без учёта масштаба

### `Page`

ID: `P:TFlex.Model.Model2D.Outline.Page`

Страница линии изображения

Examples:
- `public static void SetPage(ModelObject ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Page p = new Page(document);//создание страницы p.Name = "страница1" ob.Page = p;//cтраница, на которой размещается элемент document.EndChanges();//Закрытие блока изменений документа }`

### `PatternName`

ID: `P:TFlex.Model.Model2D.Outline.PatternName`

Имя образца штриховой линии

### `PatternScale`

ID: `P:TFlex.Model.Model2D.Outline.PatternScale`

Масштаб штрихов штриховой линии

### `Priority`

ID: `P:TFlex.Model.Model2D.Outline.Priority`

Приоритет линии изображения

### `StartArrowSize`

ID: `P:TFlex.Model.Model2D.Outline.StartArrowSize`

Размер начальной стрелки линии изображения

### `StartArrowType`

ID: `P:TFlex.Model.Model2D.Outline.StartArrowType`

Тип начальной стрелки линии изображения

### `Style`

ID: `P:TFlex.Model.Model2D.Outline.Style`

Стиль линии изображения

### `SubType`

ID: `P:TFlex.Model.Model2D.Outline.SubType`

Подтип линии изображения

### `WaveHeight`

ID: `P:TFlex.Model.Model2D.Outline.WaveHeight`

Высота волны волнистой линии

Remarks: Реальная высота волны измеряется как длина волны, умноженная на значение данного параметра

### `WaveLength`

ID: `P:TFlex.Model.Model2D.Outline.WaveLength`

Длина волны волнистой линии

### `WaveNumber`

ID: `P:TFlex.Model.Model2D.Outline.WaveNumber`

Количество волн волнистой линии

### `WaveSetting`

ID: `P:TFlex.Model.Model2D.Outline.WaveSetting`

Способ задания волнистой линии
