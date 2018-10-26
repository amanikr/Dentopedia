
def extract_summary(file):
    summary = []
    flag = False

    with open(file, 'r') as f:
        for j in f:
            if 'Sommaire' in j or flag is True:
                summary.append(j)
                flag = True

            if '___' in j:
                break

        for i in summary:
            print(i)


# extract_summary(".\\Pathologie\\Extraction_la_marche_a_suivre.md")
