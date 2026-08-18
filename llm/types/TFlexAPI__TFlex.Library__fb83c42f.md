# TFlex.Library

Assembly: `TFlexAPI`
Namespace: `TFlex`

## Summary

Класс библиотеки

## Constructors

### `Library(System.String,System.String)`

ID: `M:TFlex.Library.#ctor(System.String,System.String)`

Конструктор

Parameters:
- `name`: Название библиотеки
- `path`: Относительный путь к библиотеке

## Methods

### `Library(System.String,System.String)`

ID: `M:TFlex.Library.#ctor(System.String,System.String)`

Конструктор

Parameters:
- `name`: Название библиотеки
- `path`: Относительный путь к библиотеке

### `FindLibraryByName(System.String)`

ID: `M:TFlex.Library.FindLibraryByName(System.String)`

Поиск библиотеки по имени

### `IsDocumentExcluded(System.String)`

ID: `M:TFlex.Library.IsDocumentExcluded(System.String)`

Является ли документ исключенным

Parameters:
- `documentName`: Имя документа

## Propertys

### `FullPath`

ID: `P:TFlex.Library.FullPath`

Полный путь к библотеке

### `Name`

ID: `P:TFlex.Library.Name`

Название библиотеки

Examples:
- `public static void SetName(String name) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа //получение объекта по имени ModelObject ob = document.GetObjectByName("x"); if(ob!= null) { //назначить имя объекту ob.Name = "a1"; } document.EndChanges();//Закрытие блока изменений документа }`

### `Path`

ID: `P:TFlex.Library.Path`

Относительный путь к библиотеке
