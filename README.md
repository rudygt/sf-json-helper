# sf-json-helper
helper lambda function for json to json transforms, useful to derive parameters in step function states

this lambda uses the python [jsonpath-ng](https://pypi.org/project/jsonpath-ng/) library to allow arbitrary json to json transforms from the input event and the lambda output. 

## Examples

derive a property using a simple string concatenation. any properties in the input data prefixed with "expression_" will be evaluated as jsonpath expressions and the piece after the underscore will be used as the new property name, 
so in this case the "expression_d" part will create a new property on the output with name "d" and the value for that property will be computed  using the jsonpath expression provided, in this case
'$.k + " constant string"'.

*Input*
```json
{
	"k": "v",
	"expression_d": "$.k + \" constant string\""	
}
```

*Output*
```json
{
	"d": "v constant string"	
}
```
