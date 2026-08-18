# TFlex.Model.Database

Assembly: `TFlexAPI`
Namespace: `TFlex.Model`

## Summary

Класс базы данных

## Propertys

### `GroupType`

ID: `P:TFlex.Model.Database.GroupType`

Тип объекта

### `Name`

ID: `P:TFlex.Model.Database.Name`

Имя базы данных

Examples:
- `public static void SetName(String name) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа //получение объекта по имени ModelObject ob = document.GetObjectByName("x"); if(ob!= null) { //назначить имя объекту ob.Name = "a1"; } document.EndChanges();//Закрытие блока изменений документа }`

### `SubType`

ID: `P:TFlex.Model.Database.SubType`

Тип базы данных
