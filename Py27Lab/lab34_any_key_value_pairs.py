def sample_key_value_arguments(fix1, fix2, **kargs):
    print "fix part=%s,%s" % (str(fix1), str(fix2))
    for k,v in kargs.items():
        print 'parameter=%s, value=%s' % (k, v)


sample_key_value_arguments("hello", 'world',
                           course_name='python in action',
                           duration='16hr',
                           instructor='Mark')
l4 = {'name': 'python in action', 'duration': '16hr'}
sample_key_value_arguments("hello", "dict", **l4)
