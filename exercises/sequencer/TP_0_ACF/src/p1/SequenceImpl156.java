package p1;

import java.util.List;

import test0.Sequence;

public class SequenceImpl156 implements Sequence {

	/**
	 * @param l1
	 * @param l2
	 * @return true if list l1 is a sublist of list l2, where at most one
	 *         element of l1 may not occur in l2
	 */

	@Override
	@SuppressWarnings("rawtypes")
	public boolean subSeq(List l1, List l2) {
		int cpt = 0;
		if (l1 == null || l1.size() < 2) {// Il ya moins de deux elements dans la liste L1.
			return true;

		}else if (l1 == null || l1.size() < 2) {// Il ya moins de deux elements dans la liste L1.
			return true;

		}else if (l1.size() > 1 && l2 == null) {// Il ya au moins 2 elements dans L1 et L2 erst vide

			return false;
		}else  // sont pas identiques
		if (l1 != null && l2 != null && l1.size() - l2.size() > 1) {//Il ya plus d'elements dans L1 que dans L2
			return false;
		} else // sont pas identiques
		if (l1 != null && l2 != null && l1.size() == 2 && l2.size() == 1 && l1.contains(l2.get(0))) {// Il ya plus
																										// d'elements
																										// dans L1 que
																										// dans L2
			return true;
		} else {
		printList(l1,"L1");  printList(l2,"L2");
		int i = 0;
		int start = 0;
		int j = 0;
		boolean trouve = false;
		while (i < l1.size()) {// on parcourt l1 � la recherche de la premi�re occurrence de l1[i]
		int elti=((Integer) l1.get(i)).intValue();

				j = start;
				if (start > l1.size()) {
					j = 0;
				}

				trouve = false;
			while (j < l2.size()) {
				int eltj=((Integer) l2.get(j)).intValue();
				if ( elti== eltj) {
					//Si els deux elements sont egaux alors on sort de la boucle dans L2 et continue sur l'�lement suivant de L1
					trouve = true;
					System.out.println("index of trouve= " + j);
						start = j + 1;
					i++;
					break;
				}
				j++;
					System.out.println(" start=" + start + " L1[" + i + "]=" + elti + " "
							+ " L2[" + j + "]=" + eltj
							+ " trouve=" + trouve + " cpt= " + cpt);
			}
				System.out
						.println(" start=" + start + " L1[" + i + "]=" + elti
						+ "  trouve="
						+ trouve + " cpt= " + cpt);
			if (!trouve) {//Element courant n'est pr�sent dans la liste l2
				System.out.println("j>l2.size()? " + j+">"+l2.size());
				cpt++;
				i++;
				}
			if (cpt > 1) {//On a trouv� au moins deux elements de L1 qui n'apparaissent pas dans L2 dans le m�me ordre
				System.out.println("cpt> 1, cpt=" + cpt+ " j="+j +" start= "+start);
				return false;
			}
			System.out.println("----");
			
			

		}//end while
		}//end else
		System.out.println("cpt> 1, cpt=" + cpt);
		return cpt <= 1;
	}
	
	
	@SuppressWarnings("rawtypes")
	public boolean subSeq2(List l1, List l2) {
		int cpt = 0;
		if (l1 == null || l1.size() < 2) {// Il ya moins de deux elements dans la liste L1.
			return true;

		}
		
		if (l1 == null || l1.size() < 2) {// Il ya moins de deux elements dans la liste L1.
			return true;

		}
		if (l1.size() > 1 && l2 == null) {// Il ya au moins 2 elements dans L1 et L2 erst vide

			return false;
		}
		// sont pas identiques
		if (l1 != null && l2 != null && l1.size() - l2.size() > 1) {//Il ya plus d'elements dans L1 que dans L2
			return false;
		}
		printList(l1,"L1");  printList(l2,"L2");
		int i = 0;
		while (i < l1.size()-1) {// on parcourt l1
			
			int indexcurrent=l2.indexOf((l1.get(i)));
			int inndexnext=l2.indexOf((l1.get(i+1)));
			System.out.println("cpt= "+cpt);
			if(indexcurrent>inndexnext){
				cpt++;
				
			}
			i++;
		}
		return cpt <= 1;
	}
	public void printList(List l , String name){
		if(l==null || l.size()==0){
			System.out.println(name+"=[ ]");
		}else{
			System.out.print(name+"=[");
			for(int i=0;i<l.size(); i++){
				if(i<l.size()-1){
					System.out.print(l.get(i)+",");
				}else{
					System.out.print(l.get(i));
				}
			}
			System.out.println("]");
		}
	}
}
