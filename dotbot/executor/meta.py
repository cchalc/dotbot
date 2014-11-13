from . import Executor

class Meta(Executor):
    '''
    Prints of metadata about a task
    '''

    _directive = 'meta'

    def can_handle(self, directive):
        return directive == self._directive

    def handle(self, directive, data):
        if directive != self._directive:
            raise ValueError('Meta cannot handle directive %s' % directive)

        print("")
        for key in data:
            if key == 'title':
                self._log.warning(data[key])
            elif key == 'description':
                self._log.info("  " + data[key])

        return True
