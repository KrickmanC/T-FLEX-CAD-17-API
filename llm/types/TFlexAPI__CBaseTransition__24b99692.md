# CBaseTransition

Assembly: `TFlexAPI`

## Summary

Represents a basic transition.

## Remarks

This class encapsulates IUIAnimationTransition interface and serves as a base class for all transitions.

## Constructors

### `CBaseTransition`

ID: `M:CBaseTransition.#ctor`

Constructs a base transtion object.

## Methods

### `CBaseTransition`

ID: `M:CBaseTransition.#ctor`

Constructs a base transtion object.

### `AddToStoryboard(IUIAnimationStoryboard*)`

ID: `M:CBaseTransition.AddToStoryboard(IUIAnimationStoryboard*)`

Adds a transition to a storyboard.

Parameters:
- `pStoryboard`: A pointer to storyboard, which will animate the related variable.

Returns: TRUE, if transition was successfully added to a storyboard.

Remarks: Applies the transition to the related variable in the storyboard. If this is the first transition applied to this variable in this storyboard, the transition begins at the start of the storyboard. Otherwise, the transition is appended to the transition added most recently to the variable.

### `AddToStoryboardAtKeyframes(IUIAnimationStoryboard*)`

ID: `M:CBaseTransition.AddToStoryboardAtKeyframes(IUIAnimationStoryboard*)`

Adds a transition to a storyboard.

Parameters:
- `pStoryboard`: A pointer to storyboard, which will animate the related variable.

Returns: TRUE, if transition was successfully added to a storyboard.

Remarks: Applies the transition to the related variable in the storyboard. If the start keyframe was specified, the transition begins at that keyframe. If the end keyframe was specified, the transition begins at the start keyframe and and stops at the end keyframe. If the transition was created with a duration parameter specified, that duration is overwritten with the duration of time between the start and end keyframes. If no keyframe was specified, the transition is appended to the transition added most recently to the variable.

### `Clear`

ID: `M:CBaseTransition.Clear`

Releases encapsulated IUIAnimationTransition COM object.

Remarks: This method should be called from a derived class's Create method in order to prevent IUITransition interface leak.

### `Create(IUIAnimationTransitionLibrary*,IUIAnimationTransitionFactory*)`

ID: `M:CBaseTransition.Create(IUIAnimationTransitionLibrary*,IUIAnimationTransitionFactory*)`

Creates a COM transition.

Parameters:
- `pLibrary`: A pointer to transition library, which creates standard transitions. It can be NULL for custom transitions.
- `pFactory`: A pointer to transition factory, which creates custom transitions. It can be NULL for standard transitions.

Returns: TRUE if a transition COM object was created successfully; otherwise FALSE.

Remarks: This is a pure virtual function that must be overridden in a derived class. It's called by the framework to instantiate the underlying COM transition object.

### `Dispose`

ID: `M:CBaseTransition.Dispose`

The destructor. Called when a transition object is being destroyed.

### `GetEndKeyframe`

ID: `M:CBaseTransition.GetEndKeyframe`

Returns start keyframe.

Returns: A valid pointer to a keyframe, or NULL if a transition should not be inserted between keyframes.

Remarks: This method can be used to access a keyframe object that was previously set by SetKeyframes. It's called by top level code when transitions are being added to storyboard.

### `GetRelatedVariable`

ID: `M:CBaseTransition.GetRelatedVariable`

Returns a pointer to related variable.

Returns: A valid pointer to animation variable, or NULL if an animation variable has not been set by SetRelatedVariable.

Remarks: This is an accessor to related animation variable.

### `GetStartKeyframe`

ID: `M:CBaseTransition.GetStartKeyframe`

Returns start keyframe.

Returns: A valid pointer to a keyframe, or NULL if a transition should not start after a keyframe.

Remarks: This method can be used to access a keyframe object that was previously set by SetKeyframes. It's called by top level code when transitions are being added to storyboard.

### `GetTransition`

ID: `M:CBaseTransition.GetTransition`

Returns a pointer to underlying COM transition object.

Returns: A valid pointer to IUIAnimationTransition or NULL if underlying transition can't be created.

Remarks: It's an accessor method to underlying COM transition object. It doesn't instantiates the underlying IUIAnimationTransition COM object if it wasn't created.

### `GetTransition(IUIAnimationTransitionLibrary*,IUIAnimationTransitionFactory*)`

ID: `M:CBaseTransition.GetTransition(IUIAnimationTransitionLibrary*,IUIAnimationTransitionFactory*)`

Returns a pointer to underlying COM transition object.

Parameters:
- `pLibrary`: A pointer to transition library, which creates standard transitions. It can be NULL for custom transitions.
- `pFactory`: A pointer to transition factory, which creates custom transitions. It can be NULL for standard transitions.

Returns: A valid pointer to IUIAnimationTransition or NULL if underlying transition can't be created.

Remarks: This method returns a pointer to underlying COM transition object and creates it if necessary.

### `GetType`

ID: `M:CBaseTransition.GetType`

Returns transition type.

Returns: One of TRANSITION_TYPE enumerated values.

Remarks: This method can be used to identify a transition object by its type. The type is set in a constructor in a derived class.

### `IsAdded`

ID: `M:CBaseTransition.IsAdded`

Tells whether a transition has been added to a storyboard.

Returns: Returns TRUE if a transition has been added to a storyboard, otherwise FALSE.

Remarks: This flag is set internally when the top level code adds transitions to storyboard.

### `SetKeyframes(CBaseKeyFrame*,CBaseKeyFrame*)`

ID: `M:CBaseTransition.SetKeyframes(CBaseKeyFrame*,CBaseKeyFrame*)`

Sets keyframes for a transition.

Parameters:
- `pStart`: A keyframe that specifies the beginning of the transition.
- `pEnd`: A keyframe that specifies the end of the transition.

Remarks: This method tells the transition to start after specified keyframe and, optionally, if pEnd is not NULL, end before the specified keyframe. If the transition was created with a duration parameter specified, that duration is overwritten with the duration of time between the start and end keyframes.

### `SetRelatedVariable(CAnimationVariable*)`

ID: `M:CBaseTransition.SetRelatedVariable(CAnimationVariable*)`

Establishes a relationship between animation variable and transition.

Parameters:
- `pVariable`: A pointer to related animation variable.

Remarks: Establishes a relationship between animation variable and transition. A transition can be applied only to one variable.

## Fields

### `m_bAdded`

ID: `F:CBaseTransition.m_bAdded`

Specifies whether a transition has been added to a storyboard.

### `m_pEndKeyframe`

ID: `F:CBaseTransition.m_pEndKeyframe`

Stores a pointer to the keyframe that specifies the end of the transition.

### `m_pRelatedVariable`

ID: `F:CBaseTransition.m_pRelatedVariable`

A pointer to an animation variable, which is animated with the transition stored in m_transition.

### `m_pStartKeyframe`

ID: `F:CBaseTransition.m_pStartKeyframe`

Stores a pointer to the keyframe that specifies the beginning of the transition.

### `m_transition`

ID: `F:CBaseTransition.m_transition`

Stores a pointer to IUIAnimationTransition. NULL if a COM transition object has not been created.

### `m_type`

ID: `F:CBaseTransition.m_type`

Stores the transition type.
