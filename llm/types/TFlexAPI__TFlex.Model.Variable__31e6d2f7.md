# TFlex.Model.Variable

Assembly: `TFlexAPI`
Namespace: `TFlex.Model`

## Summary

Класс переменной

## Constructors

### `Variable(TFlex.Model.Document)`

ID: `M:TFlex.Model.Variable.#ctor(TFlex.Model.Document)`

Конструктор

Parameters:
- `document`: Документ переменной

### `Variable(TFlex.Model.Document,System.Boolean)`

ID: `M:TFlex.Model.Variable.#ctor(TFlex.Model.Document,System.Boolean)`

Конструктор

Parameters:
- `document`: Документ переменной
- `isText`: true, если переменная текстовая

### `Variable(TFlex.Model.Document,System.String,System.Double)`

ID: `M:TFlex.Model.Variable.#ctor(TFlex.Model.Document,System.String,System.Double)`

Конструктор, создающий вещественную переменную с указанным значением

Parameters:
- `document`: Документ переменной
- `name`: Имя переменной
- `value`: Значение переменной

### `Variable(TFlex.Model.Document,System.String,System.Double,System.Boolean)`

ID: `M:TFlex.Model.Variable.#ctor(TFlex.Model.Document,System.String,System.Double,System.Boolean)`

Конструктор, создающий вещественную переменную с указанным значением

Parameters:
- `document`: Документ переменной
- `name`: Имя переменной
- `value`: Значение переменной
- `external`: Признак внешней переменной

### `Variable(TFlex.Model.Document,System.String,System.String)`

ID: `M:TFlex.Model.Variable.#ctor(TFlex.Model.Document,System.String,System.String)`

Конструктор, создающий переменную с указанным выражением

Parameters:
- `document`: Документ переменной
- `name`: Имя переменной
- `expression`: Выражение переменной

### `Variable(TFlex.Model.Document,System.String,System.String,System.Boolean)`

ID: `M:TFlex.Model.Variable.#ctor(TFlex.Model.Document,System.String,System.String,System.Boolean)`

Конструктор, создающий переменную с указанным выражением

Parameters:
- `document`: Документ переменной
- `name`: Имя переменной
- `expression`: Выражение переменной
- `external`: Признак внешней переменной

## Methods

### `Variable(TFlex.Model.Document)`

ID: `M:TFlex.Model.Variable.#ctor(TFlex.Model.Document)`

Конструктор

Parameters:
- `document`: Документ переменной

### `Variable(TFlex.Model.Document,System.Boolean)`

ID: `M:TFlex.Model.Variable.#ctor(TFlex.Model.Document,System.Boolean)`

Конструктор

Parameters:
- `document`: Документ переменной
- `isText`: true, если переменная текстовая

### `Variable(TFlex.Model.Document,System.String,System.Double)`

ID: `M:TFlex.Model.Variable.#ctor(TFlex.Model.Document,System.String,System.Double)`

Конструктор, создающий вещественную переменную с указанным значением

Parameters:
- `document`: Документ переменной
- `name`: Имя переменной
- `value`: Значение переменной

### `Variable(TFlex.Model.Document,System.String,System.Double,System.Boolean)`

ID: `M:TFlex.Model.Variable.#ctor(TFlex.Model.Document,System.String,System.Double,System.Boolean)`

Конструктор, создающий вещественную переменную с указанным значением

Parameters:
- `document`: Документ переменной
- `name`: Имя переменной
- `value`: Значение переменной
- `external`: Признак внешней переменной

### `Variable(TFlex.Model.Document,System.String,System.String)`

ID: `M:TFlex.Model.Variable.#ctor(TFlex.Model.Document,System.String,System.String)`

Конструктор, создающий переменную с указанным выражением

Parameters:
- `document`: Документ переменной
- `name`: Имя переменной
- `expression`: Выражение переменной

### `Variable(TFlex.Model.Document,System.String,System.String,System.Boolean)`

ID: `M:TFlex.Model.Variable.#ctor(TFlex.Model.Document,System.String,System.String,System.Boolean)`

Конструктор, создающий переменную с указанным выражением

Parameters:
- `document`: Документ переменной
- `name`: Имя переменной
- `expression`: Выражение переменной
- `external`: Признак внешней переменной

### `AddValueListString(System.String)`

ID: `M:TFlex.Model.Variable.AddValueListString(System.String)`

Добавить строку в список значений

Parameters:
- `str`: Добавляемая строка

### `DeleteAllValueListStrings`

ID: `M:TFlex.Model.Variable.DeleteAllValueListStrings`

Удалить все строки в списке значений

### `DeleteValueListString(System.Int32)`

