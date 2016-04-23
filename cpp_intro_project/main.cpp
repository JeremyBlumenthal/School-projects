/* Jeremy Blumenthal
 * Langages de programmation 1 (INFO-F-105)
 * projet 1
 */

#include "ES.hpp"
#include <vector>

using namespace std;

int main () {
	print_bienvenue();
	int input, somme = 0, somme2 = 0, plancher = 0, plafond = 20;
	float i = 0.0, j = 0.0; // Compteurs pour les moyennes.
	bool encodage = true;
	vector<int> notes; // Vecteur contenant les notes.

	while (encodage) {
		input = ask_note();
		if (input == -1) {
			encodage = false;
		}
		else {
			if (input != 0) { // Moyenne sans 0.
				j++;
				somme2 += input;
			}
			somme += input;
			i++;
			notes.push_back(input);	
		}
  	}

	float moyenne = somme/i;
	float moyenne2 = somme2/j;
	for (int index = 1; index < notes.size(); index++) { // Recherche du plancher et plafond dans vecteur notes.
		if (plancher < notes[index] and notes[index] <= moyenne) {
			plancher = notes[index];
		}
		if (plafond > notes[index] and notes[index] >= moyenne) {
			plafond = notes[index];
		}
	}

	print_moyenne(moyenne);
	print_moyenneSansZero(moyenne2);
	print_plancher(plancher);
	print_plafond(plafond);
  	return 0;
}
