import org.junit.jupiter.api.extension.BeforeEachCallback;
import org.junit.jupiter.api.extension.ExtensionContext;

class ExampleExtension implements BeforeEachCallback {

    @Override
    public void beforeEach(ExtensionContext context) {
        // Add explicit setup only when the behavior is genuinely cross-cutting.
    }
}
