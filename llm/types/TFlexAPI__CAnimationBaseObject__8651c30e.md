# CAnimationBaseObject

Assembly: `TFlexAPI`

## Summary

The base class for all animation objects.

## Remarks

This class implements basic methods for all animation objects. An animation object can represent a value, point, size, rectangle or color in an application, as well as any custom entity. Animation objects are stored in animation groups (see CAnimationGroup). Each group can be animated separately and can be treated as an analogue of storyboard. An animation object encapsulates one or more animation variables (see CAnimationVariable), depending on its logical representation. For example, CAnimationRect contains four animation variables - one variable for each side of rectangle. Each animation object class exposes overloaded AddTransition method, which should be used to apply transitions to encapsulated animation variables. An animation object can be identified by Object ID (optionally) and by Group ID. A Group ID is necessary in order to place an animation object to correct group, but if a Group ID is not specified, an object is placed in the default group with ID 0. If you call SetID with different GroupID, an animation object will be moved to another group (a new group is created if necessary).

## Constructors

### `CAnimationBaseObject`

ID: `M:CAnimationBaseObject.#ctor`

Constructs an animation object.

Remarks: Constructs an animation objects and assigns default Object ID (0) and Group ID (0).

### `CAnimationBaseObject(System.UInt32,System.UInt32,System.UInt64)`

ID: `M:CAnimationBaseObject.#ctor(System.UInt32,System.UInt32,System.UInt64)`

Constructs an animation object.

Parameters:
- `nGroupID`: Specifies Group ID.
- `nObjectID`: Specifies Object ID.
- `dwUserData`: User-defined data, which can be associated with animation object and retrieved later at runtime.

Remarks: Constructs an animation object with specified Object ID and Group ID.

## Methods

### `CAnimationBaseObject`

ID: `M:CAnimationBaseObject.#ctor`

Constructs an animation object.

Remarks: Constructs an animation objects and assigns default Object ID (0) and Group ID (0).

### `CAnimationBaseObject(System.UInt32,System.UInt32,System.UInt64)`

ID: `M:CAnimationBaseObject.#ctor(System.UInt32,System.UInt32,System.UInt64)`

Constructs an animation object.

Parameters:
- `nGroupID`: Specifies Group ID.
- `nObjectID`: Specifies Object ID.
- `dwUserData`: User-defined data, which can be associated with animation object and retrieved later at runtime.

Remarks: Constructs an animation object with specified Object ID and Group ID.

### `ApplyTransitions(IUIAnimationStoryboard*,System.Int32)`

ID: `M:CAnimationBaseObject.ApplyTransitions(IUIAnimationStoryboard*,System.Int32)`

Adds transitions to storyboard with encapsulated animation variable.

Parameters:
- `pStoryboard`: A pointer to a storyboard.
- `bDependOnKeyframes`: With FALSE this method adds only those transitions that do not depend on keyframes.

Returns: TRUE if transitions were added successfully.

Remarks: Adds related transitions, that have been added with AddTransition (overloaded methods in derived classes), to storyboard.

### `ClearTransitions(System.Int32)`

ID: `M:CAnimationBaseObject.ClearTransitions(System.Int32)`

Removes all related transitions.

Parameters:
- `bAutodestroy`: Specifies whether to destroy transition objects automatically, or just remove them from the related list.

Remarks: Removes all related transitions and destroys them if bAutodestroy or m_bAutodestroyTransitions flag is TRUE. Transitions should be destroyed automatically only if they are not allocated on the stack. If the above flags are FALSE, transitions are just removed from the internal list of related transitions.

### `ContainsVariable(IUIAnimationVariable*)`

ID: `M:CAnimationBaseObject.ContainsVariable(IUIAnimationVariable*)`

Determines whether an animation object contains a particular animation variable.

Parameters:
- `pVariable`: A pointer to animation variable.

Returns: TRUE if the animation variable is contained in the animation object; otherwise FALSE.

Remarks: This method can be used to determine whether an animation variable specified by pVariable is contained within an animation object. An animation object, depending on its type, may contain several animation variables. For example, CAnimationColor contains three variables, one for each color component (red, green and blue). When a value of animation variable has changed, Windows Animation API sends ValueChanged or IntegerValueChanged events (if enabled), and the parameter of this event is a pointer to interface IUIAnimationVariable of animation variable. This method helps to obtain a pointer to animation from a pointer to contained COM object.

### `CreateTransitions`

ID: `M:CAnimationBaseObject.CreateTransitions`

Creates transitions associated with an animation object.

Returns: TRUE if transitions were created successfully; otherwise FALSE.

Remarks: Loops over list of animation variables encapsulated in a derived animation object and creates transitions associated with each animation variable.

### `DetachFromController`

ID: `M:CAnimationBaseObject.DetachFromController`

Detaches an animation object from parent animation controller.

Remarks: This method is used internally.

### `Dispose`

ID: `M:CAnimationBaseObject.Dispose`

The destructor. Called when an animation object is being destroyed.

### `EnableIntegerValueChangedEvent(CAnimationController*,System.Int32)`

ID: `M:CAnimationBaseObject.EnableIntegerValueChangedEvent(CAnimationController*,System.Int32)`

Sets up Integer Value Changed event handler.

Parameters:
- `pController`: A pointer to a parent controller.
- `bEnable`: Specifies whether to enable, or disable Integer Value Changed event.

