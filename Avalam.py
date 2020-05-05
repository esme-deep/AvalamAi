import cherrypy
import sys


class Server:
    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def move(self):
        # Deal with CORS
        cherrypy.response.headers['Access-Control-Allow-Origin'] = '*'
        cherrypy.response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        cherrypy.response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, X-Requested-With'
        if cherrypy.request.method == "OPTIONS":
            return ''
        
        body = cherrypy.request.json
        self.pion=1
        if body["you"] == body["players"][0]: #on regarde on joue le 1 ou le 0
            self.pion =0
        self.matrice = body["game"]
        self.lignes = len(self.matrice)
        self.colonnes = len (self.matrice[0])
       
        action ={"move": {}}

        #Plan A 
        for i in range (9):
            for j in range (9):
                #deplacement possible sur x
                for di in [-1, 0, 1]:
                    #deplacement possible sur y 
                    for dj in [-1, 0, 1]:
                        action["move"]["from"]=[i,j]
                        action["move"]["to"]=[i+di,j+dj]
                        action["message"]="yuum"
                        if self.IsItGood(action) == True :
                            if self.IsPerfect(action,self.pion):
                                return action 

        #Plan B
        for i in range (9):
            for j in range (9):
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        action["move"]["from"]=[i,j]
                        action["move"]["to"]=[i+di,j+dj]
                        action["message"]="here we are"
                        if self.IsItGood(action) == True :
                            return action 

   

                            
    def IsPerfect(self, action,pion): #voir si parmi les coups y en a un qui nous fait gagné un tour 
        #point de depart:
        a1 = action["move"]["from"][0]
        b1 = action["move"]["from"][1]
        #point d'arrivée:
        a2 = action["move"]["to"][0]
        b2 = action["move"]["to"][1]
        if len(self.matrice[a1][b1])+ len(self.matrice[a2][b2])==5 and self.matrice[a1][b1][-1]==pion :
            return True
    def IsItGood(self,action):  #voir si on respecte les régles du jeu
        #point de depart:
        a1 = action["move"]["from"][0]
        b1 = action["move"]["from"][1]
        #point d'arrivée:
        a2 = action["move"]["to"][0]
        b2 = action["move"]["to"][1]

        #vu qu'on fait des soustractions/additions aux indices : on check si on tombe sur un indice negatif ou plus grand que la taille des lignes/colonnes 
        #ou on change pas de place du tout ou on essaye de faire un coup eloigés de la cases
        if a1 < 0 or b1 < 0 or a2 < 0 or b2 < 0 or a1 >= self.lignes or b1 >= self.colonnes or a2 >= self.lignes or b2 >= self.colonnes or (a1 == a2 and b1 == b2) or (abs(a1-a2) > 1) or (abs(b1-b2) > 1):
            return False 

        if self.matrice[a1][b1]=='' or self.matrice[a2][b2]=='' :
            return False 


        h1=len( self.matrice[a1][b1])
        h2=len( self.matrice[a2][b2])
        #on sait pas deplacer un pion sur une case vide ou un qui contient 5 pion deja 
        #on sait pas deplacer un tour de 5 non plus
        if h1 <= 0 or h1 >= 5 or h2 <= 0 or h2 >= 5 or h1+h2 > 5 :
            return False

        return True 

    @cherrypy.expose          #just a test to make sure he can get infos from our server
    def ping(self):
        return "pong"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        port=int(sys.argv[1])
    else:
        port=3000

    cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': port})
    cherrypy.quickstart(Server())