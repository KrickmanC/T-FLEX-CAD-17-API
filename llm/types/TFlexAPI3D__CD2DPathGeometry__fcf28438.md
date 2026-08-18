# CD2DPathGeometry

Assembly: `TFlexAPI3D`

## Summary

ID2D1PathGeometry wrapper.

## Constructors

### `CD2DPathGeometry(CRenderTarget*,System.Int32)`

ID: `M:CD2DPathGeometry.#ctor(CRenderTarget*,System.Int32)`

Constructs a CD2DPathGeometry object.

Parameters:
- `pParentTarget`: A pointer to the render target.
- `bAutoDestroy`: Indicates that the object will be destroyed by owner (pParentTarget).

## Methods

### `CD2DPathGeometry(CRenderTarget*,System.Int32)`

ID: `M:CD2DPathGeometry.#ctor(CRenderTarget*,System.Int32)`

Constructs a CD2DPathGeometry object.

Parameters:
- `pParentTarget`: A pointer to the render target.
- `bAutoDestroy`: Indicates that the object will be destroyed by owner (pParentTarget).

### `Attach(ID2D1PathGeometry*)`

ID: `M:CD2DPathGeometry.Attach(ID2D1PathGeometry*)`

Attaches existing resource interface to the object

Parameters:
- `pResource`: Existing resource interface. Cannot be NULL

### `Create(CRenderTarget*)`

ID: `M:CD2DPathGeometry.Create(CRenderTarget*)`

Creates a CD2DPathGeometry.

Parameters:
- `pRenderTarget`: A pointer to the render target.

Returns: If the method succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

### `Destroy`

ID: `M:CD2DPathGeometry.Destroy`

Destroys a CD2DPathGeometry object.

### `Detach`

ID: `M:CD2DPathGeometry.Detach`

Detaches resource interface from the object

Returns: Pointer to detached resource interface.

### `GetFigureCount`

ID: `M:CD2DPathGeometry.GetFigureCount`

Retrieves tthe number of figures in the path geometry.

Returns: Returns the number of figures in the path geometry.

### `GetSegmentCount`

ID: `M:CD2DPathGeometry.GetSegmentCount`

Retrieves the number of segments in the path geometry.

Returns: Returns the number of segments in the path geometry.

### `Open`

ID: `M:CD2DPathGeometry.Open`

Retrieves the geometry sink that is used to populate the path geometry with figures and segments.

Returns: A pointer to the ID2D1GeometrySink that is used to populate the path geometry with figures and segments.

### `Stream(ID2D1GeometrySink*)`

ID: `M:CD2DPathGeometry.Stream(ID2D1GeometrySink*)`

Copies the contents of the path geometry to the specified ID2D1GeometrySink.

Parameters:
- `geometrySink`: The sink to which the path geometry's contents are copied. Modifying this sink does not change the contents of this path geometry.

Returns: If the method succeeds, it returns TRUE. Otherwise, it returns FALSE.

## Fields

### `m_pPathGeometry`

ID: `F:CD2DPathGeometry.m_pPathGeometry`

A pointer to an ID2D1PathGeometry.
