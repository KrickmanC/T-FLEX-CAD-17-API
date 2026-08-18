# CAnimationValue.op_Implicit~System

Assembly: `TFlexAPI`
Namespace: `CAnimationValue`

## Methods

### `Double`

ID: `M:CAnimationValue.op_Implicit~System.Double`

Provides conversion between CAnimationValue and DOUBLE.

Returns: Current value of Animation Value.

Remarks: Provides conversion between CAnimationValue and DOUBLE. This method internally calls GetValue and doesn't check for errors. If GetValue fails, the returned value will contain a default value previously set in constructor or with SetDefaultValue.

### `Int32`

ID: `M:CAnimationValue.op_Implicit~System.Int32`

Provides conversion between CAnimationValue and INT32.

Returns: Current value of Animation Value as integer.

Remarks: Provides conversion between CAnimationValue and INT32. This method internally calls GetValue and doesn't check for errors. If GetValue fails, the returned value will contain a default value previously set in constructor or with SetDefaultValue.
