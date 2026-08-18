# TFlex.Model.Model3D.Transformation

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Базовый класс для всех 3D преобразований

## Methods

### `GetTransformationMatrix`

ID: `M:TFlex.Model.Model3D.Transformation.GetTransformationMatrix`

Получаем карту преобразования

Returns: Карта преобразования

## Propertys

### `Name`

ID: `P:TFlex.Model.Model3D.Transformation.Name`

Имя преобразования

Remarks: Имя преобразования уникальное для элемента содержащего это преобразование

Examples:
- `public static void SetName(String name) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа //получение объекта по имени ModelObject ob = document.GetObjectByName("x"); if(ob!= null) { //назначить имя объекту ob.Name = "a1"; } document.EndChanges();//Закрытие блока изменений документа }`
- `public static void SetName(String name) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа //получение объекта по имени ModelObject ob = document.GetObjectByName("x"); if(ob!= null) { //назначить имя объекту ob.Name = "a1"; } document.EndChanges();//Закрытие блока изменений документа }`
- `public static void SetName(String name) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа //получение объекта по имени ModelObject ob = document.GetObjectByName("x"); if(ob!= null) { //назначить имя объекту ob.Name = "a1"; } document.EndChanges();//Закрытие блока изменений документа }`

### `OnlyForExplode`

ID: `P:TFlex.Model.Model3D.Transformation.OnlyForExplode`

Значение свойства "Только для разборки"

Remarks: Свойство "Только для разборки" предназначено для того чтобы иcпользовать преобразование только в режиме разборки

### `Suppressed`

ID: `P:TFlex.Model.Model3D.Transformation.Suppressed`

Значение свойства исключения преобразования

Remarks: Свойство подавления предназначено для исключения учёта данного преобразования для преобразования элемента
