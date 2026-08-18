# CD2DGeometry

Assembly: `TFlexCommandAPI`

## Summary

ID2D1Geometry wrapper.

## Constructors

### `CD2DGeometry(CRenderTarget*,System.Int32)`

ID: `M:CD2DGeometry.#ctor(CRenderTarget*,System.Int32)`

Constructs a CD2DGeometry object.

Parameters:
- `pParentTarget`: A pointer to the render target.
- `bAutoDestroy`: Indicates that the object will be destroyed by owner (pParentTarget).

## Methods

### `CD2DGeometry(CRenderTarget*,System.Int32)`

ID: `M:CD2DGeometry.#ctor(CRenderTarget*,System.Int32)`

Constructs a CD2DGeometry object.

Parameters:
- `pParentTarget`: A pointer to the render target.
- `bAutoDestroy`: Indicates that the object will be destroyed by owner (pParentTarget).

### `Attach(ID2D1Geometry*)`

ID: `M:CD2DGeometry.Attach(ID2D1Geometry*)`

Attaches existing resource interface to the object

Parameters:
- `pResource`: Existing resource interface. Cannot be NULL

### `CombineWithGeometry(CD2DGeometry*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,D2D1_COMBINE_MODE,D2D_MATRIX_3X2_F!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,ID2D1SimplifiedGeometrySink*,System.Single)`

ID: `M:CD2DGeometry.CombineWithGeometry(CD2DGeometry*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,D2D1_COMBINE_MODE,D2D_MATRIX_3X2_F!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,ID2D1SimplifiedGeometrySink*,System.Single)`

Combines this geometry with the specified geometry and stores the result in an ID2D1SimplifiedGeometrySink.

Parameters:
- `inputGeometry`: The geometry to combine with this instance.
- `combineMode`: The type of combine operation to perform.
- `inputGeometryTransform`: The transform to apply to inputGeometry before combining.
- `geometrySink`: The result of the combine operation.
- `flatteningTolerance`: The maximum bounds on the distance between points in the polygonal approximation of the geometries. Smaller values produce more accurate results but cause slower execution.

Returns: If the method succeeds, it returns TRUE. Otherwise, it returns FALSE.

### `CompareWithGeometry(CD2DGeometry*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,D2D_MATRIX_3X2_F!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Single)`

ID: `M:CD2DGeometry.CompareWithGeometry(CD2DGeometry*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,D2D_MATRIX_3X2_F!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Single)`

Describes the intersection between this geometry and the specified geometry. The comparison is performed using the specified flattening tolerance.

Parameters:
- `inputGeometry`: The geometry to test.
- `inputGeometryTransform`: The transform to apply to inputGeometry.
- `flatteningTolerance`: The maximum bounds on the distance between points in the polygonal approximation of the geometries. Smaller values produce more accurate results but cause slower execution.

Returns: If the method succeeds, it returns TRUE. Otherwise, it returns FALSE.

### `ComputeArea(D2D_MATRIX_3X2_F!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Single*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Single)`

ID: `M:CD2DGeometry.ComputeArea(D2D_MATRIX_3X2_F!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Single*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Single)`

Computes the area of the geometry after it has been transformed by the specified matrix and flattened using the specified tolerance.

Parameters:
- `worldTransform`: The transform to apply to this geometry before computing its area.
- `area`: When this method returns, contains a pointer to the area of the transformed, flattened version of this geometry. You must allocate storage for this parameter.
- `flatteningTolerance`: The maximum bounds on the distance between points in the polygonal approximation of the geometry. Smaller values produce more accurate results but cause slower execution.

Returns: If the method succeeds, it returns TRUE. Otherwise, it returns FALSE.

### `ComputeLength(D2D_MATRIX_3X2_F!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Single*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Single)`

ID: `M:CD2DGeometry.ComputeLength(D2D_MATRIX_3X2_F!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Single*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Single)`

Calculates the length of the geometry as though each segment were unrolled into a line.

Parameters:
- `worldTransform`: The transform to apply to the geometry before calculating its length.
- `length`: When this method returns, contains a pointer to the length of the geometry. For closed geometries, the length includes an implicit closing segment. You must allocate storage for this parameter.
- `flatteningTolerance`: The maximum bounds on the distance between points in the polygonal approximation of the geometry. Smaller values produce more accurate results but cause slower execution.

Returns: If the method succeeds, it returns TRUE. Otherwise, it returns FALSE.

### `ComputePointAtLength(System.Single,D2D_MATRIX_3X2_F!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CD2DPointF*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CD2DPointF*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Single)`

ID: `M:CD2DGeometry.ComputePointAtLength(System.Single,D2D_MATRIX_3X2_F!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CD2DPointF*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CD2DPointF*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Single)`

