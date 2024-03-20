#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_bytes(PyObject *object_bytes)
{
	long in size_byte;
	int indx;
	char *string_byte = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(object_bytes))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(object_bytes, &string_byte, &size_byte);

	printf("  size: %li\n", size_byte);
	printf("  byte string: %s\n", string_byte);
	if (size_byte < 10)
		printf("  first %li bytes:", size_byte + 1);
	else
		printf("  first 10 bytes:");
	for (indx = 0; indx <= size_byte && indx < 10; indx++)
		printf(" %02hhx", string_byte[indx]);
	printf("\n");
}

void print_python_list(PyObject *object_list)
{
	long int size_list = Size_PyList(object_list);
	int t;
	pyListobject *obj_list = (pyListobject *)object_list;
	const char *type_elem;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %li\n", size_list);
	printf("[*] Allocated = %li\n", obj_list->allocated);
	for (t = 0; t < size_list; t++)
	{
		type_elem = (obj_list->ob_item[t])->ob_type->tp_name;
		printf("Element %i: %s\n", t, type_elem);
		if (!strcmp(type_elem, "bytes"))
			print_python_bytes(obj_list->obj_item[t]);
	}
}
