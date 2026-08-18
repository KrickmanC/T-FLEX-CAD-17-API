# CD2DBrush

Assembly: `TFlexAPI`

## Summary

ID2D1Brush wrapper.

## Constructors

### `CD2DBrush(CRenderTarget*,CD2DBrushProperties*,System.Int32)`

ID: `M:CD2DBrush.#ctor(CRenderTarget*,CD2DBrushProperties*,System.Int32)`

Constructs a CD2DBrush object.

Parameters:
- `pParentTarget`: A pointer to the render target.
- `pBrushProperties`: A pointer to the opacity and transformation of a brush.
- `bAutoDestroy`: Indicates that the object will be destroyed by owner (pParentTarget).

## Methods

### `CD2DBrush(CRenderTarget*,CD2DBrushProperties*,System.Int32)`

ID: `M:CD2DBrush.#ctor(CRenderTarget*,CD2DBrushProperties*,System.Int32)`

Constructs a CD2DBrush object.

Parameters:
- `pParentTarget`: A pointer to the render target.
- `pBrushProperties`: A pointer to the opacity and transformation of a brush.
- `bAutoDestroy`: Indicates that the object will be destroyed by owner (pParentTarget).

### `Attach(ID2D1Brush*)`

ID: `M:CD2DBrush.Attach(ID2D1Brush*)`

Attaches existing resource interface to the object

Parameters:
- `pResource`: Existing resource interface. Cannot be NULL

### `Destroy`

ID: `M:CD2DBrush.Destroy`

Destroys a CD2DBrush object.

### `Detach`

ID: `M:CD2DBrush.Detach`

Detaches resource interface from the object

Returns: Pointer to detached resource interface.

### `Dispose`

ID: `M:CD2DBrush.Dispose`

The destructor. Called when a D2D brush object is being destroyed.

### `Get`

ID: `M:CD2DBrush.Get`

Returns ID2D1Brush interface

Returns: Pointer to an ID2D1Brush interface or NULL if object is not initialized yet.

### `GetOpacity`

ID: `M:CD2DBrush.GetOpacity`

Gets the degree of opacity of this brush

Returns: A value between zero and 1 that indicates the opacity of the brush. This value is a constant multiplier that linearly scales the alpha value of all pixels filled by the brush. The opacity values are clamped in the range 0 to 1 before they are multiplied together

### `GetTransform(D2D_MATRIX_3X2_F*)`

ID: `M:CD2DBrush.GetTransform(D2D_MATRIX_3X2_F*)`

Gets the current transform of the render target

Parameters:
- `transform`: When this returns, contains the current transform of the render target. This parameter is passed uninitialized

### `IsValid`

ID: `M:CD2DBrush.IsValid`

Checks resource validity

Returns: TRUE if resource is valid; otherwise FALSE.

### `SetOpacity(System.Single)`

ID: `M:CD2DBrush.SetOpacity(System.Single)`

Sets the degree of opacity of this brush

Parameters:
- `opacity`: A value between zero and 1 that indicates the opacity of the brush. This value is a constant multiplier that linearly scales the alpha value of all pixels filled by the brush. The opacity values are clamped in the range 0 to 1 before they are multiplied together

### `SetTransform(D2D_MATRIX_3X2_F!System.Runtime.CompilerServices.IsConst*)`

ID: `M:CD2DBrush.SetTransform(D2D_MATRIX_3X2_F!System.Runtime.CompilerServices.IsConst*)`

Applies the specified transform to the render target, replacing the existing transformation. All subsequent drawing operations occur in the transformed space

Parameters:
- `transform`: The transform to apply to the render target

### `op_Implicit~ID2D1Brush*`

ID: `M:CD2DBrush.op_Implicit~ID2D1Brush*`

Returns ID2D1Brush interface

Returns: Pointer to an ID2D1Brush interface or NULL if object is not initialized yet.

## Fields

### `m_pBrush`

ID: `F:CD2DBrush.m_pBrush`

Stores a pointer to an ID2D1Brush object.

### `m_pBrushProperties`

ID: `F:CD2DBrush.m_pBrushProperties`

Brush properties.