Calculates the point and tangent vector at the specified distance along the geometry after it has been transformed by the specified matrix and flattened using the specified tolerance.

Parameters:
- `length`: The distance along the geometry of the point and tangent to find. If this distance is less then 0, this method calculates the first point in the geometry. If this distance is greater than the length of the geometry, this method calculates the last point in the geometry.
- `worldTransform`: The transform to apply to the geometry before calculating the specified point and tangent.
- `point`: The location at the specified distance along the geometry. If the geometry is empty, this point contains NaN as its x and y values.
- `unitTangentVector`: When this method returns, contains a pointer to the tangent vector at the specified distance along the geometry. If the geometry is empty, this vector contains NaN as its x and y values. You must allocate storage for this parameter.
- `flatteningTolerance`: The maximum bounds on the distance between points in the polygonal approximation of the geometry. Smaller values produce more accurate results but cause slower execution.

Returns: If the method succeeds, it returns TRUE. Otherwise, it returns FALSE.

### `Destroy`

ID: `M:CD2DGeometry.Destroy`

Destroys a CD2DGeometry object.

### `Detach`

ID: `M:CD2DGeometry.Detach`

Detaches resource interface from the object

Returns: Pointer to detached resource interface.

### `Dispose`

ID: `M:CD2DGeometry.Dispose`

The destructor. Called when a D2D geometry object is being destroyed.

### `FillContainsPoint(CD2DPointF,D2D_MATRIX_3X2_F!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Int32*,System.Single)`

ID: `M:CD2DGeometry.FillContainsPoint(CD2DPointF,D2D_MATRIX_3X2_F!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Int32*,System.Single)`

Indicates whether the area filled by the geometry would contain the specified point given the specified flattening tolerance.

Parameters:
- `point`: The point to test.
- `worldTransform`: The transform to apply to the geometry prior to testing for containment.
- `contains`: When this method returns, contains a bool value that is TRUE if the area filled by the geometry contains point; otherwise, FALSE. You must allocate storage for this parameter.
- `flatteningTolerance`: The numeric accuracy with which the precise geometric path and path intersection is calculated. Points missing the fill by less than the tolerance are still considered inside. Smaller values produce more accurate results but cause slower execution.

Returns: If the method succeeds, it returns TRUE. Otherwise, it returns FALSE.

### `Get`

ID: `M:CD2DGeometry.Get`

Returns ID2D1Geometry interface

Returns: Pointer to an ID2D1Geometry interface or NULL if object is not initialized yet.

### `GetBounds(D2D_MATRIX_3X2_F!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CD2DRectF*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CD2DGeometry.GetBounds(D2D_MATRIX_3X2_F!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CD2DRectF*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Retrieves the bounds of the geometry.

Parameters:
- `worldTransform`: The transform to apply to this geometry before calculating its bounds.
- `bounds`: When this method returns, contains the bounds of this geometry. If the bounds are empty, this will be a rect where bounds.left is greater than bounds.right. You must allocate storage for this parameter.

Returns: If the method succeeds, it returns TRUE. Otherwise, it returns FALSE.

### `GetWidenedBounds(System.Single,ID2D1StrokeStyle*,D2D_MATRIX_3X2_F!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CD2DRectF*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Single)`

ID: `M:CD2DGeometry.GetWidenedBounds(System.Single,ID2D1StrokeStyle*,D2D_MATRIX_3X2_F!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CD2DRectF*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Single)`

Gets the bounds of the geometry after it has been widened by the specified stroke width and style and transformed by the specified matrix.

Parameters:
- `strokeWidth`: The amount by which to widen the geometry by stroking its outline.
- `strokeStyle`: The style of the stroke that widens the geometry.
- `worldTransform`: A transform to apply to the geometry after the geometry is transformed and after the geometry has been stroked.
- `bounds`: When this method returns, contains the bounds of the widened geometry. You must allocate storage for this parameter.
- `flatteningTolerance`: The maximum bounds on the distance between points in the polygonal approximation of the geometries. Smaller values produce more accurate results but cause slower execution.

Returns: If the method succeeds, it returns TRUE. Otherwise, it returns FALSE.

### `IsValid`

ID: `M:CD2DGeometry.IsValid`

Checks resource validity

Returns: TRUE if resource is valid; otherwise FALSE.

### `Outline(D2D_MATRIX_3X2_F!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,ID2D1SimplifiedGeometrySink*,System.Single)`

ID: `M:CD2DGeometry.Outline(D2D_MATRIX_3X2_F!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,ID2D1SimplifiedGeometrySink*,System.Single)`

Computes the outline of the geometry and writes the result to an ID2D1SimplifiedGeometrySink.

Parameters:
- `worldTransform`: The transform to apply to the geometry outline.
- `geometrySink`: The ID2D1SimplifiedGeometrySink to which the geometry transformed outline is appended.
- `flatteningTolerance`: The maximum bounds on the distance between points in the polygonal approximation of the geometry. Smaller values produce more accurate results but cause slower execution.

