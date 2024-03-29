class Solution {
    public int[] solution(int n) {
        int alen = n % 2 == 0 ? n/2: n/2 + 1;
        int[] answer = new int[alen];
        for (int i = 1; i <= n; i++){
            if (i % 2 == 1) {
                answer[i/2] = i;
            }
        }
        return answer;
    }
}