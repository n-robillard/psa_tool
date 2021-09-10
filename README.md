# GSA2PB : Implementation of Protein Block alphabet for the analysis of allosteric communication

## Description

This program is base o the GSA-tools software, which is a tool for the analysis of the allosteric communication and functionnal local motion of proteins, with the use of a specific structural alphabet generated by GROMACS tool (4.0.x or 4.5.x). 
Here, we implement an other structural alphabet, the Protein Block (PB), which are provide by the PBxplore software.

The main objective of this program is to generate a normalized mutual information on proteins. To do this, we used PBxplore for generate the structural alphabet for the protein at differents times. Then, a transition matrix is generate for each protein block, which defiened the probability to have a transition of one trajectory to another one. The mutual information, the entropy and the expect error of the mutual information are calculated for each trasition matrix to obtained the normalized mutual information.

This projet is realized as part of the Master 2 : Biology Informatic, dispense at the Univeristy of Paris-Diderot, in France.

## Installation

### Required

### Installation command

## Utilisation

## References