Returns: If the method succeeds, it returns TRUE. Otherwise, it returns FALSE.

### `Simplify(D2D1_GEOMETRY_SIMPLIFICATION_OPTION,D2D_MATRIX_3X2_F!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,ID2D1SimplifiedGeometrySink*,System.Single)`

ID: `M:CD2DGeometry.Simplify(D2D1_GEOMETRY_SIMPLIFICATION_OPTION,D2D_MATRIX_3X2_F!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,ID2D1SimplifiedGeometrySink*,System.Single)`

Creates a simplified version of the geometry that contains only lines and (optionally) cubic Bezier curves and writes the result to an ID2D1SimplifiedGeometrySink.

Parameters:
- `simplificationOption`: A value that specifies whether the simplified geometry should contain curves.
- `worldTransform`: The transform to apply to the simplified geometry.
- `geometrySink`: The ID2D1SimplifiedGeometrySink to which the simplified geometry is appended.
- `flatteningTolerance`: The maximum bounds on the distance between points in the polygonal approximation of the geometry. Smaller values produce more accurate results but cause slower execution.

Returns: If the method succeeds, it returns TRUE. Otherwise, it returns FALSE.

### `StrokeContainsPoint(CD2DPointF,System.Single,ID2D1StrokeStyle*,D2D_MATRIX_3X2_F!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Int32*,System.Single)`

ID: `M:CD2DGeometry.StrokeContainsPoint(CD2DPointF,System.Single,ID2D1StrokeStyle*,D2D_MATRIX_3X2_F!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Int32*,System.Single)`

Determines whether the geometry's stroke contains the specified point given the specified stroke thickness, style, and transform.

Parameters:
- `point`: The point to test for containment.
- `strokeWidth`: The thickness of the stroke to apply.
- `strokeStyle`: The style of the stroke to apply.
- `worldTransform`: The transform to apply to the stroked geometry.
- `contains`: When this method returns, contains a boolean value set to TRUE if the geometry's stroke contains the specified point; otherwise, FALSE. You must allocate storage for this parameter.
- `flatteningTolerance`: The numeric accuracy with which the precise geometric path and path intersection is calculated. Points missing the stroke by less than the tolerance are still considered inside. Smaller values produce more accurate results but cause slower execution.

Returns: If the method succeeds, it returns TRUE. Otherwise, it returns FALSE.

### `Tessellate(D2D_MATRIX_3X2_F!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,ID2D1TessellationSink*,System.Single)`

ID: `M:CD2DGeometry.Tessellate(D2D_MATRIX_3X2_F!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,ID2D1TessellationSink*,System.Single)`

Creates a set of clockwise-wound triangles that cover the geometry after it has been transformed using the specified matrix and flattened using the specified tolerance.

Parameters:
- `worldTransform`: The transform to apply to this geometry, or NULL.
- `tessellationSink`: The ID2D1TessellationSink to which the tessellated is appended.
- `flatteningTolerance`: The maximum bounds on the distance between points in the polygonal approximation of the geometry. Smaller values produce more accurate results but cause slower execution.

Returns: If the method succeeds, it returns TRUE. Otherwise, it returns FALSE.

### `Widen(System.Single,ID2D1StrokeStyle*,D2D_MATRIX_3X2_F!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,ID2D1SimplifiedGeometrySink*,System.Single)`

ID: `M:CD2DGeometry.Widen(System.Single,ID2D1StrokeStyle*,D2D_MATRIX_3X2_F!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,ID2D1SimplifiedGeometrySink*,System.Single)`

Widens the geometry by the specified stroke and writes the result to an ID2D1SimplifiedGeometrySink after it has been transformed by the specified matrix and flattened using the specified tolerance.

Parameters:
- `strokeWidth`: The amount by which to widen the geometry.
- `strokeStyle`: The style of stroke to apply to the geometry, or NULL.
- `worldTransform`: The transform to apply to the geometry after widening it.
- `geometrySink`: The ID2D1SimplifiedGeometrySink to which the widened geometry is appended.
- `flatteningTolerance`: The maximum bounds on the distance between points in the polygonal approximation of the geometry. Smaller values produce more accurate results but cause slower execution.

Returns: If the method succeeds, it returns TRUE. Otherwise, it returns FALSE.

### `op_Implicit~ID2D1Geometry*`

ID: `M:CD2DGeometry.op_Implicit~ID2D1Geometry*`

Returns ID2D1Geometry interface

Returns: Pointer to an ID2D1Geometry interface or NULL if object is not initialized yet.

## Fields

### `m_pGeometry`

ID: `F:CD2DGeometry.m_pGeometry`

A pointer to an ID2D1Geometry.
