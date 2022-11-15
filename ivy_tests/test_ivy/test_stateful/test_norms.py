"""Collection of tests for normalization layers."""

# global
from hypothesis import strategies as st

# local
import ivy
import ivy_tests.test_ivy.helpers as helpers
import ivy_tests.test_ivy.helpers.test_parameter_flags as pf
from ivy_tests.test_ivy.helpers import handle_method


@handle_method(
    method_tree="LayerNorm.__call__",
    dtype_and_x=helpers.dtype_and_values(available_dtypes=helpers.get_dtypes("float")),
    new_std=st.floats(min_value=0.0, max_value=1.0),
    init_with_v=st.booleans(),
    method_with_v=st.booleans(),
)
def test_layer_norm_layer(
    *,
    dtype_and_x,
    new_std,
    init_with_v,
    method_with_v,
    init_num_positional_args: pf.NumPositionalArg,
    method_as_variable: pf.AsVariableFlags,
    method_native_array: pf.NativeArrayFlags,
    method_container: pf.ContainerFlags,
    on_device,
    class_name,
    method_name
):
    input_dtype, x = dtype_and_x
    helpers.test_method(
        init_num_positional_args=init_num_positional_args,
        init_all_as_kwargs_np={
            "normalized_shape": x[0].shape,
            "epsilon": ivy._MIN_BASE,
            "elementwise_affine": True,
            "new_std": new_std,
            "device": on_device,
            "dtype": input_dtype[0],
        },
        method_input_dtypes=input_dtype,
        method_as_variable_flags=method_as_variable,
        method_num_positional_args=5,
        method_native_array_flags=method_native_array,
        method_container_flags=method_container,
        method_all_as_kwargs_np={"inputs": x[0]},
        class_name=class_name,
        method_name=method_name,
        init_with_v=init_with_v,
        method_with_v=method_with_v,
    )
