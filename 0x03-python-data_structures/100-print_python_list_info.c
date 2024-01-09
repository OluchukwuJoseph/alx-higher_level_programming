#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Prints information about a Python list.
 * @p: A pointer to the PyObject representing the Python list.
 * Return: Nothin
 */
void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int j;

	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %Li\n", size);
	printf("[*] Allocated = %Li\n", obj->allocated);
	for (j = 0; j < size; j++)
		printf("Element %i: %s\n", PY_TYPE(obj->ob_item[i])->tp_name);
}
