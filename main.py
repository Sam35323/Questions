def lubaya(kirka, rexim):
    try:
        kirk = open(kirka, rexim, encoding='utf-8')
    except:
        print('ego net')
    else:
        return kirk


def luboe_nazvanie(hhh):
    hh = hhh.readline().replace('/', '\n')
    return hh


hhhh = lubaya('Name.txt', 'r')
h = luboe_nazvanie(hhhh)
print(h)

h = luboe_nazvanie(hhhh)
print(h)

h = luboe_nazvanie(hhhh)
print(h)

h = luboe_nazvanie(hhhh)
print(h)

h = luboe_nazvanie(hhhh)
print(h)

h = luboe_nazvanie(hhhh)
print(h)

h = luboe_nazvanie(hhhh)
print(h)

h = luboe_nazvanie(hhhh)
print(h)

h = luboe_nazvanie(hhhh)
print(h)

h = luboe_nazvanie(hhhh)
print(h)

h = luboe_nazvanie(hhhh)
print(h)


def next_blok(lk):
    kategoriya = luboe_nazvanie(lk)
    sloghnost = luboe_nazvanie(lk)
    vopros = luboe_nazvanie(lk)
    variki = []
    for fcvhb in range(4):
        variki.append(luboe_nazvanie(lk))
    tuty = luboe_nazvanie(lk)
    hujy = luboe_nazvanie(lk)
    return kategoriya, vopros, sloghnost, variki, tuty, hujy,


def novaya_funkciya():
    kakayato_peremennaya = lubaya('Name.txt', 'r')
    nazvaniye = luboe_nazvanie(kakayato_peremennaya)
    print('Хело юзер зис викторина тест ёр атентион энд интуитион энд айку энд ёр майнд')
    print(nazvaniye)
    kategoriya, vopros, sloghnost, variki, tuty, hujy = next_blok(kakayato_peremennaya)
    lore = 0
    while kategoriya:
        print(kategoriya)
        print(vopros)
        print()
        for hj in variki:
            print(hj)
        glhf = str(input('vah otvetЖ'))
        if glhf == tuty:
            lore += sloghnost
            print('g', 'g')
        else:
            print('press', f'gg {glhf}')
        print(hujy)
        print(f'У вас -{lore} iq')
        kategoriya, vopros, sloghnost, variki, tuty, hujy = next_blok(kakayato_peremennaya)
    kakayato_peremennaya.close()
    print(f'пока жулаем удачи человек с -{lore} iq')


novaya_funkciya()
