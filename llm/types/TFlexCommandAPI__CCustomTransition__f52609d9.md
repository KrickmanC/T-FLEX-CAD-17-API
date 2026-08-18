# CCustomTransition

Assembly: `TFlexCommandAPI`

## Summary

Implements custom transition.

## Remarks

The CCustomTransitions class allows developers to implement custom transitions. It's created and used as a standard transition, but its constructor accepts as parameter a pointer to a custom interpolator. Perform the following steps to use custom transitions: 1. Derive a class from CCustomInterpolator and implement at least InterpolateValue method. 2. Ensure that the lifetime of custom interpolator object must be longer than duration of animation where it's used. 3. Instantiate (using operator new) a CCustomTransition object and pass a pointer to custom interpolator in the constructor. 4. Call CCustomTransition::SetInitialValue and CCustomTransition::SetInitialVelocity if these parameters are required for custom interpolation. 5. Pass the pointer to custom transition to AddTransition method of animation object, whose value should be animated with the custom algorithm. 6. When the value of animation object should change Windows Animation API will call InterpolateValue (and other relevant methods) in CCustomInterpolator.

## Constructors

### `CCustomTransition(CCustomInterpolator*)`

ID: `M:CCustomTransition.#ctor(CCustomInterpolator*)`

Constructs a custom transition object.

Parameters:
- `pInterpolator`: A pointer to custom interpolator.

## Methods

### `CCustomTransition(CCustomInterpolator*)`

ID: `M:CCustomTransition.#ctor(CCustomInterpolator*)`

Constructs a custom transition object.

Parameters:
- `pInterpolator`: A pointer to custom interpolator.

### `Create(IUIAnimationTransitionLibrary*,IUIAnimationTransitionFactory*)`

ID: `M:CCustomTransition.Create(IUIAnimationTransitionLibrary*,IUIAnimationTransitionFactory*)`

Calls the transition library to create encapsulated transition COM object.

Parameters:
- `pLibrary`: A pointer to transition library, which is responsible for creation of standard transitions.
- `pFactory`: A pointer to transition factory, which is responsible for creation of custom transitions.

Remarks: This method also can set initial value and initial velocity to be applied to an animation variable, which is associated with this transition. For this purpose you have to call SetInitialValue and SetInitialVelocity before the framework creates the encapsulated transition COM object (it happens when you call CAnimationController::AnimateGroup).

### `SetInitialValue(System.Double)`

ID: `M:CCustomTransition.SetInitialValue(System.Double)`

Sets an initial value, which will be applied to an animation variable associated with this transition.

### `SetInitialVelocity(System.Double)`

ID: `M:CCustomTransition.SetInitialVelocity(System.Double)`

Sets an initial velocity, which will be applied to an animation variable associated with this transition.

## Fields

### `m_bInitialValueSpecified`

ID: `F:CCustomTransition.m_bInitialValueSpecified`

Specifies whether the initial value was specified with SetInitialValue.

### `m_bInitialVelocitySpecified`

ID: `F:CCustomTransition.m_bInitialVelocitySpecified`

Specifies whether the initial velocity was specified with SetInitialVelocity.

### `m_initialValue`

ID: `F:CCustomTransition.m_initialValue`

Stores the initial value.

### `m_initialVelocity`

ID: `F:CCustomTransition.m_initialVelocity`

Stores the initial velocity.

### `m_pInterpolator`

ID: `F:CCustomTransition.m_pInterpolator`

Stores a pointer to a custom interpolator.
