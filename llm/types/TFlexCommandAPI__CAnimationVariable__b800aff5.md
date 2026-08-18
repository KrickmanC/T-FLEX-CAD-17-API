# CAnimationVariable

Assembly: `TFlexCommandAPI`

## Summary

Represents an animation variable.

## Remarks

The CAnimationVariable class encapsulates IUIAnimationVariable COM object. It also holds a list of transitions to be applied to the animation variable in a storyboard. CAnimationVariable objects are embedded to animation objects, which can represent in an application an animated value, point, size, color and rectangle.

## Constructors

### `CAnimationVariable(System.Double)`

ID: `M:CAnimationVariable.#ctor(System.Double)`

Constructs an animation variable object.

Parameters:
- `dblDefaultValue`: Specifies the default value.

Remarks: Constructs an animation variable object and sets its default value. A default value is used when a variable is not animated, or can't be animated.

## Methods

### `CAnimationVariable(System.Double)`

ID: `M:CAnimationVariable.#ctor(System.Double)`

Constructs an animation variable object.

Parameters:
- `dblDefaultValue`: Specifies the default value.

Remarks: Constructs an animation variable object and sets its default value. A default value is used when a variable is not animated, or can't be animated.

### `AddTransition(CBaseTransition*)`

ID: `M:CAnimationVariable.AddTransition(CBaseTransition*)`

Adds a transition.

Parameters:
- `pTransition`: A pointer to a transition to add.

Remarks: This method is called to add a transition to the internal list of transitions to be applied to the animation variable. This list should be cleared when an animation has been scheduled.

### `ApplyTransitions(CAnimationController*,IUIAnimationStoryboard*,System.Int32)`

ID: `M:CAnimationVariable.ApplyTransitions(CAnimationController*,IUIAnimationStoryboard*,System.Int32)`

Adds transitions from the internal list to storyboard.

Parameters:
- `pController`: A pointer to parent animation controller.
- `pStoryboard`: A pointer to storyboard.
- `bDependOnKeyframes`: TRUE, if this method should add transitions that depend on keyframes.

Remarks: This method adds transitions from the internal list to storyboard. It's called from the top level code several times to add transitions that do not depend on keyframes and add transitions that depend on keyframes. If the underlying animation variable COM object has not been created, this method creates it at this stage.

### `ClearTransitions(System.Int32)`

ID: `M:CAnimationVariable.ClearTransitions(System.Int32)`

Clears transitions.

Parameters:
- `bAutodestroy`: Specifies whether this method should delete transition objects.

Remarks: This method removes all transitions from the internal list of transitions. If bAutodestroy is TRUE, or m_bAutodestroyTransitions is TRUE, then transitions are deleted. Otherwise the caller should deallocate the transition objects.

### `Create(IUIAnimationManager*)`

ID: `M:CAnimationVariable.Create(IUIAnimationManager*)`

Creates the underlying animation variable COM object.

Parameters:
- `pManager`: A pointer to animation manager.

Returns: TRUE if the animation variable was successfully created; otherwise FALSE.

Remarks: This method creates the underlying animation variable COM object and sets its default value.

### `CreateTransitions(IUIAnimationTransitionLibrary*,IUIAnimationTransitionFactory*)`

ID: `M:CAnimationVariable.CreateTransitions(IUIAnimationTransitionLibrary*,IUIAnimationTransitionFactory*)`

Creates all transitions to be applied to this animation variable.

Parameters:
- `pLibrary`: A pointer to transition library.
- `pFactory`: A pointer to transition factory.

Returns: TRUE if transitions were created successfully; otherwise FALSE.

Remarks: This method is called by the framework when it needs to create transitions that have been added to the variable's internal list of transitions.

### `Dispose`

ID: `M:CAnimationVariable.Dispose`

The destructor. Called when a CAnimationVariable object is being destroyed.

### `EnableIntegerValueChangedEvent(CAnimationController*,System.Int32)`

ID: `M:CAnimationVariable.EnableIntegerValueChangedEvent(CAnimationController*,System.Int32)`

Enables or disables the IntegerValueChanged event.

Parameters:
- `pController`: A pointer to parent controller.
- `bEnable`: TRUE - enable event, FALSE - disable event.

Remarks: When ValueChanged event is enabled, the framework calls virtual method CAnimationController::OnAnimationIntegerValueChanged. You need to override it in a class derived from CAnimationController in order to process this event. This method is called every time the integer value of animation variable is changed.