Remarks: If the Integer Value Changed event handler is enabled, you can handle this event in CAnimationController::OnAnimationIntegerValueChanged method, which should be overridden in a CAnimationController-derived class. This method is called every time the animation integer value has changed.

### `EnableValueChangedEvent(CAnimationController*,System.Int32)`

ID: `M:CAnimationBaseObject.EnableValueChangedEvent(CAnimationController*,System.Int32)`

Sets up Value Changed event handler.

Parameters:
- `pController`: A pointer to a parent controller.
- `bEnable`: Specifies whether to enable, or disable Value Changed event.

Remarks: If the Value Changed event handler is enabled, you can handle this event in CAnimationController::OnAnimationValueChanged method, which should be overridden in a CAnimationController-derived class. This method is called every time the animation value has changed.

### `GetAnimationVariableList(CList<CAnimationVariable**,CAnimationVariable**>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:CAnimationBaseObject.GetAnimationVariableList(CList<CAnimationVariable**,CAnimationVariable**>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Collects pointers to contained animation variables.

Parameters:
- `lst`: A list that must be filled with animation variables contained in an animation object.

Remarks: This is a pure virtual method that must be overridden in a derived class. An animation object, depending on its type, contains one or more animation variables. For example, CAnimationPoint contains two variables, for X and Y coordinates respectively. The base class CAnimationBaseObject implements some generic methods, which act on a list of animation variables: ApplyTransitions, ClearTransitions, EnableValueChangedEvent, EnableIntegerValueChangedEvent. These methods call GetAnimationVariableList, which is filled in a derived class with actual animation variables contained in a particular animation object, then loop over the list and perform necessary actions. If you create a custom animation object, you must add to lst all animation variables contained in that object.

### `GetAutodestroyTransitions`

ID: `M:CAnimationBaseObject.GetAutodestroyTransitions`

Tells whether related transition are destroyed automatically.

Returns: If TRUE, related transitions are destroyed automatically; if FALSE, transition objects should be deallocated by calling application.

Remarks: By default this flag is TRUE. Set this flag only if you allocated transition on the stack and/or transitions should be deallocated by the calling application.

### `GetGroupID`

ID: `M:CAnimationBaseObject.GetGroupID`

Returns current Group ID.

Returns: Current Group ID.

Remarks: Use this method to retrieve Group ID. It's 0 if Group ID has not been set explicitly in constructor or with SetID.

### `GetObjectID`

ID: `M:CAnimationBaseObject.GetObjectID`

Returns current Object ID.

Returns: Current Object ID.

Remarks: Use this method to retrieve Object ID. It's 0 if Object ID has not been set explicitly in constructor or with SetID.

### `GetUserData`

ID: `M:CAnimationBaseObject.GetUserData`

Returns user defined data.

Returns: A value of custom data.

Remarks: Call this method to retrieve the custom data at runtime. The returned value will be 0 if it was not explicitly initialized in constructor or with SetUserData.

### `SetAutodestroyTransitions(System.Int32)`

ID: `M:CAnimationBaseObject.SetAutodestroyTransitions(System.Int32)`

Sets a flag that orders to automatically destroy transitions.

Parameters:
- `bValue`: Specifies the auto destroy flag.

Remarks: Set this flag only if you allocated transition objects using operator new. If for some reason transition objects are allocated on the stack, the auto destroy flag should be FALSE. By default this flag is TRUE.

### `SetID(System.UInt32,System.UInt32)`

ID: `M:CAnimationBaseObject.SetID(System.UInt32,System.UInt32)`

Sets new IDs.

Parameters:
- `nObjectID`: Specifies new Object ID.
- `nGroupID`: Specifies new Group ID.

Remarks: Allows to change Object ID and Group ID. If the new Group ID differs from the current ID, an animation object is moved to another group (a new group will be created, if necessary).

### `SetParentAnimationObjects`

ID: `M:CAnimationBaseObject.SetParentAnimationObjects`

Establishes relationship between animation variables, contained in an animation object, and their container.

Remarks: This is a helper that can be used to establish relationship between animation variables, contained in an animation object, and their container. It loops over animation variables and sets a back pointer to a parent animation object to each animation variable. In the current implementation the actual relationship is established in CAnimationBaseObject::ApplyTransitions, therefore back pointers are not set until you call CAnimationGroup::Animate. Knowing the relationship may be helpful when you processing events and need to get a parent animation object from CAnimationVariable (use CAnimationVariable::GetParentAnimationObject).

### `SetUserData(System.UInt64)`

ID: `M:CAnimationBaseObject.SetUserData(System.UInt64)`

Sets user-defined data.

Parameters:
- `dwUserData`: Specifies the custom data.

Remarks: Use this method to associate a custom data with an animation object. This data may be retrieved later at runtime by GetUserData.

## Fields

### `m_bAutodestroyTransitions`

ID: `F:CAnimationBaseObject.m_bAutodestroyTransitions`

Specifies whether related transitions should be automatically destroyed.

### `m_dwUserData`

ID: `F:CAnimationBaseObject.m_dwUserData`

Stores user-defined data.

### `m_nGroupID`

ID: `F:CAnimationBaseObject.m_nGroupID`

Specifies the Group ID of the animation object.

### `m_nObjectID`

ID: `F:CAnimationBaseObject.m_nObjectID`

Specifes the Object ID of the animation object.

### `m_pParentController`

ID: `F:CAnimationBaseObject.m_pParentController`

A pointer to the parent animation controller.
