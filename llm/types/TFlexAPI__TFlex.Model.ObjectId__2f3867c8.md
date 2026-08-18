# TFlex.Model.ObjectId

Assembly: `TFlexAPI`
Namespace: `TFlex.Model`

## Summary

Класс идентификации объектов ModelObject

## Methods

### `Clone`

ID: `M:TFlex.Model.ObjectId.Clone`

Создает новый объект, являющийся копией текущего экземпляра.

### `CompareTo(System.Object)`

ID: `M:TFlex.Model.ObjectId.CompareTo(System.Object)`

Сравнивает текущий экземпляр с другим объектом того же типа и возвращает целое число, которое показывает, расположен ли текущий экземпляр перед, после или на той же позиции в порядке сортировки, что и другой объект.

Parameters:
- `obj`: Объект для сравнения с данным экземпляром.

### `Create(System.UInt32)`

ID: `M:TFlex.Model.ObjectId.Create(System.UInt32)`

Возвращает новый ObjectId, если oldID корректный. Иначе возвращает null.

### `Create(System.UInt64)`

ID: `M:TFlex.Model.ObjectId.Create(System.UInt64)`

Возвращает новый ObjectId, если idData корректный. Иначе возвращает null.

### `Equals(System.Object)`

ID: `M:TFlex.Model.ObjectId.Equals(System.Object)`

Определяет, равны ли два экземпляра объекта.

### `GetHashCode`

ID: `M:TFlex.Model.ObjectId.GetHashCode`

Служит хэш-функцией по умолчанию.

### `Parse(System.String)`

ID: `M:TFlex.Model.ObjectId.Parse(System.String)`

Распарсить строку в ObjectId. Выбросит исключение ArgumentException, если строка некорректна.

### `ToString`

ID: `M:TFlex.Model.ObjectId.ToString`

Возвращает строку, представляющую текущий объект.

### `TryParse(System.String)`

ID: `M:TFlex.Model.ObjectId.TryParse(System.String)`

Распарсить строку в ObjectId. Вернет null, если строка некорректна.

### `TryParse(System.String,TFlex.Model.ObjectIdref )`

ID: `M:TFlex.Model.ObjectId.TryParse(System.String,TFlex.Model.ObjectId@)`

Распарсить строку в ObjectId. Вернет false, если строка некорректна.

## Propertys

### `IsValid`

ID: `P:TFlex.Model.ObjectId.IsValid`

Является ли идентификатор корректным
