# CAnimationPoint

Assembly: `TFlexAPI`

## Summary

Implements the functionality of a point whose coordinates can be animated.

## Remarks

The CAnimationPoint class encapsulates two CAnimationVariable objects and can represent in applications a point. For example, you can use this class to animate a position of any object on the screen (like text string, circle, point etc). To use this class in application, just instantiate an object of this class, add it to animation controller using CAnimationController::AddAnimationObject and call AddTransition for each transition to be applied to X and/or Y coordinates.

## Constructors

### `CAnimationPoint`

ID: `M:CAnimationPoint.#ctor`

Constructs CAnimationPoint object.

Remarks: Constructs CAnimationPoint object with default properties: default point coordinates, Group ID and Object ID are set to 0.

### `CAnimationPoint(CPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.UInt32,System.UInt32,System.UInt64)`

ID: `M:CAnimationPoint.#ctor(CPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.UInt32,System.UInt32,System.UInt64)`

Constructs CAnimationPoint object.

Parameters:
- `ptDefault`: Specifies default point coordinates.
- `nGroupID`: Specifies Group ID.
- `nObjectID`: Specifies Object ID.
- `dwUserData`: Specifies user-defined data.

Remarks: Constructs CAnimationPoint object with specified properties.

## Methods

### `CAnimationPoint`

ID: `M:CAnimationPoint.#ctor`

Constructs CAnimationPoint object.

Remarks: Constructs CAnimationPoint object with default properties: default point coordinates, Group ID and Object ID are set to 0.

### `CAnimationPoint(CPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.UInt32,System.UInt32,System.UInt64)`

ID: `M:CAnimationPoint.#ctor(CPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.UInt32,System.UInt32,System.UInt64)`

Constructs CAnimationPoint object.

Parameters:
- `ptDefault`: Specifies default point coordinates.
- `nGroupID`: Specifies Group ID.
- `nObjectID`: Specifies Object ID.
- `dwUserData`: Specifies user-defined data.

Remarks: Constructs CAnimationPoint object with specified properties.

### `AddTransition(CBaseTransition*,CBaseTransition*)`

ID: `M:CAnimationPoint.AddTransition(CBaseTransition*,CBaseTransition*)`

Adds transitions for X and Y coordinates.

Parameters:
- `pXTransition`: A pointer to transition for X coordinates.
- `pYTransition`: A pointer to transition for Y coordinate.

Remarks: Call this function to add the specified transitions to the internal list of transitions to be applied to animation variables for X and Y coordinates. When you add transitions, they are not applied immediately and stored in an internal list. Transitions are applied (added to a storyboard for a particular value) when you call CAnimationController::AnimateGroup. If you don't need to apply a transition to one of coordinates, you can pass NULL.

### `GetAnimationVariableList(CList<CAnimationVariable**,CAnimationVariable**>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CAnimationPoint.GetAnimationVariableList(CList<CAnimationVariable**,CAnimationVariable**>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Puts the encapsulated animation variables into a list.

Parameters:
- `lst`: When the function returns, it contains pointers to two CAnimationVariable objects representing the X and Y coordinates.

### `GetDefaultValue`

ID: `M:CAnimationPoint.GetDefaultValue`

Returns the default values for X and Y coordinates.

Returns: A point containing default value.

Remarks: Call this function to retrieve default value, which was previously set by constructor or SetDefaultValue.

### `GetValue(CPoint*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CAnimationPoint.GetValue(CPoint*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Returns current value.

Parameters:
- `ptValue`: Output. Contains the current value when this method returns.

Returns: TRUE, if the current value was successfully retrieved; otherwise FALSE.

Remarks: Call this function to retrieve the current value of animation point. If this method fails or underlying COM objects for X and Y coordinates have not been initialized, ptValue contains default value, which was previously set in constructor or by SetDefaultValue.

### `GetX`

ID: `M:CAnimationPoint.GetX`

Provides access to CAnimationVariable for X coordinate.

Returns: A reference to encapsulated CAnimationVariable representing X coordinate.

Remarks: You can call this method to get direct access to underlying CAnimationVariable representing X coordinate.

### `GetY`

ID: `M:CAnimationPoint.GetY`

Provides access to CAnimationVariable for Y coordinate.

Returns: A reference to encapsulated CAnimationVariable representing Y coordinate.

Remarks: You can call this method to get direct access to underlying CAnimationVariable representing Y coordinate.

### `SetDefaultValue(tagPOINT!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CAnimationPoint.SetDefaultValue(tagPOINT!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Sets default value.

Parameters:
- `ptDefault`: Specifies the default point value.

Remarks: Use this function to set a default value to animation object. This methods assigns default values to X and Y coordinates of animation point. It also recreates underlying COM objects if they have been created. If you subscribed this animation object to events (ValueChanged or IntegerValueChanged), you need to re-enable these events.

### `op_Assign(CPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CAnimationPoint.op_Assign(CPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Assigns ptSrc to CAnimationPoint.

Parameters:
- `ptSrc`: Refers to CPoint or POINT.

Remarks: Assigns ptSrc to CAnimationPoint. It's recommended to do that before animation start, because this operator calls SetDefaultValue, which recreates the underlying COM objects for X and Y coordinates if they have been created. If you subscribed this animation object to events (ValueChanged or IntegerValueChanged), you need to re-enable these events.

### `op_Implicit~CPoint`

ID: `M:CAnimationPoint.op_Implicit~CPoint`

Converts a CAnimationPoint to a CPoint.

Returns: Current value of CAnimationPoint as CPoint.

Remarks: This function internally calls GetValue. If GetValue for some reason fails, the returned point will contain default values for X and Y coordinates.

## Fields

### `m_xValue`

ID: `F:CAnimationPoint.m_xValue`

The encapsulated animation variable that represents X coordinate of animation point.

### `m_yValue`

ID: `F:CAnimationPoint.m_yValue`

The encapsulated animation variable that represents Y coordinate of animation point.
