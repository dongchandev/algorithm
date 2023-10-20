import java.util.*;

public class Solution {
    public Integer solution(int[] priorities, int location) {
        PriorityQueue<Integer> q = new PriorityQueue<>(Collections.reverseOrder()); //우선순위 큐를 내림차순 정렬로 설정한다.
        int answer = 0;

        for (int priority : priorities) {
            q.add(priority);
        }

        while (!q.isEmpty()) {
            for (int i = 0; i < priorities.length; i++) {
                if (priorities[i] == q.peek()) {
                    if (i == location) {
                        answer++;
                        return answer;
                    }
                    q.poll();
                    answer++;
                }
            }
        }
        return -1;
    }
}