import matplotlib.pyplot as plt
from matplotlib import cm
import math

def plot_utr_heatmap(data, cmap=cm.OrRd, ylim=[1750, 1500], orientation='vertical'):
    from mpl_toolkits.axes_grid1 import make_axes_locatable
    utr = data[0].copy()
    utr.sort(axis=0)
    max_val = np.max(utr)
    midpoint = math.ceil(max_val / 2)
    fig, ax = plt.subplots(figsize=(18,18))
    im = ax.imshow(utr,cmap=cmap)
    ax.set_title("Read depth at 5'UTR", fontsize=20)
    ax.set_ylim(ylim)
    ax.set_xlabel('Position from TSS', fontsize=20)
    ax.get_yaxis().set_ticks([])
    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(20)
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.05)
    cbar = fig.colorbar(im, cax=cax, ticks=[0,midpoint,max_val], orientation=orientation)
    cbar.ax.invert_yaxis()
    cbar.ax.set_xticklabels(['0', '{0}'.format(int(midpoint)), '{0}'.format(int(max_val))], fontsize=20)
    plt.show()


def plot_strand_coverage(bamfiles, reference, region):
    '''
    Plots coverage by strand for the given bamfiles, reference and region

    `bamfiles`: dictionary of the form {'plus': <filename>, 'minus': <filename>}
        where filename refers to the corresponding bamfile (strand-split)

    `reference`: reference, as specified in the bamfile header

    `region`: tuple (min, max) of the positions that define the region
    '''
    cov = []
    for strand,filename in bamfiles.iteritems():
        bamfile = pysam.AlignmentFile(filename, 'rb')
        start,end = region
        pileup = bamfile.pileup(reference, start, end)
        for col in pileup:
            cov.append((col.reference_pos, col.n, strand))
    df = pd.DataFrame.from_records(cov, columns=('position', 'coverage', 'strand'))
    df['coverage'] = np.where(df['strand'] == 'minus', -1*df['coverage'], df['coverage'])
    ymin = df['coverage'].min()
    ymax = df['coverage'].max()
    ylim = max(abs(ymin), abs(ymax))
    p = ggplot(df, aes(x='position', ymin=0, ymax='coverage', fill='strand')) \
            + geom_area(alpha=0.4) \
            + scale_x_continuous(name='position') \
            + scale_y_continuous(name='Coverage', limits=(-1*ylim, ylim))
    print p
