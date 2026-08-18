# TFlex.Model.ModelObjectGroup

Assembly: `TFlexAPI`
Namespace: `TFlex.Model`

## Summary

Класс группы объектов модели, вспомогательного объекта документа T-FLEX.

## Constructors

### `ModelObjectGroup(TFlex.Model.Document,System.String)`

ID: `M:TFlex.Model.ModelObjectGroup.#ctor(TFlex.Model.Document,System.String)`

Конструктор

Parameters:
- `Doc`: Документ объекта
- `Name`: Имя группы. Если имя уже существует или значение параметра равно null, имя подбирается автоматически

## Methods

### `ModelObjectGroup(TFlex.Model.Document,System.String)`

ID: `M:TFlex.Model.ModelObjectGroup.#ctor(TFlex.Model.Document,System.String)`

Конструктор

Parameters:
- `Doc`: Документ объекта
- `Name`: Имя группы. Если имя уже существует или значение параметра равно null, имя подбирается автоматически

### `Add(TFlex.Model.ModelObject)`

ID: `M:TFlex.Model.ModelObjectGroup.Add(TFlex.Model.ModelObject)`

Добавление объекта в группу

Parameters:
- `object`: Добавляемый в группу объект

### `Add(TFlex.Model.ModelObjectGroup)`

ID: `M:TFlex.Model.ModelObjectGroup.Add(TFlex.Model.ModelObjectGroup)`

Добавление другой группы в данную группу

Parameters:
- `group`: Группа, добавляемая в данную группу

### `FindItem(TFlex.Model.ModelObject)`

ID: `M:TFlex.Model.ModelObjectGroup.FindItem(TFlex.Model.ModelObject)`

Найти элемент группы - объект модели

### `FindItem(TFlex.Model.ModelObjectGroup)`

ID: `M:TFlex.Model.ModelObjectGroup.FindItem(TFlex.Model.ModelObjectGroup)`

Найти элемент группы - вложенную группу

### `Remove(TFlex.Model.ModelObject)`

ID: `M:TFlex.Model.ModelObjectGroup.Remove(TFlex.Model.ModelObject)`

Удаление объекта из группы

### `Remove(TFlex.Model.ModelObjectGroup)`

ID: `M:TFlex.Model.ModelObjectGroup.Remove(TFlex.Model.ModelObjectGroup)`

Удаление вложенной группы объектов из данной группы

### `RemoveAllItems`

ID: `M:TFlex.Model.ModelObjectGroup.RemoveAllItems`

Удаление всех элементов группы

## Propertys

### `Count`

ID: `P:TFlex.Model.ModelObjectGroup.Count`

Количество элементов в группе

### `Document`

ID: `P:TFlex.Model.ModelObjectGroup.Document`

Документ, являющийся родительским для данной группы

### `GroupItems`

ID: `P:TFlex.Model.ModelObjectGroup.GroupItems`

Коллекция элементов, входящих в группу

### `IsOnTopLevel`

ID: `P:TFlex.Model.ModelObjectGroup.IsOnTopLevel`

Возвращает true, если группа не входит в другую группу

### `Name`

ID: `P:TFlex.Model.ModelObjectGroup.Name`

Имя группы

Examples:
- `public static void SetName(String name) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа //получение объекта по имени ModelObject ob = document.GetObjectByName("x"); if(ob!= null) { //назначить имя объекту ob.Name = "a1"; } document.EndChanges();//Закрытие блока изменений документа }`
