# TFlex.Model.Model2D.Fragment

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Класс 2D фрагмента

## Constructors

### `Fragment(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.Fragment.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию

Parameters:
- `document`: Документ объекта

### `Fragment(TFlex.Model.Document,System.String)`

ID: `M:TFlex.Model.Model2D.Fragment.#ctor(TFlex.Model.Document,System.String)`

Конструктор с именем файла фрагмента

Parameters:
- `document`: Документ объекта
- `filePath`: Имя файла фрагмента

### `Fragment(TFlex.Model.Document,System.String,System.Boolean,System.Boolean)`

ID: `M:TFlex.Model.Model2D.Fragment.#ctor(TFlex.Model.Document,System.String,System.Boolean,System.Boolean)`

Конструктор с именем файла фрагмента

Parameters:
- `document`: Документ объекта
- `filePath`: Имя файла фрагмента
- `copy`: Использовать файл как шаблон для создания нового документа фрагмента в оперативной памяти
- `autoSave`: Создавать фрагмент в режиме автосохранения

### `Fragment(TFlex.Model.FileLink)`

ID: `M:TFlex.Model.Model2D.Fragment.#ctor(TFlex.Model.FileLink)`

Конструктор с именем файла фрагмента

Parameters:
- `link`: Ссылка на файл фрагмента

## Methods

### `Fragment(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.Fragment.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию

Parameters:
- `document`: Документ объекта

### `Fragment(TFlex.Model.Document,System.String)`

ID: `M:TFlex.Model.Model2D.Fragment.#ctor(TFlex.Model.Document,System.String)`

Конструктор с именем файла фрагмента

Parameters:
- `document`: Документ объекта
- `filePath`: Имя файла фрагмента

### `Fragment(TFlex.Model.Document,System.String,System.Boolean,System.Boolean)`

ID: `M:TFlex.Model.Model2D.Fragment.#ctor(TFlex.Model.Document,System.String,System.Boolean,System.Boolean)`

Конструктор с именем файла фрагмента

Parameters:
- `document`: Документ объекта
- `filePath`: Имя файла фрагмента
- `copy`: Использовать файл как шаблон для создания нового документа фрагмента в оперативной памяти
- `autoSave`: Создавать фрагмент в режиме автосохранения

### `Fragment(TFlex.Model.FileLink)`

ID: `M:TFlex.Model.Model2D.Fragment.#ctor(TFlex.Model.FileLink)`

Конструктор с именем файла фрагмента

Parameters:
- `link`: Ссылка на файл фрагмента

### `AssignAssemblyVariables`

ID: `M:TFlex.Model.Model2D.Fragment.AssignAssemblyVariables`

Назначить переменные сборки по умолчанию

### `Create3DFragment`

ID: `M:TFlex.Model.Model2D.Fragment.Create3DFragment`

Создать 3D фрагмент

### `EditInContext`

ID: `M:TFlex.Model.Model2D.Fragment.EditInContext`

Редактировать в контексте сборки

### `Explode(System.Boolean)`

ID: `M:TFlex.Model.Model2D.Fragment.Explode(System.Boolean)`

Раскрыть фрагмент

Parameters:
- `createConstructions`: Раскрыть фрагмент с построениями

### `Explode(TFlex.Model.Model2D.FragmentExplodeOptions)`

ID: `M:TFlex.Model.Model2D.Fragment.Explode(TFlex.Model.Model2D.FragmentExplodeOptions)`

Раскрыть фрагмент

Parameters:
- `explodeOptions`: Параметры раскрытия фрагмента

### `ExtractFragment(TFlex.Model.Model2D.FragmentExtractOptions)`

ID: `M:TFlex.Model.Model2D.Fragment.ExtractFragment(TFlex.Model.Model2D.FragmentExtractOptions)`

Создание фрагмента на основе списка объектов (Выделить фрагмент)

Parameters:
- `fragmentExtractOptions`: Параметры для выделения фрагмента

### `GetBOMQuantity(System.Boolean)`

ID: `M:TFlex.Model.Model2D.Fragment.GetBOMQuantity(System.Boolean)`

Получить количество копий фрагмента в всех массивах

Parameters:
- `onlyVisible`: Считать количество только видимых копий, иначе считать все

### `GetFixingNode(System.Int32)`

ID: `M:TFlex.Model.Model2D.Fragment.GetFixingNode(System.Int32)`

Установка узла привязки точки привязки фрагмента, привязанного при помощи переменных привязки

Parameters:
- `index`: Номер точки привязки. Может иметь значение от 1 до 9

