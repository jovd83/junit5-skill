import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertTrue;

class ExampleRepositoryIntegrationTest {

    @Test
    void savesAndLoadsEntity() {
        ExampleRepository repository = new ExampleRepository();
        ExampleEntity saved = repository.save(new ExampleEntity("id-1"));

        assertTrue(repository.findById(saved.id()).isPresent());
    }
}
