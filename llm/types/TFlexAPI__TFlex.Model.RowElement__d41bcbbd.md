# TFlex.Model.RowElement

Assembly: `TFlexAPI`
Namespace: `TFlex.Model`

## Summary

Класс элемента структуры изделия

## Methods

### `CreateChangesScope`

ID: `M:TFlex.Model.RowElement.CreateChangesScope`

Создать область изменений. Запись не будет автоматически пересчитываться при изменениях в ячейках. Вместо этого она пересчитается когда будет вызван Dispose.

Remarks: Для использования в using.

### `GetCell(System.Guid)`

ID: `M:TFlex.Model.RowElement.GetCell(System.Guid)`

Получить ячейку элемента для колонки структуры изделия

Parameters:
- `parameterId`: Идентификатор колонки структуры изделия

### `GetCell(TFlex.Model.Data.ProductStructure.ParameterDescriptor)`

ID: `M:TFlex.Model.RowElement.GetCell(TFlex.Model.Data.ProductStructure.ParameterDescriptor)`

Получить ячейку элемента для колонки структуры изделия

Parameters:
- `parameter`: Колонка структуры изделия

### `GetSourceFragmentIdChain(System.Boolean)`

ID: `M:TFlex.Model.RowElement.GetSourceFragmentIdChain(System.Boolean)`

Список идентификаторов фрагментов, из которых поднят элемент. Если элемент не поднят из фрагмента, то возвращается пустой перечислитель.

Parameters:
- `fragment3d`: Возвращать идентификаторы для 3D фрагментов

## Propertys

### `IncludeInAssembly`

ID: `P:TFlex.Model.RowElement.IncludeInAssembly`

Получить ячейку "Включать в отчёты/спецификации текущего документа"

### `IncludeInDoc`

ID: `P:TFlex.Model.RowElement.IncludeInDoc`

Получить ячейку "Включать в отчёты/спецификации текущего документа"

### `LinkedObjects`

ID: `P:TFlex.Model.RowElement.LinkedObjects`

Модельные объекты, связанные с элементом структуры изделия

### `ParentRowElement`

ID: `P:TFlex.Model.RowElement.ParentRowElement`

Родительский элемент

### `Position`

ID: `P:TFlex.Model.RowElement.Position`

Получить ячейку "Включать при вставке в сборку"

### `ProductStructure`

ID: `P:TFlex.Model.RowElement.ProductStructure`

Структура изделия, которой принадлежит элемент

### `SourceFragment3DFirstLevel`

ID: `P:TFlex.Model.RowElement.SourceFragment3DFirstLevel`

Фрагмент 3D, из которого поднят элемент. Если элемент не поднят из фрагмента или поднят из фрагмента 2D, то возвращается null.

### `SourceFragmentFirstLevel`

ID: `P:TFlex.Model.RowElement.SourceFragmentFirstLevel`

Фрагмент, из которого поднят элемент. Если элемент не поднят из фрагмента, то возвращается null.

### `SourceFragmentPath`

ID: `P:TFlex.Model.RowElement.SourceFragmentPath`

Путь к фрагменту, из которого поднят элемент. Если элемент не поднят из фрагмента, то возвращается null.

### `SourceObject`

ID: `P:TFlex.Model.RowElement.SourceObject`

Исходный модельный объект, по которому создана запись. Если элемент не собран по текущему документу, то возвращается null.

### `SourceRowElementUID`

ID: `P:TFlex.Model.RowElement.SourceRowElementUID`

Уникальный идентификатор элемента, по которому создан этот элемент. Если элемент не поднят из фрагмента, то возвращается System.Guid.Empty

### `SourceRowElementUIDFirstLevel`

ID: `P:TFlex.Model.RowElement.SourceRowElementUIDFirstLevel`

Уникальный идентификатор элемента, по которому создан этот элемент (первого уровня вложенности). Если элемент не поднят из фрагмента, то возвращается System.Guid.Empty

### `UID`

ID: `P:TFlex.Model.RowElement.UID`

Уникальный идентификатор элемента

### `default(System.Guid)`

ID: `P:TFlex.Model.RowElement.default(System.Guid)`

Получить ячейку элемента для колонки структуры изделия

Parameters:
- `parameterId`: Идентификатор колонки структуры изделия

### `default(TFlex.Model.Data.ProductStructure.ParameterDescriptor)`

ID: `P:TFlex.Model.RowElement.default(TFlex.Model.Data.ProductStructure.ParameterDescriptor)`

Получить ячейку элемента для колонки структуры изделия

Parameters:
- `parameter`: Колонка структуры изделия