Returns: Узел, к которому привязаны точки привязки фрагмента

### `GetFixingVectorCount`

ID: `M:TFlex.Model.Model2D.Fragment.GetFixingVectorCount`

Получить количество векторов привязки фрагмента

Returns: Количество векторов привязки

### `GetFixingVectorName`

ID: `M:TFlex.Model.Model2D.Fragment.GetFixingVectorName`

Получить имя текущего вектора привязки фрагмента

Returns: Имя вектора привязки

### `GetFixingVectorName(System.Int32)`

ID: `M:TFlex.Model.Model2D.Fragment.GetFixingVectorName(System.Int32)`

Получить имя вектора привязки фрагмента с указанным номером

Parameters:
- `index`: Номер вектора привязки

Returns: Имя вектора привязки

### `GetFixingX(System.Int32)`

ID: `M:TFlex.Model.Model2D.Fragment.GetFixingX(System.Int32)`

Получение координаты X точки привязки фрагмента, привязанного при помощи переменных привязки

Parameters:
- `index`: Номер точки привязки. Может иметь значение от 1 до 9

Returns: Координата X точки привязки

### `GetFixingY(System.Int32)`

ID: `M:TFlex.Model.Model2D.Fragment.GetFixingY(System.Int32)`

Получение координаты Y точки привязки фрагмента, привязанного при помощи переменных привязки

Parameters:
- `index`: Номер точки привязки. Может иметь значение от 1 до 9

Returns: Координата Y точки привязки

### `GetFragmentDocument`

ID: `M:TFlex.Model.Model2D.Fragment.GetFragmentDocument`

Получить документ фрамента

Returns: Документ фрагмента

### `GetFragmentDocument(System.Boolean)`

ID: `M:TFlex.Model.Model2D.Fragment.GetFragmentDocument(System.Boolean)`

Получить документ фрамента с подстановкой значений переменных фрагмента

Parameters:
- `substitute`: Признак необходимости подстановки значений переменных

Returns: Документ фрагмента

### `GetUserBomData(System.Boolean)`

ID: `M:TFlex.Model.Model2D.Fragment.GetUserBomData(System.Boolean)`

Пользовательские данные для спецификации

Parameters:
- `onlyVisible`: Собирать информацию только для видимых объектов

Returns: Подсборка

### `GetVariableValue(System.String,System.Boolean)`

ID: `M:TFlex.Model.Model2D.Fragment.GetVariableValue(System.String,System.Boolean)`

Получить переменную фрагмента по имени

### `GetVariableValue(System.String,System.Boolean,System.Boolean)`

ID: `M:TFlex.Model.Model2D.Fragment.GetVariableValue(System.String,System.Boolean,System.Boolean)`

Получить переменную фрагмента по имени

Parameters:
- `name`: Имя переменной
- `forSet`: Признак необходимости изменения переменной

Returns: Переменная фрагмента

### `GetVariables`

ID: `M:TFlex.Model.Model2D.Fragment.GetVariables`

Контейнер переменных фрагмента

### `GetVariables(System.Boolean)`

ID: `M:TFlex.Model.Model2D.Fragment.GetVariables(System.Boolean)`

Получить контейнер переменных фрагмента

Parameters:
- `includeInternal`: Включить скрытые переменные

Returns: Контейнер переменных фрагмента

### `GetVariables(System.Boolean,System.Boolean)`

ID: `M:TFlex.Model.Model2D.Fragment.GetVariables(System.Boolean,System.Boolean)`

Контейнер переменных фрагмента

Parameters:
- `includeInternal`: Включить скрытые переменные
- `includeFixing`: Включить переменные фиксации (x1, y1 - x9, y9)

### `GetVariablesFromFragment(TFlex.Model.Model2D.Fragment)`

ID: `M:TFlex.Model.Model2D.Fragment.GetVariablesFromFragment(TFlex.Model.Model2D.Fragment)`

Установить значения всех переменных фрагмента в соответствии с переменными входящего фрагмента

Parameters:
- `sourceFragment`: Исходный фрагмент

### `HaveFixingPoint(System.Int32)`

ID: `M:TFlex.Model.Model2D.Fragment.HaveFixingPoint(System.Int32)`

Проверка существования точки привязки фрагмента, привязанного при помощи переменных привязки

Parameters:
- `index`: Номер точки привязки. Может иметь значение от 1 до 9

Returns: true, если точка привязки фрагмента с указанным номером существует, иначе false

### `HideAssociatedLayers`

