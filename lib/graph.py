import pylab
import collections
import time

class RGraph(object):

    data = collections.defaultdict(int)
    for hour in xrange(24):
        data[str(hour)]

    @classmethod
    def compute_graph(cls, page_data):
        out = time.asctime(time.localtime(page_data['data']['created_utc']))
        out = out.split(' ')
        if len(out) > 5:
            out = out[4][:-6]
        else:
            out = out[3][:-6]
        if out[0] == '0':
            out = out[1:]
        cls.data[out] += 1

    @classmethod
    def show_graph(cls):
        fig = pylab.figure()
        ax = fig.add_subplot(1,1,1)
        y = [i for i in cls.data.values()]
        ind = range(len(y))
        ax.bar(ind, y, align='center')
        ax.set_ylabel('Posts')
        ax.set_title('Posts / hour', fontstyle='italic')
        ax.set_xticks(ind)
        ax.set_xticklabels = (["%d O'clock" % i for i in range(24)])
        pylab.show()
