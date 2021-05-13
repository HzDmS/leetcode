class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        """
        The logic is simple:
        The cases where the n-th passenger does seat on his/her own seat are
        
        Format: not in their own seat \ in their own seat
        1 2 \ 3 - n
        1 2 3 \ 4 - n
        .
        .
        .
        1 - (n - 1) \ n
        
        The cases where the n-th passenger does seat in his/her own seat are
    
        Format: in their own seat \ not in their own seat
        1 \ 2 - n
        1 2 \ 3 - n
        1 2 3 \ 4 - n
        .
        .
        .
        1 - (n - 2) \ (n - 1) - n
        
        Note that they are exactly symmetric, so the answer is obervious.
        """
        
        
        return 1 / 2 if n > 1 else 1.0
