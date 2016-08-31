(* ::Package:: *)

(* This example performs a scan including Vevacious
*)


(* Load the file which defines the properties of the different tools *)
LoadSettings="DefaultSettings.m.MSSM";

(* Several scans can be done in a row. Give each one a name... *)
RunScans = {ScanA0vevacious};

DEFINITION[a_][IncludeVevacious]=True;

(* ---------------------------------------------------------------------------------------- *)
(* Define the parameter ranges and all other information for the LesHouches input file *)
(* ---------------------------------------------------------------------------------------- *)

(* Names of all blocks *)


DEFINITION[a_][Blocks]={MODSEL,SMINPUTS,MINPAR,SPhenoInput};

(* parameter ranges *)
(* Possible Distributions: FIXED, LINEAR, LOG, RANDOM *)

DEFINITION[a_][MODSEL]={
  {{1},{Value->1}},
  {{6},{Value->1}}
};

DEFINITION[a_][SMINPUTS]={
  {{2},{Value->1.166390*10^-5}},
  {{3},{Value->0.1172}},
  {{4},{Value->91.18760}},
  {{5},{Value->4.2}},
  {{6},{Value->172.9}},
  {{7},{Value->1.777}}
};

DEFINITION[ScanA0vevacious][MINPAR]={
  {{1}, {Value->1000}},
  {{2}, {Value->1000}},
  {{3}, {Value->10}},
  {{4}, {Value->1}},
  {{5}, {Min->-2500,Max->0, Steps->10,Distribution->LINEAR}}
  };



DEFINITION[a_][SPhenoInput]={
  {{1},{Value->-1}},
  {{2},{Value->1}},
  {{11},{Value->0}},
  {{12},{Value->12}},
  {{21},{Value->0}},
  {{75},{Value->1}},
  {{76},{Value->1}}
};