module fibonacci(clock,reset,value);
input clock,reset;
output [31:0]value;
reg [31:0]previous,current;
reg [5:0]counter;
//Reset the circuitalways@(posedge reset) begin
 previous <=32’d0;
 
current <= 32’d1;
count <= 6’d1;
 endalways@(posedge clock) begin
     //increment current 
indexcounter = counter + 1;
current = current + previous; 
previous = current - previous;end//Read the value of the nth fibonacci number assign value=previous;endmodule