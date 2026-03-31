class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder sb = new StringBuilder();

        for (char c : s.toLowerCase().toCharArray()) {
            if (Character.isLetterOrDigit(c)) {
                sb.append(c);
            }
        }

        String newS = sb.toString();
        System.out.println(newS);

        int left = 0;
        int right = newS.length() - 1;

        while (right > left ) {
            if (newS.charAt(left) != newS.charAt(right)) {
                return false;
            }
            left ++;
            right --;
        }
        return true;

    }
}
