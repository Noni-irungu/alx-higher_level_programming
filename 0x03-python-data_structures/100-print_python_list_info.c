#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *py_List)
{
	long int list_size = PyList_Size(py_List);
	int index;
	PyListObject *List_obj = (PyListObject *)py_List;

	printf("[*] Size of the Python List = %li\n", list_size);
	printf("[*] Allocated = %li\n", List_obj->allocated);
	for (index = 0; index < list_size; index++)
		printf("Element %i: %s\n", index,
				Py_TYPE(List_obj->ob_item[index])->tp_name);
}
