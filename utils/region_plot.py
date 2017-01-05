def region_plot(feature, padding=50, limits=None):
    
    def _fcheck(rec):
        s = rec['TU'].replace('_', '-')
        return feature in s.split('-')
    
    vg = gff[gff['gene'] == feature][['start','end']].values
    vu = utr[utr.apply(_fcheck, axis=1)][['start','end']].values
    
    if limits is None:
        region = np.vstack((vg, vu))
        rmax = np.max(region)
        rmin = np.min(region)
        if padding is not None:
            rmax += padding
            rmin -= padding
        limits = (rmin, rmax)
    
    utrs = utr[utr.apply(_fcheck, axis=1)].copy()
    utrs['length'] = utrs['end'] - utrs['start']
    utrs.sort_values('length', ascending=False, inplace=True)
    
    utr_= utrs.iloc[0].to_frame().transpose()
    utr_['name'] = feature
    utr_['track'] = 'UTR'
    gene = gff[gff['gene'] == feature].copy()
    gene['track'] = 'gene'
    gene['name'] = feature
    
    genes = pd.concat([gene, utr_])
    genes['center'] = genes.start + (genes.end - genes.start) // 2
    genes['length'] = genes.end - genes.start

    p1 = strand_coverage(strands_nobcm, limits, "WT -BCM", genes)
    p2 = strand_coverage(strands_bcm, limits, "WT +BCM", genes)
    p = vplot(p1, p2)
    show(p)