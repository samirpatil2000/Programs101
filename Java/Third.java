import java.util.UUID;

class Address {

    private String id = UUID.randomUUID().toString();
    private String fullName;

    public String getId(){
        return this.id;
    }

    public String getFullName(){
        return this.fullName;
    }

}

public class Third{
    public static void main(String[] args) {
        System.out.println("Second");
        String uniqueID = UUID.randomUUID().toString();
        Address address = new Address();
        System.out.println(address.getId());
        Address address2 = new Address();
        System.out.println(address2.getId());
    }
}