### `EnableValueChangedEvent(CAnimationController*,System.Int32)`

ID: `M:CAnimationVariable.EnableValueChangedEvent(CAnimationController*,System.Int32)`

Enables or disables the ValueChanged event.

Parameters:
- `pController`: A pointer to parent controller.
- `bEnable`: TRUE - enable event, FALSE - disable event.

Remarks: When ValueChanged event is enabled, the framework calls virtual method CAnimationController::OnAnimationValueChanged. You need to override it in a class derived from CAnimationController in order to process this event. This method is called every time the value of animation variable is changed.

### `GetDefaultValue`

ID: `M:CAnimationVariable.GetDefaultValue`

Returns default value.

Returns: The default value.

Remarks: Use this function to obtain default value of animation variable. The default value can be set in constructor or by SetDefaultValue method.

### `GetParentAnimationObject`

ID: `M:CAnimationVariable.GetParentAnimationObject`

Returns the parent animation object.

Returns: A pointer to parent animation object, if relationship was established, otherwise NULL.

Remarks: This method can be called to retrieve a pointer to a parent animation object (a container).

### `GetValue(System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CAnimationVariable.GetValue(System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Returns the current value of animation variable.

Parameters:
- `dblValue`: The current value of the animation variable.

Returns: S_OK if the value was obtained successfully, or underlying animation variable has not been created. Otherwise HRESULT error code.

Remarks: This method can be called to retrieve the current value of animation variable. If the underlying COM object has not been created, dblValue will contain a default value, when the function returns.

### `GetValue(System.Int32*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CAnimationVariable.GetValue(System.Int32*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Returns the current value of animation variable.

Parameters:
- `nValue`: The current value of the animation variable.

Returns: S_OK if the value was obtained successfully, or underlying animation variable has not been created. Otherwise HRESULT error code.

Remarks: This method can be called to retrieve the current value of animation variable. If the underlying COM object has not been created, dblValue will contain a default value, when the function returns.

### `GetVariable`

ID: `M:CAnimationVariable.GetVariable`

Returns a pointer to IUIAnimationVariable COM object.

Returns: A valid pointer to IUIAnimationVariable COM object, or NULL if animation variable was not created, or can't be created.

Remarks: Use this function to access the underlying IUIAnimationVariable COM object and call its methods directly if needed.

### `SetDefaultValue(System.Double)`

ID: `M:CAnimationVariable.SetDefaultValue(System.Double)`

Sets default value and releases IUIAnimationVariable COM object.

Parameters:
- `dblDefaultValue`: Specifies the new default value.

Remarks: Use this method to reset the default value. This method releases the internal IUIAnimationVariable COM object, therefore when animation variable is recreated, the underlying COM object gets the new default value. The default value is returned by GetValue if the COM object representing the animation variable is not created, or if the variable has not been animated.

### `SetParentAnimationObject(CAnimationBaseObject*)`

ID: `M:CAnimationVariable.SetParentAnimationObject(CAnimationBaseObject*)`

Sets the relationship between an animation variable and an animation object.

Parameters:
- `pParentObject`: A pointer to an animation object that contains this variable.

Remarks: This method is called internally to establish one-to-one relationship between an animation variable and an animation object that encapsulates it.

## Fields

### `m_bAutodestroyTransitions`

ID: `F:CAnimationVariable.m_bAutodestroyTransitions`

Specifies whether related transition objects should be deleted.

Remarks: Set this value to TRUE to force deletion of transition objects when they are being removed from the internal list of transitions. If this value is FALSE the transitions should be deleted by calling application. The list of transitions is always cleared after an animation has been scheduled. The default value is FALSE.

### `m_dblDefaultValue`

ID: `F:CAnimationVariable.m_dblDefaultValue`

Specifies the default value, which is propagated to IUIAnimationVariable.

### `m_lstTransitions`

ID: `F:CAnimationVariable.m_lstTransitions`

Contains a list of transitions that animate this animation variable.

### `m_pParentObject`

ID: `F:CAnimationVariable.m_pParentObject`

A pointer to an animation object that encapsulates this animation variable.

### `m_variable`

ID: `F:CAnimationVariable.m_variable`

Stores a pointer to IUIAnimationVariable COM object. NULL if the COM object has not been created yet, or if creation failed.
