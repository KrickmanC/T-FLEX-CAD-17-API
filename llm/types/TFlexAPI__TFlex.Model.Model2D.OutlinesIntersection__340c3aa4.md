# TFlex.Model.Model2D.OutlinesIntersection

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Обозначение пересечения линий изображения

## Constructors

### `OutlinesIntersection(TFlex.Model.Document,TFlex.Model.Model2D.Outline,TFlex.Model.Model2D.Outline,System.Int32,TFlex.Model.Model2D.OutlinesIntersection.Forms,TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.OutlinesIntersection.#ctor(TFlex.Model.Document,TFlex.Model.Model2D.Outline,TFlex.Model.Model2D.Outline,System.Int32,TFlex.Model.Model2D.OutlinesIntersection.Forms,TFlex.Model.Parameter,TFlex.Model.Parameter)`

Конструктор

Parameters:
- `document`: Документ
- `outline1`: Первая линия изображения
- `outline2`: Вторая линия изображения
- `point`: Номер точки пересечения
- `form`: Форма обозначения
- `size`: Размер обозначения
- `lineWidth`: Толлщина линии обозначения

## Methods

### `OutlinesIntersection(TFlex.Model.Document,TFlex.Model.Model2D.Outline,TFlex.Model.Model2D.Outline,System.Int32,TFlex.Model.Model2D.OutlinesIntersection.Forms,TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.OutlinesIntersection.#ctor(TFlex.Model.Document,TFlex.Model.Model2D.Outline,TFlex.Model.Model2D.Outline,System.Int32,TFlex.Model.Model2D.OutlinesIntersection.Forms,TFlex.Model.Parameter,TFlex.Model.Parameter)`

Конструктор

Parameters:
- `document`: Документ
- `outline1`: Первая линия изображения
- `outline2`: Вторая линия изображения
- `point`: Номер точки пересечения
- `form`: Форма обозначения
- `size`: Размер обозначения
- `lineWidth`: Толлщина линии обозначения

## Propertys

### `Form`

ID: `P:TFlex.Model.Model2D.OutlinesIntersection.Form`

Форма пересечения

### `Level`

ID: `P:TFlex.Model.Model2D.OutlinesIntersection.Level`

Уровень

Examples:
- `public static void SetLevel(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("Установка уровня");//Открытие блока изменений документа ob.Level = 3;//установка уровня document.EndChanges();//Закрытие блока изменений документа }`

### `LineWidth`

ID: `P:TFlex.Model.Model2D.OutlinesIntersection.LineWidth`

Толщина линии

Examples:
- `public static void SetLineWidth(ModelObject ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("Установка толщины линии");//Открытие блока изменений документа ob.LineWidth = 3; document.EndChanges();//Закрытие блока изменений документа }`

### `Outline1`

ID: `P:TFlex.Model.Model2D.OutlinesIntersection.Outline1`

Первая линия

### `Outline2`

ID: `P:TFlex.Model.Model2D.OutlinesIntersection.Outline2`

Вторая линия

### `Page`

ID: `P:TFlex.Model.Model2D.OutlinesIntersection.Page`

Страница

### `PointIndex`

ID: `P:TFlex.Model.Model2D.OutlinesIntersection.PointIndex`

номер точки пересечения

### `Size`

ID: `P:TFlex.Model.Model2D.OutlinesIntersection.Size`

Размер
