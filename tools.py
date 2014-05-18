""" Set plot style """

import pylab as pl

__all__ = ['set_pub_single', 'set_ipynb', 'get_handle', 'myfigure',
            'hide_tick_labels', 'ImageWithColorbar', 'divide_axes',
            'plotdiff']

def set_pub_single():
    """set rc parameters for publication (single plot)"""

    ### TICKS
    tick_maj_size = 10
    tick_maj_pad  = 5
    tick_min_size = 5
    tick_min_pad  = 5
    tick_labelsize = 15
    tick_dict = {'major.size':tick_maj_size, 'major.pad':tick_maj_pad,
                 'minor.size':tick_min_size, 'minor.pad':tick_min_pad,
                 'labelsize':tick_labelsize}
    pl.rc('xtick', **tick_dict)
    pl.rc('ytick', **tick_dict)

    linewidth = 1
    axes_labelsize = 15

    ### AXES
    pl.rc('axes', lw=linewidth, labelsize=axes_labelsize)

    ### LINES
    pl.rc('lines', lw=linewidth, color='k', mew=linewidth) 

    pl.rc('legend', numpoints=1, scatterpoints=1, frameon=False)

    ### FIGURE
    pl.rc('figure.subplot', left=0.15, bottom=0.15, top=0.95, right=0.95)

    pl.rc('savefig', dpi=150)       # higher res outputs

    pl.rc('mathtext', default='regular')


def set_ipynb():
    """
    Set rc params for ipython notebook
    """
    ### TICKS
    tick_maj_size = 10
    tick_maj_pad  = 5
    tick_min_size = 5
    tick_min_pad  = 5
    tick_labelsize = 14
    tick_dict = {'major.size':tick_maj_size, 'major.pad':tick_maj_pad,
                 'minor.size':tick_min_size, 'minor.pad':tick_min_pad,
                 'labelsize':tick_labelsize}
    pl.rc('xtick', **tick_dict)
    pl.rc('ytick', **tick_dict)
    linewidth = 1
    axes_labelsize = 16
    ### AXES
    pl.rc('axes', lw=linewidth, labelsize=axes_labelsize)
    ### LINES
    pl.rc('lines', lw=linewidth, color='k', mew=linewidth) 
    pl.rc('legend', numpoints=1, scatterpoints=1, frameon=False)
    pl.rc('patch', edgecolor='None')
    ### FIGURE
    pl.rc('figure', figsize=(8,6))
    pl.rc('figure.subplot', left=0.15, bottom=0.15, top=0.95, right=0.95)

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
    """
    Hide axis tick labels
    
    ax : matplotlib Axes instance
    which : 'x' or 'y'
    """
    assert which in ['x', 'y']
    if which is 'x':
        pl.setp(ax.get_xticklabels(), visible=False)
    if which is 'y':
        pl.setp(ax.get_yticklabels(), visible=False)


def ImageWithColorbar(ax, image, **kwargs):
    """
    Plot image with colorbar on the right

    Parameters
    ------------
    ax : matplotlib Axes instance
    image : 2-d array
    Additional kwargs are passed to imshow

    Returns
    --------
    ax : image axes
    cb : colorbar axes
    """

    from mpl_toolkits.axes_grid1 import make_axes_locatable
    divider = make_axes_locatable(ax)
    ax_cb = divider.append_axes("right", size="5%", pad=0.05)
    fig1 = ax.get_figure()
    fig1.add_axes(ax_cb)

    dim = pl.atleast_1d(image.shape).astype('float')
    lim = dim - dim/2.
    extent = (-lim[0], lim[0], -lim[1], lim[1])

    im = ax.imshow(
        image,
        interpolation='nearest', origin='lower', extent=extent, **kwargs)
    ax.minorticks_on()

    cb = pl.colorbar(im, cax=ax_cb, orientation='vertical')
    ax_cb.xaxis.tick_bottom()

    return ax, cb


def divide_axes(ax, loc="bottom", size="30%", pad=0.05):
    """
    divide axes
    """
    from mpl_toolkits.axes_grid1 import make_axes_locatable
    divider = make_axes_locatable(ax)
    ax_sub = divider.append_axes(loc, size=size, pad=pad)
    return ax, ax_sub


def plotdiff(ax, x, y1, y2, ratio=False, **kwargs):
    """
    Plot difference y2-y1 or ratio y2/y1 in a subpanel
    """
    from mpl_toolkits.axes_grid1 import make_axes_locatable
    divider = make_axes_locatable(ax)
    ax_diff = divider.append_axes("bottom", size="30%", pad=0.05)
    ax.get_figure().add_axes(ax_diff)
    if ratio:
        ax_diff.plot(x, y2/y1, **kwargs)
    else:
        ax_diff.plot(x, y2-y1, **kwargs)
    return ax, ax_diff
