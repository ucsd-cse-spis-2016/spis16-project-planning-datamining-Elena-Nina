from commonProf import cmProfDepart

arts_And_HumanitiesSS = ['History/Sixth' , 'Art/Hum/SS' , 'Anthropology' , 'Cognitive' , 'Communication' , 'Economics' , 'Educational' , 'Linguistics' , 'Political' , 'Sociology' , 'Ethnic' , 'Philosophy' , 'Literature' , 'Music' , 'Theatre' , 'Dance' , 'Visual' , 'Arts' , 'Psychology' , 'History']
bio = ['bio' , 'Biochemistry' , 'Biological' , 'Biology' , 'Bioinformatics' , 'Ecology' , 'Evolution' , 'Human' , 'Microbiology' , 'Molecular' , 'Physiology' , 'Neuroscience']
engineering = ['engineering' , 'Bioengineering' , 'Computer' , 'Electrical', 'Engineering', 'Aerospace', 'NanoEngineering','Structural']
physical = ['physical' , 'physical sciences' , 'Chemistry','Biochemistry','Physics','Mathematics' , 'Mathematics/Revelle']
management = ['management' , 'Rady School of Management','Management', 'Business' , 'Finance','Accounting']
global_policy = ['global policy' , 'Global Policy', 'International' , 'Global']
medicine = ['Medicine' , 'medicine']
scripps = ['scripps' , 'Scripps', 'Oceanography','Earth', 'Marine', 'Ocean' , 'Oceanography/Biological']
pharmacy = ['pharmacy' , 'Skaggs','Pharmacy','Pharmaceutical']


other = []
for i in cmProfDepart:
    i[1] = i[1].split()
    for n in i[1]:
        if n in physical:
            i[1] = "physical"
        elif n in bio:
            i[1] = 'bio'
        elif n in engineering:
            i[1] = 'engineering'
        elif n in physical:
            i[1] = 'physical sciences'
        elif n in management:
            i[1] = 'management'
        elif n in global_policy:
            i[1] = 'global policy'
        elif n in medicine:
            i[1] = 'medicine'
        elif n in scripps:
            i[1] = 'scripps'
        elif n in pharmacy:
            i[1] = 'pharmacy'
        elif n in arts_And_HumanitiesSS:
            i[1] = 'Art/Hum/SS'
        else:
            other.append(i[1])

