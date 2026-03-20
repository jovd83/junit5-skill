import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

import static org.junit.jupiter.api.Assertions.assertEquals;

class ExampleFormatterTest {

    @ParameterizedTest
    @CsvSource({
        "1, one",
        "2, two"
    })
    void formatsValues(int input, String expected) {
        ExampleFormatter formatter = new ExampleFormatter();

        assertEquals(expected, formatter.format(input));
    }
}
