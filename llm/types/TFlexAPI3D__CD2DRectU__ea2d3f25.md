# CD2DRectU

Assembly: `TFlexAPI3D`

## Summary

D2D1_RECT_U wrapper

## Constructors

### `CD2DRectU(CRect!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CD2DRectU.#ctor(CRect!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Constructs a CD2DRectU object from CRect object.

Parameters:
- `rect`: source rectangle

### `CD2DRectU(D2D_RECT_U!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CD2DRectU.#ctor(D2D_RECT_U!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Constructs a CD2DRectU object from D2D1_RECT_U object.

Parameters:
- `rect`: source rectangle

### `CD2DRectU(D2D_RECT_U!System.Runtime.CompilerServices.IsConst*)`

ID: `M:CD2DRectU.#ctor(D2D_RECT_U!System.Runtime.CompilerServices.IsConst*)`

Constructs a CD2DRectU object from D2D1_RECT_U object.

Parameters:
- `rect`: source rectangle

### `CD2DRectU(System.UInt32,System.UInt32,System.UInt32,System.UInt32)`

ID: `M:CD2DRectU.#ctor(System.UInt32,System.UInt32,System.UInt32,System.UInt32)`

Constructs a CD2DRectU object from four UINT32 values.

Parameters:
- `uLeft`: source left coordinate
- `uTop`: source top coordinate
- `uRight`: source right coordinate
- `uBottom`: source bottom coordinate

## Methods

### `CD2DRectU(CRect!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CD2DRectU.#ctor(CRect!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Constructs a CD2DRectU object from CRect object.

Parameters:
- `rect`: source rectangle

### `CD2DRectU(D2D_RECT_U!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CD2DRectU.#ctor(D2D_RECT_U!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Constructs a CD2DRectU object from D2D1_RECT_U object.

Parameters:
- `rect`: source rectangle

### `CD2DRectU(D2D_RECT_U!System.Runtime.CompilerServices.IsConst*)`

ID: `M:CD2DRectU.#ctor(D2D_RECT_U!System.Runtime.CompilerServices.IsConst*)`

Constructs a CD2DRectU object from D2D1_RECT_U object.

Parameters:
- `rect`: source rectangle

### `CD2DRectU(System.UInt32,System.UInt32,System.UInt32,System.UInt32)`

ID: `M:CD2DRectU.#ctor(System.UInt32,System.UInt32,System.UInt32,System.UInt32)`

Constructs a CD2DRectU object from four UINT32 values.

Parameters:
- `uLeft`: source left coordinate
- `uTop`: source top coordinate
- `uRight`: source right coordinate
- `uBottom`: source bottom coordinate

### `IsNull`

ID: `M:CD2DRectU.IsNull`

Returns a Boolean value that indicates whether an expression contains no valid data (Null).

Returns: TRUE if rectangle's top, left, bottom, and right values are all equal to 0; otherwise FALSE.

### `op_Implicit~CRect`

ID: `M:CD2DRectU.op_Implicit~CRect`

Converts CD2DRectU to CRect object.

Returns: Current value of D2D rectangle.
