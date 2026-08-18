# TFlex.Model.Model2D.DrawingView.Breaks

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D.DrawingView`

## Summary

Набор разрывов чертёжного вида

## Methods

### `AddBreak`

ID: `M:TFlex.Model.Model2D.DrawingView.Breaks.AddBreak`

Добавить разрыв

Returns: Разрыв

### `AddBreak(System.Boolean)`

ID: `M:TFlex.Model.Model2D.DrawingView.Breaks.AddBreak(System.Boolean)`

Добавить разрыв

Parameters:
- `norm`: true - если горизонтальный

Returns: Разрыв

### `GetAt(System.Int32)`

ID: `M:TFlex.Model.Model2D.DrawingView.Breaks.GetAt(System.Int32)`

Получить разрыв по индексу

Parameters:
- `index`: Индекс разрыва

Returns: Рызрыв

### `GetEnumerator`

ID: `M:TFlex.Model.Model2D.DrawingView.Breaks.GetEnumerator`

Получить перечиcлитель

### `RemoveAll`

ID: `M:TFlex.Model.Model2D.DrawingView.Breaks.RemoveAll`

Удалить все разрывы

### `RemoveAt(System.Int32)`

ID: `M:TFlex.Model.Model2D.DrawingView.Breaks.RemoveAt(System.Int32)`

Добавить разрыв

Parameters:
- `index`: Index

### `Update`

ID: `M:TFlex.Model.Model2D.DrawingView.Breaks.Update`

Обновление габаритов разрывов чертежного вида

## Propertys

### `Alignment`

ID: `P:TFlex.Model.Model2D.DrawingView.Breaks.Alignment`

Способ задания позиций разрывов чертёжного вида, в соответствии с направлением разрывов(по вертикали)

### `Angle`

ID: `P:TFlex.Model.Model2D.DrawingView.Breaks.Angle`

Угол направления разрывов

### `AngleLine`

ID: `P:TFlex.Model.Model2D.DrawingView.Breaks.AngleLine`

Прямая, задающая направление разрывов (допускается значение null)

### `BrokenBoundConstruction1`

ID: `P:TFlex.Model.Model2D.DrawingView.Breaks.BrokenBoundConstruction1`

Первая линия построения, задающая границу для линий разрывов (допускается значение null)

### `BrokenBoundConstruction2`

ID: `P:TFlex.Model.Model2D.DrawingView.Breaks.BrokenBoundConstruction2`

Вторая линия построения, задающая границу для линий разрывов (допускается значение null)

### `BrokenBoundOutline1`

ID: `P:TFlex.Model.Model2D.DrawingView.Breaks.BrokenBoundOutline1`

Первая линия изображения, задающая границу для линий разрывов (допускается значение null)

### `BrokenBoundOutline2`

ID: `P:TFlex.Model.Model2D.DrawingView.Breaks.BrokenBoundOutline2`

Вторая линия изображения, задающая границу для линий разрывов (допускается значение null)

### `Count`

ID: `P:TFlex.Model.Model2D.DrawingView.Breaks.Count`

Количество разрывов

### `Gap`

ID: `P:TFlex.Model.Model2D.DrawingView.Breaks.Gap`

Размер разрыва в единицах страницы

### `HorizontalAlignment`

ID: `P:TFlex.Model.Model2D.DrawingView.Breaks.HorizontalAlignment`

Способ задания позиций разрывов чертёжного вида, в соответствии с направлением разрывов(по горизонтали)

### `KeepParts`

ID: `P:TFlex.Model.Model2D.DrawingView.Breaks.KeepParts`

Сохранять части изображения в исходном положении

### `LineColor`

ID: `P:TFlex.Model.Model2D.DrawingView.Breaks.LineColor`

Цвет линий разрыва

### `LineExtension`

ID: `P:TFlex.Model.Model2D.DrawingView.Breaks.LineExtension`

Размер выступания линий разрыва в единицах страницы

### `LineScale`

ID: `P:TFlex.Model.Model2D.DrawingView.Breaks.LineScale`

Масштаб штрихов линий разрыва

### `LineType`

ID: `P:TFlex.Model.Model2D.DrawingView.Breaks.LineType`

Тип линий разрыва

### `LineWaveHeight`

ID: `P:TFlex.Model.Model2D.DrawingView.Breaks.LineWaveHeight`

Высота волны волнистой линии

### `LineWaveLength`

ID: `P:TFlex.Model.Model2D.DrawingView.Breaks.LineWaveLength`

Длина периода волнистой линии

### `LineWaveNumber`

ID: `P:TFlex.Model.Model2D.DrawingView.Breaks.LineWaveNumber`

Количество периодов волнистой линии

### `LineWaveType`

ID: `P:TFlex.Model.Model2D.DrawingView.Breaks.LineWaveType`

Способ задания волнистой линии

### `LineWidth`

ID: `P:TFlex.Model.Model2D.DrawingView.Breaks.LineWidth`

Толщина линий разрыва

Examples:
- `public static void SetLineWidth(ModelObject ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("Установка толщины линии");//Открытие блока изменений документа ob.LineWidth = 3; document.EndChanges();//Закрытие блока изменений документа }`

### `Metric`

ID: `P:TFlex.Model.Model2D.DrawingView.Breaks.Metric`

Способ задания позиций разрывов чертёжного вида

### `Origin`

ID: `P:TFlex.Model.Model2D.DrawingView.Breaks.Origin`

Базовая точка разрывов

### `OriginNode`

ID: `P:TFlex.Model.Model2D.DrawingView.Breaks.OriginNode`

Базовый узел разрывов (допускается значение null)

### `SpecialElements`

ID: `P:TFlex.Model.Model2D.DrawingView.Breaks.SpecialElements`

Получить коллекцию элементов, управляющих отображением 2D объектов в области разрыва на чертёжном виде

### `UseLineColor`

ID: `P:TFlex.Model.Model2D.DrawingView.Breaks.UseLineColor`

Использовать особый цвет линий разрыва

### `UseLineExtension`

ID: `P:TFlex.Model.Model2D.DrawingView.Breaks.UseLineExtension`

Показывать линии разрыва с выступами

### `VerticalAlignment`

ID: `P:TFlex.Model.Model2D.DrawingView.Breaks.VerticalAlignment`

Способ задания позиций разрывов чертёжного вида, в соответствии с направлением разрывов(по вертикали)
