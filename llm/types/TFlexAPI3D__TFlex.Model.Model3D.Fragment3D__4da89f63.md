# TFlex.Model.Model3D.Fragment3D

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Класс операции 3D фрагмента

## Constructors

### `Fragment3D(System.String,TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Fragment3D.#ctor(System.String,TFlex.Model.Document)`

Конструктор для создания 3D фрагмента

Parameters:
- `fileName`: Имя файла документа фрагмента
- `document`: Документ, в котором создаётся новый объект

### `Fragment3D(System.String,TFlex.Model.Document,System.Boolean,System.Boolean)`

ID: `M:TFlex.Model.Model3D.Fragment3D.#ctor(System.String,TFlex.Model.Document,System.Boolean,System.Boolean)`

Конструктор для создания 3D фрагмента

Parameters:
- `fileName`: Имя файла документа фрагмента
- `document`: Документ, в котором создаётся новый объект
- `copy`: Использовать файл как шаблон для создания нового документа фрагмента в оперативной памяти
- `autoSave`: Создавать фрагмент в режиме автосохранения

### `Fragment3D(TFlex.Model.FileLink)`

ID: `M:TFlex.Model.Model3D.Fragment3D.#ctor(TFlex.Model.FileLink)`

Конструктор с именем файла фрагмента

Parameters:
- `link`: Ссылка на файл фрагмента

### `Fragment3D(TFlex.Model.Model2D.Fragment,TFlex.Model.Model3D.Workplane)`

ID: `M:TFlex.Model.Model3D.Fragment3D.#ctor(TFlex.Model.Model2D.Fragment,TFlex.Model.Model3D.Workplane)`

Конструктор с именем файла фрагмента

Parameters:
- `fragment`: Исходный 2D фрагмент
- `workplane`: Рабочая плоскость

## Methods

### `Fragment3D(System.String,TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Fragment3D.#ctor(System.String,TFlex.Model.Document)`

Конструктор для создания 3D фрагмента

Parameters:
- `fileName`: Имя файла документа фрагмента
- `document`: Документ, в котором создаётся новый объект

### `Fragment3D(System.String,TFlex.Model.Document,System.Boolean,System.Boolean)`

ID: `M:TFlex.Model.Model3D.Fragment3D.#ctor(System.String,TFlex.Model.Document,System.Boolean,System.Boolean)`

Конструктор для создания 3D фрагмента

Parameters:
- `fileName`: Имя файла документа фрагмента
- `document`: Документ, в котором создаётся новый объект
- `copy`: Использовать файл как шаблон для создания нового документа фрагмента в оперативной памяти
- `autoSave`: Создавать фрагмент в режиме автосохранения

### `Fragment3D(TFlex.Model.FileLink)`

ID: `M:TFlex.Model.Model3D.Fragment3D.#ctor(TFlex.Model.FileLink)`

Конструктор с именем файла фрагмента

Parameters:
- `link`: Ссылка на файл фрагмента

### `Fragment3D(TFlex.Model.Model2D.Fragment,TFlex.Model.Model3D.Workplane)`

ID: `M:TFlex.Model.Model3D.Fragment3D.#ctor(TFlex.Model.Model2D.Fragment,TFlex.Model.Model3D.Workplane)`

Конструктор с именем файла фрагмента

Parameters:
- `fragment`: Исходный 2D фрагмент
- `workplane`: Рабочая плоскость

### `ClearUDF`

ID: `M:TFlex.Model.Model3D.Fragment3D.ClearUDF`

Удаление параметров адаптивного фрагмента

### `EditAssocParams(System.Boolean)`

ID: `M:TFlex.Model.Model3D.Fragment3D.EditAssocParams(System.Boolean)`

Редактирование параметров адаптивного фрагмента

Parameters:
- `check`: Проверять актуальность ссылки

Returns: Пользовательский элемент

### `EditInContext`

ID: `M:TFlex.Model.Model3D.Fragment3D.EditInContext`

Редактировать в контексте сборки

### `FixByFragmentLCS(System.String,TFlex.Model.Model3D.LCS)`

ID: `M:TFlex.Model.Model3D.Fragment3D.FixByFragmentLCS(System.String,TFlex.Model.Model3D.LCS)`

