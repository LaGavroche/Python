import datetime

maDate = datetime.date(1994, 12, 5)
dateDuJour = datetime.date.today()
age_en_jours = dateDuJour - maDate
age_en_annees = dateDuJour.year - maDate.year

# bisextiles years
annees_bissextiles = len([annee for annee in range(maDate.year, dateDuJour.year + 1) if annee % 4 == 0])

# weeks
age_en_semaines = age_en_jours.days // 7
jours_restants = age_en_jours.days % 7

# number of days (for real)
jours_reels = age_en_jours.days - annees_bissextiles

# number of months
age_en_mois = int(age_en_jours.days / 30.44)

print("Tu as", age_en_annees, "ans")
print("Nombre de jours vécus (avec années bissextiles):", age_en_jours.days)
print(f"{age_en_semaines} semaines et {jours_restants} jours")
print("soit", age_en_mois, "mois")