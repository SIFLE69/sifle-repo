import pikepdf

b = pikepdf.Pdf.open("pform.pdf")


no_extr = pikepdf.Permissions(extract=False)

b.save("npform.pdf",encryption=pikepdf.Encryption(user="sincostan",owner="sifle",allow=no_extr))