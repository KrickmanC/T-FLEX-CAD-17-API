# CAnimationColor.op_Implicit~System.UInt32!System.Runtime.CompilerServices

Assembly: `TFlexCommandAPI`
Namespace: `CAnimationColor.op_Implicit~System.UInt32!System.Runtime`

## Methods

### `IsLong`

ID: `M:CAnimationColor.op_Implicit~System.UInt32!System.Runtime.CompilerServices.IsLong`

Converts a CAnimationColor to COLORREF.

Returns: Current value of animation color object as COLORREF.

Remarks: This function internally calls GetValue. If GetValue for some reason fails, the returned COLORREF will contain default values for all color components.
