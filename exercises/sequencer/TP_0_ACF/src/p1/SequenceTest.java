package p1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import junit.framework.Assert;
import junit.framework.TestCase;

import org.junit.Test;

import test0.Sequence;

public class SequenceTest extends TestCase {

	protected Sequence sequencer;
	private List<Integer> l1 = null;
	private List<Integer> l2 = null;

	@Override
	protected void setUp() throws Exception {

		sequencer = new SequenceImpl();

	}

	@Override
	protected void tearDown() throws Exception {
		l1=l2=null;
	}
	/*
	 * L1 et L2 sont null
	 */
	@Test
	public void testL1AndL2AreNull() {
		l1 = null;
		l2 = null;
		Assert.assertTrue(
				"The list L1 and L2 are null then the subSeq method should return true",
				sequencer.subSeq(l1, l2));
	}

	/*
	 * L1 est null et L2 non null (vide ou non)
	 */
	@Test
	public void testL1IsNullList() {
		l1 = null;
		l2 = Arrays.asList(1, 2, 3);
		Assert.assertTrue(
				"The list L1 is null  and L2 is not empty then the subSeq method should return true",
				sequencer.subSeq(l1, l2));
	}

	/*
	 * L1 est vide et L2 vide
	 */
	@Test
	public void testL1AndL2AreEmpty() {
		l1 = null;
		l2 = Arrays.asList();
		Assert.assertTrue(
				"The list L1 is null then the subSeq method should return true",
				sequencer.subSeq(l1, l2));
	}

	/*
	 * L1 n'est pas vide et contient un seul élément et L2 vide ou null
	 */
	@Test
	public void testL1ContainsOneElementAndL2IsNull() {
		l1 = Arrays.asList(1);
		l2 = null;
		Assert.assertTrue(
				"The list L1 is not empty and L2 is null then the subSeq method should return true",
				sequencer.subSeq(l1, l2));

	}

	/*
	 * L1 n'est pas vide et contient un seul élément et L2 vide ou null
	 */
	@Test
	public void testL1ContainsOneElementAndL2IsEmpty() {
		l1 = Arrays.asList(1);
		l2 = Arrays.asList();
		Assert.assertTrue(
				"The list L1 is not empty and L2 is empty then the subSeq method should return true",
				sequencer.subSeq(l1, l2));
	}

	/*
	 * L1 n'est pas vide et L2 vide ou null
	 */
	@Test
	public void testL1IsNotEmptyAndL2IsEmpty() {
		l1 = Arrays.asList(1, 2, 3, 4);
		l2 = Arrays.asList();
		Assert.assertFalse(
				"The list L1 is not empty and L2 is empty then the subSeq method should return false",
				sequencer.subSeq(l1, l2));
	}

	/*
	 * L1 n'est pas vide et L2 vide ou null
	 */
	@Test
	public void testL1IsNotEmptyAndL2IsNull() {
		l1 = Arrays.asList(1, 2, 3, 4);
		l2 = null;
		Assert.assertFalse(
				"The list L1 is not empty and L2 is null then the subSeq method should return false",
				sequencer.subSeq(l1, l2));
	}

	/*
	 * L1 contient un seul element
	 */
	@Test
	public void testL1ContainsOneElementInL2() {
		l1 = Arrays.asList(1);
		l2 = Arrays.asList(2, 3, 1, 4, 1, 3);
		Assert.assertTrue(
				"The list L1 contains 1 one element that is in L2 subSeq method should return true",
				sequencer.subSeq(l1, l2));
	}

	/*
	 * L1 contient un seul element
	 */
	@Test
	public void testL1ContainsOneElementNotInL2() {
		l1 = Arrays.asList(10);
		l2 = Arrays.asList(2, 3, 1, 4, 1, 3);
		Assert.assertTrue(
				"The list L1 contains 1 one element that is in L2 subSeq method should return true",
				sequencer.subSeq(l1, l2));
	}

	/*
	 * L1 contient un seul element
	 */
	@Test
	public void testL1ContainsMoreThanOneElementNotInL2() {
		l1 = Arrays.asList(10, 11);
		l2 = Arrays.asList(2, 3, 1, 4, 1, 3);
		Assert.assertFalse(
				"The list L1 contains more than one element that are not in L2 subSeq method should return false",
				sequencer.subSeq(l1, l2));
	}

	/*
	 * L1 contient un seul element
	 */
	@Test
	public void testL1IsSubSeqOfL2WithAllElementsInL2() {
		l1 = Arrays.asList(2, 4);
		l2 = Arrays.asList(2, 3, 1, 4, 1, 3);
		Assert.assertTrue("The list L1 is a subseq of L2",
				sequencer.subSeq(l1, l2));
	}

	/*
	 * L1 contient un seul element
	 */
	@Test
	public void testL1IsSubSeqOfL2WithOneELementNotInL2() {
		l1 = Arrays.asList(2, 4, 5);
		l2 = Arrays.asList(2, 3, 1, 4, 1, 3);
		Assert.assertTrue("The list L1 is a subseq of L2",
				sequencer.subSeq(l1, l2));
	}
	/*
	 * L1 contient un seul element
	 */
	@Test
	public void testL1IsSubSeqOfL2WithAnELementNotInL2() {
		l1 = Arrays.asList(2, 4, 5);
		l2 = Arrays.asList(2, 3, 1, 5, 1, 3);
		Assert.assertTrue("The list L1 is a subseq of L2",
				sequencer.subSeq(l1, l2));
	}

}
