class Person {
    
    String name;
    int age;

    public Person(String name, int age){
        this.name = name;
        this.age = age;
        System.out.println("Object Creation");
    }
    void walk(){
        System.out.println("Object walking");
    }

}


class Developer extends Person {
    
    String[] programmingLanguages;

    public Developer(String name, int age, String[] programmingLanguages) {
        
        super(name, age);
        this.programmingLanguages = new String[3];
        setProgrammingLanguanges(programmingLanguages);
        
    }

    public void setProgrammingLanguanges(String[] programmingLanguages) {
        for (int i = 0; i < programmingLanguages.length; i++) {
            this.programmingLanguages[i] = programmingLanguages[i];
        }
    }
    
    public void developerDetails(){
        System.out.println("Name: " + this.name);
        System.out.println("Age: " + this.age);
        System.out.println("Programming Languages: " + Second.listToString(programmingLanguages));
        ;
    }
}


public class Second{

    public static String listToString(String[] list){
        String result = new String();
        for (int i = 0; i < list.length; i++){
            result += list[i];
            result += ", ";
        }
        return result.substring(0, result.length() - 2);
    }
    public static void main(String[] args) {
        System.out.println("Second");
        Person p1 = new Person("Samir Patil", 22);
        System.out.println(p1.name + " Person One");
        
        String[] programmingLanguages = new String[]{"Python", "Java", "JavaScript"};
        Developer d1 = new Developer("Samir Patil", 22, programmingLanguages);
        System.out.println(d1.name + " Developer One");
        d1.developerDetails();
    }
}