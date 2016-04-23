#include <iostream>
#include "ES.hpp"

using namespace std;


void print_bienvenue() {

	cout<<"Bonjour et bienvenue dans moyenneCalc"<<endl;
}

int ask_note() {

	int val;
	cout<<"Veuillez entrer une note, -1 pour terminer : ";
	cin>>val;
	return val;
}

void print_moyenne(float moyenne) {

	cout<<"La moyenne arithmétique est de : "<<moyenne<<endl;
}

void print_moyenneSansZero(float moyenne2) {

	cout<<"La moyenne sans tenir compte des notes nulles est de : "<<moyenne2<<endl;
}

void print_plancher(int plancher) {

	cout<<"La valeur plancher est de : "<<plancher<<endl;
}

void print_plafond(int plafond) {

	cout<<"La valeur plafond est de : "<<plafond<<endl;
}

