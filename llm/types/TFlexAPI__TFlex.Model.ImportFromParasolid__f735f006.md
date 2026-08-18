# TFlex.Model.ImportFromParasolid

Assembly: `TFlexAPI`
Namespace: `TFlex.Model`

## Summary

Класс, импортирующий документы Parasolid

## Methods

### `Import(System.String)`

ID: `M:TFlex.Model.ImportFromParasolid.Import(System.String)`

Функция импорта файла

Parameters:
- `fileName`: Имя входного файла

Returns: Результат импорта

## Propertys

### `AddBodyRecordsInProductStructure`

ID: `P:TFlex.Model.ImportFromParasolid.AddBodyRecordsInProductStructure`

Добавить записи о телах в структуру изделия

### `CheckGeometry`

ID: `P:TFlex.Model.ImportFromParasolid.CheckGeometry`

Сделать проверку тел, после импорта

### `DestinationFolder`

ID: `P:TFlex.Model.ImportFromParasolid.DestinationFolder`

Путь сохранения результата

### `HealGeometry`

ID: `P:TFlex.Model.ImportFromParasolid.HealGeometry`

Лечение геометрии

### `ImportFormat`

ID: `P:TFlex.Model.ImportFromParasolid.ImportFormat`

Формат импортирования сборки

### `ImportSheetBodies`

ID: `P:TFlex.Model.ImportFromParasolid.ImportSheetBodies`

Импортировать листовые тела

### `ImportSolidBodies`

ID: `P:TFlex.Model.ImportFromParasolid.ImportSolidBodies`

Импортировать твёрдые тела

### `ImportWireBodies`

ID: `P:TFlex.Model.ImportFromParasolid.ImportWireBodies`

Импортировать проволочные тела(кривые)

### `Layer`

ID: `P:TFlex.Model.ImportFromParasolid.Layer`

Задание слоя

Examples:
- `public static void SetLayer(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Layer l = new Layer(document); l.Monochrome = true;//Параметр слоя "одноцветный" l.Color = 12;//цвет ob.Layer = l;//установка слоя document.EndChanges();//Закрытие блока изменений документа }`

### `UUID`

ID: `P:TFlex.Model.ImportFromParasolid.UUID`

Задание UUID

### `UpdateProductStructure`

ID: `P:TFlex.Model.ImportFromParasolid.UpdateProductStructure`

Обновить структуру изделия
