(* ::Package:: *)

(* For a variation of m_0 the check of p p > e+ e- cross sections is included *)

RunScans = {MCm0};

(* Load the file which defines the properties of the different tools *)
LoadSettings="DefaultSettings.m.MSSM";


(* --------------------------------------------------------- *)
(* Initialize MADGRAPH *)
(* --------------------------------------------------------- *)

DEFINITION[a_][IncludeMadGraph]=True; (* For including Madgraph, please keep {{520},{Value->0.}} in SPhenoInput block *)
DEFINITION[a_][MadGraphRuns]={{"/home/USER/MG5_aMC_v2_2_2/PROC_MSSM_0/","/home/USER/MG5_aMC_v2_2_2/PROC_MSSM_0/proc_card.dat"}};



(* ---------------------------------------------------------------------------------------- *)
(* Define the parameter ranges and all other information for the LesHouches input file *)
(* ---------------------------------------------------------------------------------------- *)

(* Name of all blocks *)
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

DEFINITION[a_][MINPAR]={
  {{1}, {Min->500,Max->1500, Steps->10,Distribution->LINEAR}},
  {{2}, {Value->1500}},
  {{3}, {Value->10}},
  {{4}, {Value->1}},
  {{5}, {Value->2500}}
  };

DEFINITION[a_][SPhenoInput]={ 
{{1},{Value->-1}}, (* error level *)
{{2},{Value->1}},  (* SPA conventions *)
{{7},{Value->0}},  (* Skip 2-loop Higgs corrections *)
{{11},{Value->1}}, (* Calculate widhts and BRs *)
{{12},{Value->0.00001}}, (* minimal BR to write out *) 
{{13},{Value->0}}, (* Enable 3-body decays *)
{{31},{Value->-1}}, (* fixed GUT scale (-1: dynamical GUT scale) *)
{{32},{Value->0}}, (* Strict unification *)
{{34},{Value->0.0001}}, (* precision of masses *) 
{{35},{Value->40}}, (* Maximal number of iterations *) 
{{37},{Value->1}}, (*  Set Yukawa scheme *) 
{{38},{Value->2}}, (* 1/2 - Loop RGEs *) 
{{50},{Value->1}}, (* Majorana phases: use only positive masses  *) 
{{51},{Value->0}}, (* Switch to CKM matrix *) 
{{52},{Value->0}}, (* Write spectrum in case of tachyonic states  *) 
{{55},{Value->1}}, (* 1 - Loop masses *)
{{57},{Value->1}}, (* low energy constraints *)
{{60},{Value->1}}, (* Include possible, kinetic mixing *)
{{65},{Value->1}}, (* Solution tadpole equation *)
{{75},{Value->0}}, (* Write WHIZARD files *) 
{{76},{Value->0}},  (* Write HiggsBounds files *) 
{{86},{Value->0.}},  (* Maximal width to be counted as invisible in Higgs decays; -1: only LSP *) 
{{510},{Value->0.}},  (* Write tree level values for tadpole solutions *) 
{{515},{Value->0.}},  (* Write parameter values at GUT scale *) 
{{520},{Value->0.}},  (* Write effective Higgs couplings (HiggsBounds blocks) *) 
{{525},{Value->0.}}  (* Write loop contributions to diphoton decay of Higgs *) 
}; 


(* ---------------------------------------------------------------------------------------- *)
(* Define what should be plotted                                                            *)
(* ---------------------------------------------------------------------------------------- *)

DEFINITION[MC1m0][Plots]={
  {P2D, {MINPAR[1],{CROSSSECTION[1]}},Style1,"m0_xsection.eps"}
};

BasicStyle1= {Frame->True, Axes->False,FrameLabel->{UseLaTeX["$m_0$"],UseLaTeX["$\\sigma_{pp\\to e^+e^-}$"]},Joined->False, FrameTicksStyle -> Directive[Black, 14]};
Style1 = Map[Join[BasicStyle1,{PlotStyle->#}]&,{Red}];
