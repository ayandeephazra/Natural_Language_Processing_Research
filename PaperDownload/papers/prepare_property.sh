#!/bin/bash

PROPERTY_ALL=('band gap' 'bandgap' 'eg')
UNITS_ALL=('eV')
ELEM_ABBR=(H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og)
ELEM_FULL=(Hydrogen Helium Lithium Beryllium Boron Carbon Nitrogen Oxygen Fluorine Neon Sodium Magnesium Aluminum Silicon Phosphorus Sulfur Chlorine Argon Potassium Calcium Scandium Titanium Vanadium Chromium Manganese Iron Cobalt Nickel Copper Zinc Gallium Germanium Arsenic Selenium Bromine Krypton Rubidium Strontium Yttrium Zirconium Niobium Molybdenum Technetium Ruthenium Rhodium Palladium Silver Cadmium Indium Tin Antimony Tellurium Iodine Xenon Cesium Barium Lanthanum Cerium Praseodymium Neodymium Promethium Samarium Europium Gadolinium Terbium Dysprosium Holmium Erbium Thulium Ytterbium Lutetium Hafnium Tantalum Tungsten Rhenium Osmium Iridium Platinum Gold Mercury Thallium Lead Bismuth Polonium Astatine Radon Francium Radium Actinium Thorium Protactinium Uranium Neptunium Plutonium Americium Curium Berkelium Californium Einsteinium Fermium Mendelevium Nobelium Lawrencium Rutherfordium Dubnium Seaborgium Bohrium Hassium Meitnerium Darmstadtium Roentgenium Copernicium Nihonium Flerovium Moscovium Livermorium Tennessine Oganesson)

VALUE () {
bc -l <<< $((RANDOM%100))/10 | sed 's/0*$//'
}

VALUE_INT () {
bc -l <<< $((((RANDOM%5))+1))
}

VALUE_FRAC () {
bc -l <<< $((((RANDOM%9))+1)) | awk '{printf "%0.1f", $1/10}'
}

