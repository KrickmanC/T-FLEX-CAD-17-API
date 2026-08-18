# TFlex.Model.Model3D.WorkSurface

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Базовый класс для всех типов рабочих поверхностей

## Propertys

### `GroupType`

ID: `P:TFlex.Model.Model3D.WorkSurface.GroupType`

Получить тип объекта

### `Page`

ID: `P:TFlex.Model.Model3D.WorkSurface.Page`

Страница

Examples:
- `public static void SetPage(ModelObject ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Page p = new Page(document);//создание страницы p.Name = "страница1" ob.Page = p;//cтраница, на которой размещается элемент document.EndChanges();//Закрытие блока изменений документа }`

### `ShowOn3D`

ID: `P:TFlex.Model.Model3D.WorkSurface.ShowOn3D`

Признак рисования рабочей плоскости в 3D сцене
