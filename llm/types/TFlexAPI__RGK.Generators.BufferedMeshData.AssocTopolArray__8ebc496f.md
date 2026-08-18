# RGK.Generators.BufferedMeshData.AssocTopolArray

Assembly: `TFlexAPI`
Namespace: `RGK.Generators.BufferedMeshData`

## Summary

Множество диапазонов индексов для топологических элементов

## Methods

### `CheckAllTopolInvalid`

ID: `M:RGK.Generators.BufferedMeshData.AssocTopolArray.CheckAllTopolInvalid`

### `GetAssocTopol(System.UInt32,RGK.Generators.BufferedMeshData.AssocTopol*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Generators.BufferedMeshData.AssocTopolArray.GetAssocTopol(System.UInt32,RGK.Generators.BufferedMeshData.AssocTopol*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iIndex`: Заданый индекс элемента
- `oAssocTopol`: Элемент топологии

Returns: Common::Success - в случае успеха Common::ArrayIndexOutOfBoundary - если индекс выходит за пределы допустимого диапазона

### `GetAssocTopol(std.shared_ptr<RGK.Model.Topol>!System.Runtime.CompilerServices.IsConst,RGK.Generators.BufferedMeshData.AssocTopol*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Generators.BufferedMeshData.AssocTopolArray.GetAssocTopol(std.shared_ptr<RGK.Model.Topol>!System.Runtime.CompilerServices.IsConst,RGK.Generators.BufferedMeshData.AssocTopol*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iTopol`: Заданыё топологический элемент
- `oAssocTopol`: Ассоциируемый с ним элемент

Returns: Common::Success - в случае успеха Common::ElementNotContained - в случае, если данный топологический элемент не содержится в списке

### `GetIndex(std.shared_ptr<RGK.Model.Topol>!System.Runtime.CompilerServices.IsConst)`

ID: `M:RGK.Generators.BufferedMeshData.AssocTopolArray.GetIndex(std.shared_ptr<RGK.Model.Topol>!System.Runtime.CompilerServices.IsConst)`

Parameters:
- `iTopol`: Искомый элемент

Returns: Индекс элемента в хранимом массиве. -1 - в случае если такого элемента нет.

### `Push(RGK.Generators.BufferedMeshData.AssocTopol!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Generators.BufferedMeshData.AssocTopolArray.Push(RGK.Generators.BufferedMeshData.AssocTopol!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iTopol`: Добавляемы топологический элемент

### `begin`

ID: `M:RGK.Generators.BufferedMeshData.AssocTopolArray.begin`

### `end`

ID: `M:RGK.Generators.BufferedMeshData.AssocTopolArray.end`

### `size`

ID: `M:RGK.Generators.BufferedMeshData.AssocTopolArray.size`
