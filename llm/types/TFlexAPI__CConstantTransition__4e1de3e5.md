# CConstantTransition

Assembly: `TFlexAPI`

## Summary

Encapsulates a constant transition.

## Remarks

During a constant transition, the value of an animation variable remains at the initial value over the duration of the transition. Because all transitions are cleared automatically, it's recommended to allocated them using operator new. The encapsulated IUIAnimationTransition COM object is created by CAnimationController::AnimateGroup, until then it's NULL. Changing member variables after creation of this COM object has no effect.

## Constructors

### `CConstantTransition(System.Double)`

ID: `M:CConstantTransition.#ctor(System.Double)`

Constructs a transition object and initializes its duration.

Parameters:
- `duration`: The duration of the transition.

## Methods

### `CConstantTransition(System.Double)`

ID: `M:CConstantTransition.#ctor(System.Double)`

Constructs a transition object and initializes its duration.

Parameters:
- `duration`: The duration of the transition.

### `Create(IUIAnimationTransitionLibrary*,IUIAnimationTransitionFactory*)`

ID: `M:CConstantTransition.Create(IUIAnimationTransitionLibrary*,IUIAnimationTransitionFactory*)`

Calls the transition library to create encapsulated transition COM object.

Parameters:
- `pLibrary`: A pointer to transition library, which is responsible for creation of standard transitions.
- `pFactory`: A pointer to transition factory, which is responsible for creation of custom transitions.

Returns: TRUE if transition is created successfully; otherwise FALSE.

## Fields

### `m_duration`

ID: `F:CConstantTransition.m_duration`

The duration of the transition.
