// package Basic;
class Developer{
    public void writeCode(){
        System.out.println("writing code started");
    }
    public void framworks(){
        System.out.println("framworks started");
    }
}


class BackendDeveloper extends Developer{
    public void writeCode(){
        System.out.println("writing code. in java string boot");
    }
}


public class First {
    public static void main (String[] args){
        System.out.println("First Java Code"); 
        Developer developerObject = new Developer();
        developerObject.writeCode();
        BackendDeveloper backendDeveloperObject = new BackendDeveloper();
        backendDeveloperObject.framworks();
    }
}