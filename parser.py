from os import listdir


def list_files():
    """makes a list of all the relevent files"""

    modules = ('.\\ODF', '.\\OCE', '.\\prothese', '.\\parodontologie', '.\\pathologie')
    files = []

    for m in modules:
        k = [m + '\\' + n for n in listdir(m)]
        files.extend(k)

    return files


def interpreter(priority):
    """interprets the resuts of the search as either
    very relevent or possibly useful """

    verbatum = ('You should first check: ',
                'Maybe this is relevent too: ')

    for i, v in zip((True, False), verbatum):
        p = set(priority[i])
        p = [i for i in p if i != []]

        for q in p:
            v += q+', '

        print(v)


def find_item(item):
    """searches the files for the item"""
    priority = {True: [], False: []}
    item = item.lower()

    for i in list_files():

        with open(i, 'r') as f:
            for j in f:
                if item in j.lower():
                    p = j.count('#')
                    priority[p > 0].append(i)

    interpreter(priority)
