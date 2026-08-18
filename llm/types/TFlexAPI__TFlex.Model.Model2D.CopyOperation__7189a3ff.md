# TFlex.Model.Model2D.CopyOperation

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Базовый класс операции копирования

## Methods

### `AddSource(TFlex.Model.Model2D.Object2D)`

ID: `M:TFlex.Model.Model2D.CopyOperation.AddSource(TFlex.Model.Model2D.Object2D)`

Добавление в копию исходного объекта

Parameters:
- `addSource`: Добавляемый исходный объект

Returns: Индекс в объекте-копии добавленного исходного объекта

### `DeleteAssociative(System.Int32,System.Int32)`

ID: `M:TFlex.Model.Model2D.CopyOperation.DeleteAssociative(System.Int32,System.Int32)`

Удаление ассоциативного объекта

Parameters:
- `indexSource`: Индекс исходного объекта в списке объекта-копии
- `indexTransformation`: Индекс преобразования

Returns: false - если индексы выходит за границы списка исходных объектов и трансформаций

### `Explode(System.Boolean)`

ID: `M:TFlex.Model.Model2D.CopyOperation.Explode(System.Boolean)`

Разрушение операции

Parameters:
- `GroupObjects`: Объединять разрушенные объекты в группу

### `GetAssociate(System.Int32,System.Int32)`

ID: `M:TFlex.Model.Model2D.CopyOperation.GetAssociate(System.Int32,System.Int32)`

Получение ассоциативного объекта (результата копирования)

Parameters:
- `indexSource`: Индекс исходного объекта в списке объекта-копии
- `indexTransformation`: Индекс преобразования

Returns: Ассоциативный объект (результат копирования)

### `GetSourceObject(System.Int32)`

ID: `M:TFlex.Model.Model2D.CopyOperation.GetSourceObject(System.Int32)`

Получение исходного объекта

Parameters:
- `index`: Индекс исходного объекта в списке объекта-копии

Returns: Получение исходного объекта по его индексу

### `RemoveSource(System.Int32)`

ID: `M:TFlex.Model.Model2D.CopyOperation.RemoveSource(System.Int32)`

Удаление исходного объекта из копии

Parameters:
- `index`: Индекс в удаляемого исходного объекта в списке объекта-копии

Returns: false - если индекс выходит за границы списка исходных объектов

### `RestoreDeletedAssociatives`

ID: `M:TFlex.Model.Model2D.CopyOperation.RestoreDeletedAssociatives`

Восстановление удаленных ассоциативных объектов

## Propertys

### `CopyType`

ID: `P:TFlex.Model.Model2D.CopyOperation.CopyType`

Значение подтипа объекта "Копия"

### `GroupType`

ID: `P:TFlex.Model.Model2D.CopyOperation.GroupType`

Тип объекта "Копия"

### `Page`

ID: `P:TFlex.Model.Model2D.CopyOperation.Page`

Страница, на которой размещается элемент

Examples:
- `public static void SetPage(ModelObject ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Page p = new Page(document);//создание страницы p.Name = "страница1" ob.Page = p;//cтраница, на которой размещается элемент document.EndChanges();//Закрытие блока изменений документа }`

### `SourcesCount`

ID: `P:TFlex.Model.Model2D.CopyOperation.SourcesCount`

Количество копируемых объектов

### `TransformationCount`

ID: `P:TFlex.Model.Model2D.CopyOperation.TransformationCount`

Количество преобразований копируемых объектов