ID: `M:TFlex.Model.Variable.DeleteValueListString(System.Int32)`

Удалить строку в списке значений

Parameters:
- `index`: Номер позиции в списке

### `GetDatabaseList(System.Stringref ,System.Stringref ,System.Stringref ,System.Stringref )`

ID: `M:TFlex.Model.Variable.GetDatabaseList(System.String@,System.String@,System.String@,System.String@)`

Получить параметры для формирования списка значений на основе базы данных

Parameters:
- `databaseName`: Имя базы данных
- `fromFieldName`: Имя колонки базы данных, из которой будут отбираться значения
- `showFieldName`: Имя колонки базы данных, которые будут появляться при отображении списка. Если колонок несколько, имена колонок в параметре разделяются точкой с запятой.
- `filter`: Условие, по которому будут отбираться значения из базы данных

### `GetDateListFormat`

ID: `M:TFlex.Model.Variable.GetDateListFormat`

Получить формат даты

Returns: Формат даты

### `GetValueListString(System.Int32)`

ID: `M:TFlex.Model.Variable.GetValueListString(System.Int32)`

Получить строку в списке значений

Parameters:
- `index`: Номер позиции в списке

### `InsertValueListString(System.String,System.Int32)`

ID: `M:TFlex.Model.Variable.InsertValueListString(System.String,System.Int32)`

Добавить строку в список значений

Parameters:
- `index`: Номер позиции в списке
- `str`: Добавляемая строка

### `SetDatabaseList(System.String,System.String,System.String,System.String)`

ID: `M:TFlex.Model.Variable.SetDatabaseList(System.String,System.String,System.String,System.String)`

Установить параметры для формирования списка значений на основе базы данных

Parameters:
- `databaseName`: Имя базы данных
- `fromFieldName`: Имя колонки базы данных, из которой будут отбираться значения
- `showFieldName`: Имя колонки базы данных, которые будут появляться при отображении списка. Если колонок несколько, имена колонок в параметре разделяются точкой с запятой.
- `filter`: Условие, по которому будут отбираться значения из базы данных

### `SetDateListFormat(System.String)`

ID: `M:TFlex.Model.Variable.SetDateListFormat(System.String)`

Установить формат даты

Parameters:
- `format`: Формат даты

Remarks: Формат даты: "d" День месяца в виде одной или двух цифр, "dd" День месяца в виде двух цифр, "ddd" День недели в виде трёх букв, "dddd" Полное название дня недели, "M" Номер месяца в виде одной или двух цифр, "MM" Номер месяца в виде двух цифр, "MMM" Месяц в виде трёх букв, "MMMM" Полное название месяца, "y" Последняя цифра года, "yy" Последние две цифры года, "yyy" Полный год.

### `SetName(System.String,System.Boolean)`

ID: `M:TFlex.Model.Variable.SetName(System.String,System.Boolean)`

Переименовать переменную

Parameters:
- `name`: Новое имя переменной
- `includeAllExpressions`: Заменить имя переменной на новое в выражениях других переменных

## Propertys

### `AssemblyVariableName`

ID: `P:TFlex.Model.Variable.AssemblyVariableName`

Имя переменной сборки

### `AutoUnit`

ID: `P:TFlex.Model.Variable.AutoUnit`

Автоматическое определение единицы измерения переменной

### `Comment`

ID: `P:TFlex.Model.Variable.Comment`

Комментарий переменной

### `DocumentProperty`

ID: `P:TFlex.Model.Variable.DocumentProperty`

Свойство документа

### `ErrorState`

ID: `P:TFlex.Model.Variable.ErrorState`

Состояние ошибки

### `ErrorString`

ID: `P:TFlex.Model.Variable.ErrorString`

Строка ошибки

### `Expression`

ID: `P:TFlex.Model.Variable.Expression`

Выражение, задающее значение переменной

### `External`

ID: `P:TFlex.Model.Variable.External`

true, если переменная является помеченной (внешней)

Remarks: Данный параметр можно установить в true только в том случае, если переменная является константной (свойство `P:TFlex.Model.Variable.IsConstant` должен возвращать true)

### `GroupName`

ID: `P:TFlex.Model.Variable.GroupName`

Имя группы переменной

### `GroupType`

ID: `P:TFlex.Model.Variable.GroupType`

Идентификатор типа объекта

### `Hidden`

ID: `P:TFlex.Model.Variable.Hidden`

true, если переменная является скрытой

### `IsConstant`

ID: `P:TFlex.Model.Variable.IsConstant`

true, если переменная является константной.

Remarks: Переменная является константной если её выражение состоит только из значения одного числа или текстовой константы.

