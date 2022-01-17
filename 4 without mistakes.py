class Wizard:
    
    def __init__(self, name):
        self.hp = 100
        self.name = name

    def wand(self):
        return True


class HarryPotter(Wizard):

    def faculty(self):
        print('Gryffindor')

    def skills(self):
        print('Умеет летать на метле')

    def spells(self):
        print('Экспектооо Потронум!!!')


class DracoMalfoy(Wizard):

    def faculty(self):
        print('Slytherin')

    def spells(self, name):
        print('Экcпелиармус!!!', '--Противник лешился палочки--')


class SeverusSnape(Wizard):

    def proffesion(self):
        print('Учитель Хогвартса')

    def spells(self, wizard):
        print('Авада Кидавра!!!')
        wizard.hp -= 100
        print(wizard.name, 'DEAD...')


class AlbusDumbledore(Wizard):

    def proffesion(self):
        print('Директор Хогвартса')


class LordVoldemort(Wizard):

    def spell_1(self, wizard):
        print('Авада Кидавра!!!')
        wizard.hp -= 100
        print(wizard.name, 'DEAD...')

    def spell_2(self):
        print('Круциатус!!!')

    def spell_3(self):
        print('Империус')


survivor_boy = HarryPotter('HARRY')
nasty_boy = DracoMalfoy('DRACO')
professorSnape = SeverusSnape('SEVERUS')
professorDumbledore = AlbusDumbledore('ALBUS')
dark_lord = LordVoldemort('...')

for wizard in [professorSnape, professorDumbledore]:
    print(wizard.name, wizard.proffesion())

print(nasty_boy.spells(professorDumbledore))

print(professorSnape.spells(professorDumbledore))
print(professorDumbledore.hp)

print(dark_lord.spell_1(professorSnape))
print(professorSnape.hp)
