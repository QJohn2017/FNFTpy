import sys, os

#
# https://meta.stackexchange.com/questions/272956/a-new-code-license-the-mit-this-time-with-attribution-required?cb=1
#


class HiddenPrints:
    #  Alexander Chzhen edited Jul 27 2018 at 20:02 https://stackoverflow.com/a/45669280
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')
    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout