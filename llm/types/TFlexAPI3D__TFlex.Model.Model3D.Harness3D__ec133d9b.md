# TFlex.Model.Model3D.Harness3D

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Класс 3D жгутов

## Constructors

### `Harness3D(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Harness3D.#ctor(TFlex.Model.Document)`

Конструктор для создания нового жгута

Parameters:
- `Doc`: Документ, в котором создаётся новый объект

## Methods

### `Harness3D(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Harness3D.#ctor(TFlex.Model.Document)`

Конструктор для создания нового жгута

Parameters:
- `Doc`: Документ, в котором создаётся новый объект

### `AddItem(TFlex.Model.Model3D.Construction3D)`

ID: `M:TFlex.Model.Model3D.Harness3D.AddItem(TFlex.Model.Model3D.Construction3D)`

Добавляет элемент в жгут

### `CanAddItem(TFlex.Model.Model3D.Construction3D)`

ID: `M:TFlex.Model.Model3D.Harness3D.CanAddItem(TFlex.Model.Model3D.Construction3D)`

Проверяет возможность вставить элемент в жгут, критерий: нет входит в текущий жгут и поджгуты, не принадлежит другим жгутам

### `ExistsItem(TFlex.Model.Model3D.Construction3D,System.Boolean)`

ID: `M:TFlex.Model.Model3D.Harness3D.ExistsItem(TFlex.Model.Model3D.Construction3D,System.Boolean)`

Проверяет наличие элемента в жгуте

### `GetItem(System.UInt32)`

ID: `M:TFlex.Model.Model3D.Harness3D.GetItem(System.UInt32)`

Получить элемент из жгута

### `RemoveItem(System.UInt32)`

ID: `M:TFlex.Model.Model3D.Harness3D.RemoveItem(System.UInt32)`

Удаляет элемент из жгута

## Propertys

### `ItemCount`

ID: `P:TFlex.Model.Model3D.Harness3D.ItemCount`

Количество элементов в жгуте
