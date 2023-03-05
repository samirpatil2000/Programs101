@FunctionalInterface
interface MyFunction<T> {
    T execute();
}

public class Annotation {
    public static <T> T retryRequest(MyFunction<T> function, String name) {
        try {
            T result = function.execute();
            System.out.println("Returns => " + result);
            return result;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }

    public static String retunString() {
        return "String";
    }

    public static int returnInt() {
        return 0;
    }

    public static void main(String[] args) {
        String resultString = retryRequest(() -> retunString(), "name");
        int resultInt = retryRequest(() -> returnInt(), "Int"); 
        System.out.println("Returns resultString => " + resultString);
        System.out.println("Returns resultInt => " + resultInt);
    }
}
