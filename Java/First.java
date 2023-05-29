// package Basic;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;


class Developer{
    public void writeCode(){
        System.out.println("writing code started");
    }
    public void framworks(){
        System.out.println("framworks started");
    }
}


class BackendDeveloper extends Developer{
    @Override
    public void writeCode(){
        System.out.println("writing code. in java string boot");
    }
}


public class First {
    public static void main (String[] args){
        System.out.println("First Java Code"); 
        // Developer developerObject = new Developer();
        // developerObject.writeCode();
        // BackendDeveloper backendDeveloperObject = new BackendDeveloper();
        // backendDeveloperObject.framworks();
        // String timeString = "2023-04-12T09:13:30.091Z";
        // Instant instant = Instant.parse(timeString);
        // long epochTime = instant.toEpochMilli() / 1000;
        // System.out.println(epochTime);
        String dateStr = "2023-04-23T12:02:55.860Z";
        LocalDateTime date = LocalDateTime.parse(dateStr, DateTimeFormatter.ISO_DATE_TIME);
        LocalDateTime newDate = date.plusMinutes(15);

        // Compare with other date
        LocalDateTime otherDate = LocalDateTime.now(); // replace with your other date
        int comparisonResult = newDate.compareTo(otherDate);
        if (comparisonResult < 0) {
            System.out.println("newDate is earlier than otherDate");
        } else if (comparisonResult > 0) {
            System.out.println("newDate is later than otherDate");
        } else {
            System.out.println("newDate and otherDate are equal");
        }
        LocalDateTime currentLastUpdatedTimestampString = LocalDateTime.parse("2023-04-20T11:02:31.822Z", DateTimeFormatter.ISO_DATE_TIME);
        LocalDateTime lastSuccessfulOrderLastUpdatedTimestamp = LocalDateTime.parse("2023-04-20T11:02:31.822Z", DateTimeFormatter.ISO_DATE_TIME);
        System.out.println(lastSuccessfulOrderLastUpdatedTimestamp.isAfter(currentLastUpdatedTimestampString));
    }
}