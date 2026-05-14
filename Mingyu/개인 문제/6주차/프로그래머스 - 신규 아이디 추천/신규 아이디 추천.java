import java.util.stream.*;

class Solution {
    public String solution(String new_id) {
        String step12 = new_id.toLowerCase().chars()
                .filter(c -> Character.isAlphabetic(c) || 
                             Character.isDigit(c) || 
                             c == '-' || c == '_' || c == '.')
                .mapToObj(c -> String.valueOf((char) c))
                .collect(Collectors.joining());

        String step34 = step12.replaceAll("\\.{2,}", ".")
                           .replaceAll("^[.]|[.]$", "");

        String step5 = step34.isEmpty() ? "a" : step34;

        if (step5.length() >= 16) {
            step5 = step5.substring(0, 15).replaceAll("[.]$", "");
        }

        StringBuilder sb = new StringBuilder(step5);
        while (sb.length() < 3) {
            sb.append(sb.charAt(sb.length() - 1));
        }

        return sb.toString();
    }
}