Привязать фрагмент по системе координат, существующей в документе фрагмента к системе координат в сборке

Parameters:
- `sourceLCSName`: Имя системы координат, созданной в документе фрагмента
- `targetLCS`: Система координат, созданная в документе сборки(может быть null )

### `FixByFragmentLCSToConnector(System.String,TFlex.Model.Model3D.LCS)`

ID: `M:TFlex.Model.Model3D.Fragment3D.FixByFragmentLCSToConnector(System.String,TFlex.Model.Model3D.LCS)`

Привязать фрагмент по системе координат, существующей в документе фрагмента к системе координат в сборке. Если целевая система координат является коннектором, то выполняется связывание параметров.

Parameters:
- `sourceLCSName`: Имя системы координат, созданной в документе фрагмента
- `targetLCS`: Система координат, созданная в документе сборки(может быть null )

### `FixByWorkplane(TFlex.Model.Model3D.Workplane)`

ID: `M:TFlex.Model.Model3D.Fragment3D.FixByWorkplane(TFlex.Model.Model3D.Workplane)`

Привязать фрагмент по расположению соответствующего 2D фрагмента на Рабочей плоскости

Parameters:
- `Workplane`: Рабочая плоскость(может быть null )

### `GetBOMQuantity(System.Boolean)`

ID: `M:TFlex.Model.Model3D.Fragment3D.GetBOMQuantity(System.Boolean)`

Получить количество копий фрагмента во всех массивах

Parameters:
- `onlyVisible`: Считать количество только видимых копий, иначе считать всё

Returns: Количество копий фрагмента во всех массивах

### `GetDefaultLCS`

ID: `M:TFlex.Model.Model3D.Fragment3D.GetDefaultLCS`

Имя системы координат, которая используется по умолчанию

### `GetElevableLCS`

ID: `M:TFlex.Model.Model3D.Fragment3D.GetElevableLCS`

Список систем координат, которые могут использоваться для привязки

### `GetFragmentDocument(System.Boolean)`

ID: `M:TFlex.Model.Model3D.Fragment3D.GetFragmentDocument(System.Boolean)`

Получить документ фрамента с подстановкой значений переменных фрагмента

Parameters:
- `substitute`: Признак необходимости подстановки значений переменных

Returns: Документ фрагмента

### `GetFragmentDocument(System.Boolean,System.Boolean)`

ID: `M:TFlex.Model.Model3D.Fragment3D.GetFragmentDocument(System.Boolean,System.Boolean)`

Получить документ фрамента с подстановкой значений переменных фрагмента

Parameters:
- `substitute`: Признак необходимости подстановки значений переменных
- `update`: Обновить документ фрагмента

Returns: Документ фрагмента

### `GetUserBomData(System.Boolean)`

ID: `M:TFlex.Model.Model3D.Fragment3D.GetUserBomData(System.Boolean)`

Пользовательские данные для спецификации

Parameters:
- `onlyVisible`: 

Returns: Подсборка

### `GetVariableValue(System.String,System.Boolean)`

ID: `M:TFlex.Model.Model3D.Fragment3D.GetVariableValue(System.String,System.Boolean)`

Получить переменную фрагмента по имени

Parameters:
- `name`: Имя переменной фрагмента
- `forSet`: Признак необходимости изменения переменной

Returns: Переменная фрагмента

### `GetVariableValue(System.String,System.Boolean,System.Boolean)`

ID: `M:TFlex.Model.Model3D.Fragment3D.GetVariableValue(System.String,System.Boolean,System.Boolean)`

Получить переменную фрагмента по имени

Parameters:
- `name`: Имя переменной
- `forSet`: Признак необходимости изменения переменной

Returns: Переменная фрагмента

### `GetVariables`

ID: `M:TFlex.Model.Model3D.Fragment3D.GetVariables`

Контейнер переменных фрагмента

### `GetVariablesFromFragment(TFlex.Model.Model3D.Fragment3D)`

ID: `M:TFlex.Model.Model3D.Fragment3D.GetVariablesFromFragment(TFlex.Model.Model3D.Fragment3D)`

Установить значения всех переменных фрагмента в соответствии с переменными входящего фрагмента

Parameters:
- `sourceFragment`: Исходный фрагмент

