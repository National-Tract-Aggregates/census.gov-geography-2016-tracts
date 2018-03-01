
def extract_tracts(resource, doc, *args, **kwargs):

    from operator import itemgetter

    geo_r = doc.reference('geography_file').resolved_url.get_resource()

    yield 'geoid stusab state county tract name'.split()

    ig = itemgetter(48,1,9,10,13,49)

    for e in geo_r.list():
        e = e.get_target() # Must resolve target before setting encoding.
        if e.target_format == 'csv':
            e.encoding = 'latin1'
            for row in e.generator:
                if row[2] == '140': #140 -> tract summary level
                    yield ig(row)
