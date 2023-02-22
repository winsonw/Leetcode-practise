class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        for i, email in enumerate(emails):
            sections = email.split('@')
            valid = sections[0].split('+')[0]
            emails[i] = valid.replace('.','') +'@'+ sections[1]
        return len(set(emails))