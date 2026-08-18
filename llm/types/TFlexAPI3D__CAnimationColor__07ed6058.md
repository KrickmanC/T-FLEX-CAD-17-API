# CAnimationColor

Assembly: `TFlexAPI3D`

## Summary

Implements the functionality of a color whose red, green and blue components can be animated.

## Remarks

The CAnimationColor class encapsulates three CAnimationVariable objects and can represent in applications a color. For example, you can use this class to animate colors of any object on the screen (like text color, background color etc). To use this class in application, just instantiate an object of this class, add it to animation controller using CAnimationController::AddAnimationObject and call AddTransition for each transition to be applied to Red, Green and Blue components.

## Constructors

### `CAnimationColor`

ID: `M:CAnimationColor.#ctor`

Constructs a CAnimationColor object.

Remarks: The object is constructed with default values for red, green, blue, Object ID and Group ID, which will be set to 0. They can be changed later at runtime using SetDefaultValue and SetID.

### `CAnimationColor(System.UInt32!System.Runtime.CompilerServices.IsLong,System.UInt32,System.UInt32,System.UInt64)`

ID: `M:CAnimationColor.#ctor(System.UInt32!System.Runtime.CompilerServices.IsLong,System.UInt32,System.UInt32,System.UInt64)`

Constructs an animation color object.

Parameters:
- `color`: Specifies default color.
- `nGroupID`: Specifies Group ID.
- `nObjectID`: Specifies Object ID.
- `dwUserData`: Specifies user-defined data.

Remarks: The object is constructed with specified values for RGB components, Object ID and Group ID. They can be changed later at runtime using SetDefaultValue and SetID.

## Methods

### `CAnimationColor`

ID: `M:CAnimationColor.#ctor`

Constructs a CAnimationColor object.

Remarks: The object is constructed with default values for red, green, blue, Object ID and Group ID, which will be set to 0. They can be changed later at runtime using SetDefaultValue and SetID.

### `CAnimationColor(System.UInt32!System.Runtime.CompilerServices.IsLong,System.UInt32,System.UInt32,System.UInt64)`

ID: `M:CAnimationColor.#ctor(System.UInt32!System.Runtime.CompilerServices.IsLong,System.UInt32,System.UInt32,System.UInt64)`

Constructs an animation color object.

Parameters:
- `color`: Specifies default color.
- `nGroupID`: Specifies Group ID.
- `nObjectID`: Specifies Object ID.
- `dwUserData`: Specifies user-defined data.

Remarks: The object is constructed with specified values for RGB components, Object ID and Group ID. They can be changed later at runtime using SetDefaultValue and SetID.

### `AddTransition(CBaseTransition*,CBaseTransition*,CBaseTransition*)`

ID: `M:CAnimationColor.AddTransition(CBaseTransition*,CBaseTransition*,CBaseTransition*)`

Adds transitions for Red, Green and Blue components.

Parameters:
- `pRTransition`: Transition for Red component.
- `pGTransition`: Transition for Green component.
- `pBTransition`: Transition for Blue component.

Remarks: Call this function to add the specified transitions to the internal list of transitions to be applied to animation variables representing color components. When you add transitions, they are not applied immediately and stored in an internal list. Transitions are applied (added to a storyboard for a particular value) when you call CAnimationController::AnimateGroup. If you don't need to apply a transition to one of the color components, you can pass NULL.

### `GetAnimationVariableList(CList<CAnimationVariable**,CAnimationVariable**>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CAnimationColor.GetAnimationVariableList(CList<CAnimationVariable**,CAnimationVariable**>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Puts the encapsulated animation variables into a list.

Parameters:
- `lst`: When the function returns, it contains pointers to three CAnimationVariable objects representing red, green and blue components.

### `GetB`

ID: `M:CAnimationColor.GetB`

Provides access to CAnimationVariable representing Blue component.

Returns: A reference to encapsulated CAnimationVariable representing Blue component.

Remarks: You can call this method to get direct access to underlying CAnimationVariable representing Blue component.

### `GetDefaultValue`

ID: `M:CAnimationColor.GetDefaultValue`

Returns the default values for color components.

Returns: A COLORREF value containing defaults for RGB components.

Remarks: Call this function to retrieve default value, which was previously set by constructor or SetDefaultValue.

### `GetG`

ID: `M:CAnimationColor.GetG`

Provides access to CAnimationVariable representing Green component.

Returns: A reference to encapsulated CAnimationVariable representing Green component.

Remarks: You can call this method to get direct access to underlying CAnimationVariable representing Green component.

### `GetR`

ID: `M:CAnimationColor.GetR`

Provides access to CAnimationVariable representing Red component.

Returns: A reference to encapsulated CAnimationVariable representing Red component.

Remarks: You can call this method to get direct access to underlying CAnimationVariable representing Red component.

### `GetValue(System.UInt32!System.Runtime.CompilerServices.IsLong*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CAnimationColor.GetValue(System.UInt32!System.Runtime.CompilerServices.IsLong*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Returns current value.

Parameters:
- `color`: Output. Contains the current value when this method returns.

Returns: TRUE, if the current value was successfully retrieved; otherwise FALSE.

Remarks: Call this function to retrieve the current value of animation color. If this method fails or underlying COM objects for color components have not been initialized, color contains default value, which was previously set in constructor or by SetDefaultValue.

### `SetDefaultValue(System.UInt32!System.Runtime.CompilerServices.IsLong)`

ID: `M:CAnimationColor.SetDefaultValue(System.UInt32!System.Runtime.CompilerServices.IsLong)`

Sets default value.

Parameters:
- `color`: Specifies new default values for red, green and blue components.

Remarks: Use this function to set a default value to animation object. This methods assigns default values to color components of animation color. It also recreates underlying COM objects if they have been created. If you subscribed this animation object to events (ValueChanged or IntegerValueChanged), you need to re-enable these events.

### `op_Assign(System.UInt32!System.Runtime.CompilerServices.IsLong)`

ID: `M:CAnimationColor.op_Assign(System.UInt32!System.Runtime.CompilerServices.IsLong)`

Assigns color to CAnimationColor.

Parameters:
- `color`: Specifies new value Animation Color.

Remarks: It's recommended to do that before animation start, because this operator calls SetDefaultValue, which recreates the underlying COM objects for color components if they have been created. If you subscribed this animation object to events (ValueChanged or IntegerValueChanged), you need to re-enable these events.

## Fields

### `m_bValue`

ID: `F:CAnimationColor.m_bValue`

The encapsulated animation variable that represents Blue component of animation color.

### `m_gValue`

ID: `F:CAnimationColor.m_gValue`

The encapsulated animation variable that represents Green component of animation color.

### `m_rValue`

ID: `F:CAnimationColor.m_rValue`

The encapsulated animation variable that represents Red component of animation color.
