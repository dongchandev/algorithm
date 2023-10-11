import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class Solution {
    public ArrayList<Integer> solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> answer = new ArrayList<>();
        Queue<Integer> queue = new LinkedList<>();

        for(int i=0; i<progresses.length; i++){
            queue.add((int)Math.ceil((100.0-progresses[i])/speeds[i]));
        }

        while(!queue.isEmpty()){
            int minDays=queue.poll();
            int cnt =1;
            while(!queue.isEmpty() && queue.peek() <= minDays){
                queue.poll();
                cnt++;
            }
            answer.add(cnt);
        }
        return answer;
    }
}