Bot pour automatiser la réponse aux question du site d'apprentissage en ligne Busuu.

Le but n'est pas que le bot réponde correctement aux questions, juste qu'il passe du temps sur le site. 
En effet, les rattrapages de langue d'une certaine école d'ingénieur parisienne consistent à faire x heures sur cette plateforme.
Le temps était la ressource la plus rare, et les langues concernées étant édjà soit inutiles pour les étudiants soit déjà maitrisées,
rien de plus ne sera recherché ici.

POINT FONCTIONNEMENT : 

Si il devait y avoir un algorigramme de comment a été pensé le bot, ce serait celui-ci : 
While (bot actif) :
Lancer une lecon
  while (lecon pas finie) :
    Identifier quel type de question est actuellement affiché sur l'écran
    while (bouton continuer not on screen) : 
      Envoyer une suite random d'input
  
Du coup si ça marche pas : 
 - Il faut que tu checks que tu sois bien en plein écran sur la page internet de busuu, et sur ton écran identifié comme étant le principal si t'as un setup dual screen
 - Y a moyen que l'utilisation de la librairie inputX via le module win32auto soit purement windows (d'ailleurs c'est dans le titre de du module). Du coup faut utiliser la bonne branche de commit pour les dev, et la bonne branche pour run le bail
