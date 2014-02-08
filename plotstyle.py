""" Set plot style """


import pylab as pl


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


def set_interactive():
    import pylab as pl

    """set rc parameters for interactive plotting"""

    ### FONTS
    #font_dict = {'family':'Time New Roman'}  # Serif font
    font_dict = {'family':'Trebuchet MS', 'size':20}  # Sans-Serif font
    pl.rc('font', **font_dict)


    ### TICKS
    tick_maj_size = 10
    tick_maj_pad  = 8

    tick_min_size = 5
    tick_min_pad  = 8

    tick_labelsize = 20


    tick_dict = {'major.size':tick_maj_size, 'major.pad':tick_maj_pad,
                 'minor.size':tick_min_size, 'minor.pad':tick_min_pad,
                 'labelsize':tick_labelsize}

    pl.rc('xtick', **tick_dict)
    pl.rc('ytick', **tick_dict)

    linewidth = 2
    axes_labelsize = 20

    ### AXES
    pl.rc('axes', lw=linewidth, labelsize=axes_labelsize)

    ### LINES
    pl.rc('lines', lw=linewidth, color='k', mew=linewidth) 
    pl.rc('patch', lw=linewidth)

    ### FIGURE
    pl.rc('figure', facecolor='w', figsize=(8, 6))


    pl.rc('mathtext', default='regular')

def get_handle(**kwargs):
    handle = pl.Line2D(range(0), range(0), **kwargs)
    return handle


def test_set_interactive():

    x = arange(0., 10, 0.1)
    y = sin(x)

    set_pub_single()
    plot(x, y)
    show()
    

if __name__ == '__main__':
    test_set_interactive()
