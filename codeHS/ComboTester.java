public class ComboTester {

    public static void main(String[] args){
        CombinationLock combo = new CombinationLock("frog");
        combo.getClue("form");
    }
}

class CombinationLock{
    private String combo;
    public CombinationLock(String Combo){
        combo = Combo;
    }
    public void getClue(String clue){
        String output = "";
        if(combo.indexOf(clue.charAt(0))==0){
            output += clue.charAt(0);
        }
        else if(combo.indexOf(clue.charAt(0))>=0){
            output += "+";
        }
        else{
            output+="*";
        }
        
        if(combo.indexOf(clue.charAt(1))==1){
            output += clue.charAt(1);
        }
        else if(combo.indexOf(clue.charAt(1))>=0){
            output += "+";
        }
        else{
            output+="*";
        }
        
        if(combo.indexOf(clue.charAt(2))==2){
            output += clue.charAt(2);
        }
        else if(combo.indexOf(clue.charAt(2))>=0){
            output += "+";
        }
        else{
            output+="*";
        }
        
        if(combo.indexOf(clue.charAt(3))==3){
            output += clue.charAt(3);
        }
        else if(combo.indexOf(clue.charAt(3))>=0){
            output += "+";
        }
        else{
            output+="*";
        }
        System.out.println(output);
    }
}