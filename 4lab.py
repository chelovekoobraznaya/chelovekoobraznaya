class HarryPotter:
    def __init__(self):
        self.name = 'HARRY'
        self.hp = 100

    def faculty(self):
        print('Gryffindor')

    def skills(self):
        print('Умеет летать на метле')

    def spells(self):
        print('Экспектооо Потронум!!!')


class DracoMalfoy:
    def __init__(self):
        self.name = 'DRACO'
        self.hp = 100

    def faculty(self):
        print('Slytherin')

    def wand(self):
        return True

    def spells(self, name):
        print('Экcпелиармус!!!', '--Противник лешился палочки--')


class SeverusSnape:
    def __init__(self):
        self.name = 'SEVERUS'
        self.hp = 100

    def proffesion(self):
        print('Учитель Хогвартса')

    def spells(self, wizard):
        print('Авада Кидавра!!!')
        wizard.hp -= 100
        print(wizard.name, 'DEAD...')


class AlbusDumbledore:
    def __init__(self):
        self.name = 'ALBUS'
        self.hp = 100

    def proffesion(self):
        print('Директор Хогвартса')

    def wand(self):
        return True


class LordVoldemort:
    def __init__(self):
        self.name = '...'

    def spell_1(self, wizard):
        print('Авада Кидавра!!!')
        wizard.hp -= 100
        print(wizard.name, 'DEAD...')

    def spell_2(self):
        print('Круциатус!!!')

    def spell_3(self):
        print('Империус')


class Wizards(HarryPotter, DracoMalfoy, SeverusSnape, AlbusDumbledore, LordVoldemort):

    def __init__(self):
        self.hp = HarryPotter.__init__(self)


all_wizards = Wizards()
print(all_wizards.skills())

survivor_boy = HarryPotter()
nasty_boy = DracoMalfoy()
professorSnape = SeverusSnape()
professorDumbledore = AlbusDumbledore()
dark_lord = LordVoldemort()

for wizard in [professorSnape, professorDumbledore]:
    print(wizard.name, wizard.proffesion())

print(nasty_boy.spells(professorDumbledore))
print('Пришёл Северус...')
print(professorSnape.spells(professorDumbledore))
print(professorDumbledore.hp)

print(dark_lord.spell_1(professorSnape))
print(professorSnape.hp)
