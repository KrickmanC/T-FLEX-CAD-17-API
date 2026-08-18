# TFlex.Model.Model2D.Dimension

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Базовый класс размера

## Methods

### `CopyArrows(TFlex.Model.Model2D.Dimension)`

ID: `M:TFlex.Model.Model2D.Dimension.CopyArrows(TFlex.Model.Model2D.Dimension)`

Скопировать положение манипуляторов с другого размера

### `CreateArrows(TFlex.Model.Model2D.DimensionArrowsMode)`

ID: `M:TFlex.Model.Model2D.Dimension.CreateArrows(TFlex.Model.Model2D.DimensionArrowsMode)`

Создать манипуляторы по режиму

### `ResetParameters`

ID: `M:TFlex.Model.Model2D.Dimension.ResetParameters`

Установка параметров размера по-умолчанию

### `SetArrowNodeAttachObject(TFlex.Model.Model2D.DimensionNodeType,TFlex.Model.Model2D.Node)`

ID: `M:TFlex.Model.Model2D.Dimension.SetArrowNodeAttachObject(TFlex.Model.Model2D.DimensionNodeType,TFlex.Model.Model2D.Node)`

Установить узел в качестве привязки манипулятора

### `SetArrowNodeCoords(TFlex.Model.Model2D.DimensionNodeType,System.Double,System.Double)`

ID: `M:TFlex.Model.Model2D.Dimension.SetArrowNodeCoords(TFlex.Model.Model2D.DimensionNodeType,System.Double,System.Double)`

Установить абсолютные координаты манипулятора

### `SetArrowNodeParams(TFlex.Model.Model2D.DimensionNodeType,System.Double,System.Double)`

ID: `M:TFlex.Model.Model2D.Dimension.SetArrowNodeParams(TFlex.Model.Model2D.DimensionNodeType,System.Double,System.Double)`

Установить параметры для пересчета положения манипулятора

### `SetDefaults`

ID: `M:TFlex.Model.Model2D.Dimension.SetDefaults`

Установка параметров размера в соответствии с параметрами по умолчанию

### `SetValue(System.Double)`

ID: `M:TFlex.Model.Model2D.Dimension.SetValue(System.Double)`

Установка значения размера

Remarks: Данная функция пересчитывает параметры модели таким образом, чтобы значение размера стало равным устанавливаемому.

## Propertys

### `AltValueCorrection`

ID: `P:TFlex.Model.Model2D.Dimension.AltValueCorrection`

Коррекция номинала альтернативного размера (применяется после применения масштаба)

### `BoxAroundText`

ID: `P:TFlex.Model.Model2D.Dimension.BoxAroundText`

Рамка вокруг текста

### `ClearUnderArrows`

ID: `P:TFlex.Model.Model2D.Dimension.ClearUnderArrows`

Параметр очистки фона под стрелками и размерной линией

### `ClearUnderEndArrow`

ID: `P:TFlex.Model.Model2D.Dimension.ClearUnderEndArrow`

Параметр очистки фона под второй стрелкой

### `ClearUnderLines`

ID: `P:TFlex.Model.Model2D.Dimension.ClearUnderLines`

Параметр очистки фона под выносными линиями

### `ClearUnderStartArrow`

ID: `P:TFlex.Model.Model2D.Dimension.ClearUnderStartArrow`

Параметр очистки фона под первой стрелкой

### `Color`

ID: `P:TFlex.Model.Model2D.Dimension.Color`

Цвет объекта

Examples:
- `public static void SetColor(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа ob.Color = 40;//установка цвета document.EndChanges();//Закрытие блока изменений документа }`

### `FontStyle`

ID: `P:TFlex.Model.Model2D.Dimension.FontStyle`

Получение стиля шрифта текста для получения или установки его параметров

### `GroupType`

ID: `P:TFlex.Model.Model2D.Dimension.GroupType`

Тип объекта

### `HasSourceLines`

ID: `P:TFlex.Model.Model2D.Dimension.HasSourceLines`

Проверить размер на возможность приведения параметра номинала размера к типу "По исходным линиям"

### `Layer`

ID: `P:TFlex.Model.Model2D.Dimension.Layer`

Слой, на котором размещается объект

Examples:
- `public static void SetLayer(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Layer l = new Layer(document); l.Monochrome = true;//Параметр слоя "одноцветный" l.Color = 12;//цвет ob.Layer = l;//установка слоя document.EndChanges();//Закрытие блока изменений документа }`

### `LeaderDirection`

ID: `P:TFlex.Model.Model2D.Dimension.LeaderDirection`

Направление полки с размерным числом

### `Level`

ID: `P:TFlex.Model.Model2D.Dimension.Level`

Уровень объекта

Examples:
- `public static void SetLevel(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("Установка уровня");//Открытие блока изменений документа ob.Level = 3;//установка уровня document.EndChanges();//Закрытие блока изменений документа }`

### `ManualValueCorrection`

ID: `P:TFlex.Model.Model2D.Dimension.ManualValueCorrection`

Использование заданного вручную значения коррекции размера

### `NominalOnlyText`

ID: `P:TFlex.Model.Model2D.Dimension.NominalOnlyText`

Строка текста со значением только номинала размера

### `Offset1`

ID: `P:TFlex.Model.Model2D.Dimension.Offset1`

Отступ размера. Тип отступа зависит от типа размера

### `Offset2`

ID: `P:TFlex.Model.Model2D.Dimension.Offset2`

Отступ размера. Тип отступа зависит от типа размера

### `Offset3`

ID: `P:TFlex.Model.Model2D.Dimension.Offset3`

Отступ размера. Тип отступа зависит от типа размера

### `Page`

ID: `P:TFlex.Model.Model2D.Dimension.Page`

Страница, на которой размещается элемент

Examples:
- `public static void SetPage(ModelObject ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Page p = new Page(document);//создание страницы p.Name = "страница1" ob.Page = p;//cтраница, на которой размещается элемент document.EndChanges();//Закрытие блока изменений документа }`

### `ParentDimension`

ID: `P:TFlex.Model.Model2D.Dimension.ParentDimension`

Родительский размер

Remarks: Используется для определения положения в списке размеров в цепи, от базы, строительных

### `Priority`

ID: `P:TFlex.Model.Model2D.Dimension.Priority`

Приоритет объекта

### `State`

ID: `P:TFlex.Model.Model2D.Dimension.State`

Тип положения размера

### `SubType`

ID: `P:TFlex.Model.Model2D.Dimension.SubType`

Подтип размера

### `TextAfter`

ID: `P:TFlex.Model.Model2D.Dimension.TextAfter`

Строка текста после текстом значения размера

### `TextBefore`

ID: `P:TFlex.Model.Model2D.Dimension.TextBefore`

Строка текста перед текстом значения размера

### `TextParameters`

ID: `P:TFlex.Model.Model2D.Dimension.TextParameters`

Способ отображения параметров размера

### `TextUnder`

ID: `P:TFlex.Model.Model2D.Dimension.TextUnder`

Строка текста под текстом значения размера

### `Value`

ID: `P:TFlex.Model.Model2D.Dimension.Value`

Численное значение размера

Remarks: Если у размера не установлен параметр простановки значения "вручную", новое значение не будет установлено.

### `ValueCorrection`

ID: `P:TFlex.Model.Model2D.Dimension.ValueCorrection`

Коррекция номинала размера (применяется после применения масштаба)

### `ValueText`

ID: `P:TFlex.Model.Model2D.Dimension.ValueText`

Строка текста со значением размера

### `ValueType`

ID: `P:TFlex.Model.Model2D.Dimension.ValueType`

Способ формирования строки номинала размера
