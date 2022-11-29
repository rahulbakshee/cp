# https://leetcode.com/problems/ransom-note/


  def canConstruct(self, ransomNote : str, magazine : str) -> bool :
      if len(ransomNote) > len(magazine) :
          return False
      if len(set(ransomNote)) > len(set(magazine)):
          return False

      ransom, magz = dict(), dict()

      for item in ransomNote:
          if item in ransom:
              ransom[item] += 1
          else:
              ransom[item] = 1

      for item in magazine:
          if item in magz:
              magz[item] += 1
          else:
              magz[item] = 1


      for item in ransom:
          if item in magz:
              if ransom[item] > magz[item]:
                  return False
          else:
              return False
      return True