ID: `M:TFlex.Model.Model2D.Fragment.HideAssociatedLayers`

Гасим слои, связанные с вектором привязки

### `HideAssociatedLayers(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.Fragment.HideAssociatedLayers(TFlex.Model.Document)`

Гасим слои, связанные с вектором привязки

Parameters:
- `document`: Документ для изменений

### `OpenPart`

ID: `M:TFlex.Model.Model2D.Fragment.OpenPart`

Создать деталировку

Returns: Новый деталированный документ

### `OpenPart(TFlex.Model.Model2D.Fragment.OpenPartOptions)`

ID: `M:TFlex.Model.Model2D.Fragment.OpenPart(TFlex.Model.Model2D.Fragment.OpenPartOptions)`

Создать деталировку с данными параметрами

Returns: Новый деталированный документ

### `RestoreAssociatedLayers`

ID: `M:TFlex.Model.Model2D.Fragment.RestoreAssociatedLayers`

Восстанавливаем видимость слоев, связанных с вектором привязки

### `RestoreAssociatedLayers(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.Fragment.RestoreAssociatedLayers(TFlex.Model.Document)`

Восстанавливаем видимость слоев, связанных с вектором привязки

Parameters:
- `document`: Документ для изменений

### `SetDefaultFixingVector`

ID: `M:TFlex.Model.Model2D.Fragment.SetDefaultFixingVector`

Установить привязку фрагмента по основному вектору привязки

### `SetDefaultVariableValues`

ID: `M:TFlex.Model.Model2D.Fragment.SetDefaultVariableValues`

Установить значения переменных фрагмента из документа фрагмента

### `SetFixingNode(System.Int32,TFlex.Model.Model2D.Node)`

ID: `M:TFlex.Model.Model2D.Fragment.SetFixingNode(System.Int32,TFlex.Model.Model2D.Node)`

Установка узла привязки точки привязки фрагмента, привязанного при помощи переменных привязки

Parameters:
- `index`: Номер точки привязки. Может иметь значение от 1 до 9
- `node`: Узел, к которому привязана точка привязки фрагмента

Remarks: Переменные привязки - переменные в документе фрагмента с имененем x или y и индексом от 1 до 9

### `SetFixingPoint(System.Int32,System.Double,System.Double)`

ID: `M:TFlex.Model.Model2D.Fragment.SetFixingPoint(System.Int32,System.Double,System.Double)`

Установка координат точки привязки фрагмента, привязанного при помощи переменных привязки

Parameters:
- `index`: Номер точки привязки. Может иметь значение от 1 до 9
- `x`: Координата X точки привязки
- `y`: Координата Y точки привязки

Remarks: Переменные привязки - переменные в документе фрагмента с имененем x или y и индексом от 1 до 9

### `SetFixingVectorName(System.String)`

ID: `M:TFlex.Model.Model2D.Fragment.SetFixingVectorName(System.String)`

Установить привязку фрагмента по вектору привязки с указанным именем

Parameters:
- `name`: Имя вектора привязки

### `ShowVariablesDialog`

ID: `M:TFlex.Model.Model2D.Fragment.ShowVariablesDialog`

Показать диалог "Переменные"

### `UpdateVariablesFromFragmentDocument`

ID: `M:TFlex.Model.Model2D.Fragment.UpdateVariablesFromFragmentDocument`

Обновить переменные фрагмента по документу фрагмента

## Propertys

### `AlwaysRegenerate3DModel`

ID: `P:TFlex.Model.Model2D.Fragment.AlwaysRegenerate3DModel`

Всегда пересчитывать 3D модель

### `Angle`

ID: `P:TFlex.Model.Model2D.Fragment.Angle`

Угол поворота вектора привязки

### `AutoSave`

ID: `P:TFlex.Model.Model2D.Fragment.AutoSave`

Создавать фрагмент в режиме автосохранения

### `Connector`

ID: `P:TFlex.Model.Model2D.Fragment.Connector`

Коннектор, к которому привязан фрагмент

### `Constant`

ID: `P:TFlex.Model.Model2D.Fragment.Constant`

Параметр "Постоянный фрагмент (символ)"

### `EndNode`

ID: `P:TFlex.Model.Model2D.Fragment.EndNode`

Узел привязки конечной точки вектора привязки

### `EndX`

ID: `P:TFlex.Model.Model2D.Fragment.EndX`

Координата X привязки конечной точки вектора привязки

### `EndY`

ID: `P:TFlex.Model.Model2D.Fragment.EndY`

Координата Y привязки конечной точки вектора привязки

