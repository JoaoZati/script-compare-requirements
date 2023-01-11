def main():
    with open('/home/joaozati/Dev/brain/requirements/base.txt', 'r') as base:
        str_base = base.read()

    with open('/home/joaozati/Dev/brain/requirements/base_2.txt', 'r') as base_2:
        str_base_2 = base_2.read()

    lst_base = str_base.split('\n')
    lst_base_2 = str_base_2.split('\n')

    lst_base_splits = [i.split('==')[0].lower() for i in lst_base]
    lst_base_2_splits = [i.split('==')[0].split(' @ ')[0].lower() for i in lst_base_2]

    lst_not_same_version = [i for i in lst_base if i not in lst_base_2]
    lst_not_installed = [
        i for i in lst_base_splits if i not in lst_base_2_splits
    ]

    if not lst_not_same_version:
        print('Todas as bibliotecas presentes')
        return

    print('As versoes nao instaladas na mesma versao sao as:')
    [print(i) for i  in lst_not_same_version]

    if not lst_not_installed:
        print('Todas as bibliotecas foram instaladas')
    else:
        print(f'As versoes nao instaladas sao as:')
        [print(i) for i  in lst_not_installed]

    lst_not_same_version_split = [
        i.split('==')[0].split(' @ ')[0].lower() for i in lst_not_same_version
    ]
    lst_index_base_2 = [
        lst_base_2_splits.index(i) if i in lst_base_2_splits else None 
        for i in lst_not_same_version_split
    ]

    print('As versoes diferentes sao')
    [
        print(f'Versao original servidor: {i}  -- Versao nova: {lst_base_2[index]}')
        for i, index in zip(lst_not_same_version, lst_index_base_2)
    ]

if __name__ == '__main__':
    main()
