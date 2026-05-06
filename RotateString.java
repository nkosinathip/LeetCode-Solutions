class Solution {
    public boolean rotateString(String s, String goal) {
        boolean status =false;
        for(int i=0;i<s.length(); i++){
            if(s.equals(goal)){
                return true;
            }

            char firstletter= s.charAt(0);       
            s=s.substring(1)+Character.toString(firstletter);
            
            if(s.equals(goal)){
                status =true;
            }
            
        }
        return status;
    }
}
