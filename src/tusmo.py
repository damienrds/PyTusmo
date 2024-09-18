from random import choice

# -------------------------------------------------------------------------------------------------
class tusmo( ):
    
    # ---------------------------------------------------------------------------------------------
    def __init__(self):
        self.Path = "./ods6.txt"
        self.WordList = self.getWordList( )
        self.ExcludeLetter = [ ]
        self.IncludeLetter = [ ]
        self.WordLenght = 0
        self.nb_essai = 6
    # ---------------------------------------------------------------------------------------------


    # ---------------------------------------------------------------------------------------------
    def getWordList( self ):
        
        with open( self.Path, "r", encoding="utf-8" ) as file:
            WordList = file.read( ).splitlines( )
        
        return WordList
    # ---------------------------------------------------------------------------------------------
    
    
    # ---------------------------------------------------------------------------------------------
    def generate_word( self ):
        return choice( self.WordList )
    # ---------------------------------------------------------------------------------------------


    # ---------------------------------------------------------------------------------------------
    def update_wordlist( self, inWordMap, inProposedWord ):
        self.WordList.remove( inProposedWord )
        vIncludeLetter = [ ]
        vExcludeLetter = [ ]
        
        # -- Use word map to update word list
        for vIndex in range( self.WordLenght ):
            if inWordMap[ vIndex ] == "r" :
                self.WordList = [ vWord for vWord in self.WordList if vWord[ vIndex ] == inProposedWord[ vIndex ] ]
                vIncludeLetter.append( inProposedWord[ vIndex ] )
            elif inWordMap[ vIndex ] == "y" :
                self.WordList = [ vWord for vWord in self.WordList if vWord[ vIndex ] != inProposedWord[ vIndex ] ]
                vIncludeLetter.append( inProposedWord[ vIndex ] )
            elif inWordMap[ vIndex ] == "-" :
                vExcludeLetter.append( inProposedWord[ vIndex ] )
        
        # -- Remove letters which are not in the word list
        for lLetter in set( vExcludeLetter ):
            if lLetter not in vIncludeLetter:
                self.WordList = [ vWord for vWord in self.WordList if lLetter not in vWord ]
            
        # -- Use letter occurrences to update word list
        v_OccurDict = { vKey:0 for vKey in set( vIncludeLetter ) }
        
        for vIndex in vIncludeLetter:
            v_OccurDict[ vIndex ] += 1
            
        for lKey, lValue in v_OccurDict.items():
            if lKey in vExcludeLetter:
                self.WordList = [ vWord for vWord in self.WordList if vWord.count( lKey ) == lValue ]
            else:
                self.WordList = [ vWord for vWord in self.WordList if vWord.count( lKey ) >= lValue ]            
            
    # ---------------------------------------------------------------------------------------------