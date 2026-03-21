export interface VekeEntry {
  uke: number[];
  tema: string;
  emne: string | null;
  kompetansemaal: string;
  notat: string[];
  ressurstal: number;
  oppgavetar: number;
  type: 'undervisning' | 'ferie' | 'eksamen' | 'prosjekt';
}

export interface NoteEntry {
  title: string;
  emne: string;
  uke: number[];
  kompetansemaal: string;
  tags: string[];
  relatert: string[];
  ressursar: Ressurs[];
  oppgaaver: string[];
  public?: boolean;
}

export interface Ressurs {
  type: 'lenke' | 'video' | 'notat' | 'oppgave';
  tittel: string;
  url?: string;
  lengde?: string;
}
