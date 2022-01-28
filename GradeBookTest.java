package GradeBook;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class GradeBookTest {
	GradeBook g1;
	GradeBook g2;

	@BeforeEach
	void setUp() throws Exception {
		g1 = new GradeBook(5);
		g2 = new GradeBook(5);
		g1.addScore(2);
		g1.addScore(5);
		g1.addScore(11);
		g2.addScore(5);
		g2.addScore(9);
		g2.addScore(13);
	}

	@AfterEach
	void tearDown() throws Exception {
		g1 = null;
		g2 = null;
	}

	@Test
	void testAddScore() {
		assertTrue(g1.toString().equals("2.0 5.0 11.0 "));
		assertTrue(g2.toString().equals("5.0 9.0 13.0 "));
	}

	@Test
	void testAddScorePart2() {
		assertEquals(3, g1.getScoreSize());
		assertEquals(3, g2.getScoreSize());
	}

	@Test
	void testSum() {
		assertEquals(18, g1.sum());
		assertEquals(27, g2.sum());
	}

	@Test
	void testMinimum() {
		assertEquals(2, g1.minimum());
		assertEquals(5, g2.minimum());
	}

	@Test
	void testFinalScore() {
		assertEquals(16, g1.finalScore());
		assertEquals(22, g2.finalScore());
	}
}
