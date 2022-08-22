# programme
import logging, datetime, locale
from pdfrw import PdfReader, PdfWriter, PdfDict

locale.setlocale(locale.LC_ALL, 'fr_FR')

def get_pdf_info(path):
    pdf = PdfReader(path)
    data = {"Periode": "Septembre 2022", "Date_af_date": "06/09/2022"}
    print(pdf.keys())
    print(pdf.Info)
    print(pdf.Root.keys())
    print('PDF has {} pages'.format(len(pdf.pages)))

    for page in pdf.pages:
        annotations = page['/Annots']
        if annotations is None:
            continue

        for annotation in annotations:
            if annotation['/Subtype'] == '/Widget':
                if annotation['/T']:
                    key = annotation['/T'].to_unicode()
                    print(key)
                    print(data[key])
                    annotation.update(PdfDict(V='{}'.format(data[key])))
    PdfWriter().write('out.pdf', pdf)


if __name__ == '__main__':
    #get_pdf_info('Quittance Loyer template.pdf')



    dat = datetime.datetime.now()
    print(dat.strftime('%A %d %B %Y %H:%M:%S '))
    print(dat.month)
    print(dat.year)
    print(dat.strftime("%B %Y").capitalize())
    print(dat.strftime("%x"))