### `IsFunction`

ID: `P:TFlex.Model.Variable.IsFunction`

Переменная является функцией

### `IsReal`

ID: `P:TFlex.Model.Variable.IsReal`

true, если переменная является вещественной

### `IsText`

ID: `P:TFlex.Model.Variable.IsText`

true, если переменная является текстовой

### `IsUsed`

ID: `P:TFlex.Model.Variable.IsUsed`

true, если переменная используется (есть ссылка на неё из другого модельного объекта).

### `ListType`

ID: `P:TFlex.Model.Variable.ListType`

Тип списка значений переменной

### `Name`

ID: `P:TFlex.Model.Variable.Name`

Имя переменной

Remarks: Если после переименования требуется обновить имя данной переменной в выражениях других переменных, используйте вместо данного свойства метод RenameName

Examples:
- `public static void SetName(String name) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа //получение объекта по имени ModelObject ob = document.GetObjectByName("x"); if(ob!= null) { //назначить имя объекту ob.Name = "a1"; } document.EndChanges();//Закрытие блока изменений документа }`

### `PdmConnectionDirection`

ID: `P:TFlex.Model.Variable.PdmConnectionDirection`

Строка описания параметра PDM системы

Examples:
- `public static void VariableToDOCs() { Document doc = TFlex.Application.ActiveDocument;//Получение активного документа doc.BeginChanges("Передача параметров в DOCs");//Открытие блока изменений документа //создание переменной TFlex.Model.Variable var = new TFlex.Model.Variable(doc, "$xxx", "111"); //Строка описания параметра PDM системы - в виде Guid var.PdmParameterDescription = "[262a61a6-ca61-4404-9131-ddb992230c31]"; //Направление передачи параметров при интеграции с PDM - в обе стороны var.PdmConnectionDirection = PdmConnectionDirection.Both; //Тип параметра PDM системы - параметр файла var.PdmParameterType = PdmParameterType.File; doc.EndChanges();//Закрытие блока изменений документа }`

### `PdmParameterDescription`

ID: `P:TFlex.Model.Variable.PdmParameterDescription`

Строка описания параметра PDM системы

Examples:
- `public static void VariableToDOCs() { Document doc = TFlex.Application.ActiveDocument;//Получение активного документа doc.BeginChanges("Передача параметров в DOCs");//Открытие блока изменений документа //создание переменной TFlex.Model.Variable var = new TFlex.Model.Variable(doc, "$xxx", "111"); //Строка описания параметра PDM системы - в виде Guid var.PdmParameterDescription = "[262a61a6-ca61-4404-9131-ddb992230c31]"; //Направление передачи параметров при интеграции с PDM - в обе стороны var.PdmConnectionDirection = PdmConnectionDirection.Both; //Тип параметра PDM системы - параметр файла var.PdmParameterType = PdmParameterType.File; doc.EndChanges();//Закрытие блока изменений документа }`

### `PdmParameterFormat`

ID: `P:TFlex.Model.Variable.PdmParameterFormat`

Строка форматирования параметра PDM системы

### `PdmParameterType`

ID: `P:TFlex.Model.Variable.PdmParameterType`

Тип параметра PDM системы

Examples:
- `public static void VariableToDOCs() { Document doc = TFlex.Application.ActiveDocument;//Получение активного документа doc.BeginChanges("Передача параметров в DOCs");//Открытие блока изменений документа //создание переменной TFlex.Model.Variable var = new TFlex.Model.Variable(doc, "$xxx", "111"); //Строка описания параметра PDM системы - в виде Guid var.PdmParameterDescription = "[262a61a6-ca61-4404-9131-ddb992230c31]"; //Направление передачи параметров при интеграции с PDM - в обе стороны var.PdmConnectionDirection = PdmConnectionDirection.Both; //Тип параметра PDM системы - параметр файла var.PdmParameterType = PdmParameterType.File; doc.EndChanges();//Закрытие блока изменений документа }`

### `RealValue`

ID: `P:TFlex.Model.Variable.RealValue`

Значение вещественной переменной

### `Service`

ID: `P:TFlex.Model.Variable.Service`

true, если переменная является вспомогательной

### `TextValue`

ID: `P:TFlex.Model.Variable.TextValue`

Значение текстовой переменной

### `Tolerance`

ID: `P:TFlex.Model.Variable.Tolerance`

Управление допуском переменной

### `Unit`

ID: `P:TFlex.Model.Variable.Unit`

Комментарий переменной

Remarks: null означает "на задано"

### `ValueListCount`

ID: `P:TFlex.Model.Variable.ValueListCount`

Количество строк в списке значений
