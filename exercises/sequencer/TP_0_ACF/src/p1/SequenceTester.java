package p1;

import java.util.Arrays;
import java.util.List;

import junit.framework.TestCase;

import org.junit.Test;

import test0.Sequence;

public class SequenceTester extends TestCase {

	protected Sequence sequencer;
	private List<Integer> l1 = null;
	private List<Integer> l2 = null;

	@Override
	protected void setUp() throws Exception {

		sequencer = new SequenceImpl();

	}

	
	
	/*
	 * L1 contient un seul element
	 */
	@Test
	public void testL1IsSubSeqOfL2WithOneELementNotInL2() {
		l1 = Arrays.asList(2, 4, 5);
		l2 = Arrays.asList(2, 3, 1, 4, 1, 3);
		assertTrue("The list L1 is a subseq of L2",
				sequencer.subSeq(l1, l2));
	}
	/*
	 * L1 contient un seul element
	 */
	@Test
	public void testL1IsSubSeqOfL2WithAnELementNotInL2() {
		l1 = Arrays.asList(2, 4, 5);
		l2 = Arrays.asList(2, 3, 1, 5, 1, 3);
		assertTrue("The list L1 is a subseq of L2", sequencer.subSeq(l1, l2));
	}
	
	/*
	 * L1 contient un seul element
	 */
	@Test
	public void testL1IsSubSeqOfL2WithSeveralOccurenceOfOneInL2() {
		l1 = Arrays.asList(2, 4, 5,5,5,5);
		l2 = Arrays.asList(2, 3, 1, 5, 1, 3);
		assertFalse("The list L1 is a subseq of L2", sequencer.subSeq(l1, l2));
	}
	
	/*
	 * L1 contient un seul element
	 */
	@Test
	public void testL1IsSubSeqOfL2WithElementsAtheEnd() {
		l1 = Arrays.asList(2, 4, 5);
		l2 = Arrays.asList(2, 3, 1, 1, 3,4);
		assertTrue("The list L1 is a subseq of L2", sequencer.subSeq(l1, l2));
	}
	/*
	 * L1 contient un seul element
	 */
	@Test
	public void testL1IsSubSeqOfL2WithElementsAtheEndOfL2() {
		l1 = Arrays.asList(2, 4, 5);
		l2 = Arrays.asList(23, 1, 1, 3,4,5,2);
		assertTrue("The list L1 is a subseq of L2", sequencer.subSeq(l1, l2));
	}
	
	/*
	 * L1 contient un seul element
	 */
	@Test
	public void testLastElementInHeadOfL1() {
		l1 = Arrays.asList(1,2,3,4,5);
		l2 = Arrays.asList(2,3,4,5,1,3,5,7);
		assertTrue("The list L1 is a subseq of L2", sequencer.subSeq(l1, l2));
	}
	
	/*
	 * L1 contient un seul element
	 */
	@Test
	public void testLastElementInHeadOfL11() {
		l1 = Arrays.asList(1,2);
		l2 = Arrays.asList(2,1);
		assertTrue("The list L1 is a subseq of L2", sequencer.subSeq(l1, l2));
	}
}
