""" Set plot style """

import pylab as pl

__all__ = ['set_pub_single', 'get_handle', 'myfigure', 'hide_tick_labels']

def set_pub_single():
    """set rc parameters for publication (single plot)"""

    ### FONTS
    font_dict = {'family':'Times New Roman'}  # Serif font
    # font_dict = {'family':'Trebuchet MS'}  # Sans-Serif font
    pl.rc('font', **font_dict)


    ### TICKS
    tick_maj_size = 10
    tick_maj_pad  = 5

    tick_min_size = 5
    tick_min_pad  = 5

    tick_labelsize = 20


    tick_dict = {'major.size':tick_maj_size, 'major.pad':tick_maj_pad,
                 'minor.size':tick_min_size, 'minor.pad':tick_min_pad,
                 'labelsize':tick_labelsize}

    pl.rc('xtick', **tick_dict)
    pl.rc('ytick', **tick_dict)

    linewidth = 1
    axes_labelsize = 20

    ### AXES
    pl.rc('axes', lw=linewidth, labelsize=axes_labelsize)

    ### LINES
    pl.rc('lines', lw=linewidth, color='k', mew=linewidth) 

    ### FIGURE
    # pl.rc('figure', facecolor='w', figsize=(4, 3))

    pl.rc('savefig', dpi=150)       # higher res outputs

    pl.rc('mathtext', default='regular')


def get_handle(**kwargs):
    handle = pl.Line2D(range(0), range(0), **kwargs)
    return handle


def myfigure(plotting):
    """ my figure decorator """
    def wrapper(*args, **kwargs):
        config = {}
        for k in ['savename']:
            if kwargs.has_key(k):
                config[k] = kwargs.pop(k)
        plotting(*args, **kwargs)
        if config.has_key('savename'):
            savename = config.pop('savename')
            savefig(savename)
            print savename, 'saved'
            close()
    return wrapper


def hide_tick_labels(ax, which):
    """ Hide *which*-axis tick labels in ax axis instance """

    assert which in ['x', 'y']
    if which is 'x':
        pl.setp(ax.get_xticklabels(), visible=False)
    if which is 'y':
        pl.setp(ax.get_yticklabels(), visible=False)