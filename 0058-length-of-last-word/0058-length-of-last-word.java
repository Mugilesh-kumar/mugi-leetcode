class Solution {
    public int lengthOfLastWord(String s) {
        int count=0;
        int len=s.length()-1;
       while (len>=0){
        if(s.charAt(len)!=' '){
            count++;
        }else if(s.charAt(len)==' ' && count>0){
            break;
        }       
                    len--;

     }
     return count;
    }
        
}