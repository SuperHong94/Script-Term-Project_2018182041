#include "python.h" 
#include <string>
static PyObject*

queryCode(PyObject* self, PyObject* args)
{
	using namespace std;
	const char* str = NULL;
	int len = 0;

	
	if (!PyArg_ParseTuple(args, "s", &str)) // 매개변수 값을 분석하고 지역변수에 할당 시킵니다.
		return NULL;

	if (strcmp(str,"Gapyeong")==0)
		return Py_BuildValue("i", 41820);

	else if (strcmp(str, "Goyang") == 0)
		return Py_BuildValue("i", 41280);

	else if (strcmp(str, "Gwacheon") == 0)
		return Py_BuildValue("i", 41290);

	else if (strcmp(str, "Gwangmyeong") == 0)
		return Py_BuildValue("i", 41210);
	else if (strcmp(str, "Gwangmyeong") == 0)
		return Py_BuildValue("i", 41210);

	else if (strcmp(str, "Gwangju") == 0)
		return Py_BuildValue("i", 41610);

	else if (strcmp(str, "Guri") == 0)
		return Py_BuildValue("i", 41310);

	else if (strcmp(str, "Gunpo") == 0)
		return Py_BuildValue("i", 41410);

	else if (strcmp(str, "Gimpo") == 0)
		return Py_BuildValue("i", 41570);

	else if (strcmp(str, "Namyangju") == 0)
		return Py_BuildValue("i", 41360);

	else if (strcmp(str, "Dongducheon") == 0)
		return Py_BuildValue("i", 41250);

	else if (strcmp(str, "Bucheon") == 0)
		return Py_BuildValue("i", 41190);

	else if (strcmp(str, "Seongnam") == 0)
		return Py_BuildValue("i", 41130);

	else if (strcmp(str, "Suwon") == 0)
		return Py_BuildValue("i", 41110);

	else if (strcmp(str, "Siheung") == 0)
		return Py_BuildValue("i", 41390);

	else if (strcmp(str, "Ansan") == 0)
		return Py_BuildValue("i", 41270);

	else if (strcmp(str, "Anseong") == 0)
		return Py_BuildValue("i", 41550);

	else if (strcmp(str, "Anyang") == 0)
		return Py_BuildValue("i", 41170);

	else if (strcmp(str, "Yangju") == 0)
		return Py_BuildValue("i", 41630);

	else if (strcmp(str, "Yangpyeong") == 0)
		return Py_BuildValue("i", 41830);

	else if (strcmp(str, "Yeoju") == 0)
		return Py_BuildValue("i", 41670);

	else if (strcmp(str, "Yeoncheon") == 0)
		return Py_BuildValue("i", 41800);

	else if (strcmp(str, "Osan") == 0)
		return Py_BuildValue("i", 41370);

	else if (strcmp(str, "Yongin") == 0)
		return Py_BuildValue("i", 41460);

	else if (strcmp(str, "Uiwang") == 0)
		return Py_BuildValue("i", 41430);

	else if (strcmp(str, "Uijeongbu") == 0)
		return Py_BuildValue("i", 41150);

	else if (strcmp(str, "Icheon") == 0)
		return Py_BuildValue("i", 41500);

	else if (strcmp(str, "Paju") == 0)
		return Py_BuildValue("i", 41480);

	else if (strcmp(str, "Pyeongtaek") == 0)
		return Py_BuildValue("i", 41220);

	else if (strcmp(str, "Pocheon") == 0)
		return Py_BuildValue("i", 41650);

	else if (strcmp(str, "Hanam") == 0)
		return Py_BuildValue("i", 41450);

	else if (strcmp(str, "Hwaseong") == 0)
		return Py_BuildValue("i", 41590);
	else
		return Py_BuildValue("i", 12);

}

static PyMethodDef SpamMethods[] = {
	{ "queryCode", queryCode, METH_VARARGS,
	"count a string length." },
	{ NULL, NULL, 0, NULL } // 배열의 끝을 나타냅니다.
};

static struct PyModuleDef spammodule = {
	PyModuleDef_HEAD_INIT,
	"spam",            // 모듈 이름
	"It is test module.", // 모듈 설명을 적는 부분, 모듈의 __doc__에 저장됩니다.
	-1,SpamMethods
};

PyMODINIT_FUNC
PyInit_spam(void)
{
	return PyModule_Create(&spammodule);
}
