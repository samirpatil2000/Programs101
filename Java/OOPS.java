import java.util.ArrayList;

class Person {
    String name;
    Integer age;

    public void speak(){
        System.out.println("speak");
        return;
    }

    public void walk(){
        System.out.println("walk");
        return;
    }

    public void learn(){
        System.out.println("learn");
        return;
    }

    public void eat(){
        System.out.println("eat");
        return;
    }
}

class Teacher extends Person{
    String subject;
}

class Student {

}

public class OOPS {
    public static void main(String[] args) {
        System.out.println("Second");
        
        Person person = new Person();
        person.name = "samir";
        person.age = 21;
        
        System.out.println("Name = " +  person.name + " age = " + person.age);
        person.walk();


        Teacher teacher = new Teacher();
        teacher.name = "Professor";
        teacher.age = 30;
        teacher.subject = "Maths";
        
        System.out.println("Name = " +  teacher.name + " age = " + teacher.age + " Subject = " + teacher.subject);
        teacher.walk();  
    }
}
