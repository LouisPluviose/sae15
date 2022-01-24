# Data sets location
This directory contains three another ones related to the data sets and called **raw**, **processed**, **cleaned**. A description of each one is given below. 

## Raw directory
This directory contains original and immutable data sets. Do not edit your raw data, especially with Excel, open files only in read only mode. This directory contains four csv files, each one contains a part of the dataset. Each date file is structured as follows, however only the first one has an header :

- date_reference: date_reference[date] Date de référence : dernier jour de la période observée
- semaine_injection: semaine_injection[text] Semaine datant l’injection
- Region_residence: region_residence[text] Code de la région de résidence des patients
- Libelle_region: libelle_region[text] Libellé de la région de résidence des patients
- departement_residence: departement_residence[text] Code du département de résidence des patients
- libelle_departement: libelle_departement[text] Libellé du département de résidence des patients
- population_insee: population_insee[int] Population Insee au 1er janvier 2020
- classe_age: classe_age[text] Tranche d’âge
- libelle_classe_age: libelle_classe_age[text] Libellé tranche d’âge
- type_vaccin: type_vaccin[text] Type de vaccin administré
- effectif_1_inj: effectif_1_inj[int] Effectif de patients ayant reçu au moins une première injection
- effectif_termine: effectif_termine[int] Effectif de patients dont le schéma vaccinal initial est terminé
- effectif_cumu_1_inj: effectif_cumu_1_inj[int] Effectif cumulé de patients ayant reçu au moins une première injection
- effectif_cumu_termine: effectif_cumu_termine[int] Effectif cumulé de patients dont le schéma vaccinal initial est terminé
- taux_1_inj: taux_1_inj[double] Taux de vaccination de patients ayant reçu au moins une première injection
- taux_termine: taux_termine[double] Taux de vaccination de patients dont le schéma vaccinal initial est terminé
- taux_cumu_1_inj: taux_cumu_1_inj[double] Taux cumulé de vaccination de patients ayant reçu au moins une première injection
- taux_cumu_termine: taux_cumu_termine[double] Taux cumulé de vaccination de patients dont le schéma vaccinal initial est terminé
- date: date[date] Date du dernier jour de la semaine datant l’injection
- Effectif_rappel: effectif_rappel[int] Effectif de patients ayant reçu une injection de rappel
- Effectif_cumu_rappel: effectif_cumu_rappel[int] Effectif cumulé de patients ayant reçu une injection de rappel
- Effectif_rappel_parmi_eligible: effectif_rappel_parmi_eligible[int] Effectif de patients ayant reçu une injection de rappel et étant éligible au rappel
- Effectif_eligible_au_rappel: effectif_eligible_au_rappel[int] Effectif de patients étant éligibles au rappel
- TAUX_rappel: taux_rappel[double] Taux de vaccination de patients ayant reçu une injection de rappel (rapporté à la population Insee)
- TAUX_CUMU_rappel: taux_cumu_rappel[double] Taux cumulé de vaccination de patients ayant reçu une injection de rappel (rapporté à la population Insee)
- TAUX_CUMU_rappeleli: taux_cumu_rappeleli[double] Taux cumulé de vaccination de patients ayant reçu une injection de rappel (rapporté à la population éligible au rappel)


## Processed directory
This directory contains intermediate transformed data sets. This working directory could contain multiple data sets.

## Cleaned directory
This directory contains canonical data sets could be used for publication. Theses data sets would be used for the analysis.
