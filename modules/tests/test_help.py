import modules

def test_help():
    assert('help' == modules.process_query('help')[0])
    assert('help' == modules.process_query('introduce yourself')[0])
    assert('help' == modules.process_query('What can you do?')[0])
    assert('help' != modules.process_query('something random')[0])

if __name__=='__main__':
    test_help()
