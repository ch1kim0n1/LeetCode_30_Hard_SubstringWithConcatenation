class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words or not words[0]:
            return []
        
        word_len = len(words[0])
        total_len = word_len * len(words)
        s_len = len(s)
        
        if total_len > s_len:
            return []
        
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        
        result = []
        
        for offset in range(word_len):
            left = offset
            right = offset
            current_count = {}
            matched_words = 0
            
            while right + word_len <= s_len:
                word = s[right:right + word_len]
                right += word_len
                
                if word in word_count:
                    current_count[word] = current_count.get(word, 0) + 1
                    matched_words += 1
                    
                    while current_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        matched_words -= 1
                        left += word_len
                    
                    if matched_words == len(words):
                        result.append(left)
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        matched_words -= 1
                        left += word_len
                
                else:
                    current_count.clear()
                    matched_words = 0
                    left = right
        
        return result