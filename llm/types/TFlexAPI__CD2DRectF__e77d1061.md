# CD2DRectF

Assembly: `TFlexAPI`

## Summary

D2D1_RECT_F wrapper

## Constructors

### `CD2DRectF(CRect!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CD2DRectF.#ctor(CRect!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Constructs a CD2DRectF object from CRect object.

Parameters:
- `rect`: source rectangle

### `CD2DRectF(D2D_RECT_F!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CD2DRectF.#ctor(D2D_RECT_F!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Constructs a CD2DRectF object from D2D1_RECT_F object.

Parameters:
- `rect`: source rectangle

### `CD2DRectF(D2D_RECT_F!System.Runtime.CompilerServices.IsConst*)`

ID: `M:CD2DRectF.#ctor(D2D_RECT_F!System.Runtime.CompilerServices.IsConst*)`

Constructs a CD2DRectF object from D2D1_RECT_F object.

Parameters:
- `rect`: source rectangle

### `CD2DRectF(System.Single,System.Single,System.Single,System.Single)`

ID: `M:CD2DRectF.#ctor(System.Single,System.Single,System.Single,System.Single)`

Constructs a CD2DRectF object from four FLOAT values.

Parameters:
- `fLeft`: source left coordinate
- `fTop`: source top coordinate
- `fRight`: source right coordinate
- `fBottom`: source bottom coordinate

## Methods

### `CD2DRectF(CRect!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CD2DRectF.#ctor(CRect!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Constructs a CD2DRectF object from CRect object.

Parameters:
- `rect`: source rectangle

### `CD2DRectF(D2D_RECT_F!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CD2DRectF.#ctor(D2D_RECT_F!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Constructs a CD2DRectF object from D2D1_RECT_F object.

Parameters:
- `rect`: source rectangle

### `CD2DRectF(D2D_RECT_F!System.Runtime.CompilerServices.IsConst*)`

ID: `M:CD2DRectF.#ctor(D2D_RECT_F!System.Runtime.CompilerServices.IsConst*)`

Constructs a CD2DRectF object from D2D1_RECT_F object.

Parameters:
- `rect`: source rectangle

### `CD2DRectF(System.Single,System.Single,System.Single,System.Single)`

ID: `M:CD2DRectF.#ctor(System.Single,System.Single,System.Single,System.Single)`

Constructs a CD2DRectF object from four FLOAT values.

Parameters:
- `fLeft`: source left coordinate
- `fTop`: source top coordinate
- `fRight`: source right coordinate
- `fBottom`: source bottom coordinate

### `IsNull`

ID: `M:CD2DRectF.IsNull`

Returns a Boolean value that indicates whether an expression contains no valid data (Null).

Returns: TRUE if rectangle's top, left, bottom, and right values are all equal to 0; otherwise FALSE.

### `op_Implicit~CRect`

ID: `M:CD2DRectF.op_Implicit~CRect`

Converts CD2DRectF to CRect object.

Returns: Current value of D2D rectangle.