### `FileLink`

ID: `P:TFlex.Model.Model2D.Fragment.FileLink`

Ссылка на файл фрагмента

### `FilePath`

ID: `P:TFlex.Model.Model2D.Fragment.FilePath`

Имя файла фрагмента

### `FragmentDocumentPage`

ID: `P:TFlex.Model.Model2D.Fragment.FragmentDocumentPage`

Страница с которой берётся фрагмент

### `FragmentFileFolder`

ID: `P:TFlex.Model.Model2D.Fragment.FragmentFileFolder`

Путь на папку относительно папки сборки при сохранении в папку сборки

### `FullFilePath`

ID: `P:TFlex.Model.Model2D.Fragment.FullFilePath`

Полный путь файла фрагмента

### `GroupType`

ID: `P:TFlex.Model.Model2D.Fragment.GroupType`

Тип объекта

### `HasAssociatedFragment`

ID: `P:TFlex.Model.Model2D.Fragment.HasAssociatedFragment`

### `IncludeInNewBom`

ID: `P:TFlex.Model.Model2D.Fragment.IncludeInNewBom`

Включение в новую спецификацию

### `IncludeInSpecificBom(System.String)`

ID: `P:TFlex.Model.Model2D.Fragment.IncludeInSpecificBom(System.String)`

Включение в спецификацию

### `Layer`

ID: `P:TFlex.Model.Model2D.Fragment.Layer`

Слой, на котором размещается объект

Examples:
- `public static void SetLayer(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Layer l = new Layer(document); l.Monochrome = true;//Параметр слоя "одноцветный" l.Color = 12;//цвет ob.Layer = l;//установка слоя document.EndChanges();//Закрытие блока изменений документа }`
- `public static void SetLayer(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Layer l = new Layer(document); l.Monochrome = true;//Параметр слоя "одноцветный" l.Color = 12;//цвет ob.Layer = l;//установка слоя document.EndChanges();//Закрытие блока изменений документа }`

### `Level`

ID: `P:TFlex.Model.Model2D.Fragment.Level`

Уровень объекта

Examples:
- `public static void SetLevel(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("Установка уровня");//Открытие блока изменений документа ob.Level = 3;//установка уровня document.EndChanges();//Закрытие блока изменений документа }`
- `public static void SetLevel(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("Установка уровня");//Открытие блока изменений документа ob.Level = 3;//установка уровня document.EndChanges();//Закрытие блока изменений документа }`

### `Page`

ID: `P:TFlex.Model.Model2D.Fragment.Page`

Страница, на которой размещается элемент

Examples:
- `public static void SetPage(ModelObject ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Page p = new Page(document);//создание страницы p.Name = "страница1" ob.Page = p;//cтраница, на которой размещается элемент document.EndChanges();//Закрытие блока изменений документа }`
- `public static void SetPage(ModelObject ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Page p = new Page(document);//создание страницы p.Name = "страница1" ob.Page = p;//cтраница, на которой размещается элемент document.EndChanges();//Закрытие блока изменений документа }`

### `Priority`

ID: `P:TFlex.Model.Model2D.Fragment.Priority`

Приоритет объекта

### `SaveFragmentToAssemblyFolder`

ID: `P:TFlex.Model.Model2D.Fragment.SaveFragmentToAssemblyFolder`

Cохранять файл фрагмента в папку сборки

### `Scale`

ID: `P:TFlex.Model.Model2D.Fragment.Scale`

Параметр "Масштаб"

### `ScaleLineWidth`

ID: `P:TFlex.Model.Model2D.Fragment.ScaleLineWidth`

Параметр "Масштабировать толщину линий"

### `StartNode`

ID: `P:TFlex.Model.Model2D.Fragment.StartNode`

Узел привязки начальной точки вектора привязки

### `StartX`

ID: `P:TFlex.Model.Model2D.Fragment.StartX`

Координата X привязки начальной точки вектора привязки

### `StartY`

ID: `P:TFlex.Model.Model2D.Fragment.StartY`

Координата Y привязки начальной точки вектора привязки

### `Symmetric`

ID: `P:TFlex.Model.Model2D.Fragment.Symmetric`

Параметр "Симметричный относительно вектора привязки"

### `Transformation`

ID: `P:TFlex.Model.Model2D.Fragment.Transformation`

Получить текущее преобразование фрагмента

### `UseAssemblyStatus`

ID: `P:TFlex.Model.Model2D.Fragment.UseAssemblyStatus`

Использовать статус сборки, иначе - статус документа фрагмента