ELEMENT_ABBR () {
echo ${ELEM_ABBR[$RANDOM % ${#ELEM_ABBR[@]}]}
}

ELEMENT_FULL () {
echo ${ELEM_FULL[$RANDOM % ${#ELEM_FULL[@]}]}
}

PROPERTY () {
echo ${PROPERTY_ALL[$RANDOM % ${#PROPERTY_ALL[@]}]}
}

UNIT () {
echo ${UNITS_ALL[$RANDOM % ${#UNITS_ALL[@]}]}
}

MATERIAL () {
MAT=($(ELEMENT_ABBR)$(VALUE_INT)$(ELEMENT_ABBR)$(VALUE_INT)$(ELEMENT_ABBR)$(VALUE_INT) $(ELEMENT_ABBR)$(VALUE_FRAC)$(ELEMENT_ABBR)$(VALUE_FRAC) $(ELEMENT_ABBR)$(VALUE_FRAC)$(ELEMENT_ABBR)$(VALUE_FRAC)$(ELEMENT_ABBR)$(VALUE_FRAC) $(ELEMENT_FULL) $(ELEMENT_ABBR)$(ELEMENT_ABBR))
echo ${MAT[$RANDOM % ${#MAT[@]}]}
}

if [ -e positive ]
then
  echo "File positive exists, exiting"
  exit 1
fi

for i in $(seq 5)
do

echo "The SED_PROPERTY of SED_MATERIAL at SED_VALUE GPa is SED_VALUE SED_UNIT.SED_NEWLINE We have found the SED_PROPERTY of SED_MATERIAL and SED_MATERIAL to be SED_VALUE and SED_VALUE SED_UNIT respectively.SED_NEWLINE SED_PROPERTY of SED_MATERIAL is SED_VALUE SED_UNIT.SED_NEWLINE The SED_PROPERTY for the B4 phase was determined to be SED_VALUE ± SED_VALUE SED_UNIT.SED_NEWLINE SED_MATERIAL and SED_MATERIAL have been experimentally demonstrated to have high SED_PROPERTY of SED_VALUE SED_UNIT.SED_NEWLINE The experimental value for the SED_PROPERTY of SED_MATERIAL is found to be SED_VALUE ± SED_VALUE SED_UNIT, which compares well with the calculated value of SED_VALUE SED_UNIT obtained by using the generalised gradient approximation to the exchange correlation potential.SED_NEWLINE The SED_PROPERTY of SED_MATERIAL was found to be SED_VALUE(SED_VALUE) SED_UNIT by optimized experiment and SED_VALUE SED_UNIT by theoretical simulation.SED_NEWLINE The SED_PROPERTY of SED_MATERIAL (SED_VALUE ± SED_VALUE SED_UNIT) is lower than that of SED_MATERIAL (SED_VALUE ± SED_VALUE SED_UNIT).SED_NEWLINE We investigated a new SED_MATERIAL allotrope with a direct band gap of SED_VALUE eV, high hardness of SED_VALUE GPa, and large SED_PROPERTY of SED_VALUE SED_UNIT.SED_NEWLINE The calculated value of SED_PROPERTY of SED_MATERIAL is SED_VALUE SED_UNIT in paramagnetic phase.SED_NEWLINE The SED_PROPERTY calculated from Cij components is equal SED_PROPERTY = SED_VALUE SED_UNIT.SED_NEWLINE SED_PROPERTY of SED_MATERIAL was found to be SED_VALUE SED_UNIT.SED_NEWLINE Using Eqn. 6, the SED_PROPERTY of spinel SED_MATERIAL is calculated to be SED_VALUE SED_UNIT, in good consistent with the experimental value of SED_VALUE SED_UNIT.SED_NEWLINE The SED_PROPERTY of SED_MATERIAL is SED_VALUE SED_UNIT while that of SED_MATERIAL is SED_VALUE SED_UNIT.SED_NEWLINE A newly discovered polymeric form of SED_MATERIAL also shows a high SED_PROPERTY of SED_VALUE SED_UNIT.SED_NEWLINE For SED_MATERIAL the SED_PROPERTY has been found to increase from SED_VALUE SED_UNIT for the bulk material to SED_VALUE SED_UNIT for 9 nm size crystals.SED_NEWLINE At 0 GPa and 300 K, the SED_PROPERTY for the studied SED_MATERIAL compound is equal to SED_VALUE SED_UNIT.SED_NEWLINE At atmospheric pressure, the room temperature SED_PROPERTY SED_PROPERTY are SED_VALUE SED_UNIT for SED_MATERIAL and SED_VALUE SED_UNIT for SED_MATERIAL with dBT/dp = SED_VALUE for both.SED_NEWLINE The SED_PROPERTY of SED_VALUE SED_UNIT was determined by means of high pressure X-ray diffraction.SED_NEWLINE The axial incompressibility shifts from anisotropy to isotropy, and the SED_PROPERTY increases from SED_VALUE to SED_VALUE SED_UNIT upon phase transition." > tmp_positive_sentences_tmp

while grep SED_UNIT tmp_positive_sentences_tmp > /dev/null
do
    sed -i "s/SED_UNIT/$(UNIT)/" tmp_positive_sentences_tmp
done
while grep SED_MATERIAL tmp_positive_sentences_tmp > /dev/null
do
    sed -i "s/SED_MATERIAL/$(MATERIAL)/" tmp_positive_sentences_tmp
done
while grep SED_VALUE tmp_positive_sentences_tmp > /dev/null
do
    sed -i "s/SED_VALUE/$(VALUE)/" tmp_positive_sentences_tmp
done
while grep SED_PROPERTY tmp_positive_sentences_tmp > /dev/null
do
    sed -i "s/SED_PROPERTY/$(PROPERTY)/" tmp_positive_sentences_tmp
done
sed -i 's/SED_NEWLINE /\n/g' tmp_positive_sentences_tmp

cat tmp_positive_sentences_tmp >> positive
rm tmp_positive_sentences_tmp
done
