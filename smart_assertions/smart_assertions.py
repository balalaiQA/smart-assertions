import types
import inspect

failed_conditions = []


def soft_assert(assert_condition, message=None):
    global failed_conditions
    if isinstance(assert_condition, types.FunctionType):
        try:
            assert_condition()
        except AssertionError as error:
            add_exception(message if message else error)
    else:
        try:
            assert assert_condition
        except AssertionError:
            add_exception(message if message else 'Failed by assertion!')


def verify_expectations():
    global failed_conditions
    if failed_conditions:
        report_exceptions()


def add_exception(message=None):
    global failed_conditions
    (file_path, line, function_name) = inspect.stack()[2][1:4]
    failed_conditions.append('Exception: {}\nFail in "{}:{}" {}()\n'.format(message, file_path, line, function_name))


def report_exceptions():
    global failed_conditions
    if failed_conditions:
        report = ['Failed conditions count: [ {} ]\n'.format(len(failed_conditions))]
        for index, failure in enumerate(failed_conditions, start=1):
            if len(failed_conditions) > 1:
                report.append('{}. {}'.format(index, failure))
            else:
                report.append(failure)
        failed_conditions = []
        raise AssertionError('\n'.join(report))
