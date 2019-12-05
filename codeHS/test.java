public class Car {
    private double efficiency;
    private double gas;
    private double tankCapacity;
    private double totalMilesDriven;
    public Car(double carEffeciency, double carTankCapacity){
        efficiency = carEffeciency;
        tankCapacity = carTankCapacity;
    }
    public void addGas(){
        System.out.println("Filling up ...");
        gas = tankCapacity;
    }

    public void addGas(double amount){
        System.out.println("Adding gas ...");
        if(gas+amount<=tankCapacity){
            gas += amount;
        }
    }

    public double getTotalMilesDriven(){
        return totalMilesDriven;
    }

    public void drive(double distance){
        if(distance<=gas*efficiency){
            System.out.println("Driving " + distance);
            totalMilesDriven+=distance;
            gas-=distance/efficiency;
        }
        else{
            System.out.println("Can't drive " +distance+". That's too far!");
        }
    }

    public boolean canDrive (double distance){
        if(gas<=0){
            return false;
        }
        return true;
    }

    public double milesAvailable(){
        if(gas>0){
            return efficiency*gas;
        }
        return 0.0;
    }

    public double getGas(){
        return gas;
    }
}

public class CarTester {

    public static void main(String[] args) {
        Car car = new Car(20, 15);
        //Create a car that gets 20 mpg and has a 15 gallon tank
        //Fill up the gas tank
        car.addGas();
        //Check the miles available
        System.out.println("Miles available: " + car.milesAvailable());
        //Drive 100 miles
        car.drive(100);
        //Check the miles available
        System.out.println("Miles available: " + car.milesAvailable());
        //Add 2 gallons to the gas tank
        car.addGas(2);
        //Check the miles available
        System.out.println("Miles available: " + car.milesAvailable());
        //Try driving more miles than available
        car.drive(1000);
        //Drive 200 miles
        car.drive(200);
        //Check how much gas you have left
        System.out.println("Gas remaining: "+car.getGas());
        //Print total miles driven
        System.out.println("Total Miles Driven: " + car.getTotalMilesDriven());
    }
}