### `MakeParameters(System.Collections.Generic.List`1{TFlex.Model.ModelObject},System.Boolean,System.Boolean,System.Boolean,System.Boolean,System.Boolean)`

ID: `M:TFlex.Model.Model3D.Fragment3D.MakeParameters(System.Collections.Generic.List`1{TFlex.Model.ModelObject},System.Boolean,System.Boolean,System.Boolean,System.Boolean,System.Boolean)`

В документе фрагмента создаются внешние параметры для списка операций из сборки и означиваются операциями из сборки

Parameters:
- `objects`: Операции из сборки, для которых строятся параметры
- `saveFragmentDocument`: Сохранять документ фрагмента
- `closeFragmentDocument`: Закрывать документ фрагмента
- `regenerateAssembly`: Пересчитывать сборку
- `copyConnectorInfo`: Копировать информацию о связи топологических элементов с коннекторами
- `associative`: Ассоциативные параметры

Returns: Список индентификаторов операций из сборки

### `MarkChanged`

ID: `M:TFlex.Model.Model3D.Fragment3D.MarkChanged`

Пометить объект как изменённый

### `OpenPart`

ID: `M:TFlex.Model.Model3D.Fragment3D.OpenPart`

Создать деталировку

Returns: Новый деталированный документ

### `OpenPart(TFlex.Model.Model2D.Fragment.OpenPartOptions)`

ID: `M:TFlex.Model.Model3D.Fragment3D.OpenPart(TFlex.Model.Model2D.Fragment.OpenPartOptions)`

Создать деталировку с данными параметрами

Parameters:
- `options`: Параметры

Returns: Новый деталированный документ

### `RememberTopLabel(TFlex.Model.Model3D.Fragment3D.LabelType)`

ID: `M:TFlex.Model.Model3D.Fragment3D.RememberTopLabel(TFlex.Model.Model3D.Fragment3D.LabelType)`

Запомнить метку верхушки Undo-стэка

Parameters:
- `type`: Тип действия

### `RemoveParameters(System.Collections.Generic.List`1{System.UInt32})`

ID: `M:TFlex.Model.Model3D.Fragment3D.RemoveParameters(System.Collections.Generic.List`1{System.UInt32})`

Удаление внешних параметров из фрагмента

Parameters:
- `parameters`: Список удаляемых внешних параметров

### `ShowVariablesDialog`

ID: `M:TFlex.Model.Model3D.Fragment3D.ShowVariablesDialog`

Показать диалог "Переменные"

### `UpdateDetail`

ID: `M:TFlex.Model.Model3D.Fragment3D.UpdateDetail`

Обновить деталь

### `UpdateVariablesFromFragmentDocument`

ID: `M:TFlex.Model.Model3D.Fragment3D.UpdateVariablesFromFragmentDocument`

Обновить все переменные фрагмента по документу фрагмента

### `UpdateVariablesFromFragmentDocument(System.Boolean)`

ID: `M:TFlex.Model.Model3D.Fragment3D.UpdateVariablesFromFragmentDocument(System.Boolean)`

Обновить переменные фрагмента по документу фрагмента

Parameters:
- `recalculateVariablesFromFragment`: Пересчитывать переменные типа "Из фрагмента"

## Propertys

### `AttributesFromSource`

ID: `P:TFlex.Model.Model3D.Fragment3D.AttributesFromSource`

Значение свойства "Атрибуты с исходной операции"

### `AutoSave`

ID: `P:TFlex.Model.Model3D.Fragment3D.AutoSave`

Создавать фрагмент в режиме автосохранения

### `BooleanOperationName`

ID: `P:TFlex.Model.Model3D.Fragment3D.BooleanOperationName`

Имя операция для булевой операции

### `Configuration`

ID: `P:TFlex.Model.Model3D.Fragment3D.Configuration`

Имя конфигурации модели

### `FileLink`

ID: `P:TFlex.Model.Model3D.Fragment3D.FileLink`

Ссылка на файл фрагмента

### `FilePath`

ID: `P:TFlex.Model.Model3D.Fragment3D.FilePath`

Имя файла 3D Фрагмента

### `Fixing`

ID: `P:TFlex.Model.Model3D.Fragment3D.Fixing`

Cпособ привязки 3D Фрагмента

### `FragmentFileFolder`

ID: `P:TFlex.Model.Model3D.Fragment3D.FragmentFileFolder`

Путь на папку относительно папки сборки при сохранении в папку сборки

### `FreedomPropertyContainer`

ID: `P:TFlex.Model.Model3D.Fragment3D.FreedomPropertyContainer`

Cтепени свободы 3D фрагмента

### `FullFilePath`

ID: `P:TFlex.Model.Model3D.Fragment3D.FullFilePath`

Полный путь файла 3D Фрагмента

### `GroupType`

ID: `P:TFlex.Model.Model3D.Fragment3D.GroupType`

Получить тип объекта

### `HideConnectors`

ID: `P:TFlex.Model.Model3D.Fragment3D.HideConnectors`

Скрывать коннекторы

### `HideLCSinTree`

ID: `P:TFlex.Model.Model3D.Fragment3D.HideLCSinTree`

Не показывать системы координат в дереве модели

### `IncludeInNewBom`

ID: `P:TFlex.Model.Model3D.Fragment3D.IncludeInNewBom`

Включение в новую спецификацию

### `IncludeInSpecificBom(System.String)`

ID: `P:TFlex.Model.Model3D.Fragment3D.IncludeInSpecificBom(System.String)`

Включение в спецификацию

### `InverseTransformation`

ID: `P:TFlex.Model.Model3D.Fragment3D.InverseTransformation`

Матрица обратного преобразования

### `MoveX`

ID: `P:TFlex.Model.Model3D.Fragment3D.MoveX`

Перемещение вдоль оси X

### `MoveY`

ID: `P:TFlex.Model.Model3D.Fragment3D.MoveY`

Перемещение вдоль оси Y

### `MoveZ`

ID: `P:TFlex.Model.Model3D.Fragment3D.MoveZ`

Перемещение вдоль оси Z

### `Parameters`

ID: `P:TFlex.Model.Model3D.Fragment3D.Parameters`

Список идентификаторов объектов-параметров в документе фрагмента и объектов-значений в документе сборки

### `Processing`

ID: `P:TFlex.Model.Model3D.Fragment3D.Processing`

Обработка(Обогащение) фрагмента

### `Reference`

ID: `P:TFlex.Model.Model3D.Fragment3D.Reference`

Множество ссылочных объектов из которых состоит 3D Фрагмент

### `RemoveAssociative`

ID: `P:TFlex.Model.Model3D.Fragment3D.RemoveAssociative`

Разрывать ассоциативные связи при удалении объекта-значения параметра

Remarks: Используется в мебельном модуле

### `RotateX`

ID: `P:TFlex.Model.Model3D.Fragment3D.RotateX`

Вращение по оси X

### `RotateY`

ID: `P:TFlex.Model.Model3D.Fragment3D.RotateY`

Вращение по оси Y

### `RotateZ`

ID: `P:TFlex.Model.Model3D.Fragment3D.RotateZ`

Вращение по оси Z

### `SaveFragmentToAssemblyFolder`

ID: `P:TFlex.Model.Model3D.Fragment3D.SaveFragmentToAssemblyFolder`

Cохранять файл фрагмента в папку сборки

### `Separated`

ID: `P:TFlex.Model.Model3D.Fragment3D.Separated`

Значение свойства "Как отдельные тела"

### `ShowOn2D`

ID: `P:TFlex.Model.Model3D.Fragment3D.ShowOn2D`

Показывать ли на 2D виде фрагмент

### `SourceLCSName`

ID: `P:TFlex.Model.Model3D.Fragment3D.SourceLCSName`

Имя системы координат созданной в документе фрагмента, используемой для привязки фрагмента

### `TargetLCS`

ID: `P:TFlex.Model.Model3D.Fragment3D.TargetLCS`

Целевая система координат в документе сборки, используемая для привязки фрагмента

### `UseColorFromSource`

ID: `P:TFlex.Model.Model3D.Fragment3D.UseColorFromSource`

Использовать цвет из документа фрагмента

### `UseFragmentStatus`

ID: `P:TFlex.Model.Model3D.Fragment3D.UseFragmentStatus`

Использовать статус документа фрагмента

### `Workplane`

ID: `P:TFlex.Model.Model3D.Fragment3D.Workplane`

Рабочая плоскость, используемая для привязки фрагмента
