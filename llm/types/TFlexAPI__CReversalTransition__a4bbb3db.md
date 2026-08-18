# CReversalTransition

Assembly: `TFlexAPI`

## Summary

Encapsulates a reversal transition.

## Remarks

A reversal transition smoothly changes direction over a given duration. The final value will be the same as the initial value and the final velocity will be the negative of the initial velocity. Because all transitions are cleared automatically, it's recommended to allocated them using operator new. The encapsulated IUIAnimationTransition COM object is created by CAnimationController::AnimateGroup, until then it's NULL. Changing member variables after creation of this COM object has no effect.

## Constructors

### `CReversalTransition(System.Double)`

ID: `M:CReversalTransition.#ctor(System.Double)`

Constructs a reversal transition object and initializes its duration.

Parameters:
- `duration`: The duration of the transition.

## Methods

### `CReversalTransition(System.Double)`

ID: `M:CReversalTransition.#ctor(System.Double)`

Constructs a reversal transition object and initializes its duration.

Parameters:
- `duration`: The duration of the transition.

### `Create(IUIAnimationTransitionLibrary*,IUIAnimationTransitionFactory*)`

ID: `M:CReversalTransition.Create(IUIAnimationTransitionLibrary*,IUIAnimationTransitionFactory*)`

Calls the transition library to create encapsulated transition COM object.

Parameters:
- `pLibrary`: A pointer to transition library, which is responsible for creation of standard transitions.
- `pFactory`: A pointer to transition factory, which is responsible for creation of custom transitions.

Returns: TRUE if transition is created successfully; otherwise FALSE.

## Fields

### `m_duration`

ID: `F:CReversalTransition.m_duration`

The duration of the transition.
