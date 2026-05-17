import java.util.*;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        int n = id_list.length;
        int[] answer = new int[n];

        Map<String, Integer> idToIndex = new HashMap<>();

        for (int i = 0; i < n; i++) {
            idToIndex.put(id_list[i], i);
        }

        Set<String> uniqueReports = new HashSet<>();

        for (String r : report) {
            uniqueReports.add(r);
        }

        int[] reportedCount = new int[n];

        for (String r : uniqueReports) {
            String[] parts = r.split(" ");

            String reportedUser = parts[1];
            int reportedIndex = idToIndex.get(reportedUser);

            reportedCount[reportedIndex]++;
        }

        for (String r : uniqueReports) {
            String[] parts = r.split(" ");

            String reporter = parts[0];
            String reportedUser = parts[1];

            int reporterIndex = idToIndex.get(reporter);
            int reportedIndex = idToIndex.get(reportedUser);

            if (reportedCount[reportedIndex] >= k) {
                answer[reporterIndex]++;
            }
        }

        return answer;
    }
}