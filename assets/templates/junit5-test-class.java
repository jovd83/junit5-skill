import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class ExampleServiceTest {

    @Test
    void returnsExpectedValue() {
        ExampleService service = new ExampleService();

        String result = service.compute("input");

        assertEquals("expected", result);
